# Módulo M2 — Fondos y Sociedades de Inversión
# PREGUNTAS: cada tupla es (enunciado, [4 opciones], indice_respuesta_correcta, explicacion)
# Ampliar apuntes y preguntas conforme al temario oficial EFPA. NO borrar términos ya existentes.
NOMBRE = 'Fondos y Sociedades de Inversión'

PREGUNTAS = [
    (
        '¿Cuál de las siguientes afirmaciones sobre los ETFs es CORRECTA?',
        ['Se negocian en bolsa en tiempo real', 'Tienen costes de gestión superiores a los fondos activos', 'Son siempre garantizados', 'Solo se pueden reembolsar al final del día'],
        0,
        'Los ETFs (Exchange Traded Funds) se negocian en bolsa de la misma forma que una acción ordinaria, en tiempo real.',
    ),
    (
        '¿Qué caracteriza a los Hedge Funds o IIC de Inversión Libre?',
        ['Límites de apalancamiento laxos y uso libre de derivados', 'Están garantizados por el Estado', 'Tienen comisiones de suscripción nulas obligatoriamente', 'Solo invierten en deuda pública'],
        0,
        'Las IIC de inversión libre gozan de gran flexibilidad de apalancamiento y uso de posiciones cortas sin los límites UCITS.',
    ),
    (
        '¿Qué establece la regla general del 5/10/40 para fondos de inversión UCITS armonizados?',
        ['Un fondo no puede invertir más del 10% de su patrimonio en valores de un mismo emisor, y las posiciones que superan el 5% no pueden sumar en conjunto más del 40%', 'Las comisiones del fondo de inversión no pueden superar el 5% de suscripción, 10% de gestión y 40% de éxito', 'El fondo debe mantener un 5% de liquidez, 10% en renta fija y un máximo del 40% en renta variable', 'El patrimonio mínimo debe ser de 5 millones de euros, con 10 partícipes mínimo durante 40 días'],
        0,
        'Esta regla busca diversificar el riesgo: máximo de 10% por emisor, y el total de emisores en los que se invierte entre el 5% y 10% no puede exceder el 40% del fondo.',
    ),
    (
        'En España, ¿cuál es el beneficio fiscal exclusivo para las personas físicas en relación a los fondos de inversión?',
        ['La exención por traspaso (diferimiento fiscal al cambiar de fondo sin tributar)', 'La deducción del 15% de las suscripciones en la base imponible general', 'Que los dividendos distribuidos por el fondo están exentos hasta 1.500 € anuales', 'La reducción automática del 40% de las plusvalías por antigüedad del partícipe'],
        0,
        'El régimen de traspasos permite a los residentes fiscales diferir el pago del IRPF al transferir saldo de un fondo a otro.',
    ),
    (
        'En un fondo de inversión, ¿quién calcula el valor liquidativo y custodia los activos?',
        ['La sociedad gestora calcula el valor liquidativo y la entidad depositaria custodia los activos y vigila a la gestora', 'La entidad depositaria calcula el valor liquidativo y la CNMV custodia los activos', 'La sociedad gestora realiza ambas funciones para reducir costes de intermediación', 'El comité de partícipes supervisa y calcula diariamente el valor liquidativo'],
        0,
        'La SGIIC administra y valora la cartera, mientras que el depositario custodia los valores y liquida operaciones, garantizando independencia.',
    ),
    (
        '¿Cuál es la principal ventaja de las clases de acciones de acumulación frente a las de distribución en un fondo de inversión para un inversor particular en España?',
        ['Las clases de acumulación reinvierten los rendimientos dentro del fondo, difiriendo la tributación del inversor hasta el reembolso', 'Las clases de acumulación garantizan una rentabilidad mínima fija anual', 'Las clases de acumulación tributan al 10% fijo en lugar de la escala de ahorro', 'Las clases de distribución permiten recuperar el capital inicial sin costes de suscripción'],
        0,
        'Los dividendos acumulados incrementan directamente el valor de la participación del fondo sin generar retención fiscal inmediata en el IRPF.',
    ),
    (
        '¿Cuál es el límite máximo de exposición al riesgo global a través de derivados que puede asumir un fondo UCITS armonizado según la normativa?',
        ['El 100% de su patrimonio neto (lo que permite un apalancamiento máximo de 2 veces el valor liquidativo)', 'El 50% de su patrimonio neto para evitar riesgos sistémicos', 'El 300% de su patrimonio neto siempre que cuente con un depositario de calificación AAA', 'No existe límite si el fondo está dirigido a inversores cualificados de la UE'],
        0,
        'La directiva UCITS limita la exposición global a través de derivados al 100% del valor liquidativo neto del fondo.',
    ),
    (
        'En la comercialización de fondos en España, ¿cuál es el porcentaje máximo legal que puede cobrar un fondo por comisión de gestión si se calcula exclusivamente sobre el patrimonio del fondo?',
        ['Un máximo del 2.25% anual', 'Un máximo del 5.00% anual', 'Un máximo del 1.00% anual', 'No existen límites legales, se rigen libremente por oferta y demanda'],
        0,
        'El límite máximo legal en España es del 2.25% anual sobre patrimonio para la comisión de gestión (o bien el 18% sobre resultados).',
    ),
    (
        '¿Cuál es el importe de inversión mínima inicial exigido por la ley española para que un inversor minorista pueda entrar en un Hedge Fund?',
        ['100.000 € y la firma de un documento de consentimiento de riesgos', '10.000 € sin restricciones adicionales de perfilado', '50.000 € siempre que cuente con asesoramiento independiente obligatorio', '60.000 € y ser titular de una cartera de valores cotizados de más de 300.000 €'],
        0,
        'En España, los inversores no profesionales pueden suscribir Hedge Funds a partir de 100.000 € y declarando conocer los riesgos del producto.',
    ),
    (
        "¿Qué mide la diferencia entre 'Tracking Error' y 'Tracking Difference' en un ETF?",
        ['El Tracking Error mide la volatilidad de la diferencia de rendimientos diarios frente al índice, mientras que el Tracking Difference mide la desviación acumulada neta al final del periodo', 'El Tracking Error mide las comisiones de gestión y el Tracking Difference la liquidez del mercado primario', 'El Tracking Difference aplica solo a los ETFs de réplica sintética y el Tracking Error a los de réplica física', 'Son términos sinónimos que indican el diferencial de prima sobre el valor liquidativo del ETF'],
        0,
        'El tracking error es una métrica de dispersión (desviación típica), mientras que el tracking difference es el retorno neto acumulado del ETF contra el benchmark.',
    ),
    (
        'En un proceso de fusión de dos fondos de inversión españoles, ¿cuál es el impacto fiscal para los partícipes personas físicas?',
        ['Los partícipes no tributan en el IRPF por la plusvalía acumulada en el proceso al aplicarse el régimen especial de fusiones', 'Deben tributar obligatoriamente por la ganancia patrimonial latente al desaparecer el fondo original', 'Tributan al tipo reducido de retenciones del 9.5% por rescate forzoso de participaciones', 'Están exentos solo si reinvierten el capital en planes de pensiones individuales'],
        0,
        'El régimen tributario de fusiones de IIC garantiza la neutralidad fiscal, traspasando el coste y la antigüedad al nuevo fondo resultante sin devengo de IRPF.',
    ),
    (
        "En el contexto de los fondos de inversión (IIC), ¿qué es el 'Soft Close'?",
        ['La suspensión temporal de suscripciones de nuevos partícipes, permitiendo aportaciones solo a los ya existentes', 'El reembolso forzoso de participaciones cuando el fondo sufre pérdidas consecutivas', 'La reducción voluntaria de la comisión de gestión para incentivar suscripciones', 'La liquidación definitiva de los activos del fondo por orden directa de la CNMV'],
        0,
        'El Soft Close limita la entrada de capital de nuevos inversores para proteger la estrategia de inversión cuando el tamaño del fondo es demasiado grande.',
    ),
    (
        'En un fondo de inversión que aplica una comisión de éxito bajo el sistema de marca de agua (High Watermark), ¿cuándo se devenga dicha comisión?',
        ['Solo cuando el valor liquidativo del fondo supera su máximo histórico anterior en una fecha de cálculo', 'Siempre que el fondo obtenga una rentabilidad superior a la tasa libre de riesgo oficial', 'Al final de cada ejercicio de forma fija si la rentabilidad anual ha sido positiva', 'Cuando la comisión de gestión acumulada no supera el límite máximo del 2.25%'],
        0,
        'El sistema de marca de agua exige que el gestor recupere pérdidas anteriores antes de volver a cobrar la comisión sobre nuevos máximos de valor liquidativo.',
    ),
    (
        'En la clasificación de IIC en España, ¿cuál es el plazo mínimo de preaviso que exige la ley si un partícipe desea realizar un reembolso de más de 300.000 € sin sufrir penalizaciones de liquidez?',
        ['Un preaviso mínimo de 10 días hábiles de antelación a la fecha de reembolso', 'No existe límite, los reembolsos de cualquier importe deben liquidarse en 24 horas', 'Preaviso de 30 días naturales por escrito firmado ante notario', 'Preaviso de 5 días hábiles si el fondo es de réplica sintética cotizado'],
        0,
        'La legislación española de IIC permite exigir un preaviso de hasta 10 días para reembolsos significativos (superiores a 300.000 €) para evitar distorsiones de cartera.',
    ),
    (
        '¿Qué define a un fondo de inversión de retorno absoluto?',
        ['Busca obtener rentabilidad positiva en cualquier condición de mercado, sin estar referenciado a un índice o benchmark clásico', 'Garantiza por contrato recuperar al menos el 100% de la inversión inicial a vencimiento', 'Invierte exclusivamente en derivados de divisas exóticas apalancados', 'Aplica una comisión de gestión del 0% si la rentabilidad anual es inferior al 10%'],
        0,
        'Los fondos de retorno absoluto buscan rentabilidades desvinculadas de la tendencia general de los mercados mediante estrategias flexibles no direccionales.',
    ),
    (
        "En relación con los fondos UCITS, ¿cuál es el porcentaje máximo de activos no cotizados (acciones o deuda ilíquida) que pueden mantener en cartera bajo el 'límite de basura' (trash ratio)?",
        ['Un máximo del 10% de su patrimonio neto', 'Un máximo del 5% del patrimonio neto consolidado', 'Un máximo del 25% si está destinado a inversores profesionales', 'Está prohibido en su totalidad tener activos no cotizados en fondos UCITS'],
        0,
        'Los fondos armonizados (UCITS) pueden destinar como máximo un 10% de sus activos a valores mobiliarios o instrumentos financieros no admitidos a cotización.',
    ),
    (
        'El ratio de Sharpe de un fondo de inversión mide:',
        ['La rentabilidad obtenida por encima del activo libre de riesgo por cada unidad de riesgo total (volatilidad) asumida', 'La rentabilidad del fondo por cada unidad de riesgo sistemático (beta) asumida', 'La diferencia de rentabilidad entre el fondo y su índice de referencia', 'El exceso de rentabilidad no explicado por el comportamiento del mercado'],
        0,
        'El ratio de Sharpe relaciona la prima de rentabilidad sobre el activo sin riesgo con la volatilidad (desviación típica) total de la cartera; a mayor ratio, mejor rentabilidad ajustada al riesgo total.',
    ),
    (
        '¿En qué se diferencia el ratio de Treynor del ratio de Sharpe?',
        ['El Treynor divide el exceso de rentabilidad por la beta (riesgo sistemático), mientras que el Sharpe lo divide por la desviación típica (riesgo total)', 'El Treynor solo se aplica a fondos garantizados y el Sharpe a fondos de renta variable', 'El Treynor mide el riesgo total y el Sharpe únicamente el riesgo específico o diversificable', 'Ambos ratios son idénticos y solo cambia el nombre según el proveedor de datos'],
        0,
        'El ratio de Treynor usa la beta (riesgo de mercado no diversificable) como denominador, adecuado para carteras bien diversificadas; el Sharpe emplea la volatilidad total.',
    ),
    (
        'El alfa de Jensen de un fondo representa:',
        ['El exceso de rentabilidad del fondo respecto a la que le correspondería según el CAPM por su nivel de riesgo sistemático; un alfa positivo indica buena gestión', 'La sensibilidad de la rentabilidad del fondo ante variaciones del mercado', 'La proporción de la cartera invertida en el activo libre de riesgo', 'La comisión de éxito que cobra el gestor cuando bate a su índice'],
        0,
        'El alfa de Jensen es la rentabilidad diferencial atribuible a la habilidad del gestor una vez descontada la rentabilidad exigida por el modelo CAPM; positivo indica valor añadido.',
    ),
    (
        'El ratio de información (Information Ratio) de un fondo se calcula como:',
        ['El cociente entre el exceso de rentabilidad del fondo sobre su índice de referencia y el tracking error de dicho exceso', 'El cociente entre la rentabilidad total del fondo y su comisión de gestión', 'La diferencia entre el ratio de Sharpe del fondo y el de su categoría', 'El producto de la beta del fondo por la rentabilidad del mercado'],
        0,
        'El ratio de información mide la rentabilidad activa (alfa frente al benchmark) por unidad de riesgo activo (tracking error); valora la consistencia de la gestión activa.',
    ),
    (
        'En cuanto a los estilos de gestión, ¿qué distingue al estilo "value" del estilo "growth"?',
        ['El estilo value busca compañías infravaloradas con múltiplos bajos (PER, precio/valor contable), mientras que el growth invierte en empresas con alto crecimiento esperado de beneficios', 'El estilo value invierte solo en deuda pública y el growth solo en renta variable emergente', 'El estilo value replica un índice de forma pasiva y el growth siempre usa apalancamiento', 'Ambos estilos son sinónimos de gestión pasiva indexada de bajo coste'],
        0,
        'El value selecciona valores baratos en relación con sus fundamentales; el growth prioriza el potencial de crecimiento de beneficios aunque coticen con múltiplos elevados.',
    ),
    (
        'El TER o ratio de gastos totales (gastos corrientes) de un fondo de inversión:',
        ['Recoge el conjunto de gastos anuales soportados por el fondo (gestión, depósito, auditoría, etc.) en relación con su patrimonio, y reduce directamente el valor liquidativo', 'Es una comisión adicional que el partícipe paga aparte en el momento de la suscripción', 'Solo incluye la comisión de reembolso y las penalizaciones por preaviso', 'Es un impuesto que aplica la CNMV sobre las plusvalías del fondo'],
        0,
        'El TER (gastos corrientes del DFI/KID) agrega los costes recurrentes del fondo como porcentaje del patrimonio; ya está descontado del valor liquidativo, por lo que penaliza la rentabilidad neta.',
    ),
    (
        '¿Qué es el DFI o Documento de Datos Fundamentales para el Inversor (KID/KIID)?',
        ['Un documento breve y estandarizado, previo a la suscripción, que resume objetivos, política de inversión, perfil de riesgo (indicador de 1 a 7), costes y rentabilidades históricas del fondo', 'El contrato privado entre la gestora y el depositario que fija sus comisiones internas', 'El informe trimestral de auditoría que la gestora remite exclusivamente a la CNMV', 'Un certificado fiscal que acredita el diferimiento por traspaso ante Hacienda'],
        0,
        'El DFI/KID (KIID) es el documento armonizado de entrega obligatoria antes de suscribir; sintetiza en pocas páginas la información esencial para comparar fondos y decidir con conocimiento.',
    ),
    (
        'Las Entidades de Capital Riesgo (ECR) y los fondos de inversión a largo plazo europeos (FILPE/ELTIF) se caracterizan por:',
        ['Ser IIC de tipo cerrado que invierten en activos ilíquidos (empresas no cotizadas, infraestructuras, proyectos a largo plazo) con menor liquidez para el inversor', 'Ofrecer liquidez diaria y réplica de índices bursátiles con bajísimas comisiones', 'Estar garantizados por el Fondo de Garantía de Depósitos', 'Invertir exclusivamente en deuda pública a corto plazo del mercado monetario'],
        0,
        'El capital riesgo y los ELTIF/FILPE son vehículos cerrados orientados a la financiación de empresas y proyectos a largo plazo; su iliquidez y horizonte prolongado los diferencian de las IIC abiertas.',
    ),
    (
        'En la selección de fondos, ¿cuál es la diferencia entre un "ranking" y un "rating"?',
        ['El ranking ordena los fondos por su rentabilidad pasada en un periodo dado, mientras que el rating es una calificación cualitativa/cuantitativa que valora consistencia y rentabilidad ajustada al riesgo', 'El ranking es una calificación con estrellas y el rating una simple lista alfabética de fondos', 'Ambos son idénticos y solo se diferencian en el idioma del proveedor', 'El ranking lo emite la CNMV con carácter vinculante y el rating es meramente informativo'],
        0,
        'El ranking es una clasificación por resultados históricos; el rating (p. ej. estrellas Morningstar) incorpora la consistencia y el riesgo asumido, aportando una valoración más completa y prospectiva.',
    ),
    (
        'Un fondo de gestión pasiva o indexado se caracteriza por:',
        ['Replicar la composición y el comportamiento de un índice de referencia, con comisiones reducidas y un tracking error bajo', 'Buscar batir sistemáticamente a su índice mediante selección activa de valores', 'Garantizar una rentabilidad mínima a vencimiento mediante estructuras de derivados', 'Cobrar siempre una comisión de éxito superior a la de los fondos activos'],
        0,
        'La gestión pasiva persigue reproducir un índice (no superarlo), lo que reduce costes y rotación; su calidad se mide por un tracking error bajo frente al benchmark.',
    ),
    (
        'En el análisis de la política de inversión, ¿qué distingue el enfoque "top-down" del "bottom-up"?',
        ['El top-down parte del análisis macroeconómico y sectorial para después seleccionar valores, mientras que el bottom-up prioriza el análisis fundamental de cada empresa con independencia del ciclo', 'El top-down invierte solo en grandes compañías y el bottom-up solo en pequeñas', 'El top-down es propio de la gestión pasiva y el bottom-up de la gestión garantizada', 'Ambos enfoques exigen replicar obligatoriamente un índice de referencia'],
        0,
        'El top-down decide primero la asignación por países/sectores según la coyuntura y luego elige valores; el bottom-up selecciona compañías por sus fundamentales individuales de abajo hacia arriba.',
    ),
    (
        'Un fondo tiene un patrimonio neto de 80 millones de euros y 5 millones de participaciones en circulación. ¿Cuál es su valor liquidativo?',
        ['12,00 €', '16,00 €', '20,00 €', '8,00 €'],
        1,
        'El valor liquidativo es el patrimonio neto dividido entre el número de participaciones: 80.000.000 / 5.000.000 = 16,00 € por participación.',
    ),
    (
        'El valor liquidativo de un fondo pasa de 10,00 € a 12,10 € en dos años. ¿Cuál es su rentabilidad anualizada (TAE)?',
        ['21% anual', '10% anual', '12,1% anual', '10,5% anual'],
        1,
        'La rentabilidad anualizada es (VL_final/VL_inicial)^(1/n) - 1 = (12,10/10,00)^(1/2) - 1 = (1,21)^0,5 - 1 = 1,10 - 1 = 0,10, es decir, 10% anual. El 21% sería la rentabilidad acumulada, no la anualizada.',
    ),
    (
        'Un fondo obtiene una rentabilidad del 8%, el activo libre de riesgo renta un 2% y la volatilidad del fondo es del 12%. ¿Cuál es su ratio de Sharpe?',
        ['0,25', '0,67', '1,00', '0,50'],
        3,
        'El ratio de Sharpe es (Rp - Rf) / σ = (8% - 2%) / 12% = 6 / 12 = 0,50. Relaciona el exceso de rentabilidad sobre el activo sin riesgo con la volatilidad total.',
    ),
    (
        'Un fondo espera una rentabilidad bruta del 5% anual y soporta un TER (gastos corrientes) del 1,2%. ¿Cuál es la rentabilidad neta aproximada que percibe el partícipe?',
        ['5,0%', '6,2%', '3,8%', '1,2%'],
        2,
        'El TER ya está descontado del valor liquidativo, de modo que reduce directamente la rentabilidad: 5,0% - 1,2% = 3,8% neto aproximado. Los gastos corrientes son un lastre recurrente sobre la rentabilidad.',
    ),
    (
        'Un fondo ha rentado un 12% frente al 8% de su índice de referencia, con un tracking error del 5%. ¿Cuál es su ratio de información?',
        ['0,40', '0,80', '1,60', '2,50'],
        1,
        'El ratio de información es (Rp - R_benchmark) / Tracking Error = (12% - 8%) / 5% = 4 / 5 = 0,80. Mide la rentabilidad activa por unidad de riesgo activo.',
    ),
    (
        'Según la normativa española, ¿cuál es la comisión máxima de depósito que puede cobrar la entidad depositaria sobre el patrimonio de un fondo?',
        ['1,00% anual', '0,50% anual', '0,20% anual', '5,00% anual'],
        2,
        'La comisión de depósito, que retribuye a la entidad depositaria por la custodia y vigilancia, tiene un límite legal del 0,20% anual sobre el patrimonio en España.',
    ),
    (
        'En España, ¿cuál es el capital social mínimo y el número mínimo de accionistas exigidos para constituir una SICAV?',
        ['1,2 millones € y 100 accionistas', '2,4 millones € y 50 accionistas', '3 millones € y 100 accionistas', '2,4 millones € y 100 accionistas'],
        3,
        'La SICAV es una sociedad anónima de capital variable que exige un capital social mínimo de 2,4 millones de euros y un mínimo de 100 accionistas.',
    ),
    (
        'En un fondo garantizado, ¿en qué momento opera la garantía de recuperación del capital?',
        ['En cualquier momento en que se reembolse', 'Únicamente en la fecha de vencimiento establecida', 'Solo durante los primeros 12 meses de vida del fondo', 'De forma continua y diaria sobre el valor liquidativo'],
        1,
        'La garantía de un fondo garantizado (construida con renta fija y derivados) solo es efectiva en la fecha de vencimiento. Quien reembolsa antes lo hace al valor liquidativo de mercado, que puede ser inferior al garantizado.',
    ),
    (
        '¿Cuál es la principal desventaja de un fondo de fondos (FOF)?',
        ['Que no permite diversificar la cartera', 'Que soporta una doble capa de comisiones', 'Que está prohibido para inversores minoristas', 'Que obliga a tributar en cada rebalanceo interno'],
        1,
        'El fondo de fondos invierte en participaciones de otras IIC, lo que multiplica la diversificación pero también acumula las comisiones del propio FOF y las de los fondos subyacentes: una doble capa de costes.',
    ),
    (
        'En un fondo UCITS armonizado, ¿hasta qué porcentaje del patrimonio se puede invertir en deuda emitida o garantizada por un Estado miembro de la UE, como excepción a la regla general?',
        ['10% del patrimonio', '35% del patrimonio', '100% del patrimonio', '5% del patrimonio'],
        1,
        'La normativa UCITS permite, como excepción al límite general por emisor, invertir hasta el 35% del patrimonio en valores emitidos o garantizados por un Estado miembro de la UE, dada su elevada calidad crediticia.',
    ),
    (
        'Un fondo obtiene una rentabilidad del 9%, el activo libre de riesgo renta un 3% y la beta del fondo es 1,5. ¿Cuál es su ratio de Treynor?',
        ['2,00', '4,00', '0,25', '6,00'],
        1,
        'El ratio de Treynor es (Rp - Rf) / β = (9% - 3%) / 1,5 = 6 / 1,5 = 4,00. Usa la beta (riesgo sistemático) como denominador, adecuado para carteras bien diversificadas.',
    ),
    (
        'Un fondo renta un 10%, el activo libre de riesgo un 2%, su beta es 1 y el mercado ha rentado un 8%. ¿Cuál es su alfa de Jensen?',
        ['2%', '0%', '-2%', '8%'],
        0,
        'La rentabilidad exigida por el CAPM es Rf + β·(Rm - Rf) = 2% + 1·(8% - 2%) = 8%. El alfa de Jensen es Rp menos esa exigida: 10% - 8% = 2%. Un alfa positivo indica valor añadido del gestor.',
    ),
    (
        'En una estructura master-feeder (fondo principal y fondo subordinado), ¿qué caracteriza al fondo subordinado?',
        ['Invierte la mayor parte de su patrimonio en el fondo principal', 'Garantiza contractualmente el capital del fondo principal', 'Cotiza obligatoriamente en bolsa como un ETF', 'No puede tener partícipes minoristas'],
        0,
        'En la estructura master-feeder, el fondo subordinado (feeder) canaliza la práctica totalidad de su patrimonio hacia el fondo principal (master), que es quien realiza la inversión efectiva en los mercados.',
    ),
    (
        '¿Cuál es la diferencia esencial entre el partícipe de un fondo de inversión y el socio de una SICAV?',
        ['El partícipe posee participaciones sin derechos políticos societarios, mientras que el socio es accionista con los derechos propios de una sociedad anónima', 'El partícipe tiene derecho de voto en junta y el socio no', 'El socio carece de personalidad jurídica y el partícipe la tiene', 'No existe ninguna diferencia jurídica entre ambos'],
        0,
        'El fondo carece de personalidad jurídica: el partícipe es titular de participaciones sin derechos societarios. La SICAV es una sociedad anónima, por lo que el socio es accionista con derechos de voto e información propios de una S.A.',
    ),
]

APUNTES = (
    '### M2: Fondos y Sociedades de Inversión\n\n'
    'Las **Instituciones de Inversión Colectiva (IIC)** canalizan el ahorro de múltiples inversores para invertirlo conjuntamente en activos financieros o no financieros, distribuyendo los resultados en función de las aportaciones de cada uno.\n\n'
    '#### 1. Concepto y ventajas de las IIC\n'
    'Las IIC aportan al inversor minorista ventajas difíciles de lograr individualmente:\n'
    '- **Diversificación**: reparto del riesgo entre numerosos activos incluso con aportaciones reducidas.\n'
    '- **Gestión profesional**: equipos especializados toman las decisiones de inversión.\n'
    '- **Liquidez**: en las IIC abiertas el partícipe puede suscribir y reembolsar al valor liquidativo.\n'
    '- **Seguridad jurídica y supervisión**: sujetas a regulación y a la vigilancia de la **CNMV** y del depositario.\n'
    '- **Economías de escala y acceso a mercados** a los que un particular no llegaría de forma eficiente.\n\n'
    '#### 2. Estructura y elementos intervinientes\n'
    '1. **Fondos de Inversión (FI)**: **carecen de personalidad jurídica propia**. Su patrimonio pertenece a los **partícipes** (dividido en participaciones). La gestión corresponde a una **Sociedad Gestora de IIC (SGIIC)** y la custodia a una **Entidad Depositaria**.\n'
    '2. **Sociedades de Inversión (SICAV)**: tienen **personalidad jurídica** de sociedad anónima; sus inversores son **socios/accionistas** (no partícipes). Capital variable, mínimo regulado de 2,4 millones de euros y mínimo de 100 accionistas en España.\n'
    '3. **Partícipe vs. socio**: el partícipe posee participaciones de un fondo sin derechos políticos societarios; el socio de una SICAV es accionista con los derechos propios de una sociedad anónima.\n'
    '4. **Sociedad Gestora (SGIIC)**: administra, invierte y **calcula el valor liquidativo**, lleva la contabilidad, elabora el folleto/DFI y los informes. Actúa en interés exclusivo de los partícipes.\n'
    '5. **Entidad Depositaria**: **custodia** los valores y el efectivo, liquida las operaciones y **vigila y supervisa** la actuación de la gestora. Gestora y depositario deben ser independientes.\n'
    '6. **CNMV**: autoriza, registra y supervisa las IIC, sus gestoras y depositarios; vela por la protección e información al inversor y por la transparencia del mercado.\n\n'
    '#### 3. Valor liquidativo (NAV) y rentabilidad\n'
    'El **Valor Liquidativo (VL o NAV)** es el precio unitario de la participación en un día dado:\n'
    '$$VL = \\frac{\\text{Patrimonio neto del fondo (activos a valor de mercado} - \\text{gastos y pasivos)}}{\\text{Número de participaciones en circulación}}$$\n'
    'La **rentabilidad acumulada** entre dos fechas se calcula sobre el VL:\n'
    '$$R_{acum} = \\frac{VL_{final} - VL_{inicial}}{VL_{inicial}}$$\n'
    'La **rentabilidad anualizada** (TAE) para un horizonte de *n* años se obtiene componiendo:\n'
    '$$R_{anual} = \\left(\\frac{VL_{final}}{VL_{inicial}}\\right)^{1/n} - 1$$\n\n'
    '#### 4. Comisiones y gastos\n'
    'Se distinguen las que cobra el fondo (implícitas, reducen el VL) y las que paga el partícipe directamente:\n'
    '- **Comisión de gestión**: la cobra la SGIIC. Puede calcularse sobre **patrimonio** (máx. 2,25% anual en España), sobre **resultados** (máx. 18%) o mixta (con límites combinados). \n'
    '- **Comisión de depósito**: la cobra el depositario sobre patrimonio (máx. 0,20% anual en España).\n'
    '- **Comisión de suscripción y de reembolso**: las paga el partícipe al entrar o salir; máximo 5% del importe cada una. Pueden usarse como **penalización por permanencia**.\n'
    '- **Comisión de éxito** con sistema de **marca de agua (High Watermark)**: solo se devenga cuando el VL supera su **máximo histórico** anterior, obligando a recuperar pérdidas previas antes de volver a cobrar.\n'
    '- **TER / gastos corrientes (OGC)**: ratio que agrega todos los **gastos anuales recurrentes** (gestión, depósito, auditoría, etc.) sobre el patrimonio. Aparece en el DFI/KID, ya está descontado del VL y penaliza la rentabilidad neta. No incluye la comisión de éxito ni los costes de suscripción/reembolso.\n\n'
    '#### 5. Información al partícipe: folleto y DFI/KID\n'
    '- **Folleto**: documento completo con la política de inversión, comisiones, riesgos y funcionamiento.\n'
    '- **DFI / DFCI / KID (KIID)**: **Documento de Datos Fundamentales para el Inversor**, breve y estandarizado, de **entrega obligatoria antes de la suscripción**. Resume objetivos y política, **indicador de riesgo (escala 1 a 7)**, costes (incl. gastos corrientes) y rentabilidades históricas. Permite comparar fondos.\n'
    '- **Informes periódicos**: la gestora remite informes (semestral y anual, con resumen trimestral) sobre la evolución y composición del fondo.\n\n'
    '#### 6. Regulación UCITS (Fondos Armonizados)\n'
    'Los fondos armonizados (directiva **UCITS**) gozan del **pasaporte europeo** para su comercialización transfronteriza y exigen altos estándares de liquidez y diversificación.\n'
    '- **Regla del 5/10/40**: no se puede invertir más del 5% del patrimonio en un mismo emisor; el límite sube al 10% siempre que la suma de las posiciones que superan el 5% no exceda del 40% del patrimonio.\n'
    '- **Excepción de deuda pública**: hasta el 35% en valores emitidos o garantizados por un Estado miembro de la UE.\n'
    '- **Exposición a derivados**: el riesgo global vía derivados no puede superar el 100% del patrimonio neto (apalancamiento máximo de 2x el VL).\n'
    '- **Límite de activos no cotizados (trash ratio)**: máximo 10% del patrimonio en valores no admitidos a cotización.\n\n'
    '#### 7. Tipología de fondos según destino de los beneficios\n'
    '- **De acumulación**: reinvierten los rendimientos en el propio fondo; el partícipe **difiere la tributación** hasta el reembolso.\n'
    '- **De reparto / distribución**: reparten periódicamente dividendos, que tributan en el momento del cobro.\n\n'
    '#### 8. Tipología de fondos según la naturaleza de sus activos\n'
    '- **Monetarios**: invierten en activos del mercado monetario de alta calidad crediticia y corto plazo; baja volatilidad y liquidez elevada.\n'
    '- **Renta fija, renta variable y mixtos (FI)**: según el peso de bonos y acciones.\n'
    '- **Garantizados**: aseguran a vencimiento (mediante estructuras de derivados y renta fija) la recuperación total o parcial del capital y, en su caso, una rentabilidad; la garantía solo opera en la fecha de vencimiento.\n'
    '- **Fondos de fondos (FOF)**: invierten en participaciones de otras IIC; mayor diversificación pero **doble capa de comisiones**.\n'
    '- **Fondos principales y subordinados (master-feeder)**: el subordinado canaliza su patrimonio hacia un fondo principal.\n'
    '- **Fondos cotizados (ETF)**: replican un índice y **cotizan en bolsa en tiempo real** como una acción; bajas comisiones y liquidez intradía. Se valoran por su **tracking error** (volatilidad de la diferencia diaria frente al índice) y su **tracking difference** (desviación acumulada neta). Réplica **física** o **sintética** (con derivados).\n'
    '- **Fondos de gestión pasiva / indexados**: buscan **replicar** un índice, no superarlo; comisiones reducidas y tracking error bajo.\n'
    '- **Fondos en valores no cotizados y Fondos de Inversión Libre (FIL / Hedge Funds)**: menor liquidez y mayor flexibilidad.\n'
    '- **Fondos temáticos y de impacto / ESG**: invierten en tendencias (tecnología, salud, energías renovables, cambio climático) o con criterios de sostenibilidad ambiental, social y de gobernanza.\n\n'
    '#### 9. SICAV\n'
    'Sociedad anónima de **capital variable** cuyo objeto es la inversión colectiva. Sus acciones se pueden comprar/vender y el capital fluctúa entre un mínimo y un máximo estatutario. Comparte régimen de diversificación con los FI. Los accionistas tienen derechos societarios (voto, información).\n\n'
    '#### 10. IIC de tipo cerrado (activos ilíquidos)\n'
    'Vehículos que **no ofrecen reembolso continuo**, orientados a activos ilíquidos y horizontes largos:\n'
    '- **Entidades de Capital Riesgo (ECR) / Private Equity**: financian empresas no cotizadas en distintas fases (venture capital, buyouts).\n'
    '- **Fondos de inversión a largo plazo europeos (FILPE / ELTIF)**: canalizan financiación a largo plazo hacia empresas, infraestructuras y proyectos.\n'
    '- **Fondos de emprendimiento social europeo (FESE)**: orientados a proyectos de impacto social.\n'
    'Ofrecen mayor rentabilidad potencial a cambio de **iliquidez, plazos largos y mayor riesgo**.\n\n'
    '#### 11. Hedge Funds y gestión alternativa\n'
    'Las **IIC de Inversión Libre (Hedge Funds)** aplican **gestión alternativa**: buscan rentabilidad **descorrelacionada** del mercado, con **apalancamiento**, ventas en corto y uso amplio de derivados, sin sujeción a la regla 5/10/40. En España la inversión mínima para minoristas es de **100.000 €** con consentimiento de riesgos. Existen también **IIC de IIC de inversión libre** (fondos de hedge funds). Estrategias principales:\n'
    '- **Valor relativo**: arbitraje de convertibles, arbitraje de renta fija, *equity market neutral*.\n'
    '- **Eventos societarios (Event Driven)**: arbitraje de fusiones, *distressed securities*.\n'
    '- **Oportunistas / direccionales**: *Global Macro*, *Long-Short*, ventas al descubierto, mercados emergentes.\n'
    '- **CTA / Managed Futures**: gestión sistemática o discrecional sobre futuros.\n'
    '- **Retorno absoluto**: persigue rentabilidad positiva en cualquier entorno de mercado, sin benchmark direccional.\n\n'
    '#### 12. Estilos de gestión\n'
    '- **Gestión activa**: el gestor busca **batir** a un índice mediante selección de valores y *timing*; mayores comisiones.\n'
    '- **Gestión pasiva**: **replica** un índice; menores costes y tracking error bajo.\n'
    '- **Value**: compra compañías **infravaloradas**, con múltiplos bajos (PER, precio/valor contable) y alta rentabilidad por dividendo.\n'
    '- **Growth**: invierte en empresas de **alto crecimiento** de beneficios, aunque coticen con múltiplos elevados.\n'
    '- **Blend / GARP**: combinación de value y growth.\n'
    '- **Top-down**: decide primero la asignación por países/sectores según la macro y luego elige valores.\n'
    '- **Bottom-up**: selecciona compañías por sus **fundamentales individuales**, con independencia del ciclo.\n\n'
    '#### 13. Análisis y selección de fondos\n'
    '- **Ranking**: ordena los fondos por su **rentabilidad pasada** en un periodo.\n'
    '- **Rating**: **calificación** (p. ej. estrellas Morningstar) que valora consistencia y rentabilidad **ajustada al riesgo**; más completo y prospectivo que el ranking.\n'
    '- **Style analysis**: técnica que estima la exposición real de un fondo a distintos estilos/clases de activo a partir de sus rentabilidades.\n'
    '- **Beta ($\\beta$)**: sensibilidad de la rentabilidad del fondo ante el mercado (riesgo sistemático).\n'
    '- **Alfa de Jensen ($\\alpha$)**: exceso de rentabilidad sobre la exigida por el **CAPM**; positivo indica valor añadido del gestor.\n'
    '$$\\alpha = R_p - [R_f + \\beta \\cdot (R_m - R_f)]$$\n'
    '- **Tracking Error**: desviación típica de la diferencia de rentabilidad entre el fondo y su índice (riesgo activo).\n'
    'Medidas de **rentabilidad ajustada al riesgo**:\n'
    '- **Ratio de Sharpe**: exceso de rentabilidad sobre el activo libre de riesgo por unidad de **riesgo total (volatilidad)**.\n'
    '$$S = \\frac{R_p - R_f}{\\sigma_p}$$\n'
    '- **Ratio de Treynor**: exceso de rentabilidad por unidad de **riesgo sistemático (beta)**; adecuado para carteras diversificadas.\n'
    '$$T = \\frac{R_p - R_f}{\\beta_p}$$\n'
    '- **Ratio de Información**: rentabilidad activa (alfa frente al benchmark) por unidad de **tracking error**; mide la consistencia de la gestión activa.\n'
    '$$IR = \\frac{R_p - R_{benchmark}}{Tracking\\ Error}$$\n\n'
    '#### 14. Fiscalidad de los fondos de inversión en España\n'
    '- **Régimen de traspasos**: las **personas físicas** residentes pueden traspasar su saldo de un fondo a otro **sin tributar** por la plusvalía latente (diferimiento fiscal); la tributación se pospone al reembolso definitivo. Las **personas jurídicas** no se acogen a este régimen.\n'
    '- **Reembolso**: las ganancias tributan en la **base del ahorro** del IRPF (escala 19%-28%), con retención a cuenta (19%).\n'
    '- **Fusiones de IIC**: se aplica el **régimen especial de neutralidad fiscal**; el partícipe no tributa y conserva coste y antigüedad en el nuevo fondo.\n'
    '- Otras operaciones de la operativa exigen requisitos de plazo/importe: p. ej., pueden establecerse **preavisos de hasta 10 días** para reembolsos superiores a 300.000 €.\n\n'
    '#### 15. Intuición en lenguaje llano de los conceptos clave\n'
    'Antes de calcular, conviene tener clara la idea:\n'
    '- **Valor liquidativo (VL)**: es el "precio de una participación". Imagina que el patrimonio del fondo es una tarta y las participaciones son las porciones: el VL es lo que vale cada porción hoy. Si el fondo vale 80 M€ y hay 5 M de porciones, cada una vale 16 €.\n'
    '- **TER / gastos corrientes**: es el "peaje anual" que el fondo cobra sin que lo veas, porque ya está restado del VL. No lo pagas aparte: simplemente tu rentabilidad llega mermada. Un TER del 1,5% significa que, aunque los mercados suban un 6%, a ti te queda alrededor del 4,5%.\n'
    '- **Tracking error**: mide cuánto "se despega" un fondo de su índice, no si va mejor o peor. Un fondo indexado bueno tiene tracking error bajo (se pega al índice); un fondo de gestión activa tiene tracking error alto (se aparta para intentar batirlo).\n'
    '- **Alfa**: es la "nota del gestor". Responde a: ¿el gestor ha aportado algo más allá de lo que ya explicaba el riesgo de mercado que asumió? Alfa positivo = ha añadido valor; alfa cero o negativo = no justifica sus comisiones.\n'
    '- **Beta**: mide cuánto "amplifica" el fondo los movimientos del mercado. Beta 1 = se mueve como el mercado; beta 1,5 = exagera un 50% las subidas y bajadas; beta 0,5 = amortigua.\n'
    '- **Comisiones**: las de gestión y depósito son "cuotas anuales" que erosionan el VL día a día; las de suscripción y reembolso son "peajes de entrada y salida" que paga el partícipe en el momento; la de éxito es una "propina al gestor" que solo cobra si lo hace bien (marca de agua).\n'
    '- **Fondo de acumulación vs. reparto**: acumulación = "bola de nieve" que crece sin que Hacienda te toque hasta el final; reparto = "cobras dividendos" que tributan cada vez que los recibes.\n\n'
    '#### 16. Ejemplos resueltos\n'
    '**Ejemplo 1 — Cálculo del valor liquidativo.**\n'
    'Un fondo tiene activos valorados a mercado por 51.500.000 €, gastos y pasivos pendientes por 500.000 € y 4.000.000 de participaciones en circulación.\n'
    'Patrimonio neto = 51.500.000 - 500.000 = 51.000.000 €.\n'
    '$$VL = \\frac{51.000.000}{4.000.000} = 12,75\\ \\text{€ por participación}$$\n\n'
    '**Ejemplo 2 — Rentabilidad acumulada y anualizada.**\n'
    'Un partícipe compra a un VL de 12,50 € y reembolsa dos años después a 15,00 €.\n'
    'Rentabilidad acumulada: $$R_{acum} = \\frac{15,00 - 12,50}{12,50} = 0,20 = 20\\%$$\n'
    'Rentabilidad anualizada: $$R_{anual} = \\left(\\frac{15,00}{12,50}\\right)^{1/2} - 1 = (1,20)^{0,5} - 1 = 1,0954 - 1 = 9,54\\%$$\n'
    'Clave: el 20% es lo ganado en total; el 9,54% es lo ganado "por año" de media compuesta. Nunca se dividen los 20% entre 2 (eso daría 10%, ignorando la capitalización).\n\n'
    '**Ejemplo 3 — Impacto del TER en la rentabilidad a largo plazo.**\n'
    'Se invierten 10.000 € durante 10 años. La rentabilidad bruta anual del mercado es del 6%. Comparamos un fondo caro (TER 1,5%, neto 4,5%) con la rentabilidad bruta:\n'
    '- Neto (4,5%): $$10.000 \\cdot (1,045)^{10} = 10.000 \\cdot 1,5530 = 15.530\\ \\text{€}$$\n'
    '- Bruto (6%): $$10.000 \\cdot (1,06)^{10} = 10.000 \\cdot 1,7908 = 17.908\\ \\text{€}$$\n'
    'El coste acumulado del TER durante 10 años asciende a 17.908 - 15.530 = 2.378 €, casi un 24% del capital inicial. Pequeñas diferencias de comisiones tienen un enorme efecto compuesto a largo plazo.\n\n'
    '**Ejemplo 4 — Tracking error y ratio de información.**\n'
    'Un fondo de gestión activa renta un 12% frente al 8% de su índice, con un tracking error (desviación típica del exceso de rentabilidad) del 5%.\n'
    'Rentabilidad activa = 12% - 8% = 4%.\n'
    '$$IR = \\frac{R_p - R_{benchmark}}{Tracking\\ Error} = \\frac{4\\%}{5\\%} = 0,80$$\n'
    'Un IR de 0,80 es sólido: el gestor genera 0,80 puntos de rentabilidad activa por cada punto de riesgo activo asumido. Se suele considerar bueno un IR por encima de 0,5.\n\n'
    '**Ejemplo 5 — Sharpe, Treynor y alfa de Jensen sobre una misma cartera.**\n'
    'Datos: R_p = 11%, R_f = 3%, R_m = 9%, volatilidad σ = 16%, beta β = 1,2.\n'
    '- Sharpe: $$S = \\frac{11 - 3}{16} = 0,50$$\n'
    '- Treynor: $$T = \\frac{11 - 3}{1,2} = 6,67$$\n'
    '- Rentabilidad exigida por el CAPM: $$R_f + \\beta(R_m - R_f) = 3 + 1,2 \\cdot (9 - 3) = 3 + 7,2 = 10,2\\%$$\n'
    '- Alfa de Jensen: $$\\alpha = 11 - 10,2 = 0,8\\%$$\n'
    'Interpretación: el alfa positivo (0,8%) indica que el gestor ha batido lo que le exigía su nivel de riesgo sistemático; ha aportado valor.\n\n'
    '**Ejemplo 6 — Reembolso con comisión y fiscalidad.**\n'
    'Un partícipe suscribió 500 participaciones a 12,50 € (coste 6.250 €) y las reembolsa a 15,00 € (importe bruto 7.500 €). El fondo aplica una comisión de reembolso del 1% y la ganancia soporta una retención del 19%.\n'
    '- Ganancia patrimonial: 7.500 - 6.250 = 1.250 €.\n'
    '- Comisión de reembolso: 1% · 7.500 = 75 €.\n'
    '- Retención a cuenta (19% sobre la ganancia): 0,19 · 1.250 = 237,50 €.\n'
    '- Importe neto recibido: 7.500 - 75 - 237,50 = 7.187,50 €.\n'
    'Nota: si en lugar de reembolsar traspasara el saldo a otro fondo, no habría retención ni tributación por el régimen de diferimiento (solo aplicable a personas físicas).\n\n'
    '**Ejemplo 7 — Comisión de éxito con marca de agua (High Watermark).**\n'
    'Un fondo parte de un VL máximo histórico de 100 €. En el año 1 cae a 90 €. En el año 2 sube a 105 €. La comisión de éxito es del 9% sobre la revalorización que supere el máximo histórico anterior.\n'
    '- Año 1: no se devenga comisión de éxito (VL por debajo del máximo).\n'
    '- Año 2: solo se cobra sobre lo que excede los 100 € previos, no sobre toda la subida desde 90 €. Base = 105 - 100 = 5 €. Comisión = 9% · 5 = 0,45 € por participación.\n'
    'La marca de agua impide cobrar dos veces por recuperar terreno perdido: primero hay que superar el máximo anterior.\n\n'
    '#### 17. Errores frecuentes\n'
    '- **Confundir VL con precio de mercado en los ETF**: en un fondo tradicional se suscribe/reembolsa al VL; un ETF cotiza en bolsa y su precio puede tener prima o descuento sobre el VL.\n'
    '- **Anualizar dividiendo entre los años**: la rentabilidad anualizada se compone con raíces/potencias, no se reparte linealmente.\n'
    '- **Sumar el TER como coste aparte**: el TER ya está descontado del VL; no se paga adicionalmente como la suscripción.\n'
    '- **Creer que la garantía de un fondo garantizado vale en cualquier momento**: solo opera a vencimiento.\n'
    '- **Confundir Sharpe y Treynor**: Sharpe usa la volatilidad total (σ); Treynor usa la beta (riesgo sistemático). Treynor es coherente en carteras bien diversificadas.\n'
    '- **Confundir tracking error y tracking difference**: el primero es una medida de dispersión (volatilidad de la diferencia); el segundo es la desviación acumulada neta frente al índice.\n'
    '- **Atribuir al partícipe derechos societarios**: el partícipe de un fondo no vota en junta; el accionista de una SICAV sí.\n'
    '- **Aplicar el régimen de traspasos a personas jurídicas**: el diferimiento fiscal por traspaso es exclusivo de personas físicas residentes.\n'
    '- **Olvidar que la comisión de éxito no forma parte del TER**: el TER recoge gastos corrientes recurrentes, no la comisión sobre resultados ni los costes de suscripción/reembolso.\n\n'
    '#### 18. Claves de examen\n'
    '- **Cifras clave España**: gestión máx. 2,25% sobre patrimonio (o 18% sobre resultados); depósito máx. 0,20%; suscripción y reembolso máx. 5% cada una; SICAV 2,4 M€ y 100 accionistas; Hedge Fund minorista desde 100.000 €.\n'
    '- **Regla 5/10/40** y **excepción del 35%** en deuda pública de un Estado UE; exposición a derivados máx. 100% del patrimonio; trash ratio máx. 10% en no cotizados.\n'
    '- **Quién hace qué**: la gestora (SGIIC) calcula el VL y administra; el depositario custodia y vigila; la CNMV autoriza y supervisa. Gestora y depositario deben ser independientes.\n'
    '- **Ratios**: Sharpe → σ total; Treynor → beta; Información → tracking error; Jensen → CAPM. Memoriza el denominador de cada uno, que es lo que suele distinguir la respuesta correcta.\n'
    '- **Fiscalidad**: traspasos sin tributar y fusiones con neutralidad fiscal, ambos solo para personas físicas; el reembolso tributa en la base del ahorro (19%-28%) con retención del 19%.\n'
    '- **DFI/KID**: entrega obligatoria antes de suscribir; incluye el indicador de riesgo de 1 a 7 y los gastos corrientes.'
)
