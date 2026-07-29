# Guía paso a paso: subir la Plataforma EFA a Render (gratis)

Esta guía te lleva de la mano, sin dar nada por supuesto, desde cero hasta tener
la aplicación funcionando en internet y accesible desde cualquier dispositivo
(móvil, tablet, otro ordenador), **de forma privada** (solo para las cuentas que
tú autorices).

Vamos a usar **Render**, que es **gratuito y NO pide tarjeta de crédito**, y sí
ejecuta Python/Docker (a diferencia de Hugging Face, que ahora cobra por Docker).

### ¿Cómo encaja el contenido con licencia?

Los exámenes y casos del libro (`examenes_reales.py`, `practicas_libro.py`) están
protegidos y **no** se suben a tu GitHub público. Para desplegarlos, vamos a
crear un **repositorio PRIVADO de GitHub** (solo tú lo ves) que sí los incluye, y
Render construirá la app desde ahí. Tu repo público actual se queda como está,
sin material con licencia.

Para que ese contenido **nunca** pueda escaparse al repo público por accidente,
lo aislamos en una **rama de git llamada `deploy`** que solo se envía al repo
privado. Es más fácil de lo que suena: son unos comandos que copiarás y pegarás.

> **Tiempo estimado:** 30-40 minutos la primera vez.
> **Coste:** 0 €. **Tarjeta:** no hace falta.

---

## Índice

1. [Antes de empezar](#1-antes-de-empezar)
2. [Crear el repositorio PRIVADO en GitHub](#2-crear-el-repositorio-privado-en-github)
3. [Subir TODO el contenido al repo privado (rama `deploy`)](#3-subir-todo-el-contenido-al-repo-privado)
4. [Crear la cuenta en Render y desplegar](#4-crear-la-cuenta-en-render-y-desplegar)
5. [Configurar las variables de entorno](#5-configurar-las-variables-de-entorno)
6. [Primer arranque y comprobación](#6-primer-arranque-y-comprobación)
7. [Activar el acceso con Google (opcional)](#7-activar-el-acceso-con-google-opcional)
8. [Comprobaciones finales](#8-comprobaciones-finales)
9. [Mantenimiento: actualizar la app más adelante](#9-mantenimiento-actualizar-la-app)
10. [Problemas frecuentes](#10-problemas-frecuentes)

---

## 1. Antes de empezar

Necesitas:

- **Git** instalado (ya lo usas).
- Tu cuenta de **GitHub** (la de `DkRunker`).
- Estos ficheros, que ya están preparados en tu carpeta `EFA con IA`:
  - `Dockerfile`, `.dockerignore`, `README.md` — **ya creados**.
  - `backend/content/examenes_reales.py` y `backend/content/practicas_libro.py`
    — el contenido con licencia (están en tu disco, protegidos por `.gitignore`).

Abre una terminal **dentro de la carpeta del proyecto** (`EFA con IA`). Todos los
comandos de esta guía se ejecutan ahí.

---

## 2. Crear el repositorio PRIVADO en GitHub

1. Entra en **https://github.com/new**.
2. Rellena:
   - **Repository name:** `EFA-privado` (o el nombre que quieras).
   - **Visibility:** ⚠️ marca **Private** (privado). Esto es lo importante.
   - **NO** marques "Add a README", "Add .gitignore" ni "license" (déjalo vacío
     para que no haya conflictos).
3. Pulsa **Create repository**.
4. GitHub te mostrará la dirección del repo. Será algo como:
   ```
   https://github.com/DkRunker/EFA-privado.git
   ```
   ✍️ **Apúntala.** La llamaremos **URL_REPO_PRIVADO**.

---

## 3. Subir TODO el contenido al repo privado

Ahora conectamos tu carpeta con ese repo privado y subimos **todo**, incluidos
los exámenes, en una rama separada llamada `deploy`.

Ejecuta estos comandos **uno a uno**, cambiando la URL por tu **URL_REPO_PRIVADO**:

**1) Añade el repo privado como un remoto llamado `privado`:**
```bash
git remote add privado https://github.com/DkRunker/EFA-privado.git
```

**2) Crea la rama de despliegue:**
```bash
git checkout -b deploy
```

**3) Añade a esa rama el contenido con licencia (el `-f` salta la protección
del `.gitignore`, solo en esta rama):**
```bash
git add -f backend/content/examenes_reales.py backend/content/practicas_libro.py
```

**4) Guarda el cambio en la rama `deploy`:**
```bash
git commit -m "Despliegue: incluir contenido con licencia"
```

**5) Sube la rama `deploy` SOLO al repo privado (el `-u` deja fijado que a partir
de ahora `deploy` va siempre a `privado`):**
```bash
git push -u privado deploy
```
- Usuario: tu usuario de GitHub.
- Contraseña: tu **token de GitHub** (si te lo pide; es el mismo tipo de token
  que ya usaste para subir a GitHub).

**6) Vuelve a la rama principal para tu trabajo del día a día:**
```bash
git checkout main
```

> 🔒 **REGLA DE ORO (para no filtrar los exámenes):**
> La rama `deploy` **solo** se sube a `privado`. **NUNCA** ejecutes
> `git push origin deploy`. Tu trabajo normal sigue en `main`, que va a `origin`
> (el repo público) y **no** contiene los exámenes.

Comprueba que ha ido bien: entra en `https://github.com/DkRunker/EFA-privado`,
cambia a la rama `deploy` (menú de ramas, arriba a la izquierda) y verifica que
en `backend/content/` aparecen `examenes_reales.py` y `practicas_libro.py`.

---

## 4. Crear la cuenta en Render y desplegar

### 4.1. Cuenta

1. Entra en **https://render.com** y pulsa **Get Started** / **Sign up**.
2. Regístrate **con GitHub** (botón "GitHub"). Es lo más cómodo: así Render
   podrá acceder a tu repo privado.
3. Cuando te pregunte, **autoriza a Render** a acceder a tus repos (puedes
   limitarlo solo a `EFA-privado`).

> Render **no pide tarjeta** para el plan gratuito.

### 4.2. Crear el servicio web

1. En el panel de Render, pulsa **New +** (arriba a la derecha) → **Web Service**.
2. En **Source Code**, elige **Build and deploy from a Git repository** y conecta
   tu repositorio **`EFA-privado`**. (Si no aparece, pulsa "Configure account" y
   dale acceso a ese repo.)
3. Render analizará el repo. Configura:
   - **Name:** el nombre que tendrá la app, por ejemplo `efa-prep`.
     ⚠️ Esto define tu dirección pública, que será:
     ```
     https://efa-prep.onrender.com
     ```
     ✍️ **Apúntala.** La llamaremos **URL_DE_TU_APP**. (Si el nombre está pillado,
     Render te avisa; elige otro.)
   - **Branch:** elige **`deploy`** (¡importante, no `main`!). Es la rama que
     tiene los exámenes.
   - **Region:** la más cercana (por ejemplo **Frankfurt**).
   - **Runtime / Language:** debe detectar **Docker** automáticamente (porque hay
     un `Dockerfile`). Si te deja elegir, elige **Docker**.
   - **Instance Type:** elige **Free**.
4. **Todavía no pulses "Create"**: antes añade las variables de entorno (paso 5),
   que están un poco más abajo en esa misma pantalla, en la sección
   **Environment Variables**.

---

## 5. Configurar las variables de entorno

En esa misma pantalla de creación (o luego en **Environment** del servicio), en
**Environment Variables**, añade con **Add Environment Variable**:

### 5.1. Obligatorias

| Key (nombre) | Value (valor) |
|---|---|
| `EFA_SECRET_KEY` | Una cadena larga y aleatoria (ver abajo). |
| `EFA_USUARIOS_PERMITIDOS` | Tu correo (y los de quien quieras), separados por comas. Ej: `bahillo.ortego.pablo@gmail.com` |
| `EFA_URL_FRONTEND` | **URL_DE_TU_APP**, ej: `https://efa-prep.onrender.com` |
| `EFA_ORIGENES_CORS` | Lo mismo: `https://efa-prep.onrender.com` |

**Para generar `EFA_SECRET_KEY`**, ejecuta en tu terminal:
```bash
python -c "import secrets; print(secrets.token_urlsafe(48))"
```
Copia lo que imprime y pégalo como valor.

> ⚠️ **`EFA_USUARIOS_PERMITIDOS` es lo que hace la app privada.** Solo esos
> correos podrán entrar. Si lo dejas vacío, entraría cualquiera: no lo dejes
> vacío.

### 5.2. Opcionales (Google, etc.)

Se explican en el **paso 7**. Si por ahora solo usarás usuario+contraseña,
sáltatelas.

### 5.3. Crear

Cuando tengas las 4 variables obligatorias, pulsa **Create Web Service**.
Render empezará a construir la imagen (tarda unos minutos: compila el frontend e
instala Python). Puedes seguir el progreso en la pestaña **Logs**.

---

## 6. Primer arranque y comprobación

1. Espera a que el estado del servicio sea **Live** (verde). En **Logs** verás al
   final algo como `Uvicorn running on http://0.0.0.0:...`.
2. Abre **URL_DE_TU_APP** (`https://efa-prep.onrender.com`) en el navegador.
3. Deberías ver la pantalla de acceso.

### Crea tu usuario

1. Entra en **Registrarse**.
2. Usa **el mismo correo** que pusiste en `EFA_USUARIOS_PERMITIDOS` y una
   contraseña.
3. Inicia sesión: deberías ver teoría, simuladores y exámenes.

> Si dice que tu cuenta no está autorizada, revisa que el correo coincide
> **exactamente** con el de `EFA_USUARIOS_PERMITIDOS`.

> **Sobre el plan gratuito de Render:**
> - La app **se duerme tras 15 minutos** sin uso. Al volver a abrirla, tarda
>   ~30-60 segundos en despertar. Es normal.
> - El almacenamiento es efímero: los usuarios registrados **con contraseña**
>   podrían borrarse si Render reinicia el servicio. Para el día a día es más
>   estable **acceder con Google** (paso 7), que no depende de guardar nada.

---

## 7. Activar el acceso con Google (opcional)

Permite entrar con "Continuar con Google", sin contraseñas, y es lo más robusto
en este hosting. Con Microsoft y Facebook el esquema es análogo.

### 7.1. Crear las credenciales en Google

1. Entra en **https://console.cloud.google.com/**.
2. Arriba, crea un proyecto nuevo (por ejemplo `EFA`).
3. Busca **"Pantalla de consentimiento de OAuth"** (OAuth consent screen):
   - Tipo de usuario: **External**. Rellena nombre y tu correo. Guarda.
   - En **Usuarios de prueba** añade tu correo (así entras sin publicar la app).
4. Ve a **"Credenciales" → "Crear credenciales" → "ID de cliente de OAuth"**:
   - Tipo: **Aplicación web**.
   - En **URI de redireccionamiento autorizados** → **Añadir URI**, pon
     EXACTAMENTE (cambiando por tu dominio):
     ```
     https://efa-prep.onrender.com/api/auth/oauth/google/callback
     ```
   - Pulsa **Crear**. Copia el **Client ID** y el **Client Secret**.

> ⚠️ La URI debe coincidir **carácter por carácter**. Un `/` de más o `http` en
> vez de `https` hace que falle.

### 7.2. Añadir las credenciales en Render

En **Environment** de tu servicio en Render, añade:

| Key | Value |
|---|---|
| `EFA_GOOGLE_CLIENT_ID` | el Client ID de Google |
| `EFA_GOOGLE_CLIENT_SECRET` | el Client Secret de Google |

Guarda. Render redespliega y aparecerá el botón **Continuar con Google**.

### 7.3. Microsoft y Facebook (si los quieres)

Mismo esquema; solo cambia el proveedor al final de la URI:

- Microsoft: `https://efa-prep.onrender.com/api/auth/oauth/microsoft/callback`
  (se crea en https://portal.azure.com → *Registros de aplicaciones*).
  Variables: `EFA_MICROSOFT_CLIENT_ID`, `EFA_MICROSOFT_CLIENT_SECRET`.
- Facebook: `https://efa-prep.onrender.com/api/auth/oauth/facebook/callback`
  (se crea en https://developers.facebook.com → *Facebook Login*).
  Variables: `EFA_FACEBOOK_CLIENT_ID`, `EFA_FACEBOOK_CLIENT_SECRET`.

Solo aparecen los botones de los proveedores cuyas credenciales configures.

---

## 8. Comprobaciones finales

- [ ] El servicio está **Live** en Render.
- [ ] Abres **URL_DE_TU_APP** y ves la pantalla de acceso.
- [ ] Inicias sesión (Google o usuario/contraseña).
- [ ] Ves la **teoría** de los módulos.
- [ ] Los **simuladores** calculan.
- [ ] Aparecen los **exámenes y simulacros** (si no, revisa que la rama en Render
      es `deploy` y que subiste bien los ficheros en el paso 3).
- [ ] Desde el **móvil**, con la misma URL, también entra y funciona.
- [ ] Una cuenta que **no** esté en `EFA_USUARIOS_PERMITIDOS` **no** puede entrar.

Si todo está ✔️, ya tienes la app desplegada, gratis y privada. 🎉

---

## 9. Mantenimiento: actualizar la app

Tu trabajo normal sigue en `main`. Cuando quieras publicar cambios de código,
lleva `main` a la rama `deploy` (que es la que Render construye):

```bash
git checkout deploy
git merge main -m "Actualizar despliegue"
git push privado deploy
git checkout main
```

Render detecta el push a `deploy` y **redespliega solo**.

- Si cambian los **exámenes** (`examenes_reales.py` / `practicas_libro.py`),
  después del `merge` vuelve a añadirlos con `-f` y haz commit antes del push:
  ```bash
  git add -f backend/content/examenes_reales.py backend/content/practicas_libro.py
  git commit -m "Actualizar contenido con licencia"
  ```
- Para actualizar tu repo **público** (sin exámenes): `git push origin main`.

> 🔒 Recuerda la regla de oro: **nunca** `git push origin deploy`.

---

## 10. Problemas frecuentes

**El despliegue falla en Render.**
Abre **Logs** y mira el error. Si es al construir, suele bastar con
**Manual Deploy → Clear build cache & deploy**.

**"Esta instalación es privada y tu cuenta no está autorizada".**
Tu correo no está en `EFA_USUARIOS_PERMITIDOS`, o hay una errata. Corrígelo en
**Environment** y espera al redepliegue.

**El botón de Google falla / "redirect_uri_mismatch".**
La URI en Google no coincide **exactamente** con
`https://TU-APP.onrender.com/api/auth/oauth/google/callback`. Revisa mayúsculas,
`https` y las barras.

**No aparecen los exámenes/simulacros.**
Casi seguro que Render está construyendo la rama equivocada. En **Settings** del
servicio, comprueba que **Branch = `deploy`**. Y que en el repo privado, rama
`deploy`, están los dos ficheros (paso 3).

**La primera carga tras un rato sin usar tarda mucho.**
El plan gratuito de Render **duerme** la app tras 15 min. Despierta en ~30-60 s.
Es normal.

**Me preocupa filtrar los exámenes al repo público.**
Mientras solo hagas `git push privado deploy` (nunca `git push origin deploy`) y
tu trabajo del día a día en `main`, el repo público **nunca** los tendrá: en
`main` siguen protegidos por `.gitignore`.

---

### Resumen de variables

| Variable | Obligatoria | Qué es |
|---|:--:|---|
| `EFA_SECRET_KEY` | ✅ | Clave aleatoria para firmar las sesiones. |
| `EFA_USUARIOS_PERMITIDOS` | ✅ | Correos autorizados, separados por comas. |
| `EFA_URL_FRONTEND` | ✅ | La URL pública de la app en Render. |
| `EFA_ORIGENES_CORS` | ✅ | Normalmente, la misma URL. |
| `EFA_GOOGLE_CLIENT_ID` / `_SECRET` | ⬜ | Acceso con Google. |
| `EFA_MICROSOFT_CLIENT_ID` / `_SECRET` | ⬜ | Acceso con Microsoft. |
| `EFA_FACEBOOK_CLIENT_ID` / `_SECRET` | ⬜ | Acceso con Facebook. |
