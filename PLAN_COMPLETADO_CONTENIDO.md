# Plan de Completado de Contenido — Plataforma EFA

> Orquestador (Claude) toma las decisiones de detalle; el trabajo de contenido se delega a
> **un subagente autónomo por paquete de trabajo**, con **contexto mínimo** (solo la rebanada
> del temario oficial de su módulo + el esquema de datos), de forma **secuencial** para no
> saturar la ventana de contexto global ni provocar conflictos de edición.

## Fuente de verdad
- `GUIA_DE_CERTIFICACION_EFA.pdf` (Guía oficial EFPA, V1/26, 103 págs.) → temario por módulos M1–M10.
- Rebanadas extraídas por módulo en `scratchpad/syllabus/M*_syllabus.txt` (contexto mínimo por subagente).
- `Desarrollo Plataforma EFA con IA.md` → metodología SDD+TDD y patrón orquestador/subagente.

## Estado inicial (diagnóstico)
- Backend FastAPI + `formulas.py` (15 fórmulas deterministas) + `evaluator.py` (Gemini con fallback por reglas).
- `database.py`: **62** preguntas test (M1=15,M2=6,M3=10,M4=5,M5=4,M6=3,M7=3,M8=6,M9=5,M10=5), **3** prácticas (M3,M3,M8), apuntes de los 10 módulos (2K–8K chars c/u).
- 33 tests en verde. `test_main` exige `len==50` en EFA Completo y `"Frontera Eficiente"` en M3.
- `test_ten_exams_simulation` hardcodea respuestas prácticas de ids 1001/1002/1003 (frágil ante nuevas prácticas).

## Objetivo
Contenido **completo, correcto e internamente consistente**: un aprendiz sin conocimiento previo,
estudiando SOLO la app, debe superar 10 exámenes. Requiere que cada pregunta sea respondible desde
la teoría y que los valores numéricos de las prácticas concuerden con `formulas.py`.

## Arquitectura de contenido (refactor de soporte)
Dividir el contenido en `backend/content/` — un fichero por módulo (`m1.py`…`m10.py`) con
`NOMBRE`, `PREGUNTAS` (tuplas) y `APUNTES` (str), más `practicas.py`. `database.py` pasa a ser un
ensamblador fino que conserva la API pública (`PREGUNTAS_TEST`, `PREGUNTAS_PRACTICAS`,
`APUNTES_TEORICOS`, `generar_examen`). Esto da a cada subagente **un único fichero pequeño** que
editar, sin conflictos.

## Objetivos de volumen (banco para 10 exámenes con variedad)
| Mód | Peso | Draw/50 | Test objetivo | Prácticas |
|-----|------|---------|---------------|-----------|
| M1  | 25%  | 13 | ≥30 | 2 |
| M2  | 10%  | 5  | ≥14 | 1 |
| M3  | 17.5%| 9  | ≥24 | 2 |
| M4  | 7.5% | 4  | ≥12 | 1 |
| M5  | 5%   | 3  | ≥10 | 1 |
| M6  | (prorr.) | 2 | ≥8 | 1 |
| M7  | (prorr.) | 2 | ≥8 | 1 |
| M8  | 10%  | 5  | ≥14 | 2 |
| M9  | 7.5% | 4  | ≥12 | 1 |
| M10 | 7.5% | 3  | ≥10 | 1 |
Total test ≈ **150+**, prácticas ≈ **13**.

## Fases
- **F0 Diagnóstico** — ✅ hecho.
- **F1 Refactor de soporte** — ✅ migrado a `backend/content/`, tests verdes. (Orquestador)
- **F2 Contenido por módulo (M1–M10)** — ✅ un subagente por módulo (contexto mínimo, editando un
  único fichero): APUNTES ampliados a cobertura completa del temario oficial (KaTeX) y PREGUNTAS
  ampliadas y verificadas. (10 subagentes)
- **F3 Prácticas** — ✅ `practicas.py` a 15 casos con valores verificados con `formulas.py`;
  `test_ten_exams_simulation` responde ahora cualquier práctica genéricamente.
- **F4 Validación de consistencia** — ✅ `test_content_consistency.py`: índices válidos, distribución
  de examen alcanzable, prácticas cuadran con fórmulas. Suite en verde.
- **F5 Aprendiz sin conocimiento previo** — ✅ auditoría independiente (2 subagentes) → 1 defecto
  corregido (FII 70%). Corregido el sesgo posicional (96% de claves en A) con barajado determinista
  en el ensamblado. Aprendiz que estudia SOLO los apuntes: **235/235 (100%)** y **10/10 exámenes
  aprobados**.

## Validación final (fase F)
- `pytest`: **39/39 en verde**.
- Smoke API en vivo (EFA Completo): test 100%, práctica 100%, aprobado_general = True.
- Aprendiz (solo apuntes): 100% de aciertos por módulo; 10/10 exámenes ≥70%.

---

## Ampliación (fase G): más contenido, revalidación y portable
- **Teoría enriquecida** (G1): cada módulo con intuición, ejemplos resueltos paso a paso y
  apartados de "errores frecuentes / claves de examen". Apuntes de ~8K–30K chars por módulo.
- **Banco ampliado** (G2): **365 preguntas test** (M1=57, M2=41, M3=44, M4=30, M5=31, M6=28,
  M7=30, M8=37, M9=36, M10=31).
- **Prácticas ampliadas** (G3): **28 casos** (20 numéricos verificados con `formulas.py` + 8
  conceptuales evaluados por palabras clave, cubriendo M2, M4, M5, M9, M10).
- **Revalidación** (G4): auditoría independiente (2 subagentes) → **1 defecto** (gravamen SOCIMI
  19% vs 15%), corregido en pregunta y teoría. Aprendiz que estudia SOLO los apuntes: **365/365
  (100%)** y **10/10 exámenes aprobados**.
- **Portable** (G5): frontend compilado y servido por FastAPI; lanzador `Iniciar_EFA.bat` (usa
  Python del sistema) y `Crear_ejecutable.bat` (genera `EFA_Prep.exe` autónomo con PyInstaller,
  probado y funcional). Guía en `INSTRUCCIONES_DE_USO.md`.
- **Suite**: **40/40 en verde** (incluye `test_content_consistency.py` con verificación de las
  prácticas numéricas y conceptuales).

## Resultado alcanzado (contenido final)
- Banco de test: **235 preguntas** (M1=39, M2=27, M3=28, M4=21, M5=20, M6=18, M7=18, M8=22, M9=22, M10=20).
- **15 prácticas** (M1×4, M3×5, M6×1, M7×2, M8×3), todas con valor verificado contra `formulas.py`.
- Apuntes ampliados a cobertura completa del temario oficial (8K–23K chars/módulo).
- Suite: **39 tests en verde** (incluye nuevo `test_content_consistency.py` y simulación de 10 exámenes estable).

## Reglas para subagentes (contexto mínimo)
1. Editar **solo** el fichero asignado. Prohibido tocar otros módulos, fórmulas o frontend.
2. Preservar términos ya testeados (p.ej. "Frontera Eficiente" en M3).
3. Cada pregunta: 4 opciones, una sola correcta e inequívoca, explicación que la justifique.
4. Todo dato numérico de práctica debe reproducirse con una función de `formulas.py`.
5. Devolver un resumen corto (conteos), no volcar el contenido generado.
