"""Punto de entrada de la versión PORTABLE de la Plataforma EFA.

Arranca el servidor (backend FastAPI que además sirve el frontend ya compilado)
en http://127.0.0.1:8000 y abre el navegador automáticamente.

Funciona tanto:
  - ejecutado con Python:      python run_portable.py
  - empaquetado con PyInstaller: EFA_Prep.exe  (modo "frozen")
"""
import os
import sys
import time
import threading
import webbrowser

HOST = "127.0.0.1"
PORT = 8000
URL = f"http://{HOST}:{PORT}"


def _configurar_rutas():
    """Ubica el frontend compilado según el modo de ejecución."""
    if getattr(sys, "frozen", False):
        # Ejecutable PyInstaller: los datos se descomprimen en sys._MEIPASS.
        base = sys._MEIPASS  # type: ignore[attr-defined]
        os.environ.setdefault("EFA_FRONTEND_DIST", os.path.join(base, "frontend_dist"))
        # Los usuarios registrados deben persistir junto al ejecutable, no en
        # sys._MEIPASS (que es temporal y se borra al cerrar). Así la sesión
        # sobrevive entre ejecuciones también en la versión portable.
        dir_exe = os.path.dirname(sys.executable)
        dir_datos = os.path.join(dir_exe, "datos_efa")
        os.environ.setdefault("EFA_DATA_DIR", dir_datos)
        # Clave de firma de las sesiones persistente. Si no se fija, cada
        # arranque genera una distinta y las sesiones se cierran al reiniciar
        # el .exe. La guardamos junto al ejecutable (se crea en el primer uso)
        # para que la sesión sobreviva entre ejecuciones.
        if not os.environ.get("EFA_SECRET_KEY"):
            os.environ["EFA_SECRET_KEY"] = _clave_persistente(dir_datos)
    else:
        # Ejecución normal: aseguramos el directorio del proyecto en sys.path.
        raiz = os.path.dirname(os.path.abspath(__file__))
        if raiz not in sys.path:
            sys.path.insert(0, raiz)


def _clave_persistente(dir_datos: str) -> str:
    """Lee (o crea la primera vez) la clave de firma guardada en disco."""
    import secrets
    ruta = os.path.join(dir_datos, "clave_sesion.txt")
    try:
        with open(ruta, encoding="utf-8") as f:
            clave = f.read().strip()
        if clave:
            return clave
    except (FileNotFoundError, OSError):
        pass
    clave = secrets.token_urlsafe(48)
    try:
        os.makedirs(dir_datos, exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(clave)
    except OSError:
        pass  # si no se puede escribir, se usa igualmente en memoria esta sesión
    return clave


def _abrir_navegador():
    time.sleep(1.8)
    try:
        webbrowser.open(URL)
    except Exception:
        pass


def main():
    _configurar_rutas()
    import uvicorn
    from backend.main import app

    print("=" * 60)
    print("  Plataforma EFA — Preparación de la certificación")
    print("=" * 60)
    print(f"  Abriendo la aplicación en: {URL}")
    print("  (Si el navegador no se abre solo, entra manualmente a esa dirección.)")
    print("  Para DETENER el servidor: cierra esta ventana o pulsa Ctrl + C.")
    print("=" * 60)

    threading.Thread(target=_abrir_navegador, daemon=True).start()
    uvicorn.run(app, host=HOST, port=PORT, log_level="warning")


if __name__ == "__main__":
    main()
