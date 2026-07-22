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
