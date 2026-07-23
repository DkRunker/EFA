"""Configuración común de la batería de pruebas.

Desde que los usuarios se guardan en disco, las pruebas que registran usuarios
escribirían en la base real (`data/usuarios.json`) y, además, fallarían en la
segunda ejecución porque el usuario ya existiría. Aquí se redirige el almacén a
un directorio temporal ANTES de que se importe la aplicación, de modo que cada
sesión de pruebas parte en limpio y nunca toca los datos del usuario.
"""
import os
import tempfile

_DIR_PRUEBAS = tempfile.mkdtemp(prefix="efa-tests-")
os.environ["EFA_DATA_DIR"] = _DIR_PRUEBAS


def cabeceras_auth(usuario: str = "usuario_de_pruebas") -> dict[str, str]:
    """Cabecera de sesión válida para las pruebas.

    Los endpoints exigen sesión iniciada; sin esto responderían 401. Se emite
    el token directamente, sin pasar por el registro, para que las pruebas de
    contenido no dependan del flujo de acceso (que tiene sus propias pruebas
    en test_auth.py).
    """
    from backend.auth import crear_token
    return {"Authorization": f"Bearer {crear_token(usuario)}"}
