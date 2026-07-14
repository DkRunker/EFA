# Plan — Mejoras de la teoría (por apartados) e importación de exámenes reales

> Orquestador (Claude) decide el detalle; el trabajo de contenido se delega a subagentes
> con **contexto mínimo**. Este plan se guarda para no olvidar ningún requisito.

## Requisitos del usuario (verbatim resumido)
1. **(IMPRESCINDIBLE)** Rehacer la teoría trabajando **apartado por apartado** (sección a sección),
   no módulo por módulo: hoy unos apartados están bien y otros pasan por encima de los conceptos.
2. En las **fórmulas**, definir **qué representa cada variable/letra** individualmente (hoy no se puede
   estudiar solo con la app porque faltan).
3. Cambiar el **formato**: junto a cada fórmula, incluir el **simulador correspondiente** para probar
   los cambios mientras se avanza.
4. Los **ejemplos resueltos** están al final del módulo → **intercalarlos** en el apartado que toca.
5. Los **errores comunes** están al final → **intercalarlos** en la parte correspondiente.
6. Añadir **3–4 enunciados de ejercicios por fórmula en cada apartado**; al corregirlos deben mostrar
   la **solución correcta y explicar el proceso** (el porqué).
7. Después, importar preguntas reales de examen desde
   `Examenes-certificacion-EFA-European-Financial-Advisor.pdf` (1089 págs., cientos de preguntas con
   respuesta y explicación) a los simuladores de test/examen. PDFs secundarios: `Simulación_*_Resuelta.pdf`.

## Hallazgos de exploración
- **Fuente**: PDF principal y web de referencia son de **Alberto Bernat** → coherencia total.
- **Formato del PDF de exámenes**: cada pregunta trae opciones `a/b/c/d`, línea
  `La respuesta correcta es la X.` y explicación detallada. Contiene además exámenes completos por año
  (sección 11: EFA 2018/2017/2016…) y casos prácticos (sección 12). Texto extraíble (con ruido de
  fórmulas que habrá que limpiar).
- **Sandbox actual**: 15 calculadoras (gordon_shapiro, sharpe, treynor, jensen, tae, precio_bono,
  irpf_ahorro, duracion_bono, tipo_forward, tipo_cambio_forward, ratio_informacion, ratio_sortino,
  cartera_dos_activos, valoracion_inmobiliaria, amortizacion_francesa) con estado `studyParams` y
  render por fórmula hardcodeado en `App.tsx`. Motor determinista en `backend/formulas.py`.
- **Teoría actual**: `APUNTES` (un string markdown por módulo) con secciones `##`, conceptos
  `[[término::definición]]`, fórmulas KaTeX, y ejemplos/errores agrupados al final.

## Diseño técnico

### A. Modelo de contenido por SECCIONES (refactor de soporte)
Cada `backend/content/mX.py` pasa a exponer, además de `NOMBRE` y `PREGUNTAS`:
```python
SECCIONES = [
  {
    "titulo": "Fundamentos Macroeconómicos",
    "cuerpo": "<markdown>",           # conceptos [[t::d]], fórmulas $$..$$, marcador [[sim:tae]],
                                       # callouts :::ejemplo / :::error intercalados
    "ejercicios": [
       {"enunciado": "...", "tipo": "numerico", "formula": "tae",
        "valor_esperado": 12.68, "tolerancia": 0.05, "explicacion": "paso a paso..."},
       {"enunciado": "...", "tipo": "opcion", "opciones": ["..",".."], "correcta": 1,
        "explicacion": "por qué..."},
    ],
  }, ...
]
```
`APUNTES` se deriva (compatibilidad con tests: `APUNTES_TEORICOS`, "Frontera Eficiente", longitud ≥3000).
`database.py` ensambla `SECCIONES_TEORICAS[modulo]` y mantiene `APUNTES_TEORICOS`.

### B. Marcadores nuevos en el `cuerpo` markdown
- `[[término::definición]]` — concepto con definición emergente (ya soportado).
- `[[sim:clave_formula]]` — inserta el **simulador** de esa fórmula en línea (nuevo).
- Callouts intercalados (nuevo):
  `:::ejemplo` … `:::`  (ejemplo resuelto) y  `:::error` … `:::` (error común) → caja estilizada.

### C. Simulador reutilizable (frontend)
Extraer de la Sandbox un componente `<FormulaSimulator formula="clave" />` que gestione sus
inputs/resultado (reutilizando la config por fórmula y `POST /api/formulas/calculate`). Se usa:
- En la pestaña **Sandbox** (`formula = selectedFormula`).
- **En línea en la teoría** donde aparezca `[[sim:clave]]`.

### D. API
- Nuevo `GET /api/study/secciones/{modulo}` → devuelve `SECCIONES` del módulo (título, cuerpo,
  ejercicios). Se mantiene `GET /api/study/apuntes` para compatibilidad.

### E. Render de la teoría (frontend)
- Cargar secciones; renderizar cada una: `<h2 id>` título + cuerpo (markdown con simuladores en línea,
  conceptos y callouts) + **widget de ejercicios**.
- El cuerpo se **trocea** en los marcadores `[[sim:clave]]`: se intercalan chunks de markdown con
  componentes `<FormulaSimulator>` (los widgets React no pueden ir dentro de `dangerouslySetInnerHTML`).
- Submenú lateral desde los títulos de sección (mecanismo ya existente, adaptado a datos estructurados).
- **Widget de ejercicios**: muestra enunciado + entrada (numérica o de opción) + botón "Comprobar" que
  revela solución correcta y explicación del proceso. Numéricos: se validan con tolerancia (o vía
  `/api/formulas/calculate`); de opción: se comprueba la correcta. Siempre se muestra el porqué.

### F. Metodología SECCIÓN A SECCIÓN de los subagentes
- Se trabaja por apartados con **checklist obligatorio por sección**:
  1. Explicar TODOS los conceptos del apartado en profundidad (sin pasar por encima).
  2. Cada fórmula: definir CADA variable/letra por separado.
  3. Colocar `[[sim:clave]]` junto a cada fórmula que tenga simulador.
  4. Intercalar aquí el/los ejemplo(s) resuelto(s) de ese apartado (`:::ejemplo`).
  5. Intercalar aquí los errores comunes de ese apartado (`:::error`).
  6. Añadir 3–4 `ejercicios` por fórmula, con `valor_esperado`/`correcta` y `explicacion` del proceso.
- Para evitar conflictos de fichero y el "glosado" de secciones tardías: cada subagente trabaja un
  **rango acotado de secciones** escribiendo a ficheros aislados en scratch, que el orquestador
  ensambla. Fuente: web/PDF de Alberto Bernat y la Guía oficial EFPA.

### G. Importación de exámenes reales (fase final)
- Extraer del PDF principal las preguntas (enunciado, 4 opciones, letra correcta, explicación),
  limpiando ruido de extracción. Un subagente normaliza por lotes de páginas.
- Cargar en el banco (`PREGUNTAS` por módulo, o un nuevo banco de "exámenes oficiales por año" para
  los simuladores de examen). Deduplicar. Verificar formato (4 opciones, índice 0–3) y consistencia.
- Los `Simulación_*_Resuelta.pdf` como fuente adicional.

## Fases y estado
- **H0** Refactor sandbox → componente `<FormulaSimulator>` reutilizable. *(orquestador)*
- **H1** Modelo `SECCIONES` + `database.py` + endpoint `/api/study/secciones`. *(orquestador)*
- **H2** Render de teoría por secciones: simuladores en línea, callouts, widget de ejercicios,
  troceo por `[[sim:]]`. *(orquestador)*
- **H3** Migrar el contenido actual a `SECCIONES` (sin pérdida) y validar. *(orquestador)*
- **H4** Reescritura **apartado por apartado** con el checklist (variables, sims, ejemplos/errores
  intercalados, 3–4 ejercicios por fórmula). *(subagentes por rangos de sección)*
- **H5** Importar preguntas del PDF de exámenes a los simuladores; deduplicar y validar. *(subagente + orquestador)*
- **H6** Revalidación (aprendiz sin conocimiento previo) + suite en verde + build + commit.

## Invariantes a preservar
- `PREGUNTAS` y `NOMBRE` intactos salvo ampliación deliberada (H5).
- Motor de cálculo determinista en Python (constitución del proyecto).
- Suite de tests en verde; término "Frontera Eficiente" en M3; escala IRPF 19/21/23/27/28.
- Fórmulas en KaTeX; definiciones de conceptos sin `]`, `|` ni `$`.
