"""Almacén de usuarios persistente en disco.

El registro se guardaba solo en memoria, de modo que al reiniciar el servidor
había que volver a registrarse. Aquí se persiste en un JSON y, de paso, la
contraseña deja de guardarse en claro: se almacena su derivación PBKDF2 con
una sal aleatoria por usuario.

No pretende ser un sistema de autenticación robusto (la aplicación es de
estudio y se ejecuta en local), pero evita el bug de las sesiones perdidas y
no deja contraseñas legibles en el fichero.
"""
import hashlib
import hmac
import json
import os
import secrets
import threading

_ITERACIONES = 200_000
_ALGORITMO = "sha256"

# Ubicación del fichero: configurable para el modo portable.
_DIR_DATOS = os.environ.get("EFA_DATA_DIR") or os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data"
)
RUTA_USUARIOS = os.path.join(_DIR_DATOS, "usuarios.json")

_lock = threading.Lock()


def _derivar(password: str, sal: str) -> str:
    dk = hashlib.pbkdf2_hmac(
        _ALGORITMO, password.encode("utf-8"), bytes.fromhex(sal), _ITERACIONES
    )
    return dk.hex()


def _cargar() -> dict:
    try:
        with open(RUTA_USUARIOS, encoding="utf-8") as f:
            datos = json.load(f)
        return datos if isinstance(datos, dict) else {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def _guardar(usuarios: dict) -> None:
    os.makedirs(_DIR_DATOS, exist_ok=True)
    tmp = RUTA_USUARIOS + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=1)
    os.replace(tmp, RUTA_USUARIOS)  # escritura atómica


def existe(username: str) -> bool:
    return username in _cargar()


def registrar(username: str, password: str) -> bool:
    """Crea el usuario. Devuelve False si ya existía."""
    with _lock:
        usuarios = _cargar()
        if username in usuarios:
            return False
        sal = secrets.token_hex(16)
        usuarios[username] = {"sal": sal, "hash": _derivar(password, sal)}
        _guardar(usuarios)
        return True


def verificar(username: str, password: str) -> bool:
    """Comprueba las credenciales en tiempo constante."""
    usuarios = _cargar()
    registro = usuarios.get(username)
    if not registro:
        return False
    esperado = registro.get("hash", "")
    calculado = _derivar(password, registro.get("sal", ""))
    return hmac.compare_digest(esperado, calculado)


def total_usuarios() -> int:
    return len(_cargar())


# --- Identidades externas (Google, Microsoft, Facebook) ---
#
# Un usuario que entra con un proveedor no tiene contraseña local: se le
# identifica por su correo verificado y se guarda de qué proveedor vino, para
# poder distinguirlo y para no permitir que alguien "reclame" una cuenta de
# contraseña ajena simplemente iniciando sesión con un correo homónimo.

def registrar_o_actualizar_externo(email: str, proveedor: str, nombre: str = "") -> dict:
    """Da de alta (o actualiza) al usuario que entra por un proveedor externo."""
    email = email.strip().lower()
    with _lock:
        usuarios = _cargar()
        registro = usuarios.get(email, {})
        proveedores = set(registro.get("proveedores", []))
        proveedores.add(proveedor)
        registro["proveedores"] = sorted(proveedores)
        if nombre:
            registro["nombre"] = nombre
        registro.setdefault("alta", _ahora())
        usuarios[email] = registro
        _guardar(usuarios)
        return registro


def tiene_contrasena(username: str) -> bool:
    """Indica si la cuenta tiene contraseña local (frente a solo externa)."""
    registro = _cargar().get(username, {})
    return bool(registro.get("hash"))


def _ahora() -> str:
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).isoformat(timespec="seconds")
