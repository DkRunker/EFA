"""El registro de usuarios debe sobrevivir al reinicio del servidor."""
import importlib

import pytest


@pytest.fixture()
def almacen(tmp_path, monkeypatch):
    """Carga el módulo de usuarios apuntando a un fichero temporal."""
    monkeypatch.setenv("EFA_DATA_DIR", str(tmp_path))
    import backend.usuarios as u
    importlib.reload(u)
    yield u
    importlib.reload(u)


def test_registrar_y_verificar(almacen):
    assert almacen.registrar("pablo", "clave-secreta") is True
    assert almacen.verificar("pablo", "clave-secreta") is True
    assert almacen.verificar("pablo", "otra-clave") is False
    assert almacen.verificar("desconocido", "clave-secreta") is False


def test_no_permite_duplicados(almacen):
    assert almacen.registrar("ana", "1234") is True
    assert almacen.registrar("ana", "5678") is False
    # la contraseña original sigue siendo la válida
    assert almacen.verificar("ana", "1234") is True
    assert almacen.verificar("ana", "5678") is False


def test_persiste_entre_reinicios(almacen, tmp_path, monkeypatch):
    """Este era el bug: al reiniciar había que volver a registrarse."""
    almacen.registrar("pablo", "clave-secreta")

    # simulamos un reinicio del proceso recargando el módulo
    monkeypatch.setenv("EFA_DATA_DIR", str(tmp_path))
    importlib.reload(almacen)

    assert almacen.existe("pablo") is True
    assert almacen.verificar("pablo", "clave-secreta") is True


def test_no_guarda_la_contrasena_en_claro(almacen):
    almacen.registrar("pablo", "clave-secreta")
    contenido = open(almacen.RUTA_USUARIOS, encoding="utf-8").read()
    assert "clave-secreta" not in contenido
    assert "sal" in contenido and "hash" in contenido


def test_cada_usuario_tiene_su_propia_sal(almacen):
    almacen.registrar("uno", "misma-clave")
    almacen.registrar("dos", "misma-clave")
    import json
    datos = json.load(open(almacen.RUTA_USUARIOS, encoding="utf-8"))
    assert datos["uno"]["sal"] != datos["dos"]["sal"]
    # con sales distintas, el hash de la misma contraseña difiere
    assert datos["uno"]["hash"] != datos["dos"]["hash"]


def test_fichero_corrupto_no_rompe_el_arranque(almacen):
    import os
    os.makedirs(os.path.dirname(almacen.RUTA_USUARIOS), exist_ok=True)
    open(almacen.RUTA_USUARIOS, "w", encoding="utf-8").write("{ esto no es json")
    assert almacen.existe("pablo") is False
    assert almacen.registrar("pablo", "clave") is True
