# Módulo M9 — Cumplimiento Normativo y Regulador
# PREGUNTAS: cada tupla es (enunciado, [4 opciones], indice_respuesta_correcta, explicacion)
# Ampliar apuntes y preguntas conforme al temario oficial EFPA. NO borrar términos ya existentes.
NOMBRE = 'Cumplimiento Normativo y Regulador'

PREGUNTAS = [
    (
        '¿Qué directiva de la UE regula la transparencia, comercialización y clasificación de clientes financieros?',
        ['MiFID II', 'Basilea III', 'Solvencia II', 'MiCA'],
        0,
        'MiFID II (Markets in Financial Instruments Directive II) es la directiva europea clave que regula la conducta, perfilado y clasificación de clientes.',
    ),
    (
        'Bajo la normativa MiFID II, ¿cuál es la diferencia clave entre el asesoramiento financiero independiente y el no independiente?',
        ['El asesor independiente no puede percibir retrocesiones o incentivos de terceros (inducements) y debe evaluar una gama amplia de productos del mercado', 'El asesor independiente tiene prohibido cobrar honorarios al cliente final', 'El asesor no independiente solo puede comercializar Letras del Tesoro público', 'El asesor independiente está exento de realizar el test de idoneidad al cliente'],
        0,
        'mifid ii es la directiva que prohíbe taxativamente retener incentivos (inducements) a asesores independientes, garantizando la transparencia ante el cliente.',
    ),
    (
        '¿Cuándo es obligatorio realizar el Test de Idoneidad según MiFID II?',
        ['Cuando se prestan los servicios de asesoramiento en materia de inversiones o gestión de carteras', 'Siempre que el cliente compre cualquier tipo de activo, incluidos depósitos simples', 'Únicamente cuando el cliente es clasificado como contraparte elegible', 'Cuando el cliente solicita un préstamo hipotecario sin vinculaciones'],
        0,
        'Bajo la directiva MiFID II, el test de idoneidad es obligatorio en asesoramiento y gestión discrecional de carteras del cliente. Evalúa sus conocimientos, situación financiera y objetivos de inversión.',
    ),
    (
        'Según el Código Ético de EFPA España, si existe un conflicto de interés insalvable entre el asesor y el cliente, ¿cómo debe proceder el asesor?',
        ['Debe anteponer siempre el interés del cliente y divulgar el conflicto con total transparencia', 'Debe priorizar los objetivos comerciales de su entidad financiera', 'Debe suspender la relación comercial sin dar explicaciones para proteger el secreto bancario', 'Debe cobrar una tarifa doble para compensar el riesgo operativo'],
        0,
        'El Código Ético exige actuar con objetividad y transparencia. Si el conflicto no es evitable, se debe informar por escrito y dar prioridad al cliente.',
    ),
    (
        'Bajo la directiva MiFID II, ¿qué cliente goza del menor nivel de protección regulatorio?',
        ['Contraparte elegible', 'Cliente profesional por solicitud', 'Cliente minorista', 'Pyme sin departamento financiero'],
        0,
        'Bajo la directiva MiFID II, las contrapartes elegibles se definen como un tipo de cliente institucional con conocimientos máximos, teniendo el nivel de protección más bajo de la clasificación de clientes.',
    ),
    (
        'Bajo las condiciones de MiFID II, ¿cómo puede un cliente minorista solicitar ser clasificado como profesional?',
        ['Debe cumplir al menos dos de los tres requisitos: 10 operaciones de volumen significativo por trimestre, cartera > 500.000 €, o 1 año de experiencia profesional en el sector', 'Basta con firmar un documento de exención de responsabilidades patrimoniales', 'Debe poseer una titulación universitaria de grado en economía o ADE', 'Abriendo una cuenta con un depósito bancario mínimo de 1.000.000 €'],
        0,
        'MiFID II regula el paso voluntario de minorista a profesional cumpliendo al menos dos de estos tres criterios de volumen, cartera o experiencia profesional.',
    ),
    (
        "Bajo las directrices de gobernanza de productos de MiFID II, ¿qué es el 'Mercado Objetivo Negativo'?",
        ['El grupo de clientes para cuyos intereses, necesidades y características el producto financiero NO es compatible, desaconsejando su venta', 'El conjunto de emisores financieros de países calificados como paraísos fiscales', 'El volumen de mercado de renta variable que genera pérdidas sistemáticas en la cartera', 'Las entidades de asesoramiento que carecen de licencia oficial de la CNMV'],
        0,
        'Bajo la gobernanza de productos de MiFID II, el mercado objetivo negativo especifica a qué clientes está desaconsejado venderles un activo debido a su complejidad, riesgo o plazos.',
    ),
    (
        '¿Qué plazo de conservación de registros relacionados con las recomendaciones y órdenes de clientes exige MiFID II de forma general?',
        ['Un mínimo de 5 años, pudiéndose ampliar hasta 7 años si lo solicita la CNMV', '1 año a contar desde la entrega de la declaración del IRPF del cliente', 'De por vida mientras la cuenta del cliente permanezca abierta en la entidad', '10 años naturales para cumplir con la legislación mercantil de prevención de blanqueo'],
        0,
        'MiFID II establece un plazo estándar de conservación de registros y grabaciones telefónicas de al menos 5 años, ampliable a 7 por el regulador nacional.',
    ),
    (
        "¿Qué define el concepto de 'Información Privilegiada' bajo el Reglamento de Abuso de Mercado (MAR)?",
        ['Información de carácter concreto, no pública, que se refiere a emisores y que, de hacerse pública, podría influir notablemente en la cotización', 'El análisis técnico elaborado por analistas financieros con herramientas de pago', 'Los datos macroeconómicos publicados de forma oficial por el Banco de España', 'Las circulares internas de cumplimiento normativo que regulan los horarios laborales'],
        0,
        'La información privilegiada es concreta, no pública y con capacidad de alterar de forma significativa los precios de cotización en el mercado.',
    ),
    (
        'Según el Código Ético de EFPA España, ¿cómo debe actuar el asesor en relación al Secreto Profesional?',
        ['Debe guardar estricta confidencialidad sobre toda la información financiera del cliente, salvo requerimiento judicial oficial o autorización del cliente', 'Debe revelar los datos financieros a la dirección de su sucursal bancaria con fines comerciales', 'Puede compartir la información de forma anónima en redes sociales si sirve de ejemplo', 'El secreto profesional expira automáticamente al cabo de dos años de rescindido el contrato'],
        0,
        'El principio de confidencialidad del Código Ético de la EFPA obliga al secreto absoluto de la información, salvo deber de cooperación judicial o permiso explícito.',
    ),
    (
        'Según el Código Ético de EFPA España, ¿cuál es la obligación del asesor respecto a su formación continua?',
        ['Mantener actualizados sus conocimientos profesionales mediante la acreditación anual de horas de formación exigidas por EFPA', 'Realizar un examen completo presencial cada dos años ante el regulador CNMV', 'Inscribirse obligatoriamente en un curso universitario de postgrado en finanzas cada cinco años', 'No existe obligación de formación continua tras obtener la certificación original'],
        0,
        'Para mantener las certificaciones de EFPA activas se exige acreditar anualmente un número determinado de horas de recertificación y formación continua.',
    ),
    (
        "Bajo la directiva MiFID II, ¿qué servicio financiero exige obligatoriamente a la entidad entregar una 'Declaración de Idoneidad' al cliente minorista?",
        ['El servicio de asesoramiento en materia de inversiones', 'La mera ejecución de órdenes de suscripción de acciones cotizadas (execution only)', 'La concesión de un préstamo personal con tipo de interés variable referenciado', 'El alquiler de una caja de seguridad física en la cámara acorazada de la sucursal'],
        0,
        'MiFID II exige entregar al cliente minorista una declaración por escrito detallando por qué las recomendaciones se ajustan a su idoneidad antes de ejecutar la transacción.',
    ),
    (
        '¿Qué función desempeña el Servicio Ejecutivo de la Comisión de Prevención del Blanqueo de Capitales (SEPBLAC) en España?',
        ['Es la unidad de inteligencia financiera nacional encargada de supervisar el cumplimiento de obligaciones de prevención del blanqueo', 'Regula las comisiones de depósito de los fondos de inversión UCITS de renta fija', 'Concede las licencias de apertura para nuevas sucursales bancarias internacionales', 'Audita las cuentas generales del Estado y supervisa la emisión de letras del Tesoro'],
        0,
        'El SEPBLAC es el supervisor oficial y el centro de recepción de las comunicaciones de operaciones sospechosas en España en materia de prevención de blanqueo.',
    ),
    (
        'Bajo el Reglamento General de Protección de Datos (RGPD) de la UE, ¿qué principio regula la recogida y tratamiento de datos de clientes financieros?',
        ['Principio de minimización de datos (solo se recogen los datos estrictamente necesarios para los fines del tratamiento)', 'Principio de libertad de cesión comercial a cualquier empresa vinculada al holding', 'Principio de almacenamiento indefinido para registros mercantiles generales', 'Principio de confidencialidad optativa condicionada al volumen de la cuenta'],
        0,
        'El principio de minimización de datos del RGPD establece que los datos personales recogidos deben ser adecuados, pertinentes y limitados a lo necesario.',
    ),
    (
        'Según el Código de Conducta de EFPA, ¿cómo debe actuar un asesor si recibe regalos u obsequios significativos de un emisor de productos?',
        ['Debe rechazarlos para evitar comprometer su independencia y objetividad profesional', 'Puede aceptarlos siempre que los declare como rendimientos en especie en su IRPF', 'Debe compartirlos con los miembros del departamento de riesgos de su banco', 'Puede aceptarlos solo si el valor estimado es inferior a 1.200 € anuales'],
        0,
        'La aceptación de regalos significativos vulnera el deber de objetividad y conflicto de interés del Código Ético de la EFPA, debiendo rechazarse para mantener la imparcialidad.',
    ),
    (
        'Bajo MiFID II, ¿en qué caso se aplica el Test de Conveniencia y NO el de Idoneidad?',
        ['En el servicio de asesoramiento en materia de inversiones', 'En la comercialización o venta de productos complejos sin asesoramiento, donde solo se evalúan los conocimientos y la experiencia del cliente', 'En la gestión discrecional de carteras', 'En la mera ejecución de órdenes sobre productos no complejos a iniciativa del cliente'],
        1,
        'Bajo MiFID II, el test de conveniencia se aplica a servicios distintos del asesoramiento y la gestión de carteras cuando el producto es complejo, y solo evalúa conocimientos y experiencia. El test de idoneidad se reserva al asesoramiento y la gestión discrecional de carteras.',
    ),
    (
        '¿Cuándo puede una entidad prestar el servicio de solo ejecución (execution only) sin evaluar la conveniencia?',
        ['Cuando se trata de instrumentos no complejos, el servicio se presta a iniciativa del cliente y se le advierte de que no se evalúa la conveniencia', 'Siempre que el cliente minorista firme un contrato de asesoramiento', 'Cuando el producto es un derivado estructurado complejo de alto riesgo', 'Únicamente cuando la entidad percibe incentivos del emisor'],
        0,
        'La solo ejecución exige tres condiciones: instrumento no complejo, iniciativa del cliente y advertencia de que no se evalúa la conveniencia. Con productos complejos siempre hay que evaluar al menos la conveniencia.',
    ),
    (
        'Según el Reglamento MiCA (UE 2023/1114), ¿cómo se denomina el criptoactivo que busca mantener un valor estable referenciándose a una cesta de activos, monedas o materias primas?',
        ['Ficha referenciada a activos (asset-referenced token, ART)', 'Ficha de dinero electrónico (EMT)', 'Ficha de consumo o utility token', 'Token no fungible (NFT) de coleccionismo'],
        0,
        'MiCA distingue las fichas referenciadas a activos (ART), ligadas a una cesta de activos o monedas; las fichas de dinero electrónico (EMT), ligadas a una única moneda oficial; y los utility tokens. La supervisión corresponde a ESMA (AEVM) y a la EBA (ABE).',
    ),
    (
        'En prevención del blanqueo de capitales, ¿en qué caso deben aplicarse obligatoriamente medidas reforzadas de diligencia debida?',
        ['Cuando el cliente es una entidad financiera de la UE sometida a supervisión', 'Cuando la operación es un pago de nómina domiciliado de escaso importe', 'Cuando el cliente es una persona con responsabilidad pública (PRP), por el mayor riesgo de corrupción asociado', 'Cuando el cliente es un organismo público de bajo riesgo'],
        2,
        'La Ley 10/2010 exige diligencia reforzada en situaciones de mayor riesgo, señaladamente con las personas con responsabilidad pública (PRP/PEP) y sus allegados. Las entidades supervisadas y los organismos públicos son supuestos de diligencia simplificada.',
    ),
    (
        'Bajo el RGPD, ¿cuál de los siguientes es un derecho del interesado sobre sus datos personales?',
        ['El derecho de supresión (derecho al olvido), que permite solicitar la eliminación de sus datos cuando ya no sean necesarios', 'El derecho a exigir la cesión gratuita de sus datos a la competencia', 'El derecho a que sus datos se conserven de forma indefinida sin su consentimiento', 'El derecho a percibir intereses por el tratamiento de sus datos'],
        0,
        'El RGPD reconoce los derechos de acceso, rectificación, supresión (derecho al olvido), oposición, limitación del tratamiento y portabilidad. La autoridad de control en España es la AEPD.',
    ),
    (
        'Bajo MiFID II y el Reglamento SFDR, ¿qué debe incorporar el asesor al test de idoneidad desde 2022?',
        ['Las preferencias de sostenibilidad del cliente (criterios ambientales, sociales y de gobernanza, ASG)', 'La huella de carbono personal del asesor', 'El historial crediticio del cónyuge del cliente', 'La rentabilidad garantizada de los fondos ASG'],
        0,
        'Desde 2022, MiFID II exige que el test de idoneidad recoja las preferencias de sostenibilidad (ASG) del cliente, en línea con el Reglamento SFDR (UE 2019/2088) de divulgación de información sobre sostenibilidad.',
    ),
    (
        '¿Qué documento estandarizado exige el Reglamento PRIIPs para los productos de inversión minorista empaquetados y los basados en seguros?',
        ['El Documento de Datos Fundamentales (KID / DFI), que resume riesgos, costes y escenarios de rentabilidad', 'El folleto completo de emisión de más de 200 páginas', 'La declaración anual del IRPF del cliente', 'El contrato marco de compensación de derivados EMIR'],
        0,
        'El Reglamento PRIIPs (UE 1286/2014) obliga a entregar un Documento de Datos Fundamentales (KID/DFI) breve que resume objetivo, riesgos, escenarios de rentabilidad, costes y horizonte recomendado, para facilitar la comparación por el minorista.',
    ),
    (
        'Bajo MiFID II, ¿cuál de las siguientes actividades es un servicio AUXILIAR y NO un servicio de inversión?',
        ['La gestión discrecional de carteras', 'El asesoramiento en materia de inversión', 'La ejecución de órdenes por cuenta de clientes', 'La custodia y administración de instrumentos financieros'],
        3,
        'Bajo la directiva MiFID II, la custodia y administración de instrumentos financieros por cuenta del cliente es un servicio AUXILIAR. La gestión de carteras, el asesoramiento y la ejecución de órdenes son servicios de inversión principales.',
    ),
    (
        'En España, ¿qué tipo de empresa de servicios de inversión (ESI) tiene su actividad limitada exclusivamente a la prestación de asesoramiento?',
        ['La Sociedad de Valores', 'La Empresa de Asesoramiento Financiero (EAF)', 'La Agencia de Valores', 'La Sociedad Gestora de Carteras'],
        1,
        'La Empresa de Asesoramiento Financiero (EAF) solo puede prestar asesoramiento en materia de inversión. Las Sociedades de Valores operan por cuenta propia y ajena, y las Agencias de Valores solo por cuenta ajena.',
    ),
    (
        'Bajo MiFID II, ¿en qué consiste la obligación de mejor ejecución (best execution)?',
        ['En obtener el mejor resultado posible para el cliente atendiendo a precio, costes, rapidez, probabilidad de ejecución y liquidación', 'En ejecutar siempre las órdenes en el mercado con mayor volumen de contratación', 'En garantizar al cliente una rentabilidad mínima en cada operación', 'En ejecutar las órdenes exclusivamente al precio de cierre de la sesión anterior'],
        0,
        'La mejor ejecución de MiFID II obliga a la entidad a lograr el mejor resultado posible para el cliente ponderando precio, costes, rapidez, y probabilidad de ejecución y liquidación, formalizado en una política de ejecución de órdenes.',
    ),
    (
        'Según el Reglamento SFDR, ¿cómo se clasifica un producto financiero que PROMUEVE características ambientales o sociales, sin tener la inversión sostenible como objetivo?',
        ['Producto del artículo 6', 'Producto del artículo 9', 'Producto del artículo 8', 'Producto del artículo 5'],
        2,
        'El Reglamento SFDR clasifica en artículo 6 (sin rasgos ASG), artículo 8 (promueve características ambientales o sociales, "light green") y artículo 9 (tiene como objetivo la inversión sostenible, "dark green").',
    ),
    (
        'Según el Reglamento MiCA, ¿qué criptoactivo se referencia al valor de una ÚNICA moneda oficial para mantener su estabilidad?',
        ['La ficha referenciada a activos (ART)', 'La ficha de consumo (utility token)', 'El token no fungible (NFT)', 'La ficha de dinero electrónico (EMT)'],
        3,
        'En MiCA, la ficha de dinero electrónico (EMT) se referencia a una sola moneda oficial, mientras que la ficha referenciada a activos (ART) se vincula a una cesta de varios activos, monedas o materias primas.',
    ),
    (
        'En prevención del blanqueo de capitales, ¿en cuál de los siguientes supuestos cabe aplicar medidas SIMPLIFICADAS de diligencia debida?',
        ['Cliente que es persona con responsabilidad pública (PRP)', 'Cliente que es una entidad de crédito de la UE sometida a supervisión', 'Operación con un país de alto riesgo', 'Relación de banca corresponsal transfronteriza'],
        1,
        'La Ley 10/2010 permite diligencia simplificada en supuestos de bajo riesgo, como las entidades de crédito de la UE supervisadas. Las PRP, los países de alto riesgo y la banca corresponsal exigen diligencia reforzada.',
    ),
    (
        'Ante una operación sospechosa por indicios de blanqueo de capitales, ¿cómo debe actuar el sujeto obligado?',
        ['Ejecutar la operación y comunicarla al mes siguiente', 'Advertir al cliente de que su operación está siendo investigada', 'Ignorarla si el importe es inferior a 1.000 euros', 'Abstenerse de ejecutar la operación y comunicarla al SEPBLAC'],
        3,
        'El sujeto obligado debe abstenerse de ejecutar la operación sospechosa y comunicarla al SEPBLAC. Está prohibido revelar al cliente que se ha realizado la comunicación (deber de no revelación o "tipping off").',
    ),
    (
        'Bajo el RGPD, ¿cuál es la autoridad de control competente en materia de protección de datos en España?',
        ['La Agencia Española de Protección de Datos (AEPD)', 'La Comisión Nacional del Mercado de Valores (CNMV)', 'El SEPBLAC', 'El Banco de España'],
        0,
        'La autoridad de control del RGPD en España es la Agencia Española de Protección de Datos (AEPD). La CNMV supervisa los mercados de valores y el SEPBLAC la prevención del blanqueo.',
    ),
    (
        'Bajo el Reglamento de Abuso de Mercado (MAR), ¿cuál de las siguientes es una conducta expresamente prohibida?',
        ['La aplicación del principio de minimización de datos', 'La realización del test de idoneidad al cliente', 'La manipulación de mercado', 'La aplicación de diligencia reforzada a una PRP'],
        2,
        'El Reglamento MAR (UE 596/2014) prohíbe las operaciones con información privilegiada, la comunicación ilícita de información privilegiada y la manipulación de mercado. Supervisan la CNMV y ESMA.',
    ),
    (
        'Bajo MiFID II, ¿en qué condiciones puede una entidad aceptar beneficios no monetarios MENORES de un tercero?',
        ['Nunca, están prohibidos en todos los casos', 'Cuando son razonables, proporcionados y no influyen en el comportamiento del asesor, informando al cliente', 'Solo si su valor supera los 1.000 euros anuales', 'Únicamente cuando el cliente es una contraparte elegible'],
        1,
        'Bajo MiFID II se admiten los beneficios no monetarios menores (p. ej., formación genérica o documentación de mercado) si son razonables, proporcionados, de escasa cuantía y no influyen en el comportamiento del asesor en perjuicio del cliente.',
    ),
    (
        'Según el Reglamento MiCA, ¿qué documento deben elaborar los emisores para la emisión y oferta pública de nuevos criptoactivos?',
        ['El Documento de Datos Fundamentales (KID)', 'El Documento de Datos Fundamentales para el Inversor (DFI)', 'El folleto de un fondo UCITS', 'El Libro Blanco (White Paper)'],
        3,
        'MiCA exige a los emisores publicar un Libro Blanco (White Paper) con la información sobre el criptoactivo, el proyecto y sus riesgos, además de cumplir obligaciones de transparencia con los clientes. Supervisan ESMA (AEVM) y la EBA (ABE).',
    ),
    (
        '¿Cuál de las siguientes afirmaciones describe correctamente la diferencia entre empresas Fintech e Insurtech?',
        ['Insurtech aplica la tecnología específicamente al sector asegurador, mientras que Fintech la aplica a los servicios financieros en general', 'Fintech solo opera con criptoactivos y las Insurtech solo con acciones', 'Las Insurtech están prohibidas en la Unión Europea', 'Fintech e Insurtech son términos idénticos y equivalentes'],
        0,
        'Las Fintech aplican la tecnología a los servicios financieros (roboadvisors, pagos, financiación alternativa, criptoactivos), mientras que las Insurtech son la aplicación de esa tecnología al ámbito específico de los seguros.',
    ),
    (
        'Dentro del paquete de Finanzas Digitales de la UE, ¿qué norma regula el pilar de la resiliencia operativa digital del sector financiero?',
        ['El Reglamento MiFIR', 'El Reglamento PRIIPs', 'El Reglamento DORA', 'El Reglamento EMIR'],
        2,
        'El paquete de Finanzas Digitales se apoya en cuatro pilares: estrategia de finanzas digitales, pagos minoristas, criptoactivos (MiCA) y resiliencia operativa digital, regulada por el Reglamento DORA.',
    ),
    (
        'En la diligencia debida normal de prevención del blanqueo, ¿a partir de qué porcentaje de participación se considera, con carácter general, que una persona física es titular real de una persona jurídica?',
        ['Más del 10 % del capital o los derechos de voto', 'Más del 25 % del capital o los derechos de voto', 'Más del 50 % del capital o los derechos de voto', 'Más del 5 % del capital o los derechos de voto'],
        1,
        'La Ley 10/2010 considera titular real, con carácter general, a la persona física que posee o controla, directa o indirectamente, más del 25 % del capital o de los derechos de voto de una persona jurídica.',
    ),
]

APUNTES = '### M9: Legislación, Normativa y Ética\n\nEl cumplimiento de las directivas europeas y el código de conducta ético es el pilar de la confianza de los clientes en la profesión financiera.\n\n#### 1. Directiva MiFID II (Markets in Financial Instruments Directive II)\nEsta directiva europea tiene como objetivo mejorar la protección del inversor minorista y la transparencia del mercado:\n1. **Clasificación de Clientes**:\n   - *Cliente Minorista*: Máximo nivel de protección regulatorio.\n   - *Cliente Profesional*: Entidades financieras o grandes empresas. Los minoristas pueden solicitar ser clasificados como profesionales si cumplen al menos 2 de los 3 criterios (10 operaciones significativas por trimestre, cartera > 500.000 €, o 1 año de experiencia profesional en finanzas).\n   - *Contraparte Elegible*: Menor nivel de protección (bancos, fondos).\n2. **Evaluación de Idoneidad vs Conveniencia**:\n   - **Test de Idoneidad**: Obligatorio en asesoramiento o gestión discrecional de carteras. Evalúa conocimientos y experiencia, situación financiera (capacidad de soportar pérdidas) y objetivos de inversión (tolerancia al riesgo).\n   - **Test de Conveniencia**: Obligatorio en la mera comercialización de productos complejos. Solo evalúa conocimientos y experiencia.\n3. **Incentivos (Retrocesiones)**: El asesoramiento independiente prohíbe retener retrocesiones de gestoras, debiendo transferirse al cliente o facturar solo por honorarios.\n\n#### 2. Prevención del Blanqueo de Capitales y Financiación del Terrorismo\nLas entidades financieras y asesores actúan como sujetos obligados bajo la Ley 10/2010. Sus deberes clave ante el SEPBLAC (Servicio Ejecutivo de la Comisión de Prevención del Blanqueo de Capitales) incluyen:\n- **Diligencia Debida**: Identificar formalmente a los clientes y conocer el titular real de los fondos ( KYC - Know Your Customer).\n- **Comunicación**: Declarar mensualmente operaciones con determinados países o importes y alertar de inmediato al SEPBLAC sobre cualquier indicio o sospecha de blanqueo.\n- **Abstención**: Abstenerse de ejecutar cualquier operación sospechosa hasta realizar la comunicación.\n- **Conservación**: Guardar copias de los documentos de identificación y registros durante un plazo mínimo de 10 años.\n\n#### 3. Código Ético de EFPA España\nEstablece los principios que deben guiar la conducta de un Asesor Financiero Europeo (EFA):\n- *Primacía del interés del cliente*: El interés del cliente se sitúa siempre por encima del de la entidad o el asesor.\n- *Integridad y Honestidad*: Actuar con buena fe e imparcialidad.\n- *Confidencialidad*: Secreto profesional absoluto, salvo deber de cooperar judicialmente.\n- *Conflictos de interés*: Revelar por escrito cualquier conflicto de interés inevitable antes de recomendar un producto.\n\n#### 4. Objetivos y ámbito de MiFID II. Servicios de inversión\n- **Objetivos**: reforzar la protección del inversor, aumentar la transparencia y la integridad de los mercados y armonizar la normativa en la UE. Se completa con el Reglamento MiFIR (UE 600/2014).\n- **Servicios de inversión**: recepción y transmisión de órdenes; ejecución de órdenes por cuenta de clientes; negociación por cuenta propia; gestión discrecional de carteras; asesoramiento en materia de inversión; aseguramiento y colocación de instrumentos financieros.\n- **Servicios auxiliares**: custodia y administración de instrumentos, concesión de créditos para operar, informes de inversión, servicios de cambio de divisas ligados a la inversión.\n- **Empresas de servicios de inversión (ESI)** en España: Sociedades de Valores (por cuenta propia y ajena), Agencias de Valores (solo por cuenta ajena), Sociedades Gestoras de Carteras y Empresas de Asesoramiento Financiero (EAF, solo asesoramiento).\n- Marco nacional: **Ley 6/2023** de los Mercados de Valores y de los Servicios de Inversión.\n\n#### 5. Asesoramiento independiente vs no independiente\n- **Independiente**: evalúa una gama amplia y diversificada de productos de distintos emisores; NO puede percibir ni retener incentivos (retrocesiones) de terceros; solo cobra honorarios del cliente.\n- **No independiente**: puede recomendar productos propios o de un número limitado de emisores y percibir incentivos, siempre que se informe al cliente y el incentivo aumente la calidad del servicio.\n\n#### 6. Idoneidad, conveniencia y solo ejecución\n- **Test de idoneidad**: asesoramiento y gestión de carteras. Evalúa tres bloques: conocimientos y experiencia; situación financiera y capacidad de soportar pérdidas; y objetivos de inversión, horizonte y tolerancia al riesgo. Desde 2022 incorpora las **preferencias de sostenibilidad (ASG)**. Se entrega una **declaración de idoneidad** al minorista.\n- **Test de conveniencia**: resto de servicios (comercialización o venta) cuando el producto es **complejo**. Solo evalúa conocimientos y experiencia. Si el resultado es no conveniente, se advierte al cliente, que puede seguir adelante.\n- **Solo ejecución (execution only)**: sin evaluación; solo posible con instrumentos **no complejos**, a iniciativa del cliente y advirtiéndole de que no se valora la conveniencia.\n- **Complejos vs no complejos**: no complejos (acciones cotizadas, bonos sencillos, fondos UCITS); complejos (derivados, estructurados, CFD, fondos no UCITS).\n\n#### 7. Incentivos (inducements)\n- Regla general: los incentivos de terceros solo se admiten si **aumentan la calidad del servicio** al cliente y no perjudican su interés, con obligación de informar.\n- En **asesoramiento independiente** y en **gestión de carteras**: prohibición de retener incentivos monetarios; deben devolverse al cliente.\n- **Beneficios no monetarios menores**: admisibles si son razonables, proporcionados y no influyen en el comportamiento del asesor (p. ej., formación genérica o documentación de mercado).\n\n#### 8. Información al cliente y mejor ejecución\n- **Información precontractual**: sobre la entidad, los servicios, la naturaleza y riesgos de los instrumentos, los costes y gastos agregados y los conflictos de interés. Clara, imparcial y no engañosa.\n- **Best execution (mejor ejecución)**: obligación de obtener el mejor resultado posible para el cliente considerando precio, costes, rapidez, probabilidad de ejecución y liquidación; se formaliza en una política de ejecución de órdenes.\n- **Conservación de registros**: mínimo 5 años (ampliable a 7 por la CNMV), incluidas grabaciones telefónicas.\n\n#### 9. Gobernanza de productos (product governance)\n- Fabricante y distribuidor definen un **mercado objetivo (target market) positivo**: tipo de cliente al que va dirigido el producto por sus necesidades, conocimientos, situación y tolerancia al riesgo.\n- **Mercado objetivo negativo**: grupo de clientes para el que el producto NO es adecuado y a los que se desaconseja la venta.\n\n#### 10. PRIIPs y documentos informativos\n- **Reglamento PRIIPs (UE 1286/2014)**: exige un **Documento de Datos Fundamentales (KID / DFI)** para productos empaquetados minoristas y productos basados en seguros. Resume el objetivo, los riesgos (indicador de riesgo), los escenarios de rentabilidad, los costes y el horizonte recomendado.\n- Los fondos **UCITS** entregan su propio Documento de Datos Fundamentales para el Inversor (DFI/KIID).\n\n#### 11. Abuso de mercado (MAR)\n- **Reglamento (UE) 596/2014 (MAR)**. Conductas prohibidas: operaciones con información privilegiada, comunicación ilícita de información privilegiada y manipulación de mercado.\n- **Información privilegiada**: concreta, no pública, referida a emisores o instrumentos, que de hacerse pública influiría de forma apreciable en la cotización.\n- Los emisores deben publicar la información privilegiada tan pronto como sea posible (salvo diferimiento legítimo) y llevar **listas de iniciados**.\n- Supervisan la **CNMV** (nacional) y **ESMA** (europea).\n\n#### 12. Prevención del blanqueo (ampliación)\n- **Diligencia debida normal**: identificación formal del cliente, identificación del **titular real** (persona física que, en general, controla más del 25 %), propósito e índole de la relación y seguimiento continuo.\n- **Diligencia simplificada**: clientes o productos de bajo riesgo (p. ej., entidades de crédito de la UE, organismos públicos).\n- **Diligencia reforzada**: situaciones de mayor riesgo, en particular las **personas con responsabilidad pública (PRP/PEP)** y sus allegados.\n- Organismos: **SEPBLAC** (unidad de inteligencia financiera de España) y **GAFI** (FATF) en el ámbito internacional.\n\n#### 13. Protección de datos (RGPD y AEPD)\n- **Reglamento (UE) 2016/679 (RGPD)**. Principios: licitud, lealtad y transparencia; limitación de la finalidad; **minimización de datos**; exactitud; limitación del plazo de conservación; integridad y confidencialidad; y responsabilidad proactiva.\n- **Derechos del interesado**: acceso, rectificación, **supresión (derecho al olvido)**, oposición, limitación del tratamiento y portabilidad.\n- Autoridad de control en España: **Agencia Española de Protección de Datos (AEPD)**.\n\n#### 14. Finanzas digitales y MiCA\n- El **paquete de Finanzas Digitales** de la Comisión Europea se apoya en cuatro pilares: estrategia de finanzas digitales, pagos minoristas, criptoactivos (MiCA) y resiliencia operativa digital (DORA).\n- **Reglamento MiCA (UE 2023/1114)**: regula el mercado de criptoactivos. Tipologías: **fichas referenciadas a activos (ART)**, referenciadas a una cesta de activos o monedas; **fichas de dinero electrónico (EMT)**, referenciadas a una sola moneda oficial; y demás criptoactivos (**fichas de consumo o utility tokens**).\n- Servicios sobre criptoactivos: custodia, gestión de plataformas de negociación, canje, ejecución de órdenes, colocación, asesoramiento, gestión de carteras y transferencia. Exigen el **Libro Blanco (White Paper)** y obligaciones de transparencia.\n- Supervisan **ESMA (AEVM)** y la **Autoridad Bancaria Europea (ABE / EBA)**.\n- **Fintech**: empresas que aplican tecnología a servicios financieros (roboadvisors, pagos, financiación alternativa, criptoactivos). **Insurtech**: aplicación de tecnología al sector asegurador.\n\n#### 15. Distribución de seguros (IDD) y sostenibilidad (SFDR)\n- **Directiva de Distribución de Seguros (IDD)**: normas de conducta, transparencia y evaluación de exigencias y necesidades del cliente en la venta de seguros, especialmente los productos de inversión basados en seguros.\n- **Reglamento SFDR (UE 2019/2088)**: obliga a los participantes en los mercados y asesores a divulgar cómo integran los riesgos de sostenibilidad y las principales incidencias adversas. Clasifica los productos en artículo 6 (sin rasgos ASG), artículo 8 (promueven características ASG) y artículo 9 (objetivo de inversión sostenible).\n\n#### 16. Código Ético de EFPA (ampliación)\nPrincipios rectores: **integridad**, **competencia y diligencia profesional**, **confidencialidad**, **profesionalidad**, **objetividad y gestión de conflictos de interés** y **primacía del interés del cliente**. Obliga además a la **formación continua** y a actuar conforme a la legalidad vigente.\n\n#### 17. Reglas mnemotécnicas para no confundir conceptos\n\n**A) Idoneidad vs Conveniencia vs Solo ejecución** — la clave está en QUÉ servicio se presta:\n- **Idoneidad = "A-Ge"** (**A**sesoramiento y **Ge**stión de carteras). Son los dos únicos servicios en los que el profesional decide o recomienda POR el cliente, así que necesita conocerlo a fondo. Evalúa **3 bloques** (recuérdalos como **"C-S-O"**): **C**onocimientos y experiencia, **S**ituación financiera (capacidad de soportar pérdidas) y **O**bjetivos (horizonte y tolerancia al riesgo).\n- **Conveniencia = el resto de servicios con producto complejo**. El cliente decide, pero el producto es complejo, así que solo se comprueba **1 bloque**: conocimientos y experiencia. Mnemotecnia: *conveniencia = solo "Conoces el producto"*.\n- **Solo ejecución = 0 evaluaciones**. Regla **"N-I-A"**: producto **N**o complejo + **I**niciativa del cliente + **A**dvertencia de que no se evalúa. Si falta cualquiera de las tres, NO hay solo ejecución.\n- Intuición del "embudo de protección": cuanto más decide el profesional por el cliente, más información hay que pedirle. Asesoro/gestiono -> lo sé casi todo (idoneidad). Solo le vendo un complejo -> compruebo que sabe (conveniencia). Solo ejecuto lo que me pide -> no compruebo nada (solo ejecución).\n\n**B) Clasificación de clientes (de MÁS a MENOS protección):** **Minorista > Profesional > Contraparte elegible**. Mnemotecnia: *"el que Menos sabe, Más se protege"*. El minorista es el "novato" (máxima protección); la contraparte elegible es el "experto institucional" (mínima protección). Cuidado: la protección va al REVÉS que el conocimiento.\n\n**C) Diligencia debida en blanqueo (3 niveles):** *"Simple para lo Seguro, Reforzada para lo Peligroso"*.\n- **Simplificada** -> bajo riesgo: entidades de crédito de la UE supervisadas, organismos y sociedades cotizadas.\n- **Normal** -> caso general: identificar cliente + titular real (>25 %) + propósito + seguimiento.\n- **Reforzada** -> alto riesgo: **PRP/PEP** (personas con responsabilidad pública) y allegados, banca corresponsal transfronteriza, países de alto riesgo. Regla de examen: *si aparece "PRP", "político" o "paraíso fiscal" -> diligencia REFORZADA*.\n\n**D) Tipologías de MiCA:** *"ART = cesta (Alto surtido), EMT = una sola moneda (E de Euro), Utility = ni una ni otra"*.\n- **ART** (asset-referenced token / ficha referenciada a activos): se referencia a una **cesta** de varios activos, monedas o materias primas.\n- **EMT** (electronic money token / ficha de dinero electrónico): se referencia a **una única** moneda oficial (p. ej., un euro). Piensa "E de EMT = Euro único".\n- **Utility token** (ficha de consumo): da acceso a un bien o servicio; no busca estabilidad de valor.\n\n**E) SFDR (colores del semáforo de sostenibilidad):** *"6 = gris, 8 = verde claro, 9 = verde oscuro"*.\n- **Artículo 6**: producto SIN rasgos ASG (por defecto).\n- **Artículo 8** ("light green"): **promueve** características ambientales o sociales.\n- **Artículo 9** ("dark green"): tiene como **objetivo** la inversión sostenible. Cuanto mayor el número, mayor la ambición ASG.\n\n#### 18. Casos prácticos resueltos\n\n**Caso 1 — ¿Qué test procede en cada servicio?**\nUn cliente minorista acude a su banco en tres situaciones distintas:\n1. Pide *consejo* sobre en qué fondo invertir sus ahorros -> hay **asesoramiento** -> **test de idoneidad** (C-S-O) y entrega de **declaración de idoneidad**.\n2. Por su cuenta quiere comprar un *fondo estructurado (complejo)*, sin pedir consejo -> **test de conveniencia** (solo conocimientos y experiencia). Si sale "no conveniente", se le advierte pero puede seguir.\n3. Por iniciativa propia ordena comprar *acciones cotizadas de Iberdrola* (no complejo) -> **solo ejecución**: sin evaluación, solo advertencia de que no se valora la conveniencia.\n*Error típico:* creer que comprar acciones "siempre exige test". No: si es a iniciativa del cliente y el producto es no complejo, basta la solo ejecución.\n\n**Caso 2 — Reclasificación de minorista a profesional.**\nUn ingeniero con cartera de 600.000 €, que realiza 12 operaciones significativas al trimestre pero sin experiencia laboral en el sector financiero, solicita ser tratado como profesional. ¿Puede? **Sí**: cumple 2 de los 3 criterios (cartera > 500.000 € y ≥ 10 operaciones/trimestre), y solo se exigen **2 de 3**. Al pasar a profesional PIERDE parte de la protección (menos información, no aplican ciertas advertencias). *Error típico:* pensar que hace falta una titulación en Economía: no es un criterio MiFID II.\n\n**Caso 3 — ¿Cuándo aplica diligencia reforzada?**\nCompara tres clientes nuevos: (a) un banco alemán supervisado por el BCE; (b) un asalariado que domicilia su nómina; (c) el alcalde de una gran ciudad (PRP). La diligencia **reforzada** solo procede con (c), por ser persona con responsabilidad pública. (a) es un supuesto de diligencia **simplificada** y (b) de diligencia **normal**. *Error típico:* aplicar diligencia reforzada "por importe alto" sin más: el detonante aquí es la condición de PRP.\n\n**Caso 4 — Incentivos y asesoramiento independiente.**\nUn asesor que se anuncia como **independiente** recibe una retrocesión anual de una gestora por colocar su fondo. ¿Es lícito retenerla? **No**: en asesoramiento independiente (y en gestión de carteras) está prohibido **retener** incentivos monetarios de terceros; deben devolverse íntegramente al cliente. Solo se permiten beneficios no monetarios menores (p. ej., formación genérica). Si fuera asesoramiento **no independiente**, podría percibir el incentivo informando al cliente y siempre que aumente la calidad del servicio. *Clave MiFID II:* "independiente" = amplia gama de productos + sin retrocesiones retenidas.\n\n**Caso 5 — Sostenibilidad en el test de idoneidad.**\nUn cliente de gestión de carteras manifiesta que quiere que sus inversiones tengan impacto ambiental. Desde 2022, MiFID II obliga a recoger sus **preferencias de sostenibilidad (ASG)** dentro del test de idoneidad y a alinear la cartera con ellas; el marco de divulgación es el Reglamento **SFDR**. Un producto que persigue como objetivo la inversión sostenible encajaría en el **artículo 9** de SFDR.\n\n#### 19. Errores frecuentes (evítalos)\n- Confundir **idoneidad** (asesoramiento/gestión, evalúa 3 bloques) con **conveniencia** (comercialización de complejos, evalúa 1 bloque). Es el error nº1 del examen.\n- Creer que el **minorista** tiene menos protección: es al contrario, tiene la **máxima**.\n- Pensar que la **solo ejecución** sirve para productos complejos: nunca; exige producto **no complejo**.\n- Decir que el asesor **independiente** no puede cobrar del cliente: sí puede y debe: solo cobra **honorarios del cliente**; lo prohibido es retener incentivos de terceros.\n- Aplicar **diligencia reforzada** por importe elevado sin más: el examen la asocia sobre todo a **PRP/PEP**, países de alto riesgo y banca corresponsal.\n- Confundir plazos: registros MiFID II = **5 años** (ampliable a 7); documentación de blanqueo = **10 años**.\n- Confundir **ART** (cesta de activos) con **EMT** (una sola moneda). "EMT = una moneda".\n- Asignar mal el supervisor: **CNMV/ESMA** para mercados y abuso de mercado; **SEPBLAC/GAFI** para blanqueo; **AEPD** para datos; **ESMA (AEVM) + EBA (ABE)** para MiCA.\n\n#### 20. Claves de examen (resumen rápido)\n- **Test de idoneidad** solo en **asesoramiento** y **gestión discrecional de carteras**; entrega **declaración de idoneidad** al minorista.\n- **Test de conveniencia** en comercialización de **productos complejos** sin asesoramiento.\n- **Solo ejecución**: no complejo + iniciativa del cliente + advertencia.\n- Protección: **Minorista > Profesional > Contraparte elegible**.\n- Minorista -> profesional: **2 de 3** criterios (10 operaciones/trimestre, cartera > 500.000 €, 1 año de experiencia profesional).\n- **Incentivos**: prohibida su retención en asesoramiento **independiente** y **gestión de carteras**.\n- **Registros**: 5 años MiFID II; **10 años** documentación de blanqueo (Ley 10/2010).\n- **Información privilegiada** (MAR): concreta + no pública + capacidad de influir apreciablemente en la cotización.\n- **RGPD**: principio de **minimización**; derechos ARSOPL (acceso, rectificación, supresión, oposición, limitación, portabilidad); autoridad **AEPD**.\n- **MiCA**: ART (cesta), EMT (una moneda), utility (consumo); exige **Libro Blanco**; supervisan **ESMA + EBA**.\n- **SFDR**: art. 6 (sin ASG), art. 8 (promueve ASG), art. 9 (objetivo sostenible).\n- **PRIIPs**: **KID/DFI** para empaquetados y basados en seguros.\n- **Supervisores**: CNMV/ESMA (valores y abuso de mercado), SEPBLAC/GAFI (blanqueo), AEPD (datos).'
