# Plataforma EFA — Preparación de la certificación

Aplicación privada para preparar el examen EFA (European Financial Advisor):
teoría por módulos, simuladores de fórmulas, banco de preguntas tipo test y
exámenes/simulacros.

## Cómo funciona el despliegue

Es un único contenedor Docker:

- **Frontend** (React + Vite) compilado y servido como estático.
- **Backend** (FastAPI + uvicorn) que sirve la API y ese frontend. Escucha en el
  puerto indicado por la variable `PORT` (los hosts como Render la asignan
  automáticamente; en local usa 7860 por defecto).

El acceso es **privado**: solo pueden entrar las cuentas incluidas en la lista
de permitidos (`EFA_USUARIOS_PERMITIDOS`). Se puede acceder con usuario y
contraseña o con Google / Microsoft / Facebook (los que estén configurados).

## Variables de entorno

| Variable | Para qué sirve |
|---|---|
| `EFA_SECRET_KEY` | Clave para firmar las sesiones (JWT). Obligatoria en producción. |
| `EFA_USUARIOS_PERMITIDOS` | Correos autorizados, separados por comas. Vacío = sin restricción. |
| `EFA_URL_FRONTEND` | URL pública de la app (para el retorno de OAuth). |
| `EFA_ORIGENES_CORS` | Orígenes permitidos para CORS (normalmente la misma URL). |
| `EFA_GOOGLE_CLIENT_ID` / `EFA_GOOGLE_CLIENT_SECRET` | Acceso con Google (opcional). |
| `EFA_MICROSOFT_CLIENT_ID` / `EFA_MICROSOFT_CLIENT_SECRET` | Acceso con Microsoft (opcional). |
| `EFA_FACEBOOK_CLIENT_ID` / `EFA_FACEBOOK_CLIENT_SECRET` | Acceso con Facebook (opcional). |

La guía completa paso a paso para desplegar gratis en **Render** está en
[`DESPLIEGUE_RENDER.md`](DESPLIEGUE_RENDER.md).

## Ejecutar en local

Versión portable (Windows): ejecuta `EFA_Prep.exe` en la carpeta `dist/`.
Desde el código: `python run_portable.py`.
