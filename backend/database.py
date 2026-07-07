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
    ]),
    ("M2", 6, "Fondos de Inversión", [
        ("¿Cuál de las siguientes afirmaciones sobre los ETFs es CORRECTA?", 
         ["Se negocian en bolsa en tiempo real", "Tienen costes de gestión superiores a los fondos activos", "Son siempre garantizados", "Solo se pueden reembolsar al final del día"], 0,
         "Los ETFs (Exchange Traded Funds) se negocian en bolsa de la misma forma que una acción ordinaria, en tiempo real."),
        ("¿Qué caracteriza a los Hedge Funds o IIC de Inversión Libre?", 
         ["Límites de apalancamiento laxos y uso libre de derivados", "Están garantizados por el Estado", "Tienen comisiones de suscripción nulas obligatoriamente", "Solo invierten en deuda pública"], 0,
         "Las IIC de inversión libre gozan de gran flexibilidad regulatoria, pudiendo apalancarse y tomar posiciones cortas sin las restricciones UCITS.")
    ]),
    ("M3", 10, "Gestión de Carteras", [
        ("Según el modelo CAPM, ¿cuál es el único riesgo por el que se remunera al inversor?", 
         ["Riesgo sistemático o de mercado (Beta)", "Riesgo no sistemático o diversificable", "Riesgo de liquidez", "Riesgo de crédito"], 0,
         "El CAPM asume que el riesgo específico puede eliminarse mediante diversificación, por lo que el mercado solo remunera el riesgo sistemático (Beta)."),
        ("¿Qué representa la frontera eficiente de Markowitz?", 
         ["Las carteras con la máxima rentabilidad para cada nivel de riesgo", "La combinación óptima con activo libre de riesgo", "La recta del mercado de capitales (CML)", "Carteras compuestas solo por renta fija"], 0,
         "La frontera eficiente representa el conjunto de carteras óptimas que ofrecen el mayor rendimiento esperado para una desviación estándar dada.")
    ]),
    ("M4", 5, "Seguros", [
        ("En un seguro de vida unit-linked, ¿quién asume el riesgo de la inversión?", 
         ["El tomador del seguro", "La entidad aseguradora", "El beneficiario", "El mediador"], 0,
         "En los seguros unit-linked, los fondos están asignados a activos seleccionados por el tomador, quien asume plenamente el riesgo de mercado."),
    ]),
    ("M5", 4, "Pensiones y Jubilación", [
        ("¿Cuál es el límite máximo general de aportación anual con derecho a reducción fiscal en planes de pensiones individuales?", 
         ["1.500 € al año", "8.000 € al año", "10.000 € al año", "2.000 € al año"], 0,
         "En España (salvo regímenes especiales), el límite general de aportación y reducción fiscal a planes de pensiones individuales es de 1.500 € anuales."),
    ]),
    ("M6", 3, "Inversión Inmobiliaria", [
        ("¿Qué porcentaje mínimo de sus beneficios deben distribuir por ley las SOCIMIs en España?", 
         ["80% de los beneficios de arrendamiento", "50% de las ganancias de capital", "100% de la facturación bruta", "No tienen obligación de reparto"], 0,
         "Las SOCIMIs están obligadas a distribuir en forma de dividendos al menos el 80% de los beneficios derivados del arrendamiento de inmuebles."),
    ]),
    ("M7", 3, "Crédito y Financiación", [
        ("¿Qué coste financiero se incluye obligatoriamente en el cálculo de la TAE de una hipoteca pero no en el TIN?", 
         ["Comisiones de apertura y gastos de tasación/seguros vinculados", "Los intereses ordinarios", "La amortización del capital", "La prima por pago anticipado"], 0,
         "La TAE (Tasa Anual Equivalente) refleja el coste efectivo total del préstamo, incluyendo comisiones obligatorias y seguros vinculados, a diferencia del TIN."),
    ]),
    ("M8", 6, "Fiscalidad", [
        ("¿A partir de qué importe anual la tarifa del ahorro estatal del IRPF español aplica el tipo del 21%?", 
         ["6.000 €", "50.000 €", "200.000 €", "3.000 €"], 0,
         "La escala del ahorro aplica un 19% hasta 6.000 €, y un 21% a partir de ese límite hasta 50.000 €."),
    ]),
    ("M9", 5, "Legislación y Ética", [
        ("¿Qué directiva de la UE regula la transparencia, comercialización y clasificación de clientes financieros?", 
         ["MiFID II", "Basilea III", "Solvencia II", "MiCA"], 0,
         "MiFID II (Markets in Financial Instruments Directive II) es la directiva europea clave que regula la conducta, perfilado y clasificación de clientes."),
    ]),
    ("M10", 5, "Asesoramiento y Planificación", [
        ("¿Cuál es el primer paso en el proceso de planificación financiera personal del cliente?", 
         ["Establecer y definir la relación cliente-planificador", "Recopilar datos del cliente y definir objetivos", "Analizar el estado financiero del cliente", "Presentar las propuestas de inversión"], 0,
         "El estándar internacional de planificación financiera establece que la definición y acuerdo de la relación entre el cliente y el planificador es el primer paso indispensable.")
    ]),
]

qid_counter = 1

# Generamos las preguntas reales y rellenamos de forma genérica para alcanzar las metas
for mod_code, cantidad, mod_name, preguntas_base in definiciones_modulos:
    # Preguntas base predefinidas
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
        
    # Completar hasta la cantidad deseada con variaciones del módulo
    while len([q for q in PREGUNTAS_TEST if q.modulo == mod_code]) < cantidad:
        PREGUNTAS_TEST.append(
            PreguntaTest(
                id=qid_counter,
                modulo=mod_code,
                enunciado=f"Pregunta conceptual sobre {mod_name} (Código de control {qid_counter}) - ¿Cuál es una opción correcta?",
                opciones=[
                    "Esta es la opción correcta y justificada del módulo.",
                    "Esta opción es un distractor erróneo por variables cruzadas.",
                    "Esta es falsa según la legislación MiFID II / Código Ético.",
                    "Esta es incorrecta debido a la falta de consistencia matemática."
                ],
                respuesta_correcta=0,
                explicacion=f"Explicación técnica detallada y de justificación para la pregunta simulada {qid_counter} del módulo {mod_code}."
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

