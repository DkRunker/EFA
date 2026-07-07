# Banco de preguntas oficial y simulado para preparación EFA
import random
from pydantic import BaseModel, Field

class PreguntaTest(BaseModel):
    id: int
    modulo: str  # M1 a M10
    tipo: str = "test"
    enunciado: str
    opciones: list[str]
    respuesta_correcta: int  # Índice de 0 a 3
    explicacion: str

class PreguntaPractica(BaseModel):
    id: int
    modulo: str
    tipo: str = "practico"
    enunciado: str
    rubrica: list[str]
    palabras_clave: list[str]
    valor_esperado: float | None = None
    tolerancia: float = 0.01
    explicacion: str

# Banco de preguntas prácticas (desarrollo)
PREGUNTAS_PRACTICAS = [
    PreguntaPractica(
        id=1001,
        modulo="M3",
        enunciado=(
            "Un fondo de pensiones evalúa invertir en una empresa textil que prevé pagar "
            "un dividendo esperado el próximo año de 4.00 €. La rentabilidad exigida "
            "por el mercado (ke) es del 12.0%, y la tasa de crecimiento anual indefinido "
            "de los dividendos (g) es del 8.0%. "
            "Calcule el precio teórico del activo utilizando el modelo de Gordon-Shapiro "
            "y razone cualitativamente qué ocurriría si la tasa de crecimiento (g) subiera al 9.0%."
        ),
        rubrica=[
            "Calcular el denominador ke - g = 0.04 (4%).",
            "Calcular el precio teórico inicial P0 = 4 / 0.04 = 100.00 €.",
            "Calcular el precio teórico nuevo P0 = 4 / 0.03 = 133.33 € si g sube al 9.0%.",
            "Explicar la relación directa entre el crecimiento (g) y el precio teórico del activo."
        ],
        palabras_clave=["denominador", "100", "133.33", "crecimiento", "aumenta", "Gordon-Shapiro"],
        valor_esperado=100.0,
        tolerancia=0.5,
        explicacion=(
            "Aplicando Gordon-Shapiro: P0 = D1 / (ke - g).\n"
            "Paso 1: Denominador inicial = 0.12 - 0.08 = 0.04 (4%).\n"
            "Paso 2: Precio teórico = 4.00 / 0.04 = 100.00 €.\n"
            "Paso 3: Si g = 9%, el denominador es 0.12 - 0.09 = 0.03 (3%), y P0 = 4.00 / 0.03 = 133.33 €.\n"
            "Conclusión: El aumento en la tasa de crecimiento incrementa sustancialmente el precio teórico del activo."
        )
    ),
    PreguntaPractica(
        id=1002,
        modulo="M3",
        enunciado=(
            "Una cartera A tiene una rentabilidad del 15.0%, una desviación estándar del 8.0% y una Beta de 1.2. "
            "La tasa libre de riesgo es del 3.0%. Calcule el Ratio de Sharpe y el Ratio de Treynor. "
            "Razone si es posible que la cartera A sea eficiente en términos de riesgo total pero ineficiente "
            "frente al riesgo sistemático."
        ),
        rubrica=[
            "Calcular el Ratio de Sharpe = (0.15 - 0.03) / 0.08 = 1.50.",
            "Calcular el Ratio de Treynor = (0.15 - 0.03) / 1.2 = 0.10 (10%).",
            "Explicar que Sharpe mide riesgo total (volatilidad) y Treynor riesgo sistemático (Beta).",
            "Razonar que si la cartera no está bien diversificada, puede tener un Sharpe deficiente frente a carteras eficientes, "
            "pero tener un Treynor aceptable si su riesgo sistemático es controlado."
        ],
        palabras_clave=["Sharpe", "Treynor", "1.50", "0.10", "volatilidad", "sistemático", "diversificada"],
        valor_esperado=1.50,
        tolerancia=0.01,
        explicacion=(
            "Sharpe = (Rp - Rf) / sigma_p = (0.15 - 0.03) / 0.08 = 1.50.\n"
            "Treynor = (Rp - Rf) / beta_p = (0.15 - 0.03) / 1.2 = 0.10.\n"
            "Sharpe evalúa el riesgo total, que incluye el riesgo diversificable. Si la cartera no está diversificada, "
            "el Ratio de Sharpe penalizará el riesgo no sistemático inútil. Treynor solo mide el riesgo de mercado."
        )
    ),
    PreguntaPractica(
        id=1003,
        modulo="M8",
        enunciado=(
            "Un inversor residente fiscal en España obtiene unas ganancias patrimoniales netas en el año "
            "de 70,000.00 € procedentes de la venta de acciones de bolsa. Calcule la cuota tributaria a pagar "
            "en el IRPF de 2026 aplicando la escala del ahorro."
        ),
        rubrica=[
            "Aplicar el 19% a los primeros 6.000 € = 1.140 €.",
            "Aplicar el 21% a los siguientes 44.000 € (de 6.000 € a 50.000 €) = 9.240 €.",
            "Aplicar el 23% a los restantes 20.000 € (de 50.000 € a 70.000 €) = 4.600 €.",
            "Obtener la cuota tributaria total = 1.140 + 9.240 + 4.600 = 14.980 €."
        ],
        palabras_clave=["14980", "19%", "21%", "23%", "cuota", "IRPF", "ahorro"],
        valor_esperado=14980.0,
        tolerancia=10.0,
        explicacion=(
            "La base liquidable del ahorro de 70.000 € se liquida por tramos:\n"
            "Tramo 1: 6.000 € * 19% = 1.140 €.\n"
            "Tramo 2: (50.000 - 6.000) = 44.000 € * 21% = 9.240 €.\n"
            "Tramo 3: (70.000 - 50.000) = 20.000 € * 23% = 4.600 €.\n"
            "Suma total = 14.980 €."
        )
    )
]

# Generación dinámica de 60 preguntas tipo test para cubrir holgadamente los módulos
PREGUNTAS_TEST = []

# Módulos y sus pesos
# M1 (25%): 15 preguntas
# M2 (10%): 6 preguntas
# M3 (18%): 10 preguntas
# M4 (8%): 5 preguntas
# M5 (6%): 4 preguntas
# M6 (5%): 3 preguntas
# M7 (5%): 3 preguntas
# M8 (10%): 6 preguntas
# M9 (8%): 5 preguntas
# M10 (8%): 5 preguntas
# Total: 62 preguntas de test

definiciones_modulos = [
    ("M1", 15, "Mercados e Instrumentos", [
        ("¿Cuál es la relación entre el precio y la TIR de un bono de renta fija?", 
         ["Relación inversa", "Relación directa", "No tienen relación", "Es una relación constante"], 0,
         "El precio de un bono y su TIR se relacionan de forma inversa: al subir los tipos de interés (TIR), el precio del bono cae."),
        ("El coeficiente de correlación entre dos activos es -1. ¿Qué indica esto?", 
         ["Diversificación máxima del riesgo no sistemático", "No aportan diversificación", "Riesgo nulo sistemático", "Correlación neutra"], 0,
         "Un coeficiente de correlación de -1 indica una relación lineal inversa perfecta, lo que permite la máxima reducción del riesgo diversificable."),
        ("Bajo la normativa MiFID II, ¿cuál de los siguientes es un producto complejo?", 
         ["Un fondo UCITS armonizado", "Una acción cotizada en mercado regulado", "Un derivado financiero (opción)", "Un depósito simple"], 2,
         "Los derivados como opciones y futuros se clasifican siempre como productos complejos debido a su apalancamiento y riesgo estructural."),
        ("Si el tipo de interés a 1 año es del 3.0% y el tipo a 2 años es del 4.0%, ¿cuál es el tipo forward (implícito) a 1 año dentro de 1 año?",
         ["5.01%", "4.50%", "3.50%", "6.02%"], 0,
         "Calculado como ((1.04)^2 / 1.03) - 1 = 5.01%."),
        ("Una opción de compra (Call) con precio de ejercicio 50 € cotiza con la acción subyacente a 55 €. ¿Cuál es su valor intrínseco?",
         ["0 €", "5 €", "55 €", "-5 €"], 1,
         "El valor intrínseco de un Call es Max(0, S - K) = Max(0, 55 - 50) = 5 €."),
        ("¿Cuál de las siguientes afirmaciones define la duración modificada de un bono?",
         ["Mide la variación porcentual aproximada del precio del bono ante un cambio de 1% en su TIR", "Representa el plazo medio ponderado de vencimiento de sus flujos", "Es equivalente a la duración de Macaulay en todo momento", "Indica el grado de curvatura o convexidad de la curva de precios"], 0,
         "La duración modificada mide la sensibilidad del precio ante cambios en la TIR: DM = Macaulay Duration / (1 + y/m)."),
        ("En el mercado de divisas, si la cotización EUR/USD pasa de 1.10 a 1.15, ¿qué ha ocurrido?",
         ["El Euro se ha apreciado frente al Dólar", "El Euro se ha depreciado frente al Dólar", "El Dólar se ha apreciado frente al Euro", "El tipo de interés del Euro ha subido obligatoriamente"], 0,
         "El Euro se aprecia puesto que ahora se necesitan más Dólares (1.15 frente a 1.10) para comprar un Euro."),
        ("¿Qué tipo de subasta se utiliza de forma general en la emisión de Letras del Tesoro en España?",
         ["Subasta holandesa modificada (mixta)", "Subasta inglesa de precio único", "Subasta alemana de sobre cerrado", "Venta directa sin subasta previa"], 0,
         "El Tesoro Público español emplea un sistema de subasta mixta basada en ofertas competitivas y no competitivas, aplicando precios marginales y medios."),
        ("¿Cuál de las siguientes estrategias con opciones financieras se beneficia de un mercado con alta volatilidad?",
         ["Compra de cuna (Long Strangle)", "Venta de cono (Short Straddle)", "Compra de opción de compra cubierta", "Venta de opción de venta protegida"], 0,
         "Tanto la compra de cono (Long Straddle) como de cuna (Long Strangle) consisten en comprar opciones put y call simultáneamente para rentabilizar grandes movimientos."),
        ("En relación con los criterios ESG, ¿qué implica la estrategia de 'exclusión'?",
         ["Evitar la inversión en ciertos sectores o empresas que incumplen normas éticas o ambientales", "Comprar acciones solo de las empresas con mejores puntuaciones de gobierno corporativo", "Invertir exclusivamente en bonos verdes", "Ignorar las variables ambientales al valorar el riesgo financiero"], 0,
         "La exclusión es una estrategia de inversión responsable que descarta explícitamente sectores como armas, tabaco o carbón."),
        ("¿Qué mide el tipo de interés nominal (TIN) en una operación financiera?",
         ["La rentabilidad o coste del capital sin tener en cuenta gastos ni frecuencia de capitalización", "El rendimiento real neto ajustado por la inflación acumulada", "La tasa efectiva anual que incluye todos los costes directos", "La tasa de descuento libre de riesgo del mercado interbancario"], 0,
         "El TIN es el interés pactado de forma simple. No contempla la capitalización compuesta intrayear ni otros costes añadidos."),
        ("Si la curva de tipos de interés tiene pendiente negativa (invertida), ¿qué suele anticipar según la teoría de expectativas puras?",
         ["Una bajada futura de los tipos de interés a corto plazo debido a una desaceleración económica", "Un incremento inminente de la inflación y el crecimiento", "Que los inversores prefieren activos con vencimiento más corto a cualquier precio", "Una subida inmediata de los tipos oficiales del banco central"], 0,
         "Una curva invertida históricamente refleja expectativas de caída de tipos a corto plazo ante previsiones de menor crecimiento o recesión."),
        ("¿Cuál es la principal diferencia entre un contrato de futuros y un contrato forward?",
         ["Los futuros están estandarizados y se negocian en mercados organizados con cámara de compensación, mientras que los forwards son contratos OTC a medida", "Los forwards eliminan el riesgo de contrapartida gracias a las garantías diarias", "Los futuros no tienen fecha de vencimiento fija y los forwards sí", "Los futuros son solo sobre activos físicos y los forwards sobre activos financieros"], 0,
         "Los futuros cotizan en mercados organizados (como MEFF) con liquidación diaria de pérdidas y ganancias, mientras que los forwards son OTC (Over-The-Counter)."),
        ("En opciones financieras, ¿qué indica la letra griega Delta (Δ)?",
         ["La sensibilidad del precio de la opción ante variaciones en el precio del activo subyacente", "La sensibilidad del precio de la opción ante cambios en la volatilidad implícita", "El paso del tiempo en el valor de la opción", "La variación del precio de la opción ante un cambio del tipo de interés libre de riesgo"], 0,
         "La Delta mide la ratio de cambio del precio de la opción respecto al precio del subyacente. Varía de 0 a 1 para un Call."),
        ("¿Qué es un bono cupón cero?",
         ["Un bono que no realiza pagos periódicos de cupones y se emite con descuento sobre su valor nominal", "Un bono emitido al par que paga cupones variables referenciados al Euríbor 0%", "Un bono de renta fija perpetua sin vencimiento ni valor nominal", "Un bono del Estado cuyo cupón está garantizado al 100% de la inflación"], 0,
         "El bono cupón cero no distribuye flujos intermedios; el inversor recibe la rentabilidad por la diferencia entre el precio de compra con descuento y el reembolso nominal.")
    ]),
    ("M2", 6, "Fondos de Inversión", [
        ("¿Cuál de las siguientes afirmaciones sobre los ETFs es CORRECTA?", 
         ["Se negocian en bolsa en tiempo real", "Tienen costes de gestión superiores a los fondos activos", "Son siempre garantizados", "Solo se pueden reembolsar al final del día"], 0,
         "Los ETFs (Exchange Traded Funds) se negocian en bolsa de la misma forma que una acción ordinaria, en tiempo real."),
        ("¿Qué caracteriza a los Hedge Funds o IIC de Inversión Libre?", 
         ["Límites de apalancamiento laxos y uso libre de derivados", "Están garantizados por el Estado", "Tienen comisiones de suscripción nulas obligatoriamente", "Solo invierten en deuda pública"], 0,
         "Las IIC de inversión libre gozan de gran flexibilidad regulatoria, pudiendo apalancarse y tomar posiciones cortas sin las restricciones UCITS."),
        ("¿Qué establece la regla general del 5/10/40 para fondos de inversión UCITS armonizados?",
         ["Un fondo no puede invertir más del 10% de su patrimonio en valores de un mismo emisor, y las posiciones que superan el 5% no pueden sumar en conjunto más del 40%", "Las comisiones del fondo de inversión no pueden superar el 5% de suscripción, 10% de gestión y 40% de éxito", "El fondo debe mantener un 5% de liquidez, 10% en renta fija y un máximo del 40% en renta variable", "El patrimonio mínimo debe ser de 5 millones de euros, con 10 partícipes mínimo durante 40 días"], 0,
         "Esta regla busca diversificar el riesgo: máximo de 10% por emisor, y el total de emisores en los que se invierte entre el 5% y 10% no puede exceder el 40% del fondo."),
        ("En España, ¿cuál es el beneficio fiscal exclusivo para las personas físicas en relación a los fondos de inversión?",
         ["La exención por traspaso (diferimiento fiscal al cambiar de fondo sin tributar)", "La deducción del 15% de las suscripciones en la base imponible general", "Que los dividendos distribuidos por el fondo están exentos hasta 1.500 € anuales", "La reducción automática del 40% de las plusvalías por antigüedad del partícipe"], 0,
         "El régimen de traspasos permite a los residentes fiscales diferir el pago del IRPF al transferir saldo de un fondo a otro."),
        ("En un fondo de inversión, ¿quién calcula el valor liquidativo y custodia los activos?",
         ["La sociedad gestora calcula el valor liquidativo y la entidad depositaria custodia los activos y vigila a la gestora", "La entidad depositaria calcula el valor liquidativo y la CNMV custodia los activos", "La sociedad gestora realiza ambas funciones para reducir costes de intermediación", "El comité de partícipes supervisa y calcula diariamente el valor liquidativo"], 0,
         "La SGIIC administra y valora la cartera, mientras que el depositario custodia los valores y liquida operaciones, garantizando independencia."),
        ("¿Cuál es la principal ventaja de las clases de acciones de acumulación frente a las de distribución en un fondo de inversión para un inversor particular en España?",
         ["Las clases de acumulación reinvierten los rendimientos dentro del fondo, difiriendo la tributación del inversor hasta el reembolso", "Las clases de acumulación garantizan una rentabilidad mínima fija anual", "Las clases de acumulación tributan al 10% fijo en lugar de la escala de ahorro", "Las clases de distribución permiten recuperar el capital inicial sin costes de suscripción"], 0,
         "Los dividendos acumulados incrementan directamente el valor de la participación del fondo sin generar retención fiscal inmediata en el IRPF.")
    ]),
    ("M3", 10, "Gestión de Carteras", [
        ("Según el modelo CAPM, ¿cuál es el único riesgo por el que se remunera al inversor?", 
         ["Riesgo sistemático o de mercado (Beta)", "Riesgo no sistemático o diversificable", "Riesgo de liquidez", "Riesgo de crédito"], 0,
         "El CAPM asume que el riesgo específico puede eliminarse mediante diversificación, por lo que el mercado solo remunera el riesgo sistemático (Beta)."),
        ("¿Qué representa la frontera eficiente de Markowitz?", 
         ["Las carteras con la máxima rentabilidad para cada nivel de riesgo", "La combinación óptima con activo libre de riesgo", "La recta del mercado de capitales (CML)", "Carteras compuestas solo por renta fija"], 0,
         "La frontera eficiente representa el conjunto de carteras óptimas que ofrecen el mayor rendimiento esperado para una desviación estándar dada."),
        ("¿Cuál es el Ratio de Sharpe de una cartera con una rentabilidad del 10.0%, desviación estándar del 15.0%, si la tasa libre de riesgo es del 2.0%?",
         ["0.53", "0.67", "0.80", "0.12"], 0,
         "Calculado como (0.10 - 0.02) / 0.15 = 0.533 (redondeado a 0.53)."),
        ("Si una cartera tiene una Beta de 1.5, una rentabilidad del 14.0% y la tasa libre de riesgo es del 2.0%, ¿cuál es su Ratio de Treynor?",
         ["8.00%", "9.33%", "12.00%", "6.00%"], 0,
         "Calculado como (0.14 - 0.02) / 1.5 = 0.08 o 8.00%."),
        ("El modelo CAPM estima una rentabilidad exigida para un activo del 9.0%. Si la tasa libre de riesgo es del 3.0% y la prima de riesgo del mercado es del 5.0%, ¿cuál es la Beta de dicho activo?",
         ["1.20", "1.00", "0.80", "1.50"], 0,
         "Resolviendo CAPM: 0.09 = 0.03 + Beta * 0.05 => Beta = (0.09 - 0.03) / 0.05 = 1.20."),
        ("¿Qué indica un Alfa de Jensen (α) positivo en una cartera?",
         ["Que la cartera ha batido al mercado generando un exceso de rendimiento ajustado por su riesgo sistemático", "Que la volatilidad de la cartera es inferior a la del activo libre de riesgo", "Que la cartera está perfectamente diversificada y tiene Beta cero", "Que el rendimiento de la cartera ha subido debido al efecto divisa"], 0,
         "El Alfa de Jensen mide el rendimiento anormal. Si es positivo, la gestión activa aportó valor por encima del CAPM esperado."),
        ("En la teoría de carteras, ¿qué es el riesgo específico o no sistemático?",
         ["El riesgo propio de una empresa o sector que puede ser eliminado mediante la diversificación", "El riesgo macroeconómico y de mercado que afecta a todos los activos por igual", "El riesgo asociado a variaciones en los tipos de interés oficiales", "La volatilidad histórica del índice de referencia o benchmark"], 0,
         "Es el riesgo particular de un emisor (ej. huelga, fallo de producto). Se diluye al combinar activos no correlacionados."),
        ("¿Qué mide el Tracking Error de un fondo de inversión de gestión activa?",
         ["La desviación estándar de la diferencia de rentabilidades entre el fondo y su benchmark", "La rentabilidad acumulada del fondo desde su fecha de constitución", "La comisión total devengada en relación a los costes de transacción", "El número de veces que el gestor cambia los componentes de la cartera al año"], 0,
         "Mide la consistencia de la desviación de la cartera frente a su índice. A mayor tracking error, mayor es la gestión activa."),
        ("¿Cuál es la principal diferencia entre la Capital Market Line (CML) y la Security Market Line (SML)?",
         ["La CML utiliza el riesgo total (desviación estándar) y es aplicable solo a carteras eficientes, mientras que la SML utiliza el riesgo sistemático (Beta) y aplica a carteras y activos individuales", "La CML evalúa activos individuales y la SML carteras eficientes exclusivamente", "La CML tiene pendiente negativa y la SML tiene pendiente positiva siempre", "No hay diferencia, son dos nombres para representar la frontera de Markowitz"], 0,
         "La SML se deriva del CAPM y aplica a todo tipo de activos usando la Beta. La CML nace de la frontera eficiente usando la desviación típica."),
        ("Si combinamos en una cartera un activo con riesgo y el activo libre de riesgo, ¿qué forma tendrá el conjunto de carteras resultantes en el espacio Rentabilidad-Desviación Estándar?",
         ["Una línea recta que conecta el activo libre de riesgo con la cartera de activos con riesgo", "Una parábola cóncava similar a la frontera eficiente de activos individuales", "Una elipse cerrada que representa la covarianza negativa de los activos", "Una línea quebrada con pendiente descendente hacia la volatilidad cero"], 0,
         "Al combinar un activo sin riesgo (volatilidad cero) con una cartera de riesgo, la correlación es nula y la relación riesgo-retorno es lineal.")
    ]),
    ("M4", 5, "Seguros", [
        ("En un seguro de vida unit-linked, ¿quién asume el riesgo de la inversión?", 
         ["El tomador del seguro", "La entidad aseguradora", "El beneficiario", "El mediador"], 0,
         "En los seguros unit-linked, los fondos están asignados a activos seleccionados por el tomador, quien asume plenamente el riesgo de mercado."),
        ("¿Qué es un Plan de Previsión Asegurado (PPA)?",
         ["Un seguro de vida-ahorro previsional con el mismo límite de aportaciones e incentivo fiscal que los planes de pensiones, pero con garantía de tipo de interés", "Un seguro de salud privado que reembolsa las primas no consumidas en la jubilación", "Un plan de pensiones de empleo gestionado por una compañía de seguros", "Un contrato de seguro temporal que cubre el riesgo de fallecimiento sin acumulación de capital"], 0,
         "Los PPAs comparten la fiscalidad e iliquidez de los planes de pensiones, pero la aseguradora garantiza una rentabilidad mínima por ley."),
        ("En el ámbito de los seguros, ¿qué diferencia al coaseguro del reaseguro?",
         ["En el coaseguro varios aseguradores comparten directamente el riesgo con el tomador, mientras que en el reaseguro el asegurador cede parte del riesgo a otra entidad sin intervención del tomador", "El coaseguro es obligatorio para particulares y el reaseguro solo para empresas cotizadas", "El reaseguro elimina el pago de primas por parte del asegurado original", "En el coaseguro el beneficiario asume los gastos de tramitación del siniestro"], 0,
         "En el coaseguro hay un único contrato firmado por varias aseguradoras y el tomador. En el reaseguro es un acuerdo interno B2B entre aseguradoras."),
        ("¿Cómo tributan las prestaciones en forma de capital de un seguro de vida cuando el tomador y el beneficiario son personas distintas?",
         ["Tributan en el Impuesto sobre Sucesiones y Donaciones (ISD)", "Tributan como rendimientos del trabajo en la base general del IRPF del beneficiario", "Tributan como rendimientos de capital mobiliario en la base del ahorro del IRPF", "Están completamente exentas de tributación por ley de seguros"], 0,
         "Si tomador (quien paga) y beneficiario son distintos, constituye una transmisión gratuita lucrativa inter vivos (donación) o mortis causa (sucesiones)."),
        ("En un seguro de rentas vitalicias, ¿qué factor influye principalmente en el cálculo de la renta mensual a percibir por el asegurado?",
         ["La edad del asegurado y la esperanza de vida en el momento de la contratación", "El tipo de interés oficial fijado por el Banco Central Europeo al final del año", "La evolución del índice bursátil de referencia de la aseguradora", "La cuantía de los gastos de administración cobrados por la CNMV"], 0,
         "La renta mensual depende del capital aportado, la rentabilidad técnica garantizada y la probabilidad de fallecimiento del asegurado según tablas biométricas.")
    ]),
    ("M5", 4, "Pensiones y Jubilación", [
        ("¿Cuál es el límite máximo general de aportación anual con derecho a reducción fiscal en planes de pensiones individuales?", 
         ["1.500 € al año", "8.000 € al año", "10.000 € al año", "2.000 € al año"], 0,
         "En España (salvo regímenes especiales), el límite general de aportación y reducción fiscal a planes de pensiones individuales es de 1.500 € anuales."),
        ("¿Bajo qué supuesto excepcional regulado por ley se puede rescatar un plan de pensiones por antigüedad de las aportaciones?",
         ["Aportaciones con una antigüedad mínima de 10 años", "Aportaciones de más de 5 años si el partícipe cambia de residencia fiscal", "Aportaciones con antigüedad de 15 años solo si el partícipe no tiene vivienda en propiedad", "No existe supuesto por antigüedad, solo se permite el rescate por jubilación"], 0,
         "La normativa del IRPF en España permite rescatar los derechos consolidados correspondientes a aportaciones con al menos 10 años de antigüedad."),
        ("En un plan de pensiones de prestación definida, ¿quién asume el riesgo actuarial y financiero de la jubilación?",
         ["El promotor del plan de pensiones (generalmente la empresa)", "El partícipe de forma exclusiva", "La sociedad gestora de fondos de pensiones", "El consorcio de compensación de seguros"], 0,
         "En los planes de prestación definida, el promotor se compromete a una cuantía de prestación fija, asumiendo cualquier déficit del fondo."),
        ("¿Cómo tributa el rescate en forma de capital de las aportaciones realizadas a un plan de pensiones con anterioridad al 31 de diciembre de 2006?",
         ["Se benefician de una reducción del 40% sobre el importe rescatado si se ejerce dentro del plazo legal", "Tributan exentas de IRPF al clasificarse como rentas no sujetas", "Tributan en la base del ahorro aplicando el tipo fijo del 19%", "Se reducen un 50% de la cuota tributaria si el partícipe está jubilado"], 0,
         "Los derechos consolidados anteriores a 2007 pueden acogerse a una reducción de integración del 40% si se rescatan en el año de jubilación o los dos siguientes.")
    ]),
    ("M6", 3, "Inversión Inmobiliaria", [
        ("¿Qué porcentaje mínimo de sus beneficios deben distribuir por ley las SOCIMIs en España?", 
         ["80% de los beneficios de arrendamiento", "50% de las ganancias de capital", "100% de la facturación bruta", "No tienen obligación de reparto"], 0,
         "Las SOCIMIs están obligadas a distribuir en forma de dividendos al menos el 80% de los beneficios derivados del arrendamiento de inmuebles."),
        ("En la valoración de bienes inmuebles, ¿en qué consiste el método de capitalización de rendimientos?",
         ["Estimar el valor de un inmueble en función de los flujos de caja futuros (alquileres) actualizados a una tasa de descuento", "Sumar el coste del suelo y el valor de reposición de la edificación", "Comparar los precios de compraventas recientes de inmuebles similares en la zona", "Aplicar el valor catastral multiplicado por el coeficiente del municipio"], 0,
         "Consiste en obtener el valor actual trayendo a presente las rentas netas que se estima que generará la explotación del inmueble."),
        ("En el análisis de inversiones inmobiliarias, ¿qué representa el Loan-to-Value (LTV)?",
         ["El porcentaje que representa el importe del préstamo hipotecario sobre el valor de tasación del inmueble", "La relación entre la cuota mensual de la hipoteca y los ingresos netos del comprador", "La rentabilidad bruta por alquiler dividida entre los costes de mantenimiento", "El tipo de interés real ponderado tras deducir los impuestos de transmisiones patrimoniales"], 0,
         "El LTV indica el nivel de apalancamiento. Un LTV superior al 80% suele implicar mayores costes de financiación por el riesgo asumido por el banco.")
    ]),
    ("M7", 3, "Crédito y Financiación", [
        ("¿Qué coste financiero se incluye obligatoriamente en el cálculo de la TAE de una hipoteca pero no en el TIN?", 
         ["Comisiones de apertura y gastos de tasación/seguros vinculados", "Los intereses ordinarios", "La amortización del capital", "La prima por pago anticipado"], 0,
         "La TAE (Tasa Anual Equivalente) refleja el coste efectivo total del préstamo, incluyendo comisiones obligatorias y seguros vinculados, a diferencia del TIN."),
        ("Si solicitamos un préstamo con sistema de amortización francés (cuota constante), ¿cómo evoluciona la proporción de intereses y capital dentro de la cuota?",
         ["Los intereses decrecen a lo largo del tiempo y el capital amortizado crece", "El capital amortizado decrece y los intereses crecen", "La proporción de intereses y capital se mantiene constante en todas las cuotas", "Los intereses se pagan íntegramente en la última cuota junto al vencimiento"], 0,
         "Al amortizarse capital mensualmente, la base sobre la que se calculan los intereses es menor en cada periodo, aumentando el capital amortizado neto en cada cuota."),
        ("Un préstamo hipotecario con interés variable referenciado al Euríbor a 12 meses tiene una cláusula suelo del 1.5%. Si el Euríbor cotiza al -0.5% y el diferencial es del 1.0%, ¿cuál será el tipo de interés aplicado al cliente?",
         ["1.50% debido a la cláusula suelo", "0.50% neto", "1.00% debido al Euríbor negativo", "2.00% sumando el valor absoluto del Euríbor"], 0,
         "La suma de Euríbor y diferencial es: -0.5% + 1.0% = 0.50%. Dado que el contrato tiene una cláusula suelo del 1.50%, el tipo aplicado es este límite mínimo.")
    ]),
    ("M8", 6, "Fiscalidad", [
        ("¿A partir de qué importe anual la tarifa del ahorro estatal del IRPF español aplica el tipo del 21%?", 
         ["6.000 €", "50.000 €", "200.000 €", "3.000 €"], 0,
         "La escala del ahorro aplica un 19% hasta 6.000 €, y un 21% a partir de ese límite hasta 50.000 €."),
        ("¿Qué límite existe en el IRPF para compensar saldos negativos de ganancias y pérdidas patrimoniales con el saldo de rendimientos del capital mobiliario en la base del ahorro?",
         ["Un máximo del 25% del saldo positivo de los rendimientos del capital mobiliario", "Un máximo del 10% sin posibilidad de trasladar el exceso a ejercicios futuros", "Se pueden compensar al 100% sin ningún límite cuantitativo", "No está permitida la compensación cruzada entre estos dos compartimentos"], 0,
         "La ley del IRPF permite la compensación cruzada en la base del ahorro con un límite del 25% del saldo positivo del compartimento opuesto."),
        ("¿Cuál es el tratamiento fiscal en el Impuesto sobre el Patrimonio de los planes de pensiones individuales en España?",
         ["Están totalmente exentos de declarar en el Impuesto sobre el Patrimonio", "Tributan por su valor de rescate consolidado al final del año fiscal", "Están exentos solo si el partícipe no supera los 65 años de edad", "Tributan en el impuesto al 50% de su valor neto patrimonial"], 0,
         "Los derechos consolidados en planes de pensiones son bienes inembargables y están exentos del Impuesto sobre el Patrimonio por carecer de liquidez inmediata."),
        ("Un inversor persona física vende acciones de una empresa española con ganancias patrimoniales. ¿Qué retención fiscal a cuenta del IRPF se le aplica en el momento de la venta?",
         ["0% (las ventas de acciones cotizadas no están sujetas a retención a cuenta)", "19% de retención directa aplicada por el bróker español", "21% de retención sobre el importe total de la transmisión", "Un tipo del 15% que luego se liquida en el impuesto de transmisiones patrimoniales"], 0,
         "Las ganancias patrimoniales por transmisión de acciones no sufren retención a cuenta (a diferencia de fondos de inversión), debiendo declararse en la renta anual."),
        ("En relación a la exención por reinversión en vivienda habitual en el IRPF, ¿de qué plazo dispone el contribuyente para reinvertir el importe obtenido por la venta de su vivienda habitual?",
         ["Un plazo máximo de 2 años, anteriores o posteriores a la fecha de la venta", "Un año a contar desde el devengo del impuesto", "Debe realizarse de forma inmediata y simultánea ante notario", "5 años siempre que se justifique ante la AEAT la adquisición del suelo"], 0,
         "La reinversión de la ganancia patrimonial para vivienda habitual debe producirse en un plazo no superior a dos años desde la enajenación."),
        ("¿Cómo tributan en el IRPF los dividendos distribuidos por una sociedad cotizada a una persona física residente en España?",
         ["Como rendimientos del capital mobiliario en la base del ahorro, sujetos a retención (generalmente del 19%)", "Como ganancias patrimoniales sujetas a una escala progresiva en la base general", "Están exentos los primeros 1.500 € y el resto tributa al tipo marginal del trabajo", "Tributan en la base general reduciéndose en la base imponible del ahorro"], 0,
         "Los dividendos son rendimientos de capital mobiliario que tributan en la base imponible del ahorro y sufren una retención en origen del 19%.")
    ]),
    ("M9", 5, "Legislación y Ética", [
        ("¿Qué directiva de la UE regula la transparencia, comercialización y clasificación de clientes financieros?", 
         ["MiFID II", "Basilea III", "Solvencia II", "MiCA"], 0,
         "MiFID II (Markets in Financial Instruments Directive II) es la directiva europea clave que regula la conducta, perfilado y clasificación de clientes."),
        ("Bajo la normativa MiFID II, ¿cuál es la diferencia clave entre el asesoramiento financiero independiente y el no independiente?",
         ["El asesor independiente no puede percibir retrocesiones o incentivos de terceros (inducements) y debe evaluar una gama amplia de productos del mercado", "El asesor independiente tiene prohibido cobrar honorarios al cliente final", "El asesor no independiente solo puede comercializar Letras del Tesoro público", "El asesor independiente está exento de realizar el test de idoneidad al cliente"], 0,
         "mifid ii es la directiva que prohíbe taxativamente retener incentivos (inducements) a asesores independientes, garantizando la transparencia ante el cliente."),
        ("¿Cuándo es obligatorio realizar el Test de Idoneidad según MiFID II?",
         ["Cuando se prestan los servicios de asesoramiento en materia de inversiones o gestión de carteras", "Siempre que el cliente compre cualquier tipo de activo, incluidos depósitos simples", "Únicamente cuando el cliente es clasificado como contraparte elegible", "Cuando el cliente solicita un préstamo hipotecario sin vinculaciones"], 0,
         "Bajo la directiva MiFID II, el test de idoneidad es obligatorio en asesoramiento y gestión discrecional de carteras del cliente. Evalúa sus conocimientos, situación financiera y objetivos de inversión."),
        ("Según el Código Ético de EFPA España, si existe un conflicto de interés insalvable entre el asesor y el cliente, ¿cómo debe proceder el asesor?",
         ["Debe anteponer siempre el interés del cliente y divulgar el conflicto con total transparencia", "Debe priorizar los objetivos comerciales de su entidad financiera", "Debe suspender la relación comercial sin dar explicaciones para proteger el secreto bancario", "Debe cobrar una tarifa doble para compensar el riesgo operativo"], 0,
         "El Código Ético exige actuar con objetividad y transparencia. Si el conflicto no es evitable, se debe informar por escrito y dar prioridad al cliente."),
        ("Bajo la directiva MiFID II, ¿qué cliente goza del menor nivel de protección regulatorio?",
         ["Contraparte elegible", "Cliente profesional por solicitud", "Cliente minorista", "Pyme sin departamento financiero"], 0,
         "Bajo la directiva MiFID II, las contrapartes elegibles se definen como un tipo de cliente institucional con conocimientos máximos, teniendo el nivel de protección más bajo de la clasificación de clientes.")
    ]),
    ("M10", 5, "Asesoramiento y Planificación", [
        ("¿Cuál es el primer paso en el proceso de planificación financiera personal del cliente?", 
         ["Establecer y definir la relación cliente-planificador", "Recopilar datos del cliente y definir objetivos", "Analizar el estado financiero del cliente", "Presentar las propuestas de inversión"], 0,
         "El estándar internacional de planificación financiera establece que la definición y acuerdo de la relación entre el cliente y el planificador es el primer paso indispensable."),
        ("En la planificación financiera basada en el ciclo de vida, ¿cuál es la recomendación típica de asignación de activos para un inversor en su fase de acumulación temprana (juventud)?",
         ["Mayor exposición a activos de renta variable para maximizar el crecimiento a largo plazo", "Mantener el 100% de la cartera en depósitos y pagarés a corto plazo", "Invertir exclusivamente en bonos soberanos con vencimiento superior a 30 años", "Una distribución del 50% en renta fija corporativa de alta calificación y 50% en oro"], 0,
         "Al tener un horizonte temporal a muy largo plazo, los inversores jóvenes toleran mayor volatilidad en busca de primas de riesgo de renta variable."),
        ("En el balance de situación familiar, ¿cómo se clasifica una vivienda habitual que tiene un préstamo hipotecario asociado?",
         ["La vivienda es un activo no financiero por su valor de mercado y la hipoteca pendiente es un pasivo a largo plazo", "La vivienda y la hipoteca se compensan mostrándose únicamente como patrimonio neto consolidado", "La vivienda se considera un gasto corriente mensual y la hipoteca un pasivo contingente", "No se incluyen en el balance familiar por ser bienes de uso personal e indispensables"], 0,
         "El balance familiar sigue criterios contables estándar: el activo registra el bien real por su valor actual y el pasivo las obligaciones pendientes."),
        ("Para evaluar la capacidad de endeudamiento de un cliente, ¿qué ratio de cobertura de deuda (cuota mensual de préstamos / ingresos netos mensuales) se considera el límite máximo aconsejable de salud financiera?",
         ["35% a 40% de los ingresos netos del cliente", "15% como máximo absoluto", "60% a 70% siempre que disponga de avalistas familiares", "No existe límite si el tipo de interés del préstamo es variable"], 0,
         "El Banco de España y estándares financieros estiman un ratio del 35% de esfuerzo como límite saludable de endeudamiento familiar."),
        ("En la planificación financiera personal, ¿cuál es la finalidad del 'fondo de emergencia'?",
         ["Cubrir de 3 a 6 meses de gastos corrientes del cliente ante imprevistos como desempleo o enfermedad", "Invertir en activos de alto riesgo para generar plusvalías rápidas en momentos de crisis", "Pagar las comisiones anuales de gestión del planificador financiero", "Aportar capital a planes de pensiones de empleo para reducir la cuota fiscal"], 0,
         "El fondo de emergencia garantiza la liquidez inmediata necesaria para evitar tener que liquidar inversiones a largo plazo en momentos desfavorables.")
    ])
]

qid_counter = 1

for mod_code, cantidad, mod_name, preguntas_base in definiciones_modulos:
    for enunciado, opciones, correcta, explicacion in preguntas_base:
        PREGUNTAS_TEST.append(
            PreguntaTest(
                id=qid_counter,
                modulo=mod_code,
                enunciado=enunciado,
                opciones=opciones,
                respuesta_correcta=correcta,
                explicacion=explicacion
            )
        )
        qid_counter += 1


def obtener_preguntas_test():
    return PREGUNTAS_TEST

def obtener_preguntas_practicas():
    return PREGUNTAS_PRACTICAS


def generar_examen(tipo_examen: str) -> dict:
    """
    Compone un examen simulado según la estructura del plan EFA:
    - EIP: 40 test.
    - EFA Nivel II: 40 test + 1 caso práctico.
    - EFA Completo: 50 test + 1 caso práctico.
    Respeta las ponderaciones de los 10 módulos oficiales en las preguntas tipo test.
    """
    n_test = 40
    incluye_practica = False
    
    if tipo_examen == "EFA Completo":
        n_test = 50
        incluye_practica = True
    elif tipo_examen == "EFA Nivel II":
        n_test = 40
        incluye_practica = True
    elif tipo_examen == "EIP":
        n_test = 40
        incluye_practica = False
    else:
        raise ValueError("Tipo de examen no reconocido")
        
    # Ponderaciones de test por módulo (para 40 o 50 preguntas)
    # Hacemos una asignación exacta que sume n_test
    # Para 50 preguntas: M1=13, M2=5, M3=9, M4=4, M5=3, M6=2, M7=2, M8=5, M9=4, M10=3 -> Suma = 50
    # Para 40 preguntas: M1=10, M2=4, M3=7, M4=3, M5=2, M6=2, M7=2, M8=4, M9=3, M10=3 -> Suma = 40
    distribucion = {}
    if n_test == 50:
        distribucion = {"M1": 13, "M2": 5, "M3": 9, "M4": 4, "M5": 3, "M6": 2, "M7": 2, "M8": 5, "M9": 4, "M10": 3}
    else:
        distribucion = {"M1": 10, "M2": 4, "M3": 7, "M4": 3, "M5": 2, "M6": 2, "M7": 2, "M8": 4, "M9": 3, "M10": 3}
        
    test_seleccionadas = []
    for mod_code, cant in distribucion.items():
        pool = [q for q in PREGUNTAS_TEST if q.modulo == mod_code]
        seleccion = random.sample(pool, min(len(pool), cant))
        test_seleccionadas.extend(seleccion)
        
    # Barajamos las de test
    random.shuffle(test_seleccionadas)
    
    # Seleccionamos práctica si corresponde
    practica_seleccionada = None
    if incluye_practica:
        practica_seleccionada = random.choice(PREGUNTAS_PRACTICAS)
        
    # Retornamos el examen estructurado
    # Para enviar al alumno, eliminamos la respuesta_correcta de las preguntas de test
    preguntas_test_alumno = []
    for q in test_seleccionadas:
        preguntas_test_alumno.append({
            "id": q.id,
            "modulo": q.modulo,
            "tipo": q.tipo,
            "enunciado": q.enunciado,
            "opciones": q.opciones
        })
        
    res = {
        "tipo_examen": tipo_examen,
        "n_preguntas_test": len(test_seleccionadas),
        "preguntas_test": preguntas_test_alumno,
        "incluye_practica": incluye_practica,
        "pregunta_practica": {
            "id": practica_seleccionada.id,
            "modulo": practica_seleccionada.modulo,
            "tipo": practica_seleccionada.tipo,
            "enunciado": practica_seleccionada.enunciado
        } if practica_seleccionada else None,
        # Guardamos los IDs originales de test en orden para poder calificar luego
        "ids_originales_test": [q.id for q in test_seleccionadas],
        "id_practica_original": practica_seleccionada.id if practica_seleccionada else None
    }
    return res


APUNTES_TEORICOS = {
    "M1": (
        "### M1: Instrumentos y Mercados Financieros\n\n"
        "1. **Renta Fija y Curva de Tipos**:\n"
        "   - El precio de un bono y su TIR tienen una relación inversa:\n"
        "     $$P = \\sum_{t=1}^{n} \\frac{C}{(1+y)^t} + \\frac{N}{(1+y)^n}$$\n"
        "   - **Duración de Macaulay**: Representa el promedio ponderado del tiempo hasta el cobro de flujos. Mide la sensibilidad del bono ante variaciones en los tipos.\n"
        "2. **Políticas Monetarias**: Las decisiones de los bancos centrales sobre tipos de interés (por ejemplo, el BCE) impactan directamente en la valoración de renta fija y variable.\n"
        "3. **Criterios ESG**: Integración de factores Ambientales (E), Sociales (S) y de Gobernanza (G) en el análisis y toma de decisiones de inversión."
    ),
    "M2": (
        "### M2: Fondos y Sociedades de Inversión\n\n"
        "1. **Tipos de Fondos**:\n"
        "   - **Fondos Armonizados (UCITS)**: Cumplen directivas comunitarias, lo que les permite pasaporte europeo y comercialización minorista con estrictos límites de diversificación.\n"
        "   - **Fondos de Inversión Libre (Hedge Funds)**: No armonizados, con amplia libertad de apalancamiento, uso de derivados y posiciones cortas.\n"
        "2. **Gestión Activa vs Pasiva**:\n"
        "   - La gestión activa busca batir a un índice (generar alfa) seleccionando valores individuales.\n"
        "   - La gestión pasiva replica un índice de referencia con menores costes de gestión (por ejemplo, a través de fondos indexados o ETFs)."
    ),
    "M3": (
        "### M3: Gestión de Carteras\n\n"
        "1. **Teoría Moderna de Markowitz**:\n"
        "   - **Frontera Eficiente**: Conjunto de carteras óptimas que maximizan el rendimiento esperado para cada nivel de volatilidad.\n"
        "   - La diversificación reduce el **riesgo específico o diversificable** pero no elimina el **riesgo sistemático o de mercado**.\n"
        "2. **Modelo CAPM**:\n"
        "   - Establece la rentabilidad esperada en función del riesgo sistemático (Beta):\n"
        "     $$E(R_i) = R_f + \\beta_i(E(R_m) - R_f)$$\n"
        "3. **Ratios de Evaluación**:\n"
        "   - **Ratio de Sharpe**: Evalúa rentabilidad por unidad de riesgo total:\n"
        "     $$Sharpe = \\frac{R_p - R_f}{\\sigma_p}$$\n"
        "   - **Ratio de Treynor**: Evalúa rentabilidad por unidad de riesgo sistemático:\n"
        "     $$Treynor = \\frac{R_p - R_f}{\\beta_p}$$\n"
        "   - **Alfa de Jensen**: Medida de exceso de rentabilidad ajustada por riesgo:\n"
        "     $$\\alpha_p = R_p - [R_f + \\beta_p(R_m - R_f)]$$"
    ),
    "M4": (
        "### M4: Seguros\n\n"
        "1. **Elementos del Seguro**: Tomador (paga la prima), Asegurado (persona expuesta al riesgo) y Beneficiario (recibe la indemnización).\n"
        "2. **Seguros Unit-Linked**: Seguros de vida donde el tomador asume el riesgo de la inversión, ya que las primas se destinan a cestas de fondos elegidas por él.\n"
        "3. **Fiscalidad**: Las prestaciones de seguros de vida tributan generalmente como rendimientos de capital mobiliario en el IRPF (si tomador = beneficiario) o en el Impuesto de Sucesiones y Donaciones (si tomador != beneficiario)."
    ),
    "M5": (
        "### M5: Pensiones y Jubilación\n\n"
        "1. **Planes de Pensiones**: IIC de carácter previsional y aportaciones ilíquidas hasta la jubilación o supuestos excepcionales (desempleo de larga duración, enfermedad grave o antigüedad > 10 años).\n"
        "2. **Reducción en IRPF**: Las aportaciones reducen directamente la base imponible general, con un límite máximo anual conjunto de 1.500 € en planes individuales en España.\n"
        "3. **Rescate**: Las prestaciones recibidas del plan de pensiones (sea en forma de capital, renta o mixto) tributan íntegramente como **rendimientos del trabajo** en la base general del IRPF."
    ),
    "M6": (
        "### M6: Inversión Inmobiliaria\n\n"
        "1. **Activos Inmobiliarios**: Inversión directa (compra de inmuebles) o indirecta (IIC inmobiliarias, SOCIMIs).\n"
        "2. **SOCIMIs (Sociedades Anónimas Cotizadas de Inversión en el Mercado Inmobiliario)**:\n"
        "   - Gozan de un tipo de gravamen del 0% en el Impuesto sobre Sociedades.\n"
        "   - Tienen la obligatoriedad legal de distribuir como dividendos al menos el 80% de los beneficios obtenidos del arrendamiento inmobiliario."
    ),
    "M7": (
        "### M7: Crédito y Financiación\n\n"
        "1. **TIN vs TAE**:\n"
        "   - **TIN (Tipo de Interés Nominal)**: Tipo de interés simple contratado que no tiene en cuenta comisiones ni la frecuencia de liquidación.\n"
        "   - **TAE (Tasa Anual Equivalente)**: Tipo de interés efectivo anual compuesto que incluye gastos, comisiones de apertura y frecuencia de liquidación periódica:\n"
        "     $$TAE = \\left(1 + \\frac{TIN}{m}\\right)^m - 1$$\n"
        "2. **Préstamos Hipotecarios**: Sistemas de amortización (método francés de cuota constante con mayor pago de intereses al principio)."
    ),
    "M8": (
        "### M8: Fiscalidad de las Inversiones\n\n"
        "1. **Base del Ahorro en el IRPF**: Integrada por rendimientos del capital mobiliario (dividendos, cupones) y ganancias y pérdidas patrimoniales (ventas de acciones, fondos).\n"
        "2. **Escala del Ahorro España 2026**:\n"
        "   - Hasta 6.000 €: 19%\n"
        "   - De 6.000 € a 50.000 €: 21%\n"
        "   - De 50.000 € a 200.000 €: 23%\n"
        "   - De 200.000 € a 300.000 €: 27%\n"
        "   - Más de 300.000 €: 28%\n"
        "3. **Exención por Reinversión**: Traspasos exentos de tributación en fondos de inversión para personas físicas residentes en España."
    ),
    "M9": (
        "### M9: Legislación, Normativa y Ética\n\n"
        "1. **Directiva MiFID II**:\n"
        "   - Clasifica a los clientes en Minoristas (mayor protección) y Profesionales (mayor conocimiento).\n"
        "   - **Test de Idoneidad**: Obligatorio en asesoramiento financiero o gestión de carteras (evalúa conocimientos, objetivos y situación financiera).\n"
        "   - **Test de Conveniencia**: Obligatorio en la mera ejecución (sólo evalúa conocimientos y experiencia).\n"
        "2. **Código Ético EFPA**: Obligación de primar el interés del cliente, actuar con integridad, profesionalidad, objetividad y confidencialidad."
    ),
    "M10": (
        "### M10: Asesoramiento y Planificación\n\n"
        "1. **Etapas de la Planificación Financiera**:\n"
        "   1. Establecer la relación comercial.\n"
        "   2. Recopilar datos y fijar objetivos.\n"
        "   3. Analizar estados financieros personales (balance familiar).\n"
        "   4. Desarrollar y presentar recomendaciones.\n"
        "   5. Implementar el plan.\n"
        "   6. Monitoreo y revisión periódica.\n"
        "2. **Planificación de Jubilación y Ciclo de Vida**: Adaptar el perfil de riesgo (más agresivo en juventud, conservador al acercarse al retiro)."
    )
}

def obtener_todos_apuntes() -> dict[str, str]:
    return APUNTES_TEORICOS

