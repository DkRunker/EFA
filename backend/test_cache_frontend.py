"""El navegador no debe quedarse con una versión antigua del frontend.

`index.html` mantiene siempre el mismo nombre y apunta al bundle vigente: si se
cachea, la aplicación sigue cargando la versión anterior aunque el servidor ya
tenga la nueva. Los ficheros de `assets/` sí pueden cachearse porque llevan un
hash en el nombre.
"""
import pytest
from starlette.testclient import TestClient

from backend.main import app, _FRONTEND_DIST

import os

pytestmark = pytest.mark.skipif(
    not os.path.isdir(_FRONTEND_DIST),
    reason="no hay build del frontend (frontend/dist)",
)

client = TestClient(app)


def test_index_no_se_cachea():
    r = client.get("/")
    assert r.status_code == 200
    cache = r.headers.get("cache-control", "")
    assert "no-cache" in cache, f"index.html cacheable: {cache!r}"


def test_assets_se_cachean_a_largo_plazo():
    """Los assets llevan hash en el nombre, así que son inmutables."""
    import re
    html = client.get("/").text
    bundles = re.findall(r'assets/[^"\']+\.js', html)
    assert bundles, "index.html no referencia ningún bundle"

    r = client.get("/" + bundles[0])
    assert r.status_code == 200
    cache = r.headers.get("cache-control", "")
    assert "max-age=" in cache and "immutable" in cache, f"assets sin caché: {cache!r}"


def test_el_bundle_servido_es_el_del_build_actual():
    """Detecta que se esté sirviendo un dist obsoleto respecto al de disco."""
    import re
    html = client.get("/").text
    referenciados = set(re.findall(r'assets/([^"\']+\.(?:js|css))', html))
    en_disco = set(os.listdir(os.path.join(_FRONTEND_DIST, "assets")))
    faltan = referenciados - en_disco
    assert not faltan, f"index.html apunta a ficheros que no existen: {faltan}"
