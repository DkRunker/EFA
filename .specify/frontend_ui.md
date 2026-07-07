# Especificaciones de la Interfaz de Usuario (.specify/frontend_ui.md)

Este documento detalla los requerimientos visuales y de interacción del cliente de la plataforma EFA.

## Criterios de Aceptación y Flujo de Pantallas

### 1. Paleta de Colores y Estilo (Aesthetics)
- **Tema**: Principalmente modo oscuro premium con acentos en azul eléctrico y púrpura neon.
- **Tokens de Color (CSS)**:
  - Fondo base: HSL (224, 25%, 12%) - Azul grisáceo muy oscuro.
  - Fondo de tarjetas: HSL (224, 25%, 16%) - Con efecto glassmorphic (border sutil semi-transparente, backdrop-filter).
  - Acento principal: HSL (263, 70%, 50%) - Púrpura brillante.
  - Acento secundario: HSL (190, 90%, 50%) - Cyan / Azul eléctrico.
  - Aprobados / Éxito: HSL (142, 70%, 45%) - Verde esmeralda.
  - Suspensos / Error: HSL (350, 80%, 50%) - Rojo carmín.

### 2. Panel de Control (Dashboard)
- **Visualización**:
  - Un gráfico circular o barra de progreso general con la media de aciertos histórica.
  - Un listado de tarjetas por módulo (M1 a M10) indicando la solidez estimada (porcentaje de aciertos en preguntas de ese módulo).
  - Tres botones grandes para iniciar:
    - **EIP (Asesor Financiero Nivel I)**: Simulación de 40 preguntas tipo test (1h 30m).
    - **EFA Nivel II**: Simulación de 40 preguntas tipo test + 1 caso práctico (2h 30m en total).
    - **EFA Completo**: Simulación de 50 preguntas tipo test + 1 caso práctico (2h 30m en total).

### 3. Interfaz del Simulador
- **Cabecera**:
  - Muestra el nombre del examen y un temporizador que descuenta los segundos.
  - Si el tiempo se agota, el examen se entrega automáticamente.
- **Cuerpo principal**:
  - Sección izquierda: Lista de navegación de preguntas (permite saltar directamente a cualquier pregunta; muestra visualmente cuáles ya han sido contestadas).
  - Sección central: Enunciado de la pregunta activa. Si es tipo test, presenta 4 opciones marcables de tipo radio button. Si es práctica, presenta una caja de texto grande (`textarea`) para redactar la explicación e indicar el resultado del cálculo.
- **Acciones**:
  - Botón de "Anterior" y "Siguiente".
  - Botón de "Entregar Examen" destacado con una advertencia de confirmación.

### 4. Reporte de Resultados y Corrección Profunda
- **Resumen general**:
  - Calificación final (aprobado o suspenso).
  - Desglose de puntuación de la parte teórica y de la parte práctica.
- **Corrección de test**:
  - Muestra la pregunta, la opción del alumno (marcando en rojo si falló) y la opción correcta (en verde).
  - Despliega un panel colapsable con la explicación analítica detallada de por qué es la opción correcta y por qué fallaron las otras (justificación de distractores).
- **Corrección de práctica**:
  - Muestra la respuesta redactada por el alumno.
  - Muestra la cuota y puntuación asignada por el motor de evaluación (con desglose de los puntos de la rúbrica cumplidos y fallidos).
  - Muestra la justificación cuantitativa y cualitativa oficial.
