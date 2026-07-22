# Plataforma EFA — Guía de uso

Aplicación de escritorio (local) para preparar la certificación **EFA (European Financial Advisor)**
de EFPA España: estudio de la teoría de los 10 módulos oficiales, práctica de fórmulas financieras
y simulación de exámenes (test y casos prácticos) con corrección explicada.

---

## 1. Requisitos

- **Windows 10/11**.
- **Python 3.11 o superior** instalado y añadido al PATH.
  - Si no lo tienes: descárgalo en <https://www.python.org/downloads/> y, durante la instalación,
    marca la casilla **“Add Python to PATH”**.
- Conexión a internet **solo la primera vez** (para instalar automáticamente las dependencias).

## 2. Cómo arrancar la aplicación

1. Haz **doble clic en `Iniciar_EFA.bat`**.
2. La primera vez instalará las dependencias necesarias (unos segundos).
3. Se abrirá automáticamente tu navegador en **<http://localhost:8000>**.
   - Si no se abriera solo, abre esa dirección manualmente.
4. Para **detener** la aplicación, cierra la ventana negra (consola) o pulsa `Ctrl + C` en ella.

> Alternativa manual (si prefieres la línea de comandos):
> ```bash
> pip install -r requirements-portable.txt
> python run_portable.py
> ```

### Opción B — Ejecutable independiente (sin Python)

Para usar la aplicación en un ordenador **que no tiene Python instalado**, puedes generar un
ejecutable autónomo:

1. En un equipo con Python y Node.js, haz doble clic en **`Crear_ejecutable.bat`**.
2. Se generará la carpeta **`dist\EFA_Prep\`** (~140 MB) con **`EFA_Prep.exe`**.
3. Copia esa carpeta completa al PC destino y haz **doble clic en `EFA_Prep.exe`**. No necesita
   Python ni instalación: arranca el servidor y abre el navegador automáticamente.

## 3. Cómo usar la plataforma

- **Registro / Acceso**: crea un usuario. Los datos se guardan de forma persistente en tu equipo
  (la contraseña cifrada, nunca en claro), así que no tienes que volver a registrarte cada vez.
  En la versión portable se guardan en la carpeta `datos_efa`, junto al ejecutable.
- **Estudiar (Teoría)**: consulta los apuntes de cada módulo **M1–M10**. Incluyen explicaciones,
  fórmulas matemáticas (renderizadas con KaTeX), ejemplos resueltos paso a paso y apartados de
  “errores frecuentes / claves de examen”.
- **Sandbox de fórmulas**: calcula de forma determinista fórmulas financieras (Gordon-Shapiro,
  Sharpe/Treynor/Jensen, precio y duración de bonos, TAE, cuota francesa, IRPF del ahorro, etc.).
- **Exámenes**: elige la modalidad y realiza una simulación:
  - **EIP (Nivel I)**: 40 preguntas tipo test.
  - **EFA Nivel II**: 40 preguntas test + 1 caso práctico.
  - **EFA Completo**: 50 preguntas test + 1 caso práctico.
  - Umbral de aprobado: **70%** en el test (y en la práctica, cuando aplica). Al entregar, verás la
    nota, el desglose de aciertos y la **explicación de cada pregunta**.

## 4. Corrección de los casos prácticos (opcional: IA)

La corrección de la parte práctica funciona **sin configuración** mediante un evaluador determinista
(valor numérico + conceptos clave de la rúbrica).

Opcionalmente, puedes activar una corrección cualitativa con IA (Google Gemini):
1. Crea un archivo `.env` en la carpeta `backend/` con el contenido:
   ```
   GEMINI_API_KEY=tu_clave_api
   ```
2. Reinicia la aplicación. Si la clave está presente, la evaluación de los desarrollos usará el modelo;
   si no, se usa automáticamente el evaluador determinista.

## 5. Contenido incluido

- **10 módulos** de teoría oficial (M1–M10) con explicaciones ampliadas y ejemplos resueltos.
- **365 preguntas tipo test** repartidas por módulos según la ponderación oficial de EFPA.
- **28 casos prácticos** (numéricos y conceptuales) con corrección y explicación.
- Las opciones de cada pregunta se **barajan** en cada examen para evitar la memorización posicional.

## 6. Solución de problemas

- **“No se ha encontrado Python”**: instala Python 3.11+ y marca “Add Python to PATH”.
- **El puerto 8000 está ocupado**: cierra la otra aplicación que lo use, o edita `run_portable.py`
  y cambia `PORT = 8000` (deberás usar 8000 salvo que también ajustes las URLs del frontend).
- **No se abre el navegador**: entra manualmente a <http://localhost:8000>.
- **Fallo al instalar dependencias**: comprueba tu conexión y ejecuta manualmente
  `pip install -r requirements-portable.txt`.

---

*Proyecto desarrollado con metodología SDD + TDD. El motor de cálculo financiero es determinista
(Python), garantizando la exactitud numérica de fórmulas y correcciones.*
