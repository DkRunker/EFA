# Módulo M6 — Inversión Inmobiliaria
# PREGUNTAS: cada tupla es (enunciado, [4 opciones], indice_respuesta_correcta, explicacion)
# Ampliar apuntes y preguntas conforme al temario oficial EFPA. NO borrar términos ya existentes.
NOMBRE = 'Inversión Inmobiliaria'

PREGUNTAS = [
    (
        '¿Qué porcentaje mínimo de sus beneficios deben distribuir por ley las SOCIMIs en España?',
        ['80% de los beneficios de arrendamiento', '50% de las ganancias de capital', '100% de la facturación bruta', 'No tienen obligación de reparto'],
        0,
        'Las SOCIMIs están obligadas a distribuir en forma de dividendos al menos el 80% de los beneficios derivados del arrendamiento de inmuebles.',
    ),
    (
        'En la valoración de bienes inmuebles, ¿en qué consiste el método de capitalización de rendimientos?',
        ['Estimar el valor de un inmueble en función de los flujos de caja futuros (alquileres) actualizados a una tasa de descuento', 'Sumar el coste del suelo y el valor de reposición de la edificación', 'Comparar los precios de compraventas recientes de inmuebles similares en la zona', 'Aplicar el valor catastral multiplicado por el coeficiente del municipio'],
        0,
        'Consiste en obtener el valor actual trayendo a presente las rentas netas que se estima que generará la explotación del inmueble.',
    ),
    (
        'En el análisis de inversiones inmobiliarias, ¿qué representa el Loan-to-Value (LTV)?',
        ['El porcentaje que representa el importe del préstamo hipotecario sobre el valor de tasación del inmueble', 'La relación entre la cuota mensual de la hipoteca y los ingresos netos del comprador', 'La rentabilidad bruta por alquiler dividida entre los costes de mantenimiento', 'El tipo de interés real ponderado tras deducir los impuestos de transmisiones patrimoniales'],
        0,
        'El LTV indica el nivel de apalancamiento. Un LTV superior al 80% suele implicar mayores costes de financiación por el riesgo asumido por el banco.',
    ),
    (
        '¿Qué porcentaje mínimo de sus activos deben tener invertidos los Fondos de Inversión Inmobiliaria (FII) en España en inmuebles urbanos destinados al arrendamiento?',
        ['El 70% del promedio anual de saldos mensuales de su activo', 'El 50% de su activo neto acumulado', 'El 100% excluyendo tesorería ordinaria', 'No tienen mínimo legal de inversión en activos físicos'],
        0,
        'Conforme al RD 1082/2012, las IIC inmobiliarias (FII) deben mantener invertido al menos el 70% del promedio anual de saldos mensuales de su activo en inmuebles urbanos destinados al arrendamiento. No debe confundirse con el 80% de reparto de dividendos de las SOCIMI.',
    ),
    (
        '¿Cuál es el tipo de gravamen general aplicable en el Impuesto sobre Sociedades a las Sociedades de Inversión Inmobiliaria (SII) de carácter general que cotizan como SOCIMIs?',
        ['El 0% para las SOCIMIs y el 1% para las SII que cumplen requisitos de viviendas en alquiler', 'El 25% general como cualquier otra sociedad mercantil española', 'El 15% aplicable a empresas de nueva creación en el mercado inmobiliario', 'El 10% fijo sin derecho a deducciones por doble imposición internacional'],
        0,
        'Las SOCIMIs disfrutan de un tipo de gravamen del 0% en el IS. Las SII no cotizadas pueden acogerse al tipo del 1% bajo ciertas condiciones de vivienda en alquiler.',
    ),
    (
        'Al calcular la rentabilidad neta por alquiler de un inmueble, ¿cuál de los siguientes gastos es deducible para obtener el Ingreso Operativo Neto (NOI)?',
        ['Los gastos de comunidad, seguro de impago, reparaciones del inmueble e IBI', 'La cuota total mensual del préstamo hipotecario (capital e interés)', 'El coste de adquisición de la vivienda original amortizado al 50% anual', 'Los gastos de tasación notarial de la venta de fincas colindantes'],
        0,
        'El NOI descuenta del ingreso bruto los gastos de explotación ordinaria (comunidad, seguros, IBI, mantenimiento), pero no la amortización de deuda financiera.',
    ),
    (
        'En una tasación inmobiliaria oficial, ¿cuándo se debe utilizar obligatoriamente el método de coste de reposición?',
        ['Cuando no se disponga de transacciones de mercado comparables o se valore una edificación especial/obra nueva sin mercado activo', 'Únicamente en valoraciones agrícolas y de suelo no urbanizable protegido', 'Cuando el valor catastral del municipio sea superior a 1 millón de euros', 'Siempre que el inmueble tenga un préstamo de amortización de sistema americano'],
        0,
        'El coste de reposición calcula el coste de construir de nuevo el inmueble. Es el método por defecto ante falta de comparables o en obras inacabadas.',
    ),
    (
        '¿Qué caracteriza a la inversión inmobiliaria indirecta frente a la inversión directa?',
        ['Mayor liquidez de las participaciones, menores costes de transacción iniciales y diversificación inmediata de activos', 'Mayor control físico de las reformas y negociación directa del alquiler con el arrendatario', 'Obligatoriedad de pago del Impuesto sobre Transmisiones Patrimoniales (ITP) en cada suscripción', 'Exención total del Impuesto sobre el Patrimonio sobre el 100% de la inversión'],
        0,
        'La inversión inmobiliaria indirecta (ej. SOCIMIs, FII) permite invertir con poco capital, con comisiones muy bajas y con alta liquidez comparada con un piso físico.',
    ),
    (
        'En la tasación hipotecaria de un solar urbanizable sin edificar, ¿qué método de valoración se utiliza preferentemente?',
        ['El método del valor residual (estático o dinámico)', 'El método de coste de reposición histórico amortizado', 'El método de capitalización de rentas históricas agrarias', 'El método de comparación directa con fincas rústicas de secano'],
        0,
        'El método residual deduce el valor del suelo a partir del valor estimado de la promoción inmobiliaria terminada, descontando todos los costes de construcción y beneficio del promotor.',
    ),
    (
        'En el contexto de la inversión en SOCIMIs, ¿qué ventaja fiscal tienen los dividendos distribuidos por estas sociedades a personas jurídicas con participación significativa (ej. > 5%)?',
        ['Sufren un gravamen especial del 19% en la sociedad que distribuye si tributan a un tipo inferior al 10% en sede del perceptor', 'Están exentos al 100% del Impuesto sobre Sociedades por el régimen de transparencia directa', 'No sufren retención y reducen la base imponible del Impuesto sobre el Patrimonio corporativo', 'Se consideran plusvalías de capital exentas si la SOCIMI cotiza en bolsa internacional'],
        0,
        'Conforme al art. 9.2 de la Ley 11/2009, se aplica un gravamen especial del 19% sobre los dividendos distribuidos a socios cuya participación sea >= 5% cuando dichos dividendos estén exentos o gravados a menos del 10% en el receptor, para evitar el arbitraje fiscal. (No debe confundirse con el gravamen del 15% de la Ley 11/2021, que recae sobre los beneficios NO distribuidos.)',
    ),
    (
        '¿Cuál es el cálculo de la rentabilidad por dividendo (Dividend Yield) de una SOCIMI?',
        ['Dividendo por acción distribuido anualmente dividido por el precio de cotización de la acción', 'Renta bruta anual de los alquileres dividida por el valor de adquisición de los inmuebles', 'Beneficio neto operativo total dividido por el número de participaciones de los socios fundadores', 'La plusvalía generada por ventas de fincas dividida por los gastos de gestión acumulados'],
        0,
        'El Dividend Yield mide el retorno por dividendo percibido en efectivo en relación con el precio pagado por la acción cotizada en el mercado.',
    ),
    (
        '¿Qué diferencia un fondo de inversión inmobiliaria (FII) de una sociedad de inversión inmobiliaria (SII) en España?',
        ['Los FII son patrimonios sin personalidad jurídica constituidos por aportaciones de partícipes, mientras que las SII son sociedades anónimas con personalidad jurídica propia', 'Los FII solo invierten en locales comerciales y las SII exclusivamente en viviendas de protección oficial', 'Los FII tributan al 25% en el Impuesto sobre Sociedades y las SII tributan al 0%', 'Los FII exigen una aportación inicial mínima de 1 millón de euros por partícipe minorista'],
        0,
        'Esta es la distinción contable y legal básica en la regulación de IIC inmobiliarias de carácter no cotizado en España.',
    ),
    (
        "Al evaluar un proyecto de desarrollo inmobiliario, ¿qué es la 'Tasa de Capitalización' (Cap Rate) de salida?",
        ['La rentabilidad por alquiler anual estimada que exigirá un comprador para adquirir el inmueble una vez finalizado el proyecto', 'El tipo de interés máximo que cobrará el banco financiador de la promoción hipotecaria', 'El coste total de los impuestos municipales asociados a la licencia de obras y derribo', 'La tasa de descuento requerida para que el valor actual neto del proyecto sea exactamente igual a cero'],
        0,
        'El Cap Rate de salida refleja el rendimiento anual neto que exigirá el mercado inmobiliario a la compra del activo estabilizado al final del horizonte temporal.',
    ),
    (
        'En la compraventa de un inmueble en España, ¿qué impuesto grava la adquisición según se trate de vivienda nueva (primera transmisión del promotor) o de segunda mano?',
        ['La vivienda de obra nueva tributa por IVA (10%) más AJD, mientras que la vivienda usada tributa por ITP (tipo variable por CCAA)', 'Ambas tributan siempre por IVA al 21% con independencia de quién sea el vendedor', 'La vivienda nueva queda exenta de todo impuesto indirecto y la usada tributa por IBI', 'La vivienda usada tributa por IVA y la nueva por el Impuesto sobre el Patrimonio'],
        0,
        'La entrega de vivienda nueva por el promotor es una operación sujeta a IVA (10% en vivienda) y a Actos Jurídicos Documentados; la segunda y ulteriores transmisiones tributan por Transmisiones Patrimoniales Onerosas (ITP), cuyo tipo fija cada Comunidad Autónoma.',
    ),
    (
        'Un contribuyente arrienda una vivienda como residencia habitual del inquilino. En el IRPF, ¿qué tratamiento reciben los rendimientos netos positivos del capital inmobiliario obtenidos?',
        ['Se les aplica una reducción del 60% sobre el rendimiento neto positivo del arrendamiento de vivienda', 'Están totalmente exentos de tributación en el IRPF', 'Tributan como rendimientos del trabajo en la base general sin reducción', 'Se integran en la base del ahorro con una reducción fija del 40%'],
        0,
        'El arrendamiento de bienes inmuebles destinados a vivienda genera rendimientos del capital inmobiliario que se integran en la base general; sobre el rendimiento neto positivo se aplica una reducción (con carácter general del 60%) que incentiva el alquiler residencial.',
    ),
    (
        'En un préstamo hipotecario con sistema de amortización francés a tipo fijo, ¿qué característica define su cuadro de amortización?',
        ['La cuota total periódica (interés más capital) es constante; al inicio se paga más interés y menos capital, y esa proporción se invierte con el tiempo', 'La cuota de amortización de capital es constante y la cuota total disminuye periodo a periodo', 'Solo se pagan intereses durante toda la vida del préstamo y el capital se devuelve íntegro al vencimiento', 'La cuota crece de forma progresiva cada año en función de la inflación registrada'],
        0,
        'El sistema francés se caracteriza por términos amortizativos (cuotas) constantes. En el sistema lineal, por el contrario, es la amortización de capital la que se mantiene constante y la cuota total decrece.',
    ),
    (
        'En el análisis de una inversión inmobiliaria financiada con hipoteca, ¿qué mide la rentabilidad cash-on-cash?',
        ['El flujo de caja anual antes de impuestos dividido entre el capital propio (equity) efectivamente aportado por el inversor', 'El valor de tasación del inmueble dividido entre la renta bruta anual', 'El beneficio total de la venta futura dividido entre la plusvalía municipal pagada', 'La renta bruta anual dividida entre el importe total del préstamo hipotecario'],
        0,
        'La rentabilidad cash-on-cash relaciona el flujo de caja anual generado con el dinero propio realmente desembolsado (excluyendo la parte financiada), por lo que refleja el efecto del apalancamiento sobre el retorno del inversor.',
    ),
    (
        'En relación con el impacto ESG en el mercado inmobiliario, ¿qué son certificaciones como LEED, BREEAM o WELL?',
        ['Estándares de certificación de sostenibilidad y eficiencia de los edificios que pueden mejorar la valoración y reducir el riesgo de los activos', 'Índices bursátiles que replican la evolución de las SOCIMIs cotizadas europeas', 'Tipos de contrato de arrendamiento con renta indexada obligatoria al IPC', 'Sistemas de amortización hipotecaria alternativos al francés y al lineal'],
        0,
        'LEED, BREEAM y WELL son certificaciones que evalúan la sostenibilidad ambiental, la eficiencia energética y el bienestar de los ocupantes de un edificio; los activos certificados tienden a revalorizarse y a reducir riesgos, y se vinculan con la financiación verde (bonos verdes e hipotecas verdes).',
    ),
    (
        'Un local comercial genera un ingreso operativo neto (NOI) de 20.000 € anuales. Si el mercado exige una tasa de capitalización (cap rate) del 5%, ¿cuál es su valor estimado por el método de capitalización de rentas?',
        ['200.000 €', '300.000 €', '400.000 €', '1.000.000 €'],
        2,
        'Valor = Renta Neta Anual / Cap Rate = 20.000 / 0,05 = 400.000 €. Una menor tasa de capitalización daría un valor mayor.',
    ),
    (
        'Se concede un préstamo hipotecario de 180.000 € sobre una vivienda tasada en 240.000 €. ¿Cuál es el Loan-to-Value (LTV) de la operación?',
        ['60%', '75%', '80%', '133%'],
        1,
        'LTV = importe del préstamo / valor de tasación = 180.000 / 240.000 = 0,75, es decir, un 75%.',
    ),
    (
        'Una vivienda se adquiere por 240.000 € y se alquila por 1.000 € al mes. ¿Cuál es su rentabilidad bruta por alquiler?',
        ['2,4%', '4%', '4,8%', '5%'],
        3,
        'Rentabilidad bruta = renta anual bruta / precio de compra = (1.000 × 12) / 240.000 = 12.000 / 240.000 = 5%.',
    ),
    (
        'Un inversor aporta 80.000 € de capital propio (equity) y el inmueble genera un flujo de caja anual antes de impuestos de 4.000 €. ¿Cuál es la rentabilidad cash-on-cash?',
        ['5%', '8%', '20%', '2%'],
        0,
        'Cash-on-cash = flujo de caja anual antes de impuestos / capital propio aportado = 4.000 / 80.000 = 5%. Solo se considera el equity, no la parte financiada.',
    ),
    (
        'Un inmueble con valor de adquisición de 220.000 € se vende con un valor de transmisión de 290.000 €. ¿Cuál es la ganancia patrimonial y cómo tributa en el IRPF?',
        ['Una pérdida de 70.000 € que se integra en la base general', 'Una ganancia de 290.000 € que tributa como rendimiento del trabajo', 'Una ganancia de 70.000 € que tributa en la base del ahorro por tramos progresivos', 'Una ganancia de 70.000 € totalmente exenta por reinversión automática'],
        2,
        'La ganancia patrimonial = valor de transmisión − valor de adquisición = 290.000 − 220.000 = 70.000 €, y se integra en la base del ahorro del IRPF, gravada por tramos progresivos (19%–28%).',
    ),
    (
        'En el ámbito de la tecnología blockchain aplicada al sector inmobiliario, ¿qué permite principalmente la tokenización de activos?',
        ['Eliminar por completo la tributación de las plusvalías inmobiliarias', 'Fraccionar la propiedad del activo, mejorando su liquidez y accesibilidad', 'Garantizar una revalorización mínima anual del inmueble', 'Sustituir la inscripción registral por una garantía de rentabilidad'],
        1,
        'La tokenización divide la propiedad del inmueble en participaciones digitales (tokens), lo que reduce el ticket de entrada y mejora la liquidez y accesibilidad del mercado, aunque plantea retos regulatorios y de ciberseguridad.',
    ),
    (
        'En un préstamo hipotecario amortizado por el sistema lineal (cuota de amortización de capital constante), ¿cómo evoluciona la cuota total periodo a periodo?',
        ['Permanece constante en todos los periodos', 'Crece cada año en función de la inflación', 'Se concentra íntegramente en el último periodo', 'Decrece con el tiempo al reducirse los intereses sobre el capital vivo'],
        3,
        'En el sistema lineal la amortización de capital es constante, de modo que los intereses (calculados sobre el capital vivo, que disminuye) bajan cada periodo y la cuota total decrece. En el sistema francés, en cambio, la cuota total es constante.',
    ),
    (
        'La denominada "plusvalía municipal" (IIVTNU) que se liquida al vender un inmueble urbano, ¿qué grava exactamente?',
        ['El valor catastral de la construcción durante su tenencia', 'La renta obtenida por el arrendamiento del inmueble', 'El incremento de valor del suelo urbano puesto de manifiesto en la transmisión', 'El importe del préstamo hipotecario pendiente en el momento de la venta'],
        2,
        'El Impuesto sobre el Incremento de Valor de los Terrenos de Naturaleza Urbana (IIVTNU) es un tributo local que grava el incremento de valor del suelo urbano manifestado con ocasión de su transmisión.',
    ),
    (
        'Manteniendo constante el ingreso operativo neto (NOI), ¿qué efecto tiene sobre el valor de un inmueble una reducción de la tasa de capitalización (cap rate) exigida por el mercado?',
        ['El valor del inmueble disminuye proporcionalmente', 'El valor del inmueble aumenta, al descontar la misma renta a una tasa menor', 'El valor del inmueble no varía, porque el cap rate solo afecta a la liquidez', 'El valor del inmueble se vuelve negativo'],
        1,
        'Como Valor = NOI / Cap Rate, con el NOI fijo una bajada del cap rate eleva el valor: valor y cap rate se mueven en sentido inverso. Suele darse cuando cae el riesgo percibido o aumenta la demanda.',
    ),
    (
        'Una sociedad acogida al régimen especial de arrendamiento de viviendas en el Impuesto sobre Sociedades, ¿de qué ventaja fiscal característica disfruta?',
        ['Una bonificación en la cuota íntegra del IS por las rentas del arrendamiento de viviendas, sujeta a requisitos de número y periodo de mantenimiento', 'La tributación al tipo del 0% idéntica a la de las SOCIMIs cotizadas', 'La exención total del IBI de todas las viviendas arrendadas', 'La devolución íntegra del IVA soportado en la construcción sin condiciones'],
        0,
        'El régimen especial de entidades dedicadas al arrendamiento de viviendas permite aplicar una bonificación en la cuota íntegra del IS sobre las rentas derivadas de dicho arrendamiento, condicionada al cumplimiento de requisitos (número mínimo de viviendas y periodo de mantenimiento en alquiler).',
    ),
]


INTRO = '# M6: Inversión Inmobiliaria\n\nComprar un piso para alquilarlo es, probablemente, la inversión más conocida por el gran público. Los ladrillos parecen sencillos, pero como inversión tienen sus reglas propias. Este módulo te enseña a pensar en un inmueble como lo hace un profesional: cuánto renta, cuánto cuesta, cómo se financia y cómo tributa.\n\nRasgos típicos de la inversión inmobiliaria: **baja liquidez** (un piso no se vende en un día), **altos costes de transacción** (impuestos, notaría, registro, agencia), **mucho capital inicial**, posibilidad de [[apalancamiento::usar dinero prestado (una hipoteca) para invertir más de lo que tienes; multiplica las ganancias, pero también las pérdidas]] vía hipoteca y una histórica cobertura frente a la inflación. Es un mercado muy **cíclico** y que exige gestión activa (mantenimiento, impagos, locales vacíos).'


SECCIONES = [
    {
        'titulo': 'Inversión directa frente a indirecta',
        'cuerpo': '- **Directa**: comprar el inmueble físicamente. Da control total (reformas, elegir inquilino, negociar la renta) pero exige mucho capital, tiene altos costes y poca liquidez.\n- **Indirecta**: invertir a través de vehículos (SOCIMIs/REITs, FII, SII, crowdfunding). Aporta liquidez (en los cotizados), diversificación inmediata, menos capital de entrada y gestión profesional, a cambio de comisiones y menos control.',
        'ejercicios': [],
    },
    {
        'titulo': 'Clasificación de la inversión inmobiliaria',
        'cuerpo': '- **Según el tipo de suelo**: urbano (edificable), urbanizable (pendiente de desarrollo) y rústico/no urbanizable.\n- **Según la actividad**: residencial (viviendas), oficinas, retail (locales y centros comerciales), logístico e industrial (naves), hotelero y otros usos (residencias, data centers). Cada segmento tiene su propio binomio rentabilidad-riesgo.',
        'ejercicios': [],
    },
    {
        'titulo': 'Rentabilidad y riesgo',
        'cuerpo': 'El binomio inmobiliario suele mostrar rentas relativamente estables pero fuerte sensibilidad al ciclo económico, a los tipos de interés y a la liquidez. Frente a la inversión financiera aporta descorrelación parcial y cobertura frente a la inflación, pero con menor liquidez y mayor coste de gestión.',
        'ejercicios': [],
    },
    {
        'titulo': 'Sostenibilidad (ESG) y tecnología',
        'cuerpo': '- **Factores ESG**: la eficiencia energética y las certificaciones **LEED, BREEAM y WELL** mejoran la valoración y reducen el riesgo (menos obsolescencia, mejor demanda). La financiación verde (bonos e hipotecas verdes) se vincula a estos estándares.\n- **Blockchain y tokenización**: los smart contracts automatizan y dan seguridad a las transacciones; la [[tokenización::dividir la propiedad de un activo (como un inmueble) en muchas participaciones digitales (tokens) que se pueden comprar y vender, facilitando invertir con poco dinero]] fracciona la propiedad, mejorando la liquidez y la accesibilidad, aunque plantea retos regulatorios y de ciberseguridad.',
        'ejercicios': [],
    },
    {
        'titulo': 'Vehículos de inversión inmobiliaria',
        'cuerpo': 'Una [[SOCIMI::Sociedad Cotizada de Inversión en el Mercado Inmobiliario; el equivalente español a los REIT: una empresa que cotiza en bolsa, invierte en inmuebles de alquiler y reparte la mayoría de sus beneficios como dividendo, con ventajas fiscales]] es el equivalente español a los [[REIT::sigla inglesa de los fondos de inversión inmobiliaria cotizados; empresas que invierten en inmuebles de alquiler y reparten casi todo su beneficio a los accionistas]] internacionales:\n- Tributan al **0%** en el Impuesto sobre Sociedades si cumplen los requisitos.\n- Reparto obligatorio de dividendos para mantener el régimen: al menos el **80%** de los beneficios de alquileres, el **50%** de las plusvalías por venta y el **100%** de los dividendos de otras SOCIMIs filiales.\n- Gravamen especial del **19%** (Ley 11/2009) sobre dividendos distribuidos a socios con participación ≥ 5% cuando esos dividendos estén exentos o gravados a menos del 10% en el perceptor. La Ley 11/2021 añadió un gravamen del **15%** sobre los beneficios NO distribuidos.\n- Su rentabilidad por dividendo es el dividendo anual por acción entre el precio de cotización.\n\n**FII frente a SII**: son IIC de carácter **no financiero**.\n- El [[FII (Fondo de Inversión Inmobiliaria)::fondo que invierte en inmuebles para alquilar; no cotiza en bolsa, su precio se calcula por tasación y ofrece liquidez limitada (reembolsos al menos una vez al año)]] es un patrimonio sin personalidad jurídica; la **SII** es una sociedad anónima con personalidad propia.\n- Los FII deben invertir al menos el **70%** de su activo en inmuebles urbanos de **alquiler**, con coeficiente de liquidez mínimo y obligación de dar liquidez al menos una vez al año.\n- Intervienen la sociedad gestora, la depositaria y la sociedad de [[tasación::valoración oficial de un inmueble hecha por una entidad autorizada; sirve de base para conceder hipotecas y para calcular el valor de los fondos inmobiliarios]]; el valor liquidativo se calcula a partir de la tasación periódica.\n- Frente a las SOCIMIs, los FII/SII no cotizados ofrecen menor liquidez.\n\n**Sociedades de arrendamiento de vivienda**: régimen especial del IS con bonificaciones por el alquiler de viviendas.\n\n**[[crowdfunding inmobiliario::forma de coinvertir con otras muchas personas en un proyecto inmobiliario concreto a través de una plataforma, aportando cantidades pequeñas. Más accesible, pero con riesgo de proyecto y poca liquidez]]**: plataformas que permiten coinvertir en proyectos concretos con importes reducidos; más accesibilidad pero riesgo de proyecto y liquidez limitada.',
        'ejercicios': [],
    },
    {
        'titulo': 'Métodos oficiales de valoración inmobiliaria',
        'cuerpo': '¿Cuánto vale un inmueble? Hay cuatro formas oficiales de calcularlo:\n1. **Método de comparación (mercado)**: mira a cuánto se han vendido inmuebles parecidos, ajustando diferencias de superficie, ubicación y fecha.\n2. **Método de capitalización de rentas**: calcula el valor como lo que valen hoy las rentas futuras que genera:\n   $$\\text{Valor} = \\frac{\\text{Renta Neta Anual}}{\\text{Cap Rate (Tasa de Capitalización)}}$$\n   Una tasa de capitalización menor (más demanda, menos riesgo) implica mayor valor.\n3. **Método de coste (reposición)**: cuánto costaría comprar el suelo y construir de nuevo un inmueble equivalente, menos la depreciación por antigüedad. Es el método por defecto cuando no hay comparables o el inmueble es especial.\n4. **[[método residual::forma de valorar un solar calculando cuánto podría venderse lo que se construya en él y restando todos los costes de construir y el beneficio del promotor; lo que sobra es el valor del suelo]] (del suelo)**: obtiene el valor del suelo restando del valor de la promoción terminada todos los costes, impuestos y el beneficio del promotor. Puede ser estático o dinámico. Es el preferente para valorar solares.',
        'ejercicios': [],
    },
    {
        'titulo': 'Ratios y métricas financieras inmobiliarias',
        'cuerpo': '- **[[cap rate::rentabilidad anual neta de un inmueble; se calcula dividiendo lo que renta (NOI) entre su valor. Cap rate alto = barato y con más riesgo; bajo = caro y con menos riesgo]] (Capitalization Rate)**: relaciona el ingreso operativo neto con el valor del inmueble:\n  $$\\text{Cap Rate} = \\frac{\\text{NOI (Ingreso Operativo Neto)}}{\\text{Valor del inmueble}}$$\n  El [[NOI (Ingreso Operativo Neto)::renta que genera un inmueble tras restar los gastos de explotación (comunidad, seguros, IBI, mantenimiento), pero ANTES de restar la cuota de la hipoteca]] es la renta bruta menos los gastos de explotación, sin incluir la hipoteca ni la amortización de deuda.\n- **[[LTV (Loan-to-Value)::porcentaje del valor del inmueble que financia el banco con la hipoteca. Un LTV del 80% significa que el banco presta el 80% y tú pones el 20%. A más LTV, más riesgo]]**: importe del préstamo sobre el valor de tasación. Mide el apalancamiento; por encima del **80%** implica más riesgo y peores condiciones.\n- **Rentabilidad bruta por alquiler**: renta anual bruta dividida por el precio de compra.\n- **Rentabilidad neta por alquiler**: (renta anual menos gastos) dividida por la inversión total.\n- **[[cash-on-cash::rentabilidad que obtienes sobre el dinero propio que has puesto de verdad (sin contar la hipoteca). Muestra cómo el apalancamiento multiplica el retorno de tu capital]]**: flujo de caja anual antes de impuestos dividido por el capital propio (equity) aportado:\n  $$\\text{Cash-on-Cash} = \\frac{\\text{Flujo de caja anual antes de impuestos}}{\\text{Capital propio invertido}}$$',
        'ejercicios': [],
    },
    {
        'titulo': 'Fiscalidad inmobiliaria',
        'cuerpo': 'Un inmueble paga impuestos en cada fase de su vida: al comprarlo, al tenerlo, al alquilarlo y al venderlo.\n- **Compra**:\n  - *Vivienda nueva* (primera transmisión del promotor): [[IVA::Impuesto sobre el Valor Añadido; el impuesto que se paga al comprar bienes y servicios. En vivienda nueva es del 10%; en locales y suelo, del 21%]] (10% en vivienda; 21% en locales, garajes independientes y suelo) más [[AJD (Actos Jurídicos Documentados)::impuesto que grava la formalización de ciertos documentos notariales, como la escritura de una compraventa de vivienda nueva o de una hipoteca]].\n  - *Vivienda de segunda mano*: [[ITP (Impuesto sobre Transmisiones Patrimoniales)::impuesto que se paga al comprar una vivienda usada (de segunda mano); su tipo lo fija cada Comunidad Autónoma, habitualmente entre el 6% y el 10%]], a un tipo fijado por cada Comunidad Autónoma (normalmente 6%-10%).\n- **Tenencia**: [[IBI (Impuesto sobre Bienes Inmuebles)::impuesto local que se paga cada año por ser propietario de un inmueble; se calcula sobre el valor catastral que fija el Ayuntamiento]], tributo local anual sobre el valor catastral.\n- **Alquiler (IRPF)**: los [[rendimientos del capital inmobiliario::ingresos que obtiene el propietario por alquilar un inmueble; en el IRPF se integran en la base general tras restar los gastos deducibles]] se integran en la base general. Se deducen los gastos necesarios (intereses, IBI, comunidad, seguros, amortización, reparaciones). Sobre el rendimiento neto positivo del alquiler de **vivienda** se aplica una reducción (con carácter general del **60%**).\n- **Venta**: la [[ganancia patrimonial::beneficio obtenido al vender algo por más de lo que costó (un inmueble, acciones...). Tributa en la base del ahorro del IRPF, con tipos del 19% al 28%]] (valor de transmisión menos valor de adquisición) tributa en la base del ahorro por tramos (19%-28%).\n- **[[plusvalía municipal (IIVTNU)::impuesto local que grava el aumento de valor del suelo urbano cuando se vende o transmite un inmueble; lo cobra el Ayuntamiento]]**: grava el incremento de valor del suelo urbano al transmitir.',
        'ejercicios': [],
    },
    {
        'titulo': 'Productos hipotecarios y métodos de amortización',
        'cuerpo': '- **Concesión**: el banco evalúa la cuantía, la edad, el historial, el tipo de actividad y la capacidad de pago mediante sistemas de [[scoring::sistema automático que puntúa a un solicitante de crédito según sus datos (ingresos, historial, deudas) para estimar el riesgo de que no pague]].\n- **[[sistema francés::el método de amortización de hipoteca más habitual: se paga la misma cuota todos los meses; al principio la cuota es casi todo intereses y poco capital, y con el tiempo se invierte la proporción]]**: cuota constante. Al principio se paga más interés y menos capital, proporción que se invierte con el tiempo. Cuota:\n  $$a = C \\cdot \\frac{i}{1 - (1 + i)^{-n}}$$\n- **Sistema lineal (o de cuota de capital constante)**: la amortización de capital es constante cada periodo y la cuota total decrece con el tiempo.\n- **Hipotecas verdes**: financiación con condiciones preferentes para inmuebles eficientes o reformas sostenibles, vinculada a criterios ESG.',
        'ejercicios': [],
    },
    {
        'titulo': 'Intuición de los conceptos clave',
        'cuerpo': '- **Métodos de valoración**: comparación responde a "¿por cuánto se venden inmuebles similares?"; capitalización a "¿qué renta genera y a qué rentabilidad lo compraría el mercado?"; coste a "¿cuánto costaría construirlo de nuevo?"; residual a "¿cuánto vale el suelo según lo que puede promoverse en él?".\n- **Cap rate**: es la rentabilidad que exige el mercado; equivale a descontar una renta perpetua. Cap rate alto = activo barato y con más riesgo; cap rate bajo = caro y con menos riesgo. Valor y cap rate se mueven en sentido inverso.\n- **LTV**: qué parte financia el banco. Más LTV = más apalancamiento = más riesgo; a partir del 80% se endurecen condiciones.\n- **SOCIMI frente a FII**: la SOCIMI cotiza (líquida, IS al 0%, reparte al menos el 80% de las rentas de alquiler); el FII no cotiza (menos líquido, invierte al menos el 70% del activo en inmuebles de alquiler, valor por tasación).\n- **Fiscalidad de un vistazo**: compra (IVA+AJD si es nueva / ITP si es usada), tenencia (IBI), alquiler (IRPF en base general, reducción del 60% en vivienda) y venta (ganancia patrimonial en base del ahorro + plusvalía municipal).',
        'ejercicios': [],
    },
    {
        'titulo': 'Ejemplos resueltos',
        'cuerpo': '**Ejemplo 1 — Valoración por capitalización de rentas.** Un local produce una renta bruta anual de 24.000 € y soporta 4.000 € de gastos. El NOI = 24.000 − 4.000 = **20.000 €**. Con un cap rate del **5%**: Valor = 20.000 / 0,05 = **400.000 €**. (Si el cap rate bajara al 4%, el valor subiría a 500.000 €.)\n\n**Ejemplo 2 — Cálculo del LTV.** Vivienda tasada en 250.000 € financiada con un préstamo de 200.000 €. LTV = 200.000 / 250.000 = **80%**. El inversor aporta el 20% restante (50.000 €) más los gastos.\n\n**Ejemplo 3 — Rentabilidad bruta, neta y cash-on-cash.** Precio 200.000 € + gastos 20.000 € → inversión total **220.000 €**. Hipoteca de 160.000 € (LTV 80%), por lo que el equity aportado = 60.000 €. Renta bruta anual 14.000 €; gastos 3.000 € → NOI = **11.000 €**.\n  - Rentabilidad **bruta** = 14.000 / 200.000 = **7%**.\n  - Rentabilidad **neta** = 11.000 / 220.000 = **5%**.\n  - Con una cuota de hipoteca de 7.400 €/año, el flujo de caja antes de impuestos = 11.000 − 7.400 = 3.600 €. **Cash-on-cash** = 3.600 / 60.000 = **6%**. El apalancamiento eleva el retorno sobre el capital propio por encima de la rentabilidad neta.\n\n**Ejemplo 4 — Ganancia patrimonial en la venta (IRPF).** Adquisición 200.000 € + 20.000 € de gastos → valor de adquisición **220.000 €**. Venta 300.000 € − 10.000 € de gastos → valor de transmisión **290.000 €**. Ganancia = 290.000 − 220.000 = **70.000 €**, que tributa en la base del ahorro por tramos (6.000 × 19% + 44.000 × 21% + 20.000 × 23% = **14.980 €**; tipo medio ≈ 21,4%). Además se liquida la plusvalía municipal sobre el suelo.',
        'ejercicios': [],
    },
    {
        'titulo': 'Errores frecuentes',
        'cuerpo': '- Confundir el **80%** de reparto de dividendos de las **SOCIMI** con el **70%** de inversión mínima en inmuebles de los **FII**: son magnitudes y vehículos distintos.\n- Incluir la **cuota de la hipoteca** en el cálculo del **NOI**: el NOI es *antes* de deuda; el servicio de la deuda solo entra en el flujo de caja y en el cash-on-cash.\n- Suponer que cap rate y valor se mueven en el mismo sentido: la relación es **inversa** (menor cap rate → mayor valor).\n- Aplicar **IVA** a la vivienda de **segunda mano**: la usada tributa por **ITP**; solo la primera entrega del promotor lleva IVA (10%) + AJD.\n- Calcular el **cash-on-cash** sobre la inversión total en lugar de sobre el capital propio (equity).\n- Creer que la reducción del **60%** se aplica a cualquier alquiler: solo al de **vivienda** y sobre el rendimiento neto positivo.',
        'ejercicios': [],
    },
    {
        'titulo': 'Claves de examen',
        'cuerpo': '- Memoriza **Valor = Renta Neta Anual / Cap Rate** y su despeje (Cap Rate = NOI / Valor).\n- **SOCIMI**: IS 0%, cotiza, reparte al menos el 80% de las rentas de alquiler, el 50% de las plusvalías y el 100% de los dividendos de filiales; gravamen especial del 19% (Ley 11/2009) y del 15% (Ley 11/2021) sobre beneficios no distribuidos.\n- **FII**: IIC no financiera, al menos el 70% del activo en inmuebles urbanos en alquiler, liquidez al menos anual; la **SII** es una sociedad anónima.\n- **Sistema francés**: cuota constante. **Sistema lineal**: amortización de capital constante y cuota total decreciente.\n- **Método residual** para suelo y solares; **coste de reposición** ante falta de comparables u obra nueva especial.\n- Distingue la tributación por fases: compra (IVA+AJD / ITP), tenencia (IBI), alquiler (IRPF, reducción 60% vivienda) y venta (ganancia patrimonial en base del ahorro + IIVTNU).',
        'ejercicios': [],
    },
]
