# **Diseño Arquitectónico de una Plataforma Inteligente de Preparación EFA: Desarrollo Concurrente SDD-TDD y Orquestación de Agentes Multi-Modelo**

La obtención de la certificación de Asesor Financiero Europeo (EFA, por sus siglas en inglés), otorgada en España por la European Financial Planning Association (EFPA), representa uno de los hitos más exigentes para los profesionales del sector de la banca personal y la planificación patrimonial1. Con la plena vigencia de la directiva comunitaria MiFID II, disponer de una certificación acreditada es un requisito imperativo para el ejercicio de las labores de asesoramiento financiero directo2. La preparación para este examen requiere no solo la asimilación memorística de un temario multidisciplinar y denso, sino la capacidad de resolver casos prácticos donde la argumentación y la precisión matemática son evaluadas de forma concurrente3.  
Para dar respuesta a estas necesidades, se proyecta el diseño de una plataforma de preparación avanzada que integra simulaciones de exámenes reales de convocatorias previas, exámenes generados dinámicamente y un motor explicativo de corrección profunda4. La construcción de este sistema no se aborda mediante metodologías convencionales de ingeniería de software, sino a través de un enfoque de Inteligencia Artificial nativo fundamentado en el Desarrollo Basado en Especificaciones (SDD) y el Desarrollo Guiado por Pruebas (TDD)6. El núcleo operativo del desarrollo se confía a un patrón de diseño jerárquico de Orquestador y Sub-agentes8. Este diseño aísla los entornos de ejecución y minimiza la huella de memoria del sistema mediante la segregación estricta del contexto de trabajo11.

## **Estructura Exponencial y Exigencias del Examen EFA**

El diseño de la plataforma de preparación debe ajustarse fielmente a las normativas de evaluación y a la variabilidad estructural que EFPA España aplica en las distintas convocatorias de examen4. La flexibilidad de la plataforma para adaptarse a estas condiciones de evaluación es crítica para ofrecer simulaciones realistas4.

### **Comparativa de Estructuras Oficiales de Examen**

El motor de simulación de la plataforma debe modelar de forma diferenciada las tres modalidades principales de evaluación vigentes en el esquema de certificación de EFPA España15. Los parámetros técnicos de configuración del motor de exámenes se estructuran de la siguiente manera:

| Parámetro del Sistema | EIP (EFA Nivel I) | EFA Nivel II | EFA Completo |
| :---- | :---- | :---- | :---- |
| **Preguntas de la Parte I (Test)** | 40 preguntas tipo test15 | 40 preguntas tipo test3 | 50 preguntas tipo test4 |
| **Umbral de Aprobado (Test)** | Mínimo 70% (28 aciertos)15 | Mínimo 70% (28 aciertos)3 | Mínimo 70% (35 aciertos)4 |
| **Penalización por Error** | No resta puntos15 | No resta puntos3 | No resta puntos4 |
| **Duración de la Parte I** | 1 hora y 30 minutos15 | 1 hora y 30 minutos3 | 1 hora y 30 minutos4 |
| **Estructura de la Parte II** | No aplicable15 | Resolución de ejercicios prácticos3 | Resolución de ejercicios prácticos4 |
| **Duración de la Parte II** | No aplicable15 | 1 hora de duración3 | 1 hora de duración4 |
| **Criterio de Calificación** | Solo respuestas correctas16 | Aprobado independiente en test y práctica con valoración del razonamiento3 | Aprobado independiente en test y práctica con valoración del razonamiento4 |

Es sumamente relevante destacar que el examen EFA de acceso directo (EFA Completo) exige que el alumno apruebe ambas partes de forma independiente4. En la segunda prueba, de carácter eminentemente cuantitativo y analítico, el tribunal calificador no se limita a contrastar la solución numérica final obtenida, sino que evalúa de forma prioritaria la calidad de la explicación cualitativa, el rigor en el uso de las variables y la coherencia de los argumentos de razonamiento financiero empleados por el aspirante3. Asimismo, la normativa fiscal aplicada debe corresponderse estrictamente con el marco legal del país de realización de la prueba, lo que añade una capa de complejidad al motor explicativo debido a la actualización constante de la legislación española4.

### **Ponderación y Distribución del Temario Oficial EFA 2026**

La plataforma segmentará su banco de preguntas de test y ejercicios prácticos utilizando un sistema de pesos dinámicos basado en las directrices de EFPA España18. Las simulaciones de exámenes reales y mock-ups generarán cuestionarios representativos que respetarán los siguientes porcentajes de distribución y focos temáticos18:

| Módulo del Programa | Peso Oficial | Áreas Clave de Evaluación y Fórmulas Asociadas |
| :---- | :---- | :---- |
| **M1: Instrumentos y Mercados Financieros** | 25,0% | Indicadores macroeconómicos, políticas monetarias, valoración de renta fija y variable, productos derivados y criterios ESG18. |
| **M2: Fondos y Sociedades de Inversión** | 10,0% | Tipología de fondos, análisis de estilos de gestión, Hedge Funds, selección cualitativa y cuantitativa de fondos18. |
| **M3: Gestión de Carteras** | 17,5% | Teoría de Markowitz, frontera eficiente, modelo CAPM, cálculo de Beta, ratios de Sharpe, Treynor y Jensen18. |
| **M4: Seguros** | 7,5% | Contrato de seguro, coberturas de riesgos personales, seguros de vida y de ahorro-inversión, fiscalidad de primas18. |
| **M5: Pensiones y Jubilación** | 5,0% | Planes y fondos de pensiones, planificación financiera de la jubilación, estimación de flujos de ingresos y gastos18. |
| **M6: Inversión Inmobiliaria** | *S/D (Prorrateado)* | Productos de inversión inmobiliaria, metodologías de valoración de inmuebles y fiscalidad asociada19. |
| **M7: Crédito y Financiación** | *S/D (Prorrateado)* | Estructura de préstamos hipotecarios, análisis del riesgo de particulares, cálculo de TIN y TAE, apalancamiento19. |
| **M8: Fiscalidad de las Inversiones** | 10,0% | Tratamiento del IRPF, rendimientos del capital mobiliario, ganancias y pérdidas patrimoniales, IP, ISD y su impacto financiero18. |
| **M9: Legislación, Normativa y Ética** | 7,5% | Directiva MiFID II, prevención del blanqueo, protección de datos, finanzas digitales (MiCA) y Código Ético EFPA18. |
| **M10: Asesoramiento y Planificación** | 7,5% | Perfilado de clientes, estados patrimoniales familiares, determinación de objetivos y planificación del ciclo de vida18. |

## **Motores de Explicación Financiera y Razonamiento Cuantitativo**

La principal exigencia de la plataforma es que el sistema no se limite a ofrecer una validación dicotómica de correcto o incorrecto, sino que desarrolle un motor de argumentación explicativa detallada para cada opción de respuesta5. Esta funcionalidad de corrección profunda requiere abordar dos tipos de razonamientos diferenciados: cualitativos y cuantitativos2.

### **El Reto de la Precisión Numérica en Entornos de IA**

Los modelos de lenguaje (LLM) tradicionales demuestran limitaciones estructurales severas al realizar tareas de matemática financiera bajo métodos probabilísticos nativos5. Estas limitaciones se derivan principalmente de tres factores:

1. **La segmentación del tokenizador**: Al procesar números, los algoritmos de tokenización fragmentan cadenas numéricas continuas en sub-tokens basados en frecuencia estadística (por ejemplo, el número 87439 puede transformarse en tokens inconexos como 87 y 439), impidiendo al modelo percibir correctamente el valor posicional de las cifras22.  
2. **La variabilidad de formatos locales**: Expresiones equivalentes como 1.000,50, 1000.50 o 1 000,50 desestabilizan las predicciones probabilísticas del modelo de lenguaje al alterar las secuencias lógicas del entrenamiento de base22.  
3. **La incapacidad en la propagación de acarreos**: En multiplicaciones o divisiones complejas de varios dígitos, la IA tiende a emular de memoria patrones visuales próximos en lugar de computar la lógica del algoritmo matemático paso a paso, lo que resulta en alucinaciones numéricas sutiles pero inaceptables en un entorno financiero profesional22.

Para solventar esta debilidad, la plataforma adopta un patrón híbrido en el que toda la lógica de cálculo aritmético y financiero se externaliza de forma estricta a un intérprete determinista de Python5. El LLM se reserva exclusivamente para las tareas de análisis semántico, la generación del plan de cálculo paso a paso, la estructuración del código en Python y la posterior redacción pedagógica de la explicación en lenguaje natural para el estudiante5.

### **Arquitectura de Representación de Fórmulas y Razonamiento Secuencial**

Para modelar problemas financieros que involucren razonamiento de múltiples etapas (como la obtención de la rentabilidad de una cartera a través de varias fórmulas encadenadas), la plataforma utiliza un banco de fórmulas estructurado sobre Grafos Acíclicos Dirigidos (DAG)23. De este modo, el sistema desglosa los problemas matemáticos complejos en un árbol jerárquico de sub-fórmulas unitarias para asegurar la trazabilidad del cálculo23.

#### **Ejemplo de Desglose Matemático: Valoración por Descuento de Dividendos (Gordon-Shapiro)**

Supóngase una pregunta típica del examen real EFA en la que una empresa prevé pagar un dividendo esperado el próximo año (![][image1]) de ![][image2]24. La rentabilidad exigida por el mercado (![][image3]) es del ![][image4], y la tasa de crecimiento anual indefinido de los dividendos (![][image5]) es del ![][image6]24. Se requiere determinar el precio teórico del activo (![][image7])24.  
La plataforma estructura el flujo matemático empleando la fórmula de Gordon-Shapiro mediante LaTeX para su visualización23:  
![][image8]  
El motor explicativo, al procesar la respuesta del estudiante, despliega un flujo de razonamiento secuencial interactivo guiado por Chain-of-Thought (CoT)25:

Python  
\# Script de cálculo generado y ejecutado en el sandbox seguro de Python  
def calcular\_gordon\_shapiro(d1: float, ke: float, g: float) \-\> dict:  
    if ke \<= g:  
        raise ValueError("La rentabilidad exigida (ke) debe ser mayor que la tasa de crecimiento (g).")  
    denominador \= ke \- g  
    precio\_teorico \= d1 / denominador  
    return {  
        "denominador": denominador,  
        "precio\_teorico": precio\_teorico  
    }

\# Ejecución de la aserción matemática con datos estandarizados  
resultado \= calcular\_gordon\_shapiro(d1=4.00, ke=0.12, g=0.08)  
print(resultado)  
\# Retorno del sandbox: {'denominador': 0.04, 'precio\_teorico': 100.0}

A partir de la ejecución exitosa en el sandbox, el sistema compone dinámicamente la explicación analítica para el usuario:

* **Identificación de Variables**: Se extraen los datos provistos por el enunciado estandarizando sus formatos numéricos26:  
  * Dividendo esperado (![][image1]) \= ![][image9]  
    \[cite: 24\]  
  * Rentabilidad requerida por el mercado (![][image3]) \= ![][image10]  
    \[cite: 24\]  
  * Tasa constante de crecimiento (![][image5]) \= ![][image11]  
    \[cite: 24\]  
* **Paso 1 (Cálculo del Denominador)**: Se evalúa la prima de rendimiento neta exigida al activo restando la tasa de crecimiento de la tasa de descuento25:  
  ![][image12]  
* **Paso 2 (Cálculo del Precio Teórico)**: Se descuenta el dividendo esperado entre la prima obtenida25:  
  ![][image13]  
* **Justificación de Distractores**: El motor analiza los errores comunes. Por ejemplo, explica que la opción de respuesta de ![][image14] surge del error de aplicar directamente ![][image15] o de no restar el crecimiento en el denominador, ofreciendo una retroalimentación precisa al alumno para reconducir su aprendizaje24.

#### **Ejemplo de Desglose Matemático: Evaluación de Rentabilidades Ajustadas al Riesgo**

Para el Módulo de Gestión de Carteras, la plataforma desglosa la prima de riesgo del activo respecto a su volatilidad y su riesgo sistemático (![][image16])21:  
![][image17]  
![][image18]  
Donde ![][image19] representa el rendimiento esperado de la cartera, ![][image20] la tasa libre de riesgo y ![][image21] la desviación estándar de los retornos21. El sistema guiará al alumno demostrando paso a paso por qué una cartera con un ratio de Sharpe superior puede no ser eficiente si su riesgo sistemático medido por el ratio de Treynor resulta deficiente debido a la falta de diversificación.

## **Metodología de Desarrollo: SDD y TDD en Entornos de IA**

La ingeniería de la plataforma se rige por un marco de trabajo que fusiona el Desarrollo Basado en Especificaciones (Spec Driven Development \- SDD) con el Desarrollo Guiado por Pruebas (Test Driven Development \- TDD)6. El desarrollo guiado por IA altera el rol tradicional del programador, quien deja de escribir código línea a línea para convertirse en un diseñador y supervisor de especificaciones extremadamente precisas27.

### **Niveles de Compromiso SDD y el Enfoque Seleccionado**

En la literatura de ingeniería de software con IA se identifican tres niveles de madurez para los flujos basados en especificaciones28:

1. **Spec-first**: La especificación se redacta al inicio del ciclo en forma de historia de usuario o documento de criterios de aceptación y se entrega a la IA para codificar28. Sin embargo, la especificación no se mantiene activamente y queda obsoleta conforme el software evoluciona28.  
2. **Spec-anchored**: La especificación y el código funcional evolucionan de manera coordinada como activos vivos de la base de código6. Las especificaciones se someten a control de versiones y se ejecutan pruebas automatizadas (BDD/TDD) de forma continuada en cada commits de Git para forzar la alineación estricta y evitar desviaciones6.  
3. **Spec-as-source**: El nivel más extremo en el que el único documento que edita el desarrollador humano es la especificación técnica formal, tratándose todo el código fuente resultante como un mero producto compilado no editable de forma directa28.

Para el desarrollo de esta plataforma de preparación de exámenes, **se selecciona de forma unánime el nivel Spec-anchored**30. El nivel *spec-anchored* ofrece el equilibrio idóneo entre rigor arquitectónico y flexibilidad operativa para sistemas de producción6. Al anclar las especificaciones junto con las suites de pruebas, se asegura que las fórmulas financieras complejas y el comportamiento del simulador permanezcan siempre alineados con los requisitos normativos del examen sin el riesgo de degradación que introduce la generación autónoma sin supervisión6.

### **El Pipeline Operativo de Desarrollo (SDD \+ TDD)**

La implementación de cualquier funcionalidad de la plataforma sigue de manera obligatoria una secuencia de desarrollo rigurosa de fases y compuertas de validación (*gates*)7:

┌────────────────────────────────────────────────────────────────────────┐  
│                          FASE 1: ESPECIFICAR                           │  
│  \- Redacción del Spec en formato estructurado Markdown/TOML (ZeeSpec). │  
│  \- Definición de criterios de aceptación con sintaxis Gherkin (Given-  │  
│    When-Then) \[cite: 7, 33\].                                          │  
│  \- Validación: Aprobación del contrato por el desarrollador.           │  
└───────────────────────────────────┬────────────────────────────────────┘  
                                    ▼  
┌────────────────────────────────────────────────────────────────────────┐  
│                            FASE 2: PLANEAR                             │  
│  \- Generación de esquemas de datos estructurados (Zod / OpenAPI)       │  
│    por el Orquestador \[cite: 29, 31\].                                  │  
│  \- Definición de la arquitectura interna y mock-ups \[cite: 30, 31\].    │  
│  \- Validación: Verificación de la consistencia del plan.    │  
└───────────────────────────────────┬────────────────────────────────────┘  
                                    ▼  
┌────────────────────────────────────────────────────────────────────────┐  
│                            FASE 3: TAREAS                              │  
│  \- Desglose del plan en subtareas atómicas, autocontenidas y aisladas  │  
│    \[cite: 30, 34\].                                                     │  
│  \- Validación: Inspección y ordenación de dependencias de tareas.      │  
└───────────────────────────────────┬────────────────────────────────────┘  
                                    ▼  
┌────────────────────────────────────────────────────────────────────────┐  
│                          FASE 4: IMPLEMENTAR                           │  
│  \- Ciclo TDD: Red (crear prueba fallida) \-\> Green (implementar mínimo  │  
│    código funcional para pasar) \-\> Refactor.         │  
│  \- Validación: Ejecución exitosa de la suite completa de pruebas.      │  
└───────────────────────────────────┬────────────────────────────────────┘  
                                    ▼  
┌────────────────────────────────────────────────────────────────────────┐  
│                        FASE 5: REVISIÓN ADVERSARIAL                    │  
│  \- Sometimiento del código final a un modelo externo alternativo       │  
│    para auditoría y detección de debilidades.           │  
└────────────────────────────────────────────────────────────────────────┘

Un ejemplo real de especificación en formato Gherkin para la integración del simulador de exámenes ilustra la solidez de este método33:

Gherkin  
Feature: Simulación de Examen EFA Completo  
  Scenario: Generación exitosa de examen respetando ponderación oficial  
    Given que un alumno inicia una simulación del examen "EFA Completo"  
    And la base de datos de preguntas cuenta con reactivos cargados para todos los módulos  
    When el motor de generación compila el cuestionario  
    Then el examen resultante debe constar exactamente de 50 preguntas tipo test  
    And el peso del módulo "Instrumentos y Mercados Financieros" debe ser del 25.0% (12 o 13 preguntas)  
    And el peso del módulo "Gestión de Carteras" debe ser del 17.5% (8 o 9 preguntas)  
    And el límite de tiempo de ejecución del test debe configurarse en 1 hora y 30 minutos

### **Salvaguardas Contra Modos de Fallo Críticos de la IA**

Para asegurar la robustez de la plataforma y evitar la acumulación de deuda técnica o código redundante generado por asistentes virtuales, se programan salvaguardas explícitas integradas en el pipeline de desarrollo7:

* **Prevención de la Deriva de Especificación** (*Spec Drift*)7: Los archivos de especificación se tratan como activos bajo control de versiones Git en un directorio .specify/7. El Orquestador tiene estrictamente prohibido mutar código funcional si no existe un cambio validado previo mediante diff en los specs7.  
* **Mitigación de la Inversión de Pruebas** (*Test Inversion*)7: Para evitar que la IA escriba pruebas unitarias tautológicas adaptadas a su propia lógica errónea, se aplica el enfoque TDD riguroso: el agente debe generar y ejecutar la suite de pruebas unitarias basadas en la especificación antes de iniciar el desarrollo del código que le dará soporte7.  
* **Control de la Deriva Semántica** (*Semantic Drift*)7: Las optimizaciones internas de las funciones lógicas (por ejemplo, refactorizar una consulta SQL para el cálculo de respuestas) se someten a aserciones de invariabilidad semántica7. Se ejecutan pruebas basadas en propiedades (*property-based testing*) para verificar que los resultados numéricos de las fórmulas matemáticas sigan siendo idénticos tras cualquier refactorización7.  
* **Mitigación de la Deriva Arquitectónica** (*Architectural Drift*)7: El sistema previene el crecimiento desordenado de código repetitivo y la duplicación de dependencias (por ejemplo, que diferentes agentes creen clientes HTTP aislados en lugar de consumir un servicio centralizado de la aplicación)7. Cada sesión del sub-agente se inicializa con la carga forzada de un archivo CONSTITUTION.md o CLAUDE.md que define los patrones técnicos permitidos del proyecto29.

## **Arquitectura de Orquestación Multi-Agente y Minimización de Contexto**

La construcción de una plataforma integral de estudio, práctica y simulación del temario EFA no puede descansar sobre un único agente conversacional debido a la limitación de la ventana de contexto de los modelos y al riesgo inherente de acumulación de alucinaciones en sesiones de larga duración8. El patrón de diseño elegido distribuye y segrega el trabajo a través de una jerarquía de agentes independientes bajo el esquema Orquestador-Trabajador con minimización estricta de contexto8.

### **El Principio de Contexto Mínimo Efectivo**

El factor determinante del éxito de este patrón arquitectónico es la reducción drástica de la información enviada a los sub-agentes11. En lugar de transferir la base de código completa del proyecto o historiales de conversación extensos, el Orquestador Principal aísla los parámetros y proporciona exclusivamente los elementos necesarios para la resolución de cada subtarea específica8:

1. **Instrucciones del sistema sumamente acotadas**: Delimitación rigurosa de lo que el sub-agente debe realizar y, de manera crucial, lo que tiene estrictamente prohibido investigar o modificar para evitar solapamientos13.  
2. **Esquemas de entrada y salida perfectamente tipados**: Uso de validaciones mediante esquemas estrictos de Zod para obligar al agente a retornar respuestas estructuradas sin divagaciones lingüísticas13.  
3. **Filtrado de contexto redundante**: El Orquestador depura cualquier información superflua antes de instanciar al sub-agente, reduciendo en más del 90% los tokens consumidos en las llamadas a los modelos subordinados8.

### **Tipología e Interfaces de los Sub-Agentes en el Desarrollo**

Para optimizar el uso de tokens y controlar la latencia y los costes del sistema, el Orquestador distribuye el trabajo entre perfiles de sub-agentes especializados8. Esta jerarquía de especialización se detalla a continuación:

| Agente | Modelo de IA Asignado | Tipo de Acceso | Herramientas Permitidas | Restricciones de Contexto |
| :---- | :---- | :---- | :---- | :---- |
| **Master Orchestrator** \[cite: 8, 35\] | Claude 3.5 Opus / GPT-4o8 | Solo Lectura | Task Tool, Agent Registry, Diff Viewer32 | Acceso al estado de planificación global. No escribe código de forma directa8. |
| **Agente Explore** \[cite: 12\] | Claude 3.5 Haiku / GPT-4o-mini12 | Solo Lectura12 | Read File, Grep, Glob, Directory Search12 | Solo visualiza rutas y archivos de código sugeridos por el Orquestador12. |
| **Agente Plan** \[cite: 12\] | Claude 3.5 Sonnet12 | Solo Lectura12 | Read File, Terminal Execution (no edits)8 | Análisis conceptual exclusivo. No realiza modificaciones sobre la base de código12. |
| **Agente General-purpose** \[cite: 12\] | Claude 3.5 Sonnet / GPT-4o12 | Lectura / Escritura12 | Read/Write File, Edit File, Terminal Compiler, Test Suite8 | Restringido exclusivamente al árbol de trabajo (*Worktree*) de Git asignado para la tarea12. |
| **Agente Verifier** \[cite: 40\] | Claude 3.5 Opus40 | Solo Lectura | Bash, Test Executor, Schema Validator | Contraste de las salidas frente a las especificaciones originales del negocio40. |

### **Mecanismos de Sincronización, Aislamiento y Reducción Conversacional**

El funcionamiento seguro y coordinado del ecosistema multi-agente exige la implementación de tres salvaguardas arquitectónicas:

* **Aislamiento de Entornos Mediante Git Worktrees**12: Cuando múltiples sub-agentes del tipo *General-purpose* operan de forma paralela en la implementación de diferentes módulos (por ejemplo, el módulo de cálculo de IRPF y el módulo de perfilado de clientes), se evita la generación de conflictos o bloqueos en el repositorio local mediante el uso de árboles de trabajo aislados de Git12. Cada sub-agente ejecuta sus cambios en un directorio físico temporal (.claude/worktrees/\<name\>/) sobre una rama de desarrollo independiente12. El Orquestador se encarga de revisar los commits resultantes y de unificar las ramas de manera ordenada tras validar las pruebas unitarias12.  
* **Llamadas de Herramienta Síncronas y Asíncronas**: La comunicación entre el Orquestador y los sub-agentes se realiza mediante llamadas a herramientas estructuradas11. Las llamadas síncronas se emplean para tareas secuenciales inmediatas, pausando la ejecución del orquestador hasta el retorno de la respuesta11. Para tareas complejas de larga duración (como la depuración de una suite de integración de pruebas del simulador de exámenes), el Orquestador realiza llamadas asíncronas en segundo plano, recibiendo un identificador de tarea y continuando con otras tareas de control hasta recibir la notificación de finalización del sub-agente11.  
* **Compresión Semántica del Historial Conversacional**: Para impedir que la acumulación de mensajes sature la ventana de contexto del Orquestador Principal, se aplica un protocolo de compresión obligatorio en el flujo de retorno8. Los sub-agentes no transmiten su historial de conversación detallado, sus intentos fallidos de compilación o la totalidad de la salida de consola8. Al concluir su labor, el sub-agente genera exclusivamente un reporte consolidado que detalla las funciones creadas, los esquemas alterados y el estado del paso de las pruebas unitarias8. Este reporte de alta compresión semántica mantiene el contexto global del Orquestador completamente limpio y optimiza la precisión del razonamiento general8.

## **Estrategia de Implementación Tecnológica**

Para asegurar el desarrollo ordenado de esta plataforma de preparación del examen EFA, se estructura un plan de despliegue progresivo dividido en tres etapas técnicas consecutivas43:

### **Fase I: Piloto Cuantitativo e Ingestión de Datos (Semanas 1-4)**

Esta etapa inicial sienta las bases técnicas del sistema de datos y del motor de ejecución aritmética44:

* **Ingestión y tipado de exámenes históricos**: Diseño de la base de datos de preguntas y exámenes reales de convocatorias previas4. Las preguntas y respuestas se estructuran bajo un modelo de datos robusto en formato JSON jerárquico que preserva las dependencias cualitativas y cuantitativas45.  
* **Configuración del Sandbox de Cálculo**: Despliegue del entorno de ejecución aislado de Python encargado de procesar todas las aserciones de cálculo financiero (TIR, TAE, ratios de carteras, liquidaciones fiscales), eliminando las aproximaciones probabilísticas de los modelos de lenguaje5.  
* **Integración de Chain-of-Thought (CoT)**: Programación de las plantillas de razonamiento sistemático para guiar la explicación matemática detallada paso a paso cuando el usuario comete un error5.

### **Fase II: Orquestación del Entorno SDD-TDD (Semanas 5-8)**

En este período se habilita el marco de desarrollo de software asistido por Inteligencia Artificial para la plataforma32:

* **Despliegue de Especificaciones Base**: Redacción de los archivos de constitución del proyecto y los specs anclados (.specify/) de las funcionalidades principales utilizando sintaxis Gherkin (Given-When-Then)7.  
* **Configuración de la Suite de Agentes**: Programación del registro de sub-agentes y automatización del control de Git Worktrees para permitir que la IA implemente código de forma aislada y controlada12.  
* **Ciclo Automatizado TDD**: Integración en el servidor de integración continua (CI) de las compuertas de verificación que exigen la creación y fallo de pruebas unitarias antes de la compilación del código final de la aplicación7.

### **Fase III: Generador de Simulaciones y Cierre de Calidad (Semanas 9-12)**

La última fase se orienta a consolidar la experiencia del usuario y completar el contenido educativo44:

* **Simulador Dinámico de Convocatorias**: Programación del algoritmo de selección aleatoria que compone simulaciones de examen del EFA Completo respetando estrictamente las ponderaciones de los 10 módulos oficiales y los tiempos límite de las convocatorias reales (1h 30m para el test y 1h para el bloque práctico)3.  
* **Mecanismo de Verificación de Argumentos**: Implementación de un modelo de evaluación específico encargado de contrastar las respuestas redactadas por el estudiante en la parte práctica de desarrollo frente a la rúbrica oficial, valorando de forma rigurosa la coherencia cualitativa de las respuestas3.  
* **Pruebas Adversariales de Cobertura**: Sometimiento del sistema a un agente de auditoría adversarial con el objetivo de detectar posibles alucinaciones en las justificaciones de las preguntas cualitativas de ética profesional y normativa MiFID II, asegurando que la plataforma responda con absoluta fiabilidad antes de su lanzamiento comercial definitivo7.

#### **Obras citadas**

1. La Asociación Europea de Asesoría y Planificación Financiera en España \- EFPA, [https://www.efpa.es/docs/dossier-informativo-efpa-asociacion.pdf](https://www.efpa.es/docs/dossier-informativo-efpa-asociacion.pdf)  
2. Examen EFA MIFID EFPA España | Guía completa para superarlo, [https://www.examenesmifid.com/examen-efa-mifid-efpa-espana/](https://www.examenesmifid.com/examen-efa-mifid-efpa-espana/)  
3. Exámenes certificación EFPA European Financial Advisor (EFA), examen parcial Nivel II, [https://www.efpa.es/examenes-certificacion-efa-nivel-II](https://www.efpa.es/examenes-certificacion-efa-nivel-II)  
4. Exámenes certificación EFPA European Financial Advisor (EFA), [https://www.efpa.es/examenes-certificacion-efa](https://www.efpa.es/examenes-certificacion-efa)  
5. Your AI financial analysis is wrong (how to fix it in 3-minutes) \- AI Finance Club, [https://ai-finance.club/the-ai-finance-pro/your-ai-financial-analysis-is-wrong-how-to-fix-it-in-3-minutes/](https://ai-finance.club/the-ai-finance-pro/your-ai-financial-analysis-is-wrong-how-to-fix-it-in-3-minutes/)  
6. Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants \- arXiv, [https://arxiv.org/html/2602.00180v1](https://arxiv.org/html/2602.00180v1)  
7. Spec \+ TDD: The Combination That Actually Produces Shippable AI Code, [https://www.augmentcode.com/guides/spec-tdd-shippable-ai-generated-code](https://www.augmentcode.com/guides/spec-tdd-shippable-ai-generated-code)  
8. How to Use a Smart Orchestrator Model to Direct Cheaper Sub-Agent Models in Claude Code | MindStudio, [https://www.mindstudio.ai/blog/smart-orchestrator-cheaper-sub-agent-models-claude-code](https://www.mindstudio.ai/blog/smart-orchestrator-cheaper-sub-agent-models-claude-code)  
9. Multi Agent Architecture: Patterns, Use Cases & Production Reality \- Truefoundry, [https://www.truefoundry.com/blog/multi-agent-architecture](https://www.truefoundry.com/blog/multi-agent-architecture)  
10. Agentic AI Architecture: 5 Patterns Explained \- Redis, [https://redis.io/blog/agentic-ai-architecture-examples/](https://redis.io/blog/agentic-ai-architecture-examples/)  
11. The 3 Essential Sub-Agent Patterns for Production-Grade AI Systems | Epsilla Blog, [https://www.epsilla.com/blogs/2026-03-14-ai-sub-agent-patterns](https://www.epsilla.com/blogs/2026-03-14-ai-sub-agent-patterns)  
12. Claude Code Subagents: How Is Work Divided and Processed? \- MadPlay, [https://madplay.github.io/en/post/claude-code-subagent-architecture](https://madplay.github.io/en/post/claude-code-subagent-architecture)  
13. Pattern: Orchestrator-Worker \- Intelligence Patterns: Reusable Elements of Agentic Design, [https://agents.kour.me/orchestrator-worker/](https://agents.kour.me/orchestrator-worker/)  
14. Exámenes EFPA 2026: Fechas y Convocatorias Completas \- FIKAI Escuela de Finanzas, [https://www.fikai.com/general/examenes-efpa-2026-calendario-fechas-convocatorias.html](https://www.fikai.com/general/examenes-efpa-2026-calendario-fechas-convocatorias.html)  
15. EFPA European Financial Advisor (EFA) \_\_\_\_\_ Guía de Certificación, [https://www.efpa.es/descargas/documentos/GUIA\_DE\_CERTIFICACION\_EFA.pdf](https://www.efpa.es/descargas/documentos/GUIA_DE_CERTIFICACION_EFA.pdf)  
16. Exámenes certificación EFPA European Financial Advisor (EFA), examen parcial Nivel I (EIP), [https://www.efpa.es/examenes-certificacion-efa-eip](https://www.efpa.es/examenes-certificacion-efa-eip)  
17. EFPA, Certificación para Profesionales de Finanzas \- Grupo IOE, [https://grupoioe.es/efpa-certificacion-para-profesionales-de-las-finanzas/](https://grupoioe.es/efpa-certificacion-para-profesionales-de-las-finanzas/)  
18. Temario EFA 2026: módulos, examen y guía EFPA \- Alberto Bernat, [https://www.albertobernat.com/temario-examenes-efa/](https://www.albertobernat.com/temario-examenes-efa/)  
19. Manual EFA 2026: temario completo de teoría \- Alberto Bernat, [https://www.albertobernat.com/temario-completo-efa-2026-manual-teoria/](https://www.albertobernat.com/temario-completo-efa-2026-manual-teoria/)  
20. Programa Superior \- Fundación de Estudios Bursátiles y Financieros, [https://febf.org/wp-content/uploads/2025/11/EFFA\_2025\_ONLINE.pdf](https://febf.org/wp-content/uploads/2025/11/EFFA_2025_ONLINE.pdf)  
21. Fórmulas financieras EFA para preparar el examen EFPA \- Alberto Bernat, [https://www.albertobernat.com/formulas-financieras/](https://www.albertobernat.com/formulas-financieras/)  
22. Why LLMs Struggle: Math, Structured Data & AI Reasoning Limits \- AI Agent platform for Financial Services, [https://moveo.ai/blog-new/why-llm-struggle](https://moveo.ai/blog-new/why-llm-struggle)  
23. FinMathBench: A Formula-Driven Benchmark for Evaluating LLMs' Math Reasoning Capabilities in Finance \- AAAI Publications, [https://ojs.aaai.org/index.php/AAAI/article/view/40358/44319](https://ojs.aaai.org/index.php/AAAI/article/view/40358/44319)  
24. Examen EFA MODELO A Pregunta 1 Un fondo de pensiones evalúa invertir en una empresa textil que ha mostrado buenos resultados fi \- EFPA, [https://www.efpa.es/docs/simulacion\_examen\_efa\_completo.pdf](https://www.efpa.es/docs/simulacion_examen_efa_completo.pdf)  
25. Chain-of-Thought (CoT) Prompting in AI-Powered Financial Analysis, [https://corporatefinanceinstitute.com/resources/financial-modeling/chain-of-thought-prompting-financial-analysis/](https://corporatefinanceinstitute.com/resources/financial-modeling/chain-of-thought-prompting-financial-analysis/)  
26. How AI Shapes Financial Narratives \- Lucid.now, [https://www.lucid.now/blog/ai-shapes-financial-narratives/](https://www.lucid.now/blog/ai-shapes-financial-narratives/)  
27. Vibe Coding vs Spec-Driven Development: coding with AI | Tech Insights \- Digital55, [https://digital55.com/blog-en/spec-driven-development-sdd-desarrollo-con-ia](https://digital55.com/blog-en/spec-driven-development-sdd-desarrollo-con-ia)  
28. What is Spec-Driven Development? \- IBM, [https://www.ibm.com/think/topics/spec-driven-development](https://www.ibm.com/think/topics/spec-driven-development)  
29. From Vibes to Specs: Examining the Shift to Spec-Driven Development \- Itential, [https://www.itential.com/resource/blog/vibes-to-specs-development/](https://www.itential.com/resource/blog/vibes-to-specs-development/)  
30. Spec-Driven Development (SDD) — best practices (so far) \- Allegro Tech Blog, [https://blog.allegro.tech/2026/06/spec-driven-development-best-practices.html](https://blog.allegro.tech/2026/06/spec-driven-development-best-practices.html)  
31. Spec driven development: a guide to moving beyond vibe-coding with AI | SparkFabrik, [https://www.sparkfabrik.com/en/blog/spec-driven-development-guide/](https://www.sparkfabrik.com/en/blog/spec-driven-development-guide/)  
32. Spec-Driven Development (SDD): The Definitive 2026 Guide, [https://thebcms.com/blog/spec-driven-development](https://thebcms.com/blog/spec-driven-development)  
33. What is Specification Driven Development (SDD)? \- NimblePros Blog, [https://blog.nimblepros.com/blogs/sdd-overview/](https://blog.nimblepros.com/blogs/sdd-overview/)  
34. Orchestrating AI Agent Teams: How Skills, Hooks, and Context Flow Make Autonomous Coding Reliable \- Dotzlaw Consulting, [https://dotzlaw.com/insights/claude-deterministic-agent-engineering/](https://dotzlaw.com/insights/claude-deterministic-agent-engineering/)  
35. Building Multi-Agent Research Systems | Vinci Rufus, [https://www.vincirufus.com/en/posts/building-multi-agent-research-systems/](https://www.vincirufus.com/en/posts/building-multi-agent-research-systems/)  
36. Agents: Workflow Patterns \- AI SDK, [https://ai-sdk.dev/docs/agents/workflows](https://ai-sdk.dev/docs/agents/workflows)  
37. Spring AI Agentic Patterns (Part 4): Subagent Orchestration, [https://spring.io/blog/2026/01/27/spring-ai-agentic-patterns-4-task-subagents/](https://spring.io/blog/2026/01/27/spring-ai-agentic-patterns-4-task-subagents/)  
38. What Is the /workflows Command in Claude Code? Dynamic Multi-Agent Orchestration, [https://www.mindstudio.ai/blog/claude-code-workflows-command-dynamic-multi-agent-2](https://www.mindstudio.ai/blog/claude-code-workflows-command-dynamic-multi-agent-2)  
39. The Orchestrator Pattern: Managing AI Work at Scale | by Ronie Uliana \- Medium, [https://ronie.medium.com/the-orchestrator-pattern-managing-ai-work-at-scale-a0f798d7d0fb](https://ronie.medium.com/the-orchestrator-pattern-managing-ai-work-at-scale-a0f798d7d0fb)  
40. How Agents Manage Other Agents: Four Subagents Patterns in 2026 \- Medium, [https://medium.com/design-bootcamp/how-agents-manage-other-agents-four-subagents-patterns-in-2026-7abe5ab83b88](https://medium.com/design-bootcamp/how-agents-manage-other-agents-four-subagents-patterns-in-2026-7abe5ab83b88)  
41. The Evolution of AI Agentic Patterns \- m a i, [https://tieukhoimai.me/blog/evolution-of-agentic-patterns](https://tieukhoimai.me/blog/evolution-of-agentic-patterns)  
42. Financial AI Tools for 2026: What Actually Works for Finance Teams \- V7 Labs, [https://www.v7labs.com/blog/financial-ai-tools](https://www.v7labs.com/blog/financial-ai-tools)  
43. How to Use LLMs for Financial Data Analysis: The Complete Enterprise Guide \- Daloopa, [https://daloopa.com/blog/analyst-best-practices/exploratory-financial-data-analysis-using-large-language-models](https://daloopa.com/blog/analyst-best-practices/exploratory-financial-data-analysis-using-large-language-models)  
44. How to Process LLM Tabular Financial Data: Advanced Techniques and Implementation Guide \- Daloopa, [https://daloopa.com/blog/analyst-best-practices/processing-tabular-financial-data-with-large-language-models](https://daloopa.com/blog/analyst-best-practices/processing-tabular-financial-data-with-large-language-models)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAAbCAYAAACJISRoAAABKUlEQVR4XmNgGAWDHbACsTgQS6JhAWRFlIJWIP6PB/8C4vlArA7TQAn4xgAxFB0wA3ElA0TOFk2OZAAy5B+6IBRwAvEOKAaxyQKCDBBLtqJLIAFfBoiaIHQJYoE+A8SAcnQJJACzBJ8avGAOED8BYhl0CSQAUkO2T0BBdZoBElQcaHIwAFPzFYiN0eSIAtEMEBe6oEsggRwGiJoGKF8IiMOB+D0QP4SK4QWgPAAyAFdQwVIWSI0iVAxkiT8Qr2Ag0hJQMIAMwBVUHgyQpI0tDy1kINISfPkD5GKQ/HYg5keTAwGiLGFkgBgCSlnowACIrzNAgpMbTQ4G8FoCKgBBhuPCoPIKlC9AhSc+gNcSagG6WYItqKkCxID4MAMieEEWZaCoGAWjgGYAAGPIS0MG4A5TAAAAAElFTkSuQmCC>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAYCAYAAADkgu3FAAABFElEQVR4XmNgGAVDFYgB8RV0QTyAD4jLgPg/FK8BYl8UFTjAXwaIBmKAGRC/h9IwwArE85H4GIARiJuB+AQDcRZFMEDUKaFLAIEIugAysAXiC0B8gIE4i7YyQNRxoEvgAyDfrGKAePsAA3EW/WMgTh0KMAdiFSj7AAN+A0COAsUBLPLR8W8gtoGrRgKVQLwZiX+AgTKLWhFKUcE1INZG4h9gwG8RDMBcTxQwZsB0ETL+ilCKAZ4zEOcgMBAC4hA0DMoXIANAbH+EUgwAypggdfzoEsSChwzEuRSUQkEp9RYQyyOJgyyeicTHAAJArMMACS6QRZ5ALI2iAhNIMEDU3gFiGSBWBeKTQGyJrGgUjIJRQDkAANQOR4pzDEOnAAAAAElFTkSuQmCC>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAbCAYAAABxwd+fAAABGklEQVR4XmNgGAWkAA4glgFiNyAWQpMjCbQC8X8o1kSTIxmsYYAYRDF4wEAlg0CGnEYXJBWAAhtk0CQkMVBYgQKfJOACxG8ZIJpB7MNAHADE34BYEkkdQVDOAPGWIBDvYIAkhasMEFeKI6nDC6QZIAH9Doj3oEqRBmyA+DcQ/2SAuCAXiDlRVBAJQN4CGSAMxHpQ9i4UFUSCuwyo6ecrFIMAKOB5oGx7Bki4hTBAYpcRKg4HIG+BYgwGQF58yABROAVJ/AsQh0PZOkDMjSQHBiDXNCDxi4H4HwPE8CComCcDxKBHQNwIxCpQcRSgBsTMaGICQMyPxE8HYl8kPtlAEYijoWyQl/0YyIxZELgDxAuB+AwDxPujYEgDAI9HM3oA3Pb7AAAAAElFTkSuQmCC>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACYAAAAYCAYAAACWTY9zAAAB20lEQVR4Xu2VPShGURjHH2EQJR/5KCKLURJKMjFIFhmM72iwIiaLQcmklJQom9WC4bVIrAaJYjKIiUHy8f8753ife7rvfe9VZLi/+tU5z7n33Oc899xzRVJS8lIBL2E7PIJbweEvimAG9nrxSHjTgB9U1MB1a7M3RibhhG13wWe4AFttrBTuww8xz4pkBT7CNzE3zAaHv7mDfbZdLLnr+TDSCG9hk+2TRdV2XEvCarmJwxLj6pnEiYr1w1e4C0tgm5jkOY9Dz8UKzcBKFYtFVGJMgok9qJhLJCtmb1XBM9hhx5nIjm2THjHVSkxUYmEMwne4Kbn90gIPxVSF+3DNxjl+YOOJSZrYqpgqDnnxK/gkJsEGG2O16I9IkhhXzqRYlULMiUnScQ/3rHHuj50Yv0JOuGzbheC+ctXiXjwVc+xwcVkbjyRuYjybMqpfLeFnEmOslt5X8xKcn197veqHEiexETjmxfiayr0Y4Vnlf4VbEpyfZ54+XkIplBh/NceSO/nptoRfz2q5r1PjV6wb1qp+AL53JjUNX8T8MoZhnZgTnnBl3OxhjtprNKxWpx8Uc8RsqP6UmMP5T2BFuLh8nMMLeAOXgkO/Cyuo/5c+ZXBczH/XvZGUlJR/zSd8TV13db2vxwAAAABJRU5ErkJggg==>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAaCAYAAABhJqYYAAAAxElEQVR4Xu3Qrw5BcRjG8XfDxkbTiIpJgimioJvgClwDcwuKCaquCIKsmGsQBM3MBILNn+/7O4e9fqPbeLZP8JzHOed3RP75+jRxwAondDFEwo40MVzRRgRlHDFHyuykgC1qpotjipbpXAa4IW26LDYomc5FH6djm07YRb3ejfVANvoK/g1cFhL84RE9rA7XpnumjguSyGEiwXhsR5+iB9XPWPUvvEtFglfIeL2MsEM+/K1326P4XJj0MEMDfZyxfFn8Su4hfCU5Q9CK0wAAAABJRU5ErkJggg==>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAZCAYAAADAHFVeAAAB2ElEQVR4Xu2UPShGURjHH6HIVz5KymKUSYpFJjKZLIqJQVkVkeEtq0kmJSSLlEkW8ZZFUUpZlEGRkExKJP7/95xzz8c9YTO4v/p17/m495znPOcckYw/4BmuwEp4A0f95gIVcAPWhA0hY3BZP+uDtnJRA7To8jT8hENif8znNXzR5Sid8A4W6XIxnIGDSQ+RAbgptk8tPLDNCXn5IaoduBrUMZJjsR8yknXbXFjKvFMmnHRXUJeCoTMfLiXwAjbocjfcF5UT0gxP9TuZkvTgUU5ErT8TziUknGHOdACN4g/OXB3aZrmSX0RFSuGCqAHpG5z1eigm4Ct8gHOivmMOGdW3eQphRGYweuY3J5TBJqfMPF06ZUa3BnvEbiaPJfiu39nhUdSAfLaZThHYl3k0UXXAeV3PQc91vceHqE6GalE7jwPmnPoQ/pCRGRZhr37nBtt22gpwFjyEnJWLWdbdoN7AaPJil6oKHon/Hx4XD87gCbaGDaIOOmcbg7vPjYp55BFyBxt23hMYAW+MEOaxL6wUFRV3oLsBYpHFdrTUwS14KypXfHIC3NohzBOjitEu6ibid7zqeH6jcJbjoi7iEUlfxIRXFA/yZNjgwHO4B+9hf9CWkfEf+QK+QFTHp7CmDgAAAABJRU5ErkJggg==>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABUAAAAbCAYAAACTHcTmAAABHUlEQVR4Xu2UvWoCQRSFryRCisSfSgQb7WxUkDyGILGMT5FGCOnElwhC2rxAalvBWm0jCBYiNknKJOcyOzhzNLuuBBv94IOdPTN378wuK3LmGGRgnrzyZsSkB38ifIIpuyAOX2IK7GItJrvkIApd9M03A2Zi8hwHYWTFLHrjIEAfpnmagzCqYhY9cgASsjnbWPThHBbofgVO4avE7FK3PoJL+AKfA9/FdKfneWEn78u9mMV3HBDaaRdewwls+bGPdqdFyxwQHTG7UrQRPZY/0a1r0RsOHOwRWW7hhzPeYp83W4efIWMP+7msOCAa4j94Z1H9YdgOXR/cSQ5chMcHUYILZ/wvRZU2LAbX+mkNnexgknAAm3AMa3585nT5BX+3Q/N1y8afAAAAAElFTkSuQmCC>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAABJCAYAAACAa3qJAAADTklEQVR4Xu3dT8hNaRwH8EcaiZk0EYnyZ1jKwsrCjiKxkDRlISuyHGmWWMzCdpZSspNsSWYWb1naEimFRE1NUlbKn+fnOdc97/Peew1znfvet8+nvt1zfs+p913+Os85v5MSAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALAhrq/wwexkAgElalEqT9iHnWHMceZ3zd+s6AAAmaFUqDdvSqv4+Z29VAwBgAo6m0pzVZnLu1EUAALp3N+dGXcwe5zytiwAAdC+2Q3fXxVTql+siAADd+jkNfn5tTVPf1JyfynnXXwYAoCvDnl+7lXOvqtkeBQCYgPtp7vNrMerjbVULGjYAgA7FFuiBVLY9L+QcbnK1qQ2iYQMAFoQfc7an0vT8ksoQ2g05L9PcLcZpo2EDABaME2nuc2G9rwlMq+ep/P9vcrZVawAAU2fQXLMYmzHNDRsAwIIyaK7Zi5yLVQ0AgAnozTWLgbPRoF1pzo+0L/qCZ1/IX/1LAQD4WjHXbNTW5585++viGJ0bY842GVRrrw2qta8HAJhX4vm1YR9M39H8bs7Z214AAKA7cXftYF1s9F5EiNEf0dgNE2+UjsrK/qUAAPxX0USdTKVhO55KU1brzTGLNTPNAADmoZnmV8MGADBPbWl+d+XsbC98B6tz/s05VC8AADBafL+zq2fQYns2xowAADAPrUujx4sAADBhv6f+m6hncm631r6na6k8q/dPKgN+F81aBQDgsyepDPG9lErT1MXdtkc5e5rj9ambvwkAMLWiWYqXDr7lDlc0evFZrWGJZqwWL1G0G7SYRfe4dQ4AQEvv+bXlOe/S8EG+4xRDgdvDgGdS2ZYFAGCA31L/81jx8fnI0v7yp+N4W3Wcruf80TqPhjEaRwAABrifyrZmiI/Nn0hlKzPczFnRHO9rfsch5r69ylmW8zJ5fg0AYKSN1fnWnMWpbJFGI/Uw5/CsK8bL82sAAN/op1S2R3uWtI7/j7hj176j9iDn19Y5AABfaW1dGIPzOc9yTtcLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANPvI1Odi9jYjKApAAAAAElFTkSuQmCC>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADcAAAAZCAYAAACVfbYAAAACMUlEQVR4Xu2WP0sdQRTFr4iFKIooiqgERAuJYCFio1Yi2GojxC5FRLRRjJBvECtJmUYtLPwOFouVYGNhIgjCsxCxCMEilfHPPdwZHS9z9+0+BUX2B4f35syZt+/uzs4MUUFBwVuglXWkzRwss36yJlg1qs/TTpL7QZLLA8Zesu5Y56xNVnUYSOOGZGBepknG+oI+sE7cZwhyKL5cLgZ+H9mQRtaq8qLgqaGwSoo7Zv1V3gJrnVXl2m0kuf6HhIDrIZdGF+uWNaU7mBVtaEZZh6yE8heHP48xu8ofJPlD4669QZKre0gI/0hyFi2sXyTTuCL2WbNUWXH1JGO2lN/t/CXXTlxbc0Fx3zPCuqb4UyvLMKvHfU8o/UIx8JLHitP+mWtrLB/4G2cJN8YEL2QStPHdupCFLsLyrSIs34Px6Mfv5eI362PQTij9QjF0EZZvFWH5nm8k/ZjmmcFTm1NeQukXioFVMK04vxCcuramXHFfSPqHdEcaWM0wyBJWsSz492Jb+X3O1wtKlQ84/jjfwi8on3RHXqy7OMYa0GYAxhwob5JVYnW49gxJrskHHPBKytNgz8Q+qvdIgL5Mp5RYcbjT/mlaxDZxnBxeahNvJsnpvbSTMpxu/IoUKpyWV6z/JFMwBgrAHcS5dJ4kj0I0yOEYhdx3khymbxYaWF/p8f8tsmqfJJ4BXmirOM9nkrMj9k5rquApILdGknt1cNDd0eZ7Aaf5PW2+F3q1UVBQUOC5B+m9n5SZAf46AAAAAElFTkSuQmCC>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGMAAAAZCAYAAAAlgpAyAAAEKklEQVR4Xu2YX6hPWRTHl/Ag/xoj//L/gXhBQibJw5ASKZTiQTyYNE/zQDyRPCh5kDxoSpQoj5MI6aA8MC+kyJ/Ci6ShNDM1+bs+d+/td866e58/t/u7c7t+n/p2z2/tc89ZZ6291t7niHTo0KHDd8cI1WPVbNUN1enicBeDVNtUS4y9isWqV9bYD8HPDdbYEwjUcmvM8aPqpNcUMwa/qDb744Wqf1T7VdO9bajqiuqLuHs1gSQftEbPDnE+bVINN2NNwcc51ujB51ni7nVC0vd6LS4pjTmqeqv6JC5Ie4rD32BW/uSPB0vrfJyHiaoXqsn+NxzKHQeeSfOqWKn61RrFPfA71Wj/m7/XvL0J51V/qz6Ke6a1xeEueM7rqjH+9yhx5xIHC/7G7JUQmI2qqeKCGUsGFXFGnAOB38U5YyuBpATstQjWXmlWFUNU51QzjH2Y6rLqs7GvVv0hbrwuK1TrxSWRZ4glY4Vqu7iJGHgiLgbWN9p1phpv7LUJM9sGEJaJu+lfOdtMcdWSibv5D6q7qnl+nICf9cfAg1IVTcEf7m0JdntNngP7TmOvQ5hQsWRQ5Vz3Ys62xdtSMWMSMZkaU5YMgs0MPJ6z2WQQfMZ/9uPMlvv+GGgfVEVTePh/rVHc5oBAZMbOpMBO5TalLBlMMvygggJlyaAqmCg9qo6yZMQg8DhCf8zzVFz/JfgTvI2qaNrHA+9Vt6xRXBJiyWBixOx1KEtGjIfi7jXODngYq3utAk2TgdPczPZ/eirOhd7KOnFVWudxnwOqXVKvr1ORJNaSSTzofZkM7sP5KRj/zRrrUDcZ7CrY2h3xx1VQqqEqCNQdcRsCkpR5exk8EC3Jkkk86H2RjGnittpr7IAh1cIqqZuM3aoPUtxVpCDgnB+qgvXkWGu4q+dWLXCpZFAtsaCHZOQX2rrUTQb3fmmNEdqeDJzdlvvNvtu2KsDGgh3eAWCfFK/Pw1ctcKlkhAXcridjvb23F/AA3YBqz78YMgFitC0ZtBpK0xILFGTiqiIP5+avz44s/14Sg+Bk1qgsVf0n3T+RsOvhfwhsYJZ032jEqEoGz3PD2Ni9pc4nGamxUqqSQSJuS+tzCOJFMHY+VUEp56sCbGUsEjeTy2AW4pcl9dK3Trq/9IWvBVUtsSoZjF2QYgwuSTHxAT6V2ElRCcHBUSsCEGYtztnxIHuzsoWZcia408UtgvcKo3GCfylYRPGVRPP3TXG4CyYRSbO+BkLLs8qk1YJS56BYm+Kl75TEW3ifQfCuWGOOB6pHqueqw8WhKKEdlc3qTeI+3K2S9A5vpKST0Q6IA1U64Eh9KGzCVilPaG+Cv+w4ByTMdioq9aZbBS3xT2tsI6xZN61xIMFuzu6c6jJX0u2rt8HPDdY4EJmvWmCN/YhJ4r4w/K+LdocOHTq0ga+0hQQp3lpPSQAAAABJRU5ErkJggg==>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFkAAAAZCAYAAABaU4LDAAAEe0lEQVR4Xu2YX6hOWRTA18SUPzMYVzSZuogHUdOkISUPMn8QDySKh4kHJW9qNPKg5mnkQdPkQXTzIMXDNBleRjmNmpQiRaQURZI0UaSRYf3uPvueddbsfb9zbm6+qe9Xq+98a+/z7b3XXn/2/kR69OjRY1T4W+WYyjcq91XG1JsHmajyp8pk39CBxSobvLLL+EDlpkq/b2jDdpUj5WefaxsvwbCzy+97JAy4eaiHyHcq91SWGF0TmPRtCYvwTJIwp8MSNnCkfKqyW+Vnla9dm4U+jLdR0uMNqJz3yibgRQ+lWiQe+oPUPWutygmp+nyi8mXVPAgTLJyuCa9VdnmlhMixC+IZHfNtA+vAcB+W3+OmWo+kDzaI4FRH5b9jsf5DKoucviO/StghC4Nckirs8dzjVbN8JMHwljvS3ovHSj1CIoz/r8q3RsczujNG14kZEiJuodO/kWCsyDUJa7Tw7kkJc7Rg4F8kHXlZCHE8xMIP31CZVn5fJsGTYgh9pjK/fGaw76V9HgYWtsUrJejZNBYaIeSZKwZqCs5Dfx/6zyVsmP2Od1uI1rMq45we+E2bKjtyWcJL26QqZnjk/thBwmKt0RkAbwZCCoO0hcmzCJ92gKgppBoDWHSca1MKSfcnNVh9/P6VVB66SfKGpC/ppDHkqoMSXkT+Udlb6xHYqfJS5YXKvlLHhP6QkXnx5yrPVD52egxblGKNHPXM0eqHI+f5Xs/8T5c6BM/eato9vI+0Ag+OAyBX681D4H1TzHe8OBYHDE4E/K6yfKhHnpUSQtaH8vswMkwodVF+qzfXIKJwkMaQxF+VzxjqsYRB+FwQOyXgBGKrP7v/Y/mMsX0x81A4/ULhfRj5nFR1CYcjmmm/rjI9djIUEtbbGI5Q0TjA2ZScyCD7jd5DHrZHHLwS7wQKZ6qgWXJGxrPZvELyRk4VoxTMMTWGNzJzt+mBws4c6JPKy4W0MDKeS2d/7ovpg8KUghzGiSIWCfKq/51OhSFnZGCTL0o9X1N0Kb65d1IUEvrHeUaelHpg8+6qzBxqrfT04QLjKaSFkfE4BozHMQsVNzUAqcCfJjheeSNjqOGgL++kQn+phPHnGF0slHZxFG3yvzdiBC/EUJxMLOjuls+02ZOThTS6wytlBIWPAcmvHgbgSOMpJHixJeXJqQ2ycCxks9ggT+oysk7CXO1lhAtFLqShyWWEDWIsjmyWWJ9SdYnNLrxyOKaqnFJ5IMH7+GQS8RpqwYu/8MoSCsdA+cw1NVUwPLnLCKyRsHEcJxEWvKLWQ2SVylOVC5KOCMBY1B2K2E8S+vvInaXyl8otCX+CsRaKXy5CsA+b3gp+jLDgjk8B6Ks3D8IiWEyO9RLO0Zw3H7m2HKSF1NU1QhHkzyGiIrXpEbw7Z2RgPfzxdUDyV3/qEBGKDagX/mgZyeXwrib3B1FTMH4uXbxrcEbSTCqFdDWkKkJ5pJCaUpE3GmBc0lYujXQ1nLcxVlsI6XleOUpgWIpov2/4P3FF8kW1G1itMtcre/To0eMd8RaSrQPd2rcvxQAAAABJRU5ErkJggg==>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAA7CAYAAADGgdZDAAAGlUlEQVR4Xu3cW6h92xwH8CGU+7VcQuefUHJyDbmmXOKBXIoTTzoPx4M8UNTx5o0HSaJEhweSlIQ4eNgdkniQIjqRP4mQRFGSy/g259hr7LHnWut/1n+u//mf3edTv/acY84917ys3fjt35hzlgIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAxfPYGq+tcf9xAVwA36lx37FxwX1q/LXGw8r0O6M/DvPvrXHD0AYAR/OEGv+rca9xwQXy+Bp/q3FTjf+WK+vAI+fkwzVOFtr/WeNrZTp3Hz27eDWH7vc/atxc46c1XjMs+36NT5dp378wLFvbO2t8q8a7avxyWLZNzu2/a7ytxh9qPPPs4lNfrfG+sXHwphqvHBtnaf9NN39bmf5xiVzPJGS5tok7alyal/X+XC723w0A15HnlKmDvMj6hPTRZepo93lcjZfV+Gw5n7D9pMZD5ulUZrL9JFVrO2S/v1nj1d18Er1WPU0Sl+NqklC9oJtfU/Y3Fasmn/WRbn6bn9e4sZtf+mfiaXP7voQtx74k28vv9wlbpvO3EEncHjRPJ0lOMrck639sbASAY0hn9KWx8QJJp5rOuZf5+w1t2ywlbElw/9LNpxJ00s2v4dD9zjpJlpokIrfM0zmWVI6aVLFe0c2vKd+rfmgxx7MtgWpaIvXAri3VwnEfT8p0XLsStnzetu/198r0u33ClnVbNfLWrj1Vyl3GawQAR5EO8cXz9C/K1ImNFY1jeUyN/9T4cY031Hj/2cWrSMecY+ylk33q0LbNUsI2SiKyrQpzqEP2O1WhrNOqQ3FS4+vz9LPKtDzDrA8uV1axO1S+Rzl3Te6V3JfcLK2T7fRDzl8s0/dzX8L2qbIZ4uy9pMaTyvmE7aE17izTtm+f2zKkesPpGsv+Xs6ebwBYXatoZNjnc2VKBsYKx7GkI0yy1vyubCpBo99eQTzydO2ztiU+bfhrn30JW6uErZ3kHrLf2xK2RPPCMq2TeGvXPvpyOX+Ox/jA6drnrZmwte1cKpt70vYlbD+r8YyhLdco977FmLBFlrfqZP4mPjlPZ/j7ZP45+lE5/zkAsKqWbKQacYiXl6lT2xYf36x6zr/K2QQt+9EP5a3lkMSntythS6feEt5txnMyxtM3q55xyH7vS9hScWpJSIYrs+475vm1HSNhS3LUt+9K2LI82+t9u5teSth6Sfgi9yj+fp6+bf7ZOym7rwkAXLV0QLl3J1WLdJTpnK6F3IeVz3v4PN8SjWNIkpInOnt3JTnclbAloUpVJh7RL1jBofuddTLc2STxaAn5eI7zcEJ/L96aTspUtW1a9XaX9j1o5zSyf+8u0/nIsjG2JV1jwta2vRSjt5TNUOgbyyZhzPbGatpJkbABcGS5/+a583Q6rnRIqXq1DjOVo9fP02tqT1Y2r6txuZsfZb/2Rd/J93JvUv9ZGe7t5/Nak6WhrmZbwnbnMN9Xk9awb7+fUpbfnZfK5RO7+VzjllCMyUmuQ6skjTLEPJ7jMXbdu5WnZvuKWG7ov9zNv7QsX7PsY0vk23z/ZGuTZHlXhe2k7E6kcr2Wkr1+KDTyGe3aZr/GbY6JIQCsLp1hq6rlxvlUvm6f5/O6gkvzdCoca8vTd3nY4c1l2o9jfEaT4b8XzdN5r1r/pGQ+e+m1Jum4byxTQpMhsSeXzROaea1HX6FJLN3gfrX27XeeTh09r8Z35+m8x61/tUZ+v6963VGmdY4l9yi2pPJPZVO1asnn0lOcudH/M/N0qlljYpwkL8eY7+tXajzq7OJT+cfj1rFxlv1IMpmkL9e1NyawqQy2p11TkUwi3RuTYABY3aVuOh3hs7v5dES/KtO7u44tn7VvqO9qPb9MlZOlhxP6JOZ6s2u/8/LbJUmIcv/gq8YFZUo42othlypca8v350M17j0uKJsHAEY51hxzjv1QOc48yHJXZPhzKYH9RpleNpwnVHupMF4e2gDgmklHftLNP6CbXkM6wLfP00nU7u4qRX8z+j3J58eGe5BUMI/xsuFeqrhLw8ZryYuA8xJfALjbfLBMVY4fjAtWkPusMgSa6kuStWvxGpFtPlF2P+V5vcrQ9bWokB3Lr8eGI8h1/eHYuJJsu38xMAAAB8rQ6HvGxhX0D1QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwnv8DrHZYYL3Dgu0AAAAASUVORK5CYII=>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAABMCAYAAADQpus6AAAEfUlEQVR4Xu3dPYgdVRgG4BOSgBKjokERIoqNSPwJqAFFsTGiiBaiIGhnkUabqAhWaS0EsbAQQSxESCdBsLAYtFNQC0VQxB+QlKKg4L/n48wk556dO3d3w81ubp4HXnbmO3NvsVvsx8w5Z1ICAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADOdydyXmiLlR05f+YczNmZ83HO0ZkrAABYmgM5/6Xphu2bnEea2vPNOQAAS9Ll/JDmN2z7UmnoAADYAsdTedw51bAdyfm9LQIAsHzX5hzuj6catrdSGQcA4Cz7pDqeathezDnZFgEAWK6HUpmX1mbsTtpdyRw2AIAt91uaf4ctRMN2Y1N7ujkHAGAJYsHBoZx/c97NuWJ2+JQbUmna7k+lcetmRgEAAABgGYa5X23+ybm+uo6Ne64t9J7NeTVndzuQpsdaL6fyt/op585mDABYMXtT+ccfPwcX9rWrqxqL3ZRKs/t3Gl8cEWNDM/Z1zjXrHGvFtfX4h9UxALCCHk5rV1ju6muxUpONi8URbcP2eM5H1Xnc3fy+P54aax1Ls9udhJi/BwCssA/SbLMQYuJ+NGxxp42NG2vYulQ2+B1cl043yl2aP9b6K619ZyoAsOKiMagbgIv72sGqNuWCnKsWZN7Kzu1mf86P68giYw1bnNdNWfxehqZsaqzWpbXzDSPR4AEAK2pPKv/w38x5vc9t1XgsPIjasu+0tQ3IsnNPWq6z3bABACtsbP7aIBYcPNEft3OmmDbWsH2b5jdlU2OtqN/eFgGA1dXlfNkWe7G9xK39cTQT8x67RdPXPjJs8+mpq7e3nWnt49yxLDLWsL2RZjfzjd9tbAYcpsZa0Ty/0xYBgNUVd2uOtMVel2YbtuGYxcYatitzfq7O45pX1jHWujyVv9slVe3t6hgAWBHRgNVzoGKlaKtu0jRs6zM8yqxTv/803m36Rc5LOV9V9UVjrVgYEhvmxvc/04wBAOeReNR5b3/8XiqrQZctXvD+VCqNywPN2DwP5nyWyud+acYGO9L8OWEAAOe073IeTeWuz7K9n8r+b4OYw7VodWqM13O94vMnqvNBNIAaNgCAMxQNVczlGsQcsHnz6wbxuDFWWA7GVlfenXPzSB0AgA24KJWGKn4OulQexU7p+gyG7xke38aj0ONVHQCATZrXsEWmdH0G7fd0TR0AgE1qG63Q9ZnS9RnU33Mo50BTBwDgDERDtbc6jw19Y0PZKbHdSP3i+n3pdGMWK07juI3tSQAANumPNPs2hV/T6eYq5qIdrsYGd+ScrM5vSaVRa40tRgAAYIPiEeZwt2x/mt35/2gqDdfY67Hiusv6489T+Z7apalsLhufj73dds8OAwCwEXtyXsu5rx1I5XHpvMeZj6Xy7lPNGADAFnoyZ1dbBABge4hVnsfaIgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwLnkf2PiEcsI0aAFAAAAAElFTkSuQmCC>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAZCAYAAABZ5IzrAAABy0lEQVR4Xu2VvyuGURTHj1AGkR+ZWJS/QBRZlRKLgcEgk6QoRTYGm0lKyUJZzGzSW94MmJQUJimTwWBAfpzve+593/Oc977v8xDb86lvPefHPc+997nnPkQpKX/LPGuLNcSqNzFPE0kO1GZicQyysqwv1htrlqReEUusS2WPkwyaUj7wyOp1z5WsD5K86nxGGCzuiLXAqlD+UdatsvNckRRucXYr64F1zmpwPqxkl1XnbLBNMm5M+UIskuTVGj/sHePLsUnRAe0ku4GJNjtfn8t5cjbweRkqfpnGjvsxwyRFlpUPL/xkbShfkglVkdQ6sYEkdJBsPwrsm1gITA65/Tbg8AsrpdVCaph7pwuSjojjhaSwPqiWTpIcnKNfgwN85hRqS3QV2n7NPZcDDZJoN+JYJyk0YwMk7ftO0vpxoClQZ88GyoEOgjS+VQ+NH+BTTSi7kUp/Nn+ocYUkAt3hD5nG3zHYKU8360bZnuBdorim8FmDPWl8OSeScZV7MMkM65XVo/yYzCkVfh0QLsu4A+tv/hHjn2bNGV+OLtYd65jkJRj8TNEV4f/md9IKnRQHauHz43eDxR9Ew8XggK6QTGiAVRMNp6SkpPwL3wnSbMhPyOttAAAAAElFTkSuQmCC>

[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAAeCAYAAADnydqVAAAD3klEQVR4Xu2aTchMYRTHj1A+Q+Qj6n19JwpJInYUiQVlwcKShSwIJUlJibKQj4heFjYSNsjulSWx8UokQz4WQikbCufnuc87z5y5M3Nn5mLmzv3Vv+Y593PueZ5zz3meK5LTDINVo6zxLzDEGjqVYaorql+R3qq+qwqqHcXdUmGQars1KgutIQVWqG5aYyfzVXUtaG9WfRM34tJilZSO3iWqB+I6VtoMUJ2yxk7mh2q5sS1SnTQ2Cw+y2xqVsarhQZtzvQjaHux0pL/BGNUWa+xERqj6VOOMnYdP+MaJlSDs7pfyfW6puoL2NtX9oO1Jw8Fce524TmWpdf8dwXpxDrDsUx2xxgocV+1RzRHnXEuvxJ+rWQc/Vx2Ofq+W8v/xWjXJ2DoOwrANz2ShOGpl1GYULC5uLoN3NU62I9fTK67DWCo5GKdUEhEHuKcvqnlRm3Bs7/GDapqx1QW90megceIGDvTv3Xow4j6JC7UhZ8Xde8hl0w5ZoLqrOihuJFt6pT4HJwFn+qjA+5aEzYbjpkcwvYkTvBPn0OlRG9GT6UHY43p1K7BByrNYHhIPfaOxV3MwzuU/MpJxsn3QZOgXjA2acTDHcv/+d9x5XqomWGMj8JB+WqM4R9OLUrtQShCCL0kx0ryJVFDt7d+rlDgHU0cTmi07VcuCNu/5J0EbqIn99T9LfBJWi8fini+jt89sIyrFRY26obdyk0wSWIj/jOKmQ0ULEOfgpExVPbPGFMHBPcbGNZcaW0PMF+dgygULxTbb4mZw2omL4jrqUdVosy0pU1RzrbFB1kjx1TJRdUdKJ1EomW4H7aYgeyM8+4wz5L24G0lzRqiduSrpzEVzjtPiwvpD1dDSzXJItdvYGsJnbx/FhYjzkQriHLtJNVBcGGdq7oxqLQcmgPeWfzcm0SN3WE6aEJ6Zx6UXeeciCu7u4m5/Epd74kIHsyv/c0T7xKYTVTc94g6knqxGmGSNFHecLSVyWhC/GoLTKkFJEjqY2pnjCO85LU6Soe9r4dDBScomOoafNEmi8e6wloK15VrPp2Xx9S9TfdVggqMRB2cBZppYimwrcIx9eaNd4U4BzKhYB5PeVwvrWYH/Gbe6lDkY5T4RY9211kJ6VuB/M11ItJsl5fVqZiBUvVJtVT2VzsmgC+IWYFhtIsJVinKZgBq40pcHWYQqgQWGc1GbERx+xpPT5hC1+JBghuqG5J+yZg7yjMnRb1/384qC2apj4r60zGlDusQttHhYSr0uLvcgyTwhbpGG76hy2hAcGc7UURr6ZUa+vpgZbMvJGDifdWVGMM7OySDhiM7J+Xf8BsDG/1s23zMAAAAAAElFTkSuQmCC>

[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAAaCAYAAABsONZfAAAA50lEQVR4Xu2RPwtBURjGX0kZpJTIpGxSFlHKJB/DZvAdTD6EyWIym+x3UGSx2X0CC4uE57nn4Hjvvdj51a/bfc6/95xX5LdIwx5cwYEaC2ULy85/Cc5g0sleqMCGygpwZ78BmnCtQ9CCHkyp3GcEhyqL2byr8gcLmIMneLWe4cSdpOFgQp6LDvAIx+4klyys6RB04EUiXq4uZqGGG/G0jB7gZac6tLCxLDVwEk9Y6tDiiVkUoC/hA0W4l2CzfVjaXMylCcutwg1s3ydpWBpL5HPnxfQq/jIjBJ7E3b8mqj9vierPn0/cANuhIz/Hs+3XAAAAAElFTkSuQmCC>

[image17]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAABKCAYAAAAG/wgnAAAEj0lEQVR4Xu3d3ctlUxgA8CUzNUKaRuSjfIQauZML5UKSjwsujAvlD+BCCqHcEEkkaVJKykchE7mQciG9cSNuKBPFFJqhlKRQyMd6Wns5a6/3fSdlznnPnP371dNZ+1l7n337tPb6SAkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACOWqfmOK2JRTsmjd+/a9wNAEAUSYdyvD+0I17M8WcqxdS8bU/lnX/nuHJon5/jpxwnNfcBAExaLZb63N4uNy+7U3lfKwq3/V0OAGCSdqZSLO1octuG3C1Nbp4ezvFDl7s5x1tdDgBgkqIw+qvLvZPj0y43T9+l8WhefIrtR9wAACbro1SKoxpRvB0/umP+2vdHvD3uHrm2TwAArLp+/tpzOT5prv+LWBzwzGHijtmt65yb1o+mxfXlXS68ksqCiEv7DgCAVbXR/LXX0vr5ZPO00fy1zebPxcpVAIBJidG0g10uiqW1oR2fS8/J8eNw/VIaF3dHQrzvhua6bvFxcY6Xm/wJqRSTAMCE3ZXj1RwXpDLpPX5DFBCrNm+qFkVtVI+nMpL1SI6zUvlkee/QF9tsnDi0/68X0vj98bmz+iWVFaJ7mtwlaVzYAQATEwVKbOAazkyzEZ4QRcvXQ3uK4pPlGUO7jrRthVhFGqcyAAATFKNna13utjQr2MKUC7bYcuODHF+mxZx8sJkDfQIAmI7Yh+y3LhcjOQq24qs+sWAx8vl8js+6PAAwIcel2TyqmNS+0We3KNjik1zsDxb3tWdcxsjTQzleT2WeVVX/M+bGfZPjqVTmgkUu/u/nHL/neK8+MNiX441UNq59tOtbtLNT2ZZjKw6Fr6Jg+3D4BQAmrM5bq9EffB65eh1zutojk6Lvoqbdiutrctye4+khd12OP/69I6Uvcrw5tKPwazeN7Uf+qvhEGUXg4QIAYGWdnkqhFSNiVaxarGKUbK25DsfmuCptXLD1qyqjYGv/77I0ey5OGXgix41DfF5vOsIeWJEAACaiblnRinlt7by1tt0XbPFZ8/6hHYXXtqYvrmP/sFZfsMVcuVqwxW/0AwDQiALs3S73bI6bmuvNRtjuTGUVZRUFV8z3qkXXZgVb+0n02xxPDu3r0/hd5zVtAIDJigKsnmf5cY5DqZwAUEW+RrvZax11i9WLsYAgjleKCfox4hbz3drn2lG8OsL2fSpz5e5u+sIVqTwThVzfBwDAAvSfRAEAWDJxvNKvfRIAgOWwO81WgNbjngAAAAAAymKNdqFFxI7RHQAAbJk4WSGO69qVSqHW7kUHAMAWuzWNNxKOfeliM2AAAJZEjKidPLRjZC2uAQBYIgdz7BzacYj9nqbvlBwPpnI+ahz3dU/TBwDAgmxP5dD6OOHhwq7vvlROeYjtTILRNwCAJXRg+I1RuP1tBwAAy6GOqu1LZSUpAABLJE5z2JvKXDYAAJbQYzmu7pMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAR69/ANba+fWcBGLfAAAAAElFTkSuQmCC>

[image18]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAABKCAYAAAAG/wgnAAAEvklEQVR4Xu3dO4hdRRgH8BEjKCgqBFQQFx8IgoUgFoJaxRdiKrsgCBbpLAwoiMiC2FiIiiCEkKBgZUAsfMXmoIVoGpsgRCwMPgoRETQYEx/zec5k58zdXQhx70nu/f3gzz0zc3fPbvcxM2dOSgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALAwrmkybxenae8PAHDOiyLpeM6bw/UDOf/kPFR/aQtdkXN/6u9ZirZDOb/XXwIAWHZRLN1StZ8e+ubl1Zyfm764/+6mDwBgKd2QZouzwzl/N31b6cfUF23Flan/m3ZUfQAAS+uFNJ7dWkl9sXR51bfV2hm+ozkfVG0AgKUWs1tRMJU8NhrdemWGr+SPnItG31hzQc59bScAwKJrZ7eiHU9unomXcvZukii0NtLO8HU571Tt2nc536b5zv4BAExqvf1r0d7e9G2ldv9a7J87UrVr37QdAACLrsv5tOkrBdydOTfnXJX6PWWh/e7ZujT197us6ov2G8P151X/7Tm7qjYAwEKL4qfeN3aiGov2npyPh/ZdOTuH61i63Gx580zEOWv13xAFYnh7GNufxkufz+RcW7UBgAUTe58ez3kk9XugTg7XMWMTxcKDa1+lcTD1M2Hbcr5qxuZpo2VSAGBB1HufutQXbUWc+fVk1WYsZt+6nC+b/nmrZwEBgAX0XnXdpXHBFvY1bXoxq9a1nXO2kvrZ0dfaAQBgcXVptmAL5XVMXc7XOe8P/bFn69ecF3P+zLlt6C97r2KDfNk8H4l3YZbr63K+z/kljfdjXZ1zKvV7xeIz2iF+V9lDdixNX6SUYzni/5tK7Fv7pO0EABZbl9Yv2MLDqS+Y4sXn5aT9H1L/QvQQM04xXtTXb6XxhvwYe7lql1m+S4axWrTLYbFxHfd7Iuf1098Yi2Jus5QHBgAAzktd2rxgiwcUijhANgqoR1P/kEIk2nHURYjrW4frD4fPIsbiacyiGz7joNj2/vFUZDwFGeLn6mMu/m+rCxQAYEF1abZgKqJgq8fKUudGS4KrqT/oNY6kuH489N/PxfJo0Q2fsezZ3j/a0R82ux8AwFLo0mzBVLQFWziUc6BqP59mlz67ql1sNMMWS58xVn5HfEZ729BWsAEAS6tLfTFUJ5Yii/LQQaTMdhXx6qTo/y31p//XYolzvdm1krIvLlKKwdjHdjz1y6/xGe0Q9y3fjb8HAICzUJ76/GLUu9xitvCVNPsABgDAJGIWbCXn3nZgSUUBu1q1/6quAQAmcc8Qeu1MYxS0AACcI+Jok3ofX7TbAg4AgAkdSP3ycMyqxVLoT+NhAACm9lnTjrdD1K/iAgBgQvE06O6mL44n2dX0AQAwkSjW2iM8Ymm0vL4LAICJHUnjBw6eytk7XMeRJ+/mPJtz9PQ3AACYqzgk96OcYzmn0viok+fS2iu5DiazbgAAc7c95462s3Fi+Dw56gUAYC7W279Wi5fYx/tSb8rZ04wBADAHd7cdjZ05O3IubAcAAJheFGmHc25sBwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADOH/8Cl2IDFTLciboAAAAASUVORK5CYII=>

[image19]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAaCAYAAACtv5zzAAABW0lEQVR4Xu2VzSuEURTGH0kpSlKk5COllBJLxcrG3+APGM1yllOztLCwYCklCzsbC3s7C1sLC4oiS6Uo5ON5OvftvU4T3XEXFvOrp+k+Z94zc889575Am/9GFzVEDTtloxeW8I76pCbDWloI3jvVUTzQKs+wZJ4NmL/oAyno3ynJrQ+QGiy27wMp9MOSHPsAOYTFKj6Qwir1QS07vw+W/Nz5yezCyjOCsquq1A3sDHrKr6YzSz1S9cjrhHXOa+S1jMqjMvjy7AV/wPnJnMESdTu/ONxp5yfzhOb9fwXz/VSrpEuw1p7CLzv8qf/lS5p0oZ3OUxPUNmzKxQGatLcSz1BrsCQX1BjKZOIlxDQj4ogaDesTlCVVKbXbZIoS7FCNyF+B/XjBG2xH2VinrqP1AzUXrf/MPew8dDddIsMt69EAamYGYQOZDSXTu+I0fGZnnNqCHfrm91CbRL4AE6hD1OamyQgAAAAASUVORK5CYII=>

[image20]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAAbCAYAAACJISRoAAABXElEQVR4Xu2UsStFYRjGX0kp7iCDlIXBTQpFSslklfWW3WA0klESf4CkZLJYDWSzMfkDDEoZzJQUnsd7vnu++1z36p5zlOH+6jec5/1677nf957PrM1/pwsOwEGxUDbgZxOPYbm6Oiev5k2VXfP8TQtZYKMPDcGSpf8qF33mTc61AM6soB+ZNG/C81GezWs3WmiVI/gIhyydtjX4YH4mPenSbHCrbq1+qng+m9G6RnTCBfOXa8iKedNFyTm6zPslj5mDT/AFnkqthtCMWxUTvp9pyWO24T2ctV+2NGxVt+RhqsYkj+E0Xmn4E2H/FWas8cwUDsae+ZpLuAo7alZEsMBGnCwlDEBv8jwMx9PyN+9wXrIqvADjSQpWojX7SbaTeBfVCF/wGpYkbwk2GYWHcMvqb2Zu44lkhcOR17EvnHU4omFRzMBl89H/Mw7Mr5vcF2YzpuAFnNBCm8x8AXpvUeeCnvd8AAAAAElFTkSuQmCC>

[image21]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAaCAYAAAC3g3x9AAABBElEQVR4XmNgGAWjYASAMCC+AcT/seCLSOqIAhIMmIYg41UIpYTBLAaIJlYkMWkg/gbEpkhiRIO/QHwbTUyQAWKJL5o4QSDOANHoiSbuAsTPgVgJTZwg0Afit0CsiSbeCsTLgZgFSYwZiG2gNAi7ATE3kjwY8DNgumQCA8TVjEhiIDCPAeKjW0CsAsS8QHwYRQUUgDTXQNmcQPwPiY8MshkgkTUJygeF82kGLK4EAQ4gNgJiAXQJNFDEgPBNNAPEMWQDUHiuAWIeKB8UxtcR0qQDUIT8BOIDQLwaiO1RZMkA5QyQFAFyoTCaHMkAlIueMUBcBkoyFAMDBkgWBWFYGI4CBgYAzl4wi1t1WX8AAAAASUVORK5CYII=>