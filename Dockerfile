# Imagen de la Plataforma EFA para desplegar en Hugging Face Spaces (u otro
# hosting con Docker). Un solo contenedor sirve la API y el frontend compilado.
#
# El contenido con licencia (backend/content/examenes_reales.py y
# practicas_libro.py) no está en el repositorio público; si está presente en el
# contexto de construcción, se incluye en la imagen. Si no, la aplicación
# funciona igual con el banco propio.

# ---- Etapa 1: compilar el frontend (React + Vite) ----
FROM node:20-slim AS frontend
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

# ---- Etapa 2: servidor Python (FastAPI + uvicorn) ----
FROM python:3.12-slim
WORKDIR /app

# Dependencias del servidor
COPY requirements-portable.txt ./
RUN pip install --no-cache-dir -r requirements-portable.txt

# Código del backend (incluye el contenido con licencia si está en el contexto)
COPY backend/ ./backend/
# Frontend ya compilado en la etapa anterior
COPY --from=frontend /app/frontend/dist ./frontend/dist

# Hugging Face Spaces enruta al puerto declarado (7860 por defecto).
ENV PORT=7860
# En hosting gratuito el sistema de ficheros suele ser efímero o de solo
# lectura; los datos de usuario van a un directorio escribible. Con acceso por
# Google la sesión es sin estado, así que esto es suficiente.
ENV EFA_DATA_DIR=/tmp/efa_datos
EXPOSE 7860

# proxy-headers para que la app sepa que está tras un proxy HTTPS (el redirect
# de OAuth y las cookies dependen de conocer el esquema real).
CMD ["sh", "-c", "uvicorn backend.main:app --host 0.0.0.0 --port ${PORT} --proxy-headers --forwarded-allow-ips='*'"]
