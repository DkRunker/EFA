"""Acceso con proveedores externos: Google, Microsoft y Facebook.

Las credenciales NUNCA se escriben en el código: se leen de variables de
entorno que configura la persona que despliega (ver .env.ejemplo). Un proveedor
sin credenciales simplemente no se ofrece, de modo que la aplicación arranca
igual aunque solo se configure uno.

Flujo estándar de código de autorización:
  1. El navegador va a /api/auth/oauth/<proveedor>
  2. El proveedor autentica al usuario y vuelve a /api/auth/oauth/<proveedor>/callback
  3. Se comprueba que el correo esté verificado y autorizado, se emite el JWT
     propio de la aplicación y se redirige al frontend con él.
"""
import os
from urllib.parse import urlencode

from authlib.integrations.starlette_client import OAuth, OAuthError
from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import RedirectResponse

from backend import usuarios
from backend.auth import crear_token, esta_permitido

router = APIRouter(prefix="/api/auth/oauth", tags=["auth"])

# Definición de los proveedores soportados. `clave_email` indica de qué campo
# del perfil sale el correo, que es la identidad que usamos en la aplicación.
PROVEEDORES = {
    "google": {
        "nombre": "Google",
        "metadata": "https://accounts.google.com/.well-known/openid-configuration",
        "scope": "openid email profile",
    },
    "microsoft": {
        "nombre": "Microsoft",
        # "common" admite cuentas personales y de organización
        "metadata": "https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration",
        "scope": "openid email profile",
    },
    "facebook": {
        "nombre": "Facebook",
        "authorize_url": "https://www.facebook.com/v19.0/dialog/oauth",
        "access_token_url": "https://graph.facebook.com/v19.0/oauth/access_token",
        "api_base_url": "https://graph.facebook.com/v19.0/",
        "scope": "email public_profile",
    },
}

oauth = OAuth()


def _credenciales(proveedor: str) -> tuple[str, str]:
    prefijo = proveedor.upper()
    return (
        os.environ.get(f"EFA_{prefijo}_CLIENT_ID", ""),
        os.environ.get(f"EFA_{prefijo}_CLIENT_SECRET", ""),
    )


def proveedores_configurados() -> list[dict]:
    """Proveedores con credenciales presentes, para que la interfaz sepa qué botones mostrar."""
    salida = []
    for clave, datos in PROVEEDORES.items():
        client_id, client_secret = _credenciales(clave)
        if client_id and client_secret:
            salida.append({"id": clave, "nombre": datos["nombre"]})
    return salida


def registrar_proveedores() -> None:
    """Registra en Authlib los proveedores que tengan credenciales."""
    for clave, datos in PROVEEDORES.items():
        client_id, client_secret = _credenciales(clave)
        if not (client_id and client_secret):
            continue
        kwargs = {"client_id": client_id, "client_secret": client_secret,
                  "client_kwargs": {"scope": datos["scope"]}}
        if "metadata" in datos:
            kwargs["server_metadata_url"] = datos["metadata"]
        else:
            kwargs["authorize_url"] = datos["authorize_url"]
            kwargs["access_token_url"] = datos["access_token_url"]
            kwargs["api_base_url"] = datos["api_base_url"]
        oauth.register(name=clave, **kwargs)


def _url_frontend() -> str:
    return os.environ.get("EFA_URL_FRONTEND", "http://localhost:8000").rstrip("/")


def _url_callback(proveedor: str, request: Request) -> str:
    """URL de retorno del proveedor.

    Se construye sobre EFA_URL_FRONTEND para que sea SIEMPRE la misma y coincida
    con la que hay que registrar en el proveedor, sin depender de si el usuario
    entró por 'localhost' o por '127.0.0.1'. Como último recurso (si la variable
    no está), se deduce del propio host de la petición.
    """
    ruta = request.url_for("callback", proveedor=proveedor).path
    base = os.environ.get("EFA_URL_FRONTEND")
    if base:
        return f"{base.rstrip('/')}{ruta}"
    return str(request.url_for("callback", proveedor=proveedor))


def _volver_con_error(motivo: str) -> RedirectResponse:
    return RedirectResponse(f"{_url_frontend()}/?{urlencode({'error_auth': motivo})}")


@router.get("/proveedores")
def api_proveedores():
    """Proveedores disponibles en esta instalación."""
    return {"proveedores": proveedores_configurados()}


@router.get("/{proveedor}")
async def iniciar(proveedor: str, request: Request):
    if proveedor not in PROVEEDORES:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Proveedor no soportado.")
    cliente = getattr(oauth, proveedor, None)
    if cliente is None:
        raise HTTPException(
            status.HTTP_503_SERVICE_UNAVAILABLE,
            f"El acceso con {PROVEEDORES[proveedor]['nombre']} no está configurado en este servidor.",
        )
    redirect_uri = _url_callback(proveedor, request)
    return await cliente.authorize_redirect(request, redirect_uri)


@router.get("/{proveedor}/callback", name="callback")
async def callback(proveedor: str, request: Request):
    cliente = getattr(oauth, proveedor, None)
    if cliente is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Proveedor no configurado.")

    try:
        token = await cliente.authorize_access_token(request)
    except OAuthError:
        return _volver_con_error("No se pudo completar el acceso con el proveedor.")

    perfil = token.get("userinfo") or {}
    if not perfil and proveedor == "facebook":
        # Facebook no es OIDC: hay que pedir el perfil a su API
        respuesta = await cliente.get("me?fields=id,name,email", token=token)
        perfil = respuesta.json()

    email = (perfil.get("email") or "").strip().lower()
    if not email:
        return _volver_con_error("El proveedor no ha facilitado un correo electrónico.")

    # Google y Microsoft informan de si el correo está verificado; si dicen que
    # no lo está, no lo aceptamos como identidad.
    verificado = perfil.get("email_verified")
    if verificado is False:
        return _volver_con_error("El correo de esa cuenta no está verificado.")

    if not esta_permitido(email):
        return _volver_con_error("Esta instalación es privada y tu cuenta no está autorizada.")

    # Anotar el alta del usuario es solo contabilidad: el acceso se decide por
    # la lista de permitidos y la sesión es un JWT sin estado. Si el sistema de
    # ficheros es de solo lectura (habitual en hosting gratuito), no debe
    # impedir el acceso, así que un fallo al escribir se ignora.
    try:
        usuarios.registrar_o_actualizar_externo(
            email=email, proveedor=proveedor, nombre=perfil.get("name", "")
        )
    except OSError:
        pass
    jwt_propio = crear_token(email, proveedor=proveedor)
    parametros = urlencode({"token": jwt_propio, "usuario": email})
    return RedirectResponse(f"{_url_frontend()}/?{parametros}")
