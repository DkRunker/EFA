# Guía paso a paso: subir la Plataforma EFA a Hugging Face Spaces

Esta guía te lleva de la mano, sin dar nada por supuesto, desde cero hasta tener
la aplicación funcionando en internet y accesible desde cualquier dispositivo
(móvil, tablet, otro ordenador), **de forma privada** (solo para las cuentas que
tú autorices).

Vas a usar **Hugging Face Spaces**, que es gratuito y sí ejecuta Python. La
aplicación se sube como una imagen **Docker** (un único contenedor que incluye
el frontend ya compilado y el backend).

> **Tiempo estimado:** entre 30 y 45 minutos la primera vez.
> **Coste:** 0 €.
> **No necesitas** saber programar. Solo copiar y pegar comandos y hacer clics.

---

## Índice

1. [Antes de empezar (lo que necesitas)](#1-antes-de-empezar)
2. [Crear la cuenta y el Space en Hugging Face](#2-crear-la-cuenta-y-el-space)
3. [Subir el código de la aplicación (git)](#3-subir-el-código-de-la-aplicación)
4. [Subir el contenido con licencia (exámenes)](#4-subir-el-contenido-con-licencia)
5. [Configurar los Secrets (variables de entorno)](#5-configurar-los-secrets)
6. [Primer arranque y comprobación](#6-primer-arranque-y-comprobación)
7. [Activar el acceso con Google / Microsoft / Facebook](#7-activar-el-acceso-con-google-etc-opcional)
8. [Comprobaciones finales](#8-comprobaciones-finales)
9. [Mantenimiento: actualizar la app más adelante](#9-mantenimiento-actualizar-la-app)
10. [Problemas frecuentes](#10-problemas-frecuentes)

---

## 1. Antes de empezar

Necesitas tener instalado en tu ordenador:

- **Git** (ya lo tienes: es lo que usamos para subir el código).
- Una cuenta de correo para registrarte en Hugging Face.

Y a mano, en tu carpeta del proyecto (`EFA con IA`), estos ficheros que ya están
preparados:

- `Dockerfile` — la receta para construir la aplicación. **Ya creado.**
- `.dockerignore` — lo que no se sube. **Ya creado.**
- `README.md` — con la cabecera que Hugging Face necesita. **Ya creado.**
- `backend/content/examenes_reales.py` y `backend/content/practicas_libro.py` —
  el contenido con licencia (exámenes y casos del libro). **Están en tu disco
  pero NO en GitHub** (los tienes protegidos en `.gitignore`).

> **Idea clave que debes entender:** el contenido con licencia NO se sube a
> GitHub (es público). Pero SÍ lo vamos a subir a tu Space de Hugging Face,
> porque tu Space va a ser **privado**. Lo subiremos en un paso aparte
> (paso 4), no con GitHub.

---

## 2. Crear la cuenta y el Space

### 2.1. Crear la cuenta

1. Entra en **https://huggingface.co/join**.
2. Regístrate con tu correo (o con Google, es indiferente).
3. Confirma el correo de verificación que te envían.

### 2.2. Crear el Space

1. Arriba a la derecha, pulsa tu **foto de perfil → New Space**.
   (O entra directamente a **https://huggingface.co/new-space**.)
2. Rellena:
   - **Owner:** tu usuario.
   - **Space name:** por ejemplo `efa-prep` (sin espacios; puedes usar guiones).
   - **License:** puedes dejar la que viene o poner `other`.
   - **Select the Space SDK:** elige **Docker** → **Blank / Empty**.
   - **Space hardware:** **CPU basic (free)**.
   - **Visibility:** ⚠️ elige **Private**. Esto es importante: el contenido con
     licencia solo debe verlo quien tú autorices.
3. Pulsa **Create Space**.

Ahora tu Space existe pero está vacío. Su dirección será algo como:

```
https://huggingface.co/spaces/TU_USUARIO/efa-prep
```

Y la web pública de la aplicación (cuando funcione) será:

```
https://TU_USUARIO-efa-prep.hf.space
```

> ✍️ **Apunta esa segunda dirección** (`https://TU_USUARIO-efa-prep.hf.space`).
> La vas a necesitar varias veces. La llamaremos **URL_DE_TU_APP**.

---

## 3. Subir el código de la aplicación

Hugging Face te da un repositorio git para tu Space. Vamos a enviar ahí el
código. Lo haremos con un **remoto git aparte** llamado `space`, para no mezclar
nada con tu GitHub público.

### 3.1. Consigue un token de acceso de Hugging Face

Para subir por git, Hugging Face pide un token (hace de contraseña):

1. Ve a **https://huggingface.co/settings/tokens**.
2. Pulsa **New token** (o **Create new token**).
3. Ponle un nombre, por ejemplo `subir-efa`.
4. En tipo/permiso elige **Write** (escritura).
5. Pulsa **Generate** y **copia el token** (empieza por `hf_...`). Guárdalo en un
   sitio seguro; no se vuelve a mostrar.

### 3.2. Conecta tu carpeta con el Space y sube el código

Abre una terminal **en la carpeta del proyecto** (`EFA con IA`) y ejecuta estos
comandos, **cambiando `TU_USUARIO` por tu usuario de Hugging Face**:

```bash
git remote add space https://huggingface.co/spaces/TU_USUARIO/efa-prep
```

Ahora sube el código a la rama `main` del Space:

```bash
git push space main
```

- Cuando te pida **usuario**, escribe tu usuario de Hugging Face.
- Cuando te pida **contraseña**, pega el **token `hf_...`** (no tu contraseña
  normal).

> Si `git push space main` se queja de que la rama del Space tiene contenido que
> tú no tienes (porque HF creó un commit inicial), ejecuta primero:
> ```bash
> git pull space main --allow-unrelated-histories --no-edit
> ```
> y vuelve a hacer `git push space main`.

Cuando termine, ve a la web de tu Space. Verás que empieza a **construir**
(_Building_). Tarda unos minutos porque compila el frontend e instala Python.

> ⚠️ **Todavía no funcionará del todo**, porque aún falta subir el contenido con
> licencia (paso 4) y configurar los Secrets (paso 5). Es normal. Continúa.

---

## 4. Subir el contenido con licencia

Estos dos ficheros están en tu ordenador pero **no** se han subido con git
(están protegidos en `.gitignore`, y así debe seguir siendo para que nunca
acaben en GitHub):

- `backend/content/examenes_reales.py`
- `backend/content/practicas_libro.py`

Los vamos a subir **directamente por la web de Hugging Face**, que al ser tu
Space privado es seguro:

1. Entra en la web de tu Space:
   `https://huggingface.co/spaces/TU_USUARIO/efa-prep`.
2. Pulsa la pestaña **Files** (Archivos), arriba.
3. Navega hasta la carpeta `backend` → `content` (haz clic en `backend`, luego
   en `content`).
4. Pulsa el botón **+ Add file → Upload files**.
5. Arrastra desde tu ordenador los dos ficheros:
   `examenes_reales.py` y `practicas_libro.py`
   (están en `EFA con IA\backend\content\`).
6. Abajo, en **Commit changes**, pulsa **Commit changes to main**.

Al confirmar, el Space se **reconstruye** solo e incluirá ya los exámenes.

> **¿Por qué así y no con git?** Porque `git push` respeta tu `.gitignore` y esos
> ficheros no viajarían. Subiéndolos por la web entran solo en tu Space privado,
> nunca en GitHub. Es exactamente lo que queremos.

---

## 5. Configurar los Secrets

Los "Secrets" son variables de configuración privadas (claves, tu lista de
correos autorizados, etc.). Se ponen en la web del Space:

1. En tu Space, pulsa **Settings** (Ajustes), arriba a la derecha.
2. Baja hasta **Variables and secrets**.
3. Ve añadiendo, uno a uno, con **New secret**:

### 5.1. Obligatorios

| Nombre (Name) | Valor (Value) |
|---|---|
| `EFA_SECRET_KEY` | Una cadena larga y aleatoria (ver abajo cómo generarla). |
| `EFA_USUARIOS_PERMITIDOS` | Tu correo (y los de quien quieras que entre), separados por comas. Ej: `bahillo.ortego.pablo@gmail.com` |
| `EFA_URL_FRONTEND` | **URL_DE_TU_APP**, es decir `https://TU_USUARIO-efa-prep.hf.space` |
| `EFA_ORIGENES_CORS` | Lo mismo: `https://TU_USUARIO-efa-prep.hf.space` |

**Para generar `EFA_SECRET_KEY`**, ejecuta en tu terminal:

```bash
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

Copia lo que imprime y pégalo como valor de `EFA_SECRET_KEY`.

> ⚠️ **`EFA_USUARIOS_PERMITIDOS` es lo que hace la app privada.** Solo esos
> correos podrán entrar (tanto por contraseña como por Google/Microsoft/
> Facebook). Si lo dejas **vacío**, entraría cualquiera que se registre: no lo
> dejes vacío en internet.

### 5.2. Opcionales (acceso con Google, etc.)

Estos se explican en el **paso 7**. Si por ahora solo vas a usar
usuario+contraseña, sáltatelos.

Cada vez que guardas un secret, el Space se reinicia. Es normal.

---

## 6. Primer arranque y comprobación

1. Ve a tu Space y espera a que el estado pase de **Building** a **Running**
   (verde). Puedes ver el progreso en la pestaña **Logs**.
2. Abre **URL_DE_TU_APP** en el navegador:
   `https://TU_USUARIO-efa-prep.hf.space`
3. Deberías ver la pantalla de acceso de la aplicación.

### Crea tu usuario con contraseña

1. En la pantalla de acceso, entra en **Registrarse**.
2. Usa **el mismo correo** que pusiste en `EFA_USUARIOS_PERMITIDOS` y una
   contraseña.
3. Inicia sesión. Deberías ver la teoría, los simuladores y los exámenes.

> Si al registrarte te dice que tu cuenta no está autorizada, revisa que el
> correo coincide **exactamente** con el de `EFA_USUARIOS_PERMITIDOS`
> (sin espacios, mismas mayúsculas/minúsculas da igual, pero el texto sí).

> **Aviso sobre los usuarios de contraseña:** en el hosting gratuito el
> almacenamiento es efímero (se puede reiniciar). Los usuarios registrados con
> contraseña podrían borrarse si el Space se reinicia por completo. Por eso, para
> el uso diario, es **más cómodo y estable acceder con Google** (paso 7): ese
> acceso no depende de guardar nada, solo de tu lista de correos permitidos.

---

## 7. Activar el acceso con Google (etc.) — opcional

Esto permite entrar con un botón "Continuar con Google" sin recordar
contraseñas, y es la forma más robusta en este hosting. Se explica con Google;
Microsoft y Facebook son análogos.

### 7.1. Crear las credenciales en Google

1. Entra en **https://console.cloud.google.com/**.
2. Arriba, crea un proyecto nuevo (por ejemplo `EFA`).
3. En el buscador de arriba, busca **"APIs y servicios" → "Pantalla de
   consentimiento de OAuth"** (OAuth consent screen).
   - Tipo de usuario: **External**.
   - Rellena nombre de la app y tu correo de contacto. Guarda.
   - En **Usuarios de prueba** añade tu correo (así puedes entrar sin publicar
     la app).
4. Ahora ve a **"Credenciales" → "Crear credenciales" → "ID de cliente de
   OAuth"**.
   - Tipo de aplicación: **Aplicación web**.
   - En **URI de redireccionamiento autorizados**, pulsa **Añadir URI** y pon
     EXACTAMENTE:
     ```
     https://TU_USUARIO-efa-prep.hf.space/api/auth/oauth/google/callback
     ```
     (cambia `TU_USUARIO-efa-prep` por lo tuyo).
   - Pulsa **Crear**.
5. Google te muestra un **Client ID** y un **Client Secret**. Cópialos.

> ⚠️ La URI de redirección debe coincidir **carácter por carácter** con la de
> arriba. Un `/` de más o `http` en vez de `https` hace que falle.

### 7.2. Poner las credenciales como Secrets

En **Settings → Variables and secrets** de tu Space, añade:

| Nombre | Valor |
|---|---|
| `EFA_GOOGLE_CLIENT_ID` | el Client ID que te dio Google |
| `EFA_GOOGLE_CLIENT_SECRET` | el Client Secret que te dio Google |

Guarda. El Space se reinicia y aparecerá el botón **Continuar con Google** en la
pantalla de acceso.

### 7.3. Microsoft y Facebook (si los quieres)

Es el mismo esquema. La URI de redirección cambia solo el proveedor al final:

- Microsoft: `https://TU_USUARIO-efa-prep.hf.space/api/auth/oauth/microsoft/callback`
  - Se crea en **https://portal.azure.com** → *Microsoft Entra ID* →
    *Registros de aplicaciones* → *Nuevo registro*. Copia *Application (client)
    ID* y crea un *Client secret*.
  - Secrets: `EFA_MICROSOFT_CLIENT_ID`, `EFA_MICROSOFT_CLIENT_SECRET`.
- Facebook: `https://TU_USUARIO-efa-prep.hf.space/api/auth/oauth/facebook/callback`
  - Se crea en **https://developers.facebook.com** → *Mis apps* → *Crear app* →
    producto *Facebook Login*.
  - Secrets: `EFA_FACEBOOK_CLIENT_ID`, `EFA_FACEBOOK_CLIENT_SECRET`.

Solo aparecen los botones de los proveedores cuyas credenciales hayas puesto.

---

## 8. Comprobaciones finales

Repasa esta lista:

- [ ] El Space está en **Running** (verde).
- [ ] Abres `https://TU_USUARIO-efa-prep.hf.space` y ves la pantalla de acceso.
- [ ] Puedes iniciar sesión (con Google o con tu usuario/contraseña).
- [ ] Ves la **teoría** de los módulos.
- [ ] Los **simuladores de fórmulas** calculan.
- [ ] Aparecen los **exámenes y simulacros** (si no aparecen, revisa que subiste
      bien `examenes_reales.py` en el paso 4).
- [ ] Desde el **móvil**, con la misma URL, también entra y funciona.
- [ ] Una cuenta **que NO esté** en `EFA_USUARIOS_PERMITIDOS` **no** puede entrar.

Si todo eso está ✔️, ya tienes la aplicación desplegada y privada. 🎉

---

## 9. Mantenimiento: actualizar la app

Cuando cambies algo del código en tu ordenador y quieras publicarlo:

```bash
git add -A
git commit -m "describe tu cambio"
git push space main
```

El Space se reconstruye solo. (Si además usas GitHub, recuerda que a GitHub se
sube con `git push origin main`, y ahí el contenido con licencia sigue sin ir.)

Si actualizas los **exámenes** (`examenes_reales.py` o `practicas_libro.py`),
vuelve a subirlos por la web como en el **paso 4** (porque git los ignora).

---

## 10. Problemas frecuentes

**El Space se queda en "Building" y falla.**
Abre la pestaña **Logs** y mira el error. Lo más habitual es un fallo al
compilar; suele bastar con volver a lanzar la construcción (**Settings →
Factory reboot** / *Restart this Space*).

**"Esta instalación es privada y tu cuenta no está autorizada".**
Tu correo no está en `EFA_USUARIOS_PERMITIDOS`, o hay una errata. Corrige el
secret y espera a que reinicie.

**El botón de Google falla / "redirect_uri_mismatch".**
La URI de redirección en Google no coincide **exactamente** con
`https://TU_USUARIO-efa-prep.hf.space/api/auth/oauth/google/callback`. Revisa
mayúsculas, `https`, y que no sobre ninguna barra.

**Entré con contraseña ayer y hoy no está mi usuario.**
El almacenamiento gratuito es efímero. Usa el acceso con **Google** para el día
a día (no depende de guardar usuarios), o vuelve a registrarte.

**No aparecen los exámenes/simulacros.**
No se subió el contenido con licencia. Repite el **paso 4**.

**La página tarda en cargar la primera vez tras un rato sin usarla.**
Los Spaces gratuitos "se duermen" si no se usan. Al abrirlos, despiertan en unos
segundos. Es normal.

---

### Resumen de las variables de configuración

| Variable | Obligatoria | Qué es |
|---|:--:|---|
| `EFA_SECRET_KEY` | ✅ | Clave aleatoria para firmar las sesiones. |
| `EFA_USUARIOS_PERMITIDOS` | ✅ | Correos autorizados, separados por comas. |
| `EFA_URL_FRONTEND` | ✅ | La URL pública del Space. |
| `EFA_ORIGENES_CORS` | ✅ | Normalmente, la misma URL del Space. |
| `EFA_GOOGLE_CLIENT_ID` / `_SECRET` | ⬜ | Acceso con Google. |
| `EFA_MICROSOFT_CLIENT_ID` / `_SECRET` | ⬜ | Acceso con Microsoft. |
| `EFA_FACEBOOK_CLIENT_ID` / `_SECRET` | ⬜ | Acceso con Facebook. |
