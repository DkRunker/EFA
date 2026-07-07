# Constitución de la Plataforma EFA (EFA Platform Constitution)

Este documento establece las directrices técnicas, arquitectónicas y de desarrollo para la construcción de la plataforma de preparación de la certificación EFA.

## 1. Paradigma de Desarrollo (SDD & TDD)
- **Spec-Anchored**: Toda funcionalidad nueva o modificación debe contar con una especificación previa en el directorio `.specify/` (formato Gherkin o Markdown).
- **Test-First (TDD)**:
  1. Se crea la especificación del componente.
  2. Se escribe la suite de pruebas unitarias que define el comportamiento esperado (los tests deben fallar inicialmente).
  3. Se escribe el código mínimo para hacer pasar los tests (Fase Green).
  4. Se refactoriza el código manteniendo los tests en verde.

## 2. Arquitectura de Software
- **Backend (Python / FastAPI)**:
  - Responsable de la persistencia de datos (exámenes, preguntas, perfiles de alumnos).
  - Aloja el motor de cálculo financiero determinista (`backend/formulas.py`).
  - **REGLA CRÍTICA**: Los modelos de IA no deben realizar cálculos aritméticos o financieros complejos sobre texto. Toda evaluación numérica se delega a funciones deterministas en Python.
- **Frontend (Vite / React / TypeScript / Vanilla CSS)**:
  - Interfaz de usuario rica, moderna y fluida.
  - Diseño responsive y premium (paleta de colores curada, modo oscuro, KaTeX para la visualización de fórmulas matemáticas).
  - Sin dependencias de frameworks CSS invasivos (se usará Vanilla CSS de alto rendimiento).

## 3. Estructura de Archivos
```text
/
├── .specify/             # Especificaciones técnicas (Gherkin/Markdown)
├── backend/              # Backend en Python (FastAPI + Pytest)
│   ├── formulas.py       # Fórmulas financieras deterministas
│   ├── simulator.py      # Motor de simulación de exámenes
│   ├── main.py           # Endpoints de la API
│   └── test_*.py         # Suite de pruebas unitarias de Python
└── frontend/             # Frontend en React + Vite + Vitest
```
