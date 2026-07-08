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
    else:
        # Ejecución normal: aseguramos el directorio del proyecto en sys.path.
        raiz = os.path.dirname(os.path.abspath(__file__))
        if raiz not in sys.path:
            sys.path.insert(0, raiz)


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
