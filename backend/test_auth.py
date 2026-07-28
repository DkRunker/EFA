"""Comprobaciones del sistema de sesiones y del acceso privado.

Antes existía un «token» simulado que no se verificaba en ninguna parte:
cualquiera podía llamar a la API sin identificarse. Estas pruebas fijan el
comportamiento correcto para que no vuelva a ocurrir.
"""
import importlib
import os

import pytest
from starlette.testclient import TestClient

import backend.auth as auth
from backend.main import app

client = TestClient(app)

CREDENCIALES = {"username": "tester_auth", "password": "clave-larga-123"}

# Endpoints que NO deben responder sin sesión iniciada.
PROTEGIDOS_GET = [
    "/api/exams/oficiales",
    "/api/study/apuntes",
    "/api/study/apuntes/M1",
    "/api/study/secciones/M1",
]


@pytest.fixture()
def sesion_iniciada():
    client.post("/api/auth/register", json=CREDENCIALES)
    r = client.post("/api/auth/login", json=CREDENCIALES)
    assert r.status_code == 200, r.text
    return r.json()["token"]


def cabecera(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


def test_los_endpoints_exigen_sesion():
    for ruta in PROTEGIDOS_GET:
        r = client.get(ruta)
        assert r.status_code == 401, f"{ruta} respondió {r.status_code} sin sesión"

    r = client.post("/api/exams/start", json={"tipo_examen": "EIP"})
    assert r.status_code == 401
    r = client.post("/api/formulas/calculate", json={"formula": "tae", "params": {"tin": 0.06, "m": 12}})
    assert r.status_code == 401


def test_con_sesion_se_puede_acceder(sesion_iniciada):
    for ruta in PROTEGIDOS_GET:
        r = client.get(ruta, headers=cabecera(sesion_iniciada))
        assert r.status_code == 200, f"{ruta} falló con sesión: {r.status_code}"


def test_el_token_es_real_y_no_simulado(sesion_iniciada):
    assert not sesion_iniciada.startswith("mock-token")
    datos = auth.leer_token(sesion_iniciada)
    assert datos["sub"] == CREDENCIALES["username"]
    assert "exp" in datos and "iat" in datos


def test_token_manipulado_se_rechaza(sesion_iniciada):
    falso = sesion_iniciada[:-4] + "aaaa"
    r = client.get("/api/study/secciones/M1", headers=cabecera(falso))
    assert r.status_code == 401
    r = client.get("/api/study/secciones/M1", headers={"Authorization": "Bearer inventado"})
    assert r.status_code == 401


def test_token_caducado_se_rechaza(monkeypatch):
    monkeypatch.setenv("EFA_HORAS_SESION", "-1")  # ya nacido caducado
    importlib.reload(auth)
    token = auth.crear_token("quien_sea")
    with pytest.raises(Exception):
        auth.leer_token(token)
    monkeypatch.delenv("EFA_HORAS_SESION", raising=False)
    importlib.reload(auth)


def test_contrasena_corta_se_rechaza():
    r = client.post("/api/auth/register", json={"username": "corta", "password": "1234"})
    assert r.status_code == 400
    assert "8" in r.json()["detail"]


def test_lista_de_acceso_privada(monkeypatch):
    """Con lista de permitidos, una cuenta ajena no entra aunque exista."""
    monkeypatch.setenv("EFA_USUARIOS_PERMITIDOS", "solo_yo@ejemplo.com")
    assert auth.esta_permitido("solo_yo@ejemplo.com")
    assert auth.esta_permitido("SOLO_YO@EJEMPLO.COM")  # sin distinguir mayúsculas
    assert not auth.esta_permitido("intruso@ejemplo.com")
    monkeypatch.delenv("EFA_USUARIOS_PERMITIDOS", raising=False)
    # sin lista, no se restringe (modo local)
    assert auth.esta_permitido("cualquiera")


def test_cors_no_es_comodin():
    """allow_origins="*" junto a credenciales sería inseguro y no funcionaría."""
    origenes = auth.origenes_permitidos()
    assert "*" not in origenes
    assert all(o.startswith("http") for o in origenes)


def test_un_usuario_no_puede_entregar_el_examen_de_otro(sesion_iniciada):
    r = client.post("/api/exams/start", json={"tipo_examen": "EIP"},
                    headers=cabecera(sesion_iniciada))
    assert r.status_code == 200
    sesion_examen = r.json()["session_id"]

    otro = {"username": "otro_tester", "password": "otra-clave-larga"}
    client.post("/api/auth/register", json=otro)
    token_otro = client.post("/api/auth/login", json=otro).json()["token"]

    r = client.post(
        "/api/exams/submit",
        json={"session_id": sesion_examen, "respuestas_test": {}, "respuestas_practica": {}},
        headers=cabecera(token_otro),
    )
    assert r.status_code == 404, "un usuario ha podido entregar el examen de otro"


def test_proveedores_solo_los_configurados():
    """Sin credenciales no se ofrece ningún proveedor externo."""
    r = client.get("/api/auth/oauth/proveedores")
    assert r.status_code == 200
    for p in r.json()["proveedores"]:
        assert p["id"] in {"google", "microsoft", "facebook"}


def test_proveedor_no_configurado_avisa():
    r = client.get("/api/auth/oauth/google", follow_redirects=False)
    # o no está configurado (503) o redirige al proveedor (302/307)
    assert r.status_code in (302, 307, 503)


def test_redirect_uri_es_deterministica(monkeypatch):
    """La URI de retorno OAuth se fija por EFA_URL_FRONTEND, no por el host.

    Así coincide siempre con la registrada en el proveedor, sin importar si se
    entra por localhost o por 127.0.0.1 (Google exige coincidencia exacta).
    """
    import backend.oauth as oauth

    class _Req:
        def url_for(self, name, proveedor):
            from types import SimpleNamespace
            return SimpleNamespace(path=f"/api/auth/oauth/{proveedor}/callback")

    monkeypatch.setenv("EFA_URL_FRONTEND", "https://efa.ejemplo.com")
    uri = oauth._url_callback("google", _Req())
    assert uri == "https://efa.ejemplo.com/api/auth/oauth/google/callback"


def test_endpoint_yo_devuelve_la_identidad(sesion_iniciada):
    r = client.get("/api/auth/yo", headers=cabecera(sesion_iniciada))
    assert r.status_code == 200
    assert r.json()["username"] == CREDENCIALES["username"]
    assert r.json()["proveedor"] == "password"
