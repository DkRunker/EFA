"""Sesiones y control de acceso de la plataforma.

Sustituye al «token» simulado anterior, que no se comprobaba en ninguna parte:
cualquiera podía llamar a la API sin identificarse. Aquí se emiten JWT firmados
y con caducidad, y se ofrece la dependencia `usuario_actual` para exigirlos.

La instalación es PRIVADA: además de estar autenticado, el usuario debe figurar
en la lista de acceso (`EFA_USUARIOS_PERMITIDOS`). Así, aunque alguien tenga
una cuenta de Google válida, no entra si no está autorizado.
"""
import os
from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

ALGORITMO = "HS256"
DURACION_SESION_HORAS = int(os.environ.get("EFA_HORAS_SESION", "72"))

_esquema = HTTPBearer(auto_error=False)


def clave_secreta() -> str:
    """Clave de firma de los tokens.

    En despliegue DEBE venir de EFA_SECRET_KEY. En local se genera una
    efímera: basta para desarrollar, pero invalida las sesiones al reiniciar,
    lo que evita que una clave por defecto acabe en producción por descuido.
    """
    clave = os.environ.get("EFA_SECRET_KEY")
    if clave:
        return clave
    global _clave_efimera
    try:
        return _clave_efimera
    except NameError:
        import secrets
        _clave_efimera = secrets.token_urlsafe(48)
        return _clave_efimera


def _lista_permitidos() -> set[str]:
    """Identidades autorizadas (correos o nombres de usuario), en minúsculas.

    Si la variable está vacía, no se restringe: es el modo local de siempre,
    pensado para el uso en el propio equipo. Al desplegar debe definirse.
    """
    crudo = os.environ.get("EFA_USUARIOS_PERMITIDOS", "")
    return {x.strip().lower() for x in crudo.split(",") if x.strip()}


def esta_permitido(identidad: str) -> bool:
    permitidos = _lista_permitidos()
    if not permitidos:
        return True
    return identidad.strip().lower() in permitidos


def crear_token(sujeto: str, proveedor: str = "password", **extra) -> str:
    """Emite un JWT firmado para el usuario indicado."""
    ahora = datetime.now(timezone.utc)
    carga = {
        "sub": sujeto,
        "proveedor": proveedor,
        "iat": ahora,
        "exp": ahora + timedelta(hours=DURACION_SESION_HORAS),
        **extra,
    }
    return jwt.encode(carga, clave_secreta(), algorithm=ALGORITMO)


def leer_token(token: str) -> dict:
    """Descodifica y valida el token. Lanza 401 si no es válido o ha caducado."""
    try:
        return jwt.decode(token, clave_secreta(), algorithms=[ALGORITMO])
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="La sesión ha caducado. Vuelve a iniciar sesión.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Sesión no válida.",
            headers={"WWW-Authenticate": "Bearer"},
        )


def usuario_actual(
    credenciales: HTTPAuthorizationCredentials | None = Depends(_esquema),
) -> dict:
    """Dependencia para los endpoints que exigen sesión iniciada."""
    if credenciales is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Necesitas iniciar sesión.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    datos = leer_token(credenciales.credentials)
    sujeto = datos.get("sub", "")
    if not sujeto:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Sesión no válida.")
    if not esta_permitido(sujeto):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Esta instalación es privada y tu cuenta no está autorizada.",
        )
    return datos


def origenes_permitidos() -> list[str]:
    """Orígenes admitidos por CORS.

    Antes estaba en "*" junto con allow_credentials=True, combinación que los
    navegadores rechazan y que además abriría la API a cualquier web. Ahora se
    declara explícitamente con EFA_ORIGENES_CORS; en local basta el propio host.
    """
    crudo = os.environ.get("EFA_ORIGENES_CORS", "")
    origenes = [x.strip() for x in crudo.split(",") if x.strip()]
    if origenes:
        return origenes
    return [
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:5173",  # servidor de desarrollo de Vite
        "http://127.0.0.1:5173",
    ]
