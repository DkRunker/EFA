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

APUNTES = '### M6: Inversión Inmobiliaria\n\nLa inversión en bienes raíces es una de las clases de activos tradicionales. Presenta **baja liquidez** física, **altos costes de transacción** (impuestos, notaría, registro, intermediación), **elevados requerimientos de capital inicial**, posibilidad de **apalancamiento** vía deuda hipotecaria y cobertura histórica frente a la **inflación** (rentas y valores tienden a actualizarse con los precios). Es un mercado **cíclico** y con gestión activa (mantenimiento, morosidad, vacancia).\n\n#### 1. Inversión directa vs. inversión indirecta\n- **Directa**: adquisición física del inmueble. Ofrece control total (reformas, selección de inquilino, negociación de renta) pero exige mucho capital, soporta altos costes de transacción y tiene baja liquidez.\n- **Indirecta**: se invierte a través de vehículos (SOCIMIs/REITs, FII, SII, crowdfunding inmobiliario). Aporta **liquidez** (en los cotizados), **diversificación** inmediata, **menor capital** de entrada y **gestión profesional**, a cambio de comisiones y de menor control sobre los activos.\n\n#### 2. Clasificación de la inversión inmobiliaria\n- **Según el tipo de suelo**: urbano (edificable), urbanizable (pendiente de desarrollo) y rústico/no urbanizable.\n- **Según la actividad**: residencial (viviendas), oficinas, retail (centros comerciales y locales), logístico e industrial (naves), hotelero y otros usos alternativos (residencias, data centers, etc.). Cada segmento tiene su propio binomio rentabilidad-riesgo y su ciclicidad.\n\n#### 3. Rentabilidad y riesgo\nEl binomio rentabilidad-riesgo inmobiliario suele mostrar rentas relativamente estables pero fuerte sensibilidad al ciclo económico, a los tipos de interés y a la liquidez. Frente a la inversión financiera tradicional aporta descorrelación parcial y cobertura frente a la inflación, pero con menor liquidez y mayor coste de gestión.\n\n#### 4. Sostenibilidad (ESG) y tecnología\n- **Factores ESG**: la eficiencia energética y las certificaciones **LEED, BREEAM y WELL** mejoran la valoración de los activos y reducen su riesgo (menor obsolescencia, mejor demanda). La financiación verde (bonos verdes, hipotecas verdes) se vincula a estos estándares.\n- **Blockchain y tokenización**: los *smart contracts* automatizan y aportan seguridad a las transacciones; la **tokenización** de activos inmobiliarios fracciona la propiedad, mejorando la **liquidez** y la accesibilidad del mercado, aunque plantea retos regulatorios y de ciberseguridad.\n\n#### 5. Vehículos de inversión inmobiliaria\n**SOCIMIs (Sociedades Cotizadas de Inversión en el Mercado Inmobiliario)** — vehículos cotizados, equivalentes españoles a los **REITs** internacionales:\n- *Impuesto sobre Sociedades*: tributan al tipo del **0%** en el IS si cumplen los requisitos legales.\n- *Reparto obligatorio de dividendos* para mantener el régimen fiscal especial:\n  - Al menos el **80%** de los beneficios procedentes del arrendamiento de inmuebles.\n  - Al menos el **50%** de las plusvalías por venta de inmuebles (reinvirtiendo el resto).\n  - El **100%** de los beneficios procedentes de dividendos de otras SOCIMIs filiales.\n- *Gravamen especial del 19%*: la SOCIMI soporta un gravamen especial del 19% (art. 9.2 Ley 11/2009) sobre los dividendos distribuidos a socios con participación >= 5% cuando dichos dividendos estén exentos o gravados a menos del 10% en sede del perceptor (para evitar el arbitraje fiscal). Adicionalmente, la Ley 11/2021 introdujo un gravamen especial del 15% sobre los beneficios NO distribuidos.\n- *Rentabilidad por dividendo (Dividend Yield)*: dividendo por acción anual dividido por el precio de cotización.\n\n**FII (Fondos de Inversión Inmobiliaria) vs. SII (Sociedades de Inversión Inmobiliaria)**: son IIC de carácter **no financiero**.\n- El **FII** es un **patrimonio sin personalidad jurídica** formado por aportaciones de partícipes; la **SII** es una **sociedad anónima con personalidad jurídica** propia.\n- Los FII deben invertir al menos el **70%** (promedio anual de saldos mensuales de su activo, RD 1082/2012) en inmuebles urbanos destinados al **arrendamiento**, con coeficiente de liquidez mínimo y obligación de ofrecer liquidez (reembolsos) al menos una vez al año.\n- Intervienen la **sociedad gestora**, la **sociedad depositaria** y la **sociedad de tasación**; el **valor liquidativo** se calcula a partir de la tasación periódica del patrimonio.\n- Frente a las SOCIMIs, los FII/SII no cotizados ofrecen menor liquidez.\n\n**Sociedades de arrendamiento de vivienda**: régimen especial del IS con bonificaciones en la cuota por el arrendamiento de viviendas, sujeto a requisitos de número y periodo de mantenimiento.\n\n**Crowdfunding inmobiliario**: plataformas de financiación participativa que permiten coinvertir en proyectos concretos con tickets reducidos; mayor accesibilidad pero riesgo de proyecto y liquidez limitada.\n\n#### 6. Métodos oficiales de valoración inmobiliaria\n1. **Método de Comparación (mercado)**: valor de mercado a partir de transacciones recientes de inmuebles homólogos, ajustando diferencias físicas, de superficie, ubicación y temporales.\n2. **Método de Capitalización de Rentas**: estima el valor como el valor actual de las rentas netas futuras de la explotación:\n   $$\\text{Valor} = \\frac{\\text{Renta Neta Anual}}{\\text{Cap Rate (Tasa de Capitalización)}}$$\n   Una menor tasa de capitalización (mayor demanda/menor riesgo) implica un mayor valor del inmueble.\n3. **Método de Coste (Reposición)**: coste de adquirir el suelo y construir de nuevo un inmueble equivalente, menos la depreciación por antigüedad y estado. Es el método por defecto cuando no hay comparables o el inmueble es especial/obra nueva.\n4. **Método Residual (del suelo)**: obtiene el valor del suelo deduciendo del valor de la promoción terminada todos los costes de construcción, gastos, impuestos y el beneficio del promotor. Puede ser **estático** (sin descontar en el tiempo) o **dinámico** (descontando flujos). Es el método preferente para valorar solares y suelo en desarrollo.\n\n#### 7. Ratios y métricas financieras inmobiliarias\n- **Capitalization Rate (Cap Rate)**: rentabilidad neta anual del activo. Relaciona el ingreso operativo neto (NOI) con el valor/precio del inmueble:\n  $$\\text{Cap Rate} = \\frac{\\text{NOI (Ingreso Operativo Neto)}}{\\text{Valor del inmueble}}$$\n  El **NOI** es la renta bruta menos los gastos de explotación (comunidad, seguros, IBI, mantenimiento, vacancia), **sin** incluir la cuota de la hipoteca ni la amortización de deuda.\n- **Loan-to-Value (LTV)**: importe del préstamo hipotecario sobre el valor de tasación. Mide el apalancamiento; por encima del **80%** implica mayor riesgo y peores condiciones de financiación.\n- **Rentabilidad bruta por alquiler**: renta anual bruta dividida por el precio de compra.\n- **Rentabilidad neta por alquiler**: (renta anual menos gastos) dividida por la inversión total (precio más costes de adquisición).\n- **Cash-on-cash return**: flujo de caja anual antes de impuestos dividido por el **capital propio (equity)** efectivamente aportado. Refleja el efecto del apalancamiento sobre el retorno del inversor:\n  $$\\text{Cash-on-Cash} = \\frac{\\text{Flujo de caja anual antes de impuestos}}{\\text{Capital propio invertido}}$$\n\n#### 8. Fiscalidad inmobiliaria\n- **Compra**:\n  - *Vivienda nueva* (primera transmisión del promotor): **IVA** (10% en vivienda; 21% en locales, garajes independientes y suelo) más **AJD** (Actos Jurídicos Documentados).\n  - *Vivienda de segunda mano*: **ITP** (Transmisiones Patrimoniales Onerosas), a un tipo variable fijado por cada Comunidad Autónoma (habitualmente entre el 6% y el 10%).\n- **Tenencia**: **IBI** (Impuesto sobre Bienes Inmuebles), tributo local anual sobre el valor catastral.\n- **Alquiler (IRPF)**: los rendimientos del capital inmobiliario se integran en la base general. Se deducen los gastos necesarios (intereses, IBI, comunidad, seguros, amortización, reparaciones). Sobre el **rendimiento neto positivo** del arrendamiento de **vivienda** se aplica una **reducción** (con carácter general del **60%**), que incentiva el alquiler residencial.\n- **Venta**: la **ganancia patrimonial** (diferencia entre valor de transmisión y de adquisición) tributa en la **base del ahorro** del IRPF por tramos progresivos (19%–28%).\n- **Plusvalía municipal (IIVTNU)**: Impuesto local sobre el Incremento de Valor de los Terrenos de Naturaleza Urbana; grava el incremento de valor del suelo urbano puesto de manifiesto en la transmisión.\n\n#### 9. Productos hipotecarios y métodos de amortización\n- **Concesión**: el banco evalúa cuantía, edad del solicitante, historial y experiencia con productos de activo, tipo de actividad (cuenta propia/ajena) y capacidad de pago, mediante sistemas de **scoring**.\n- **Sistema francés**: **cuota (término amortizativo) constante**; al principio se paga más interés y menos capital, proporción que se invierte con el tiempo. Cuota:\n  $$a = C \\cdot \\frac{i}{1 - (1 + i)^{-n}}$$\n- **Sistema lineal (o de cuota de capital constante)**: la **amortización de capital es constante** cada periodo y la cuota total (capital más interés) **decrece** con el tiempo, al reducirse los intereses sobre el capital vivo.\n- **Hipotecas verdes**: financiación con condiciones preferentes (tipos, plazos) para inmuebles energéticamente eficientes o reformas sostenibles, vinculada a criterios ESG y a certificaciones energéticas, y relacionada con la emisión de bonos verdes por las entidades financieras.\n\n#### 10. Intuición de los conceptos clave\n- **Métodos de valoración**: *comparación* responde a «¿por cuánto se venden inmuebles similares?»; *capitalización* a «¿qué renta genera y a qué rentabilidad lo compraría el mercado?»; *coste* a «¿cuánto costaría construirlo de nuevo?»; *residual* a «¿cuánto vale el suelo según lo que puede promoverse en él?».\n- **Cap rate**: es la rentabilidad exigida por el mercado; equivale a descontar una renta perpetua. Cap rate **alto** significa activo **barato** y más riesgo; cap rate **bajo**, activo **caro** y menos riesgo. Valor y cap rate se mueven en sentido **inverso**.\n- **LTV**: qué parte del inmueble financia el banco. Más LTV = más apalancamiento = más riesgo y peores condiciones; a partir del **80%** se endurecen tipos y garantías.\n- **SOCIMI vs. FII**: la SOCIMI **cotiza** (líquida, IS al 0%, reparte al menos el 80% de las rentas de alquiler); el FII **no cotiza** (menos líquido, invierte al menos el 70% del activo en inmuebles de alquiler, valor liquidativo por tasación).\n- **Fiscalidad de un vistazo**: compra (IVA+AJD si es nueva / ITP si es usada), tenencia (IBI), alquiler (IRPF en base general, reducción del 60% en vivienda) y venta (ganancia patrimonial en base del ahorro + plusvalía municipal IIVTNU).\n\n#### 11. Ejemplos resueltos\n**Ejemplo 1 — Valoración por capitalización de rentas.** Un local produce una renta bruta anual de 24.000 € y soporta 4.000 € de gastos de explotación (IBI, comunidad, seguro, mantenimiento). El NOI = 24.000 − 4.000 = **20.000 €**. Con un cap rate de mercado del **5%**: Valor = Renta Neta Anual / Cap Rate = 20.000 / 0,05 = **400.000 €**. (Si el cap rate bajara al 4%, el valor subiría a 500.000 €: menor tasa → mayor valor.)\n\n**Ejemplo 2 — Cálculo del LTV.** Vivienda tasada en 250.000 € financiada con un préstamo de 200.000 €. LTV = 200.000 / 250.000 = **80%**. El inversor aporta el 20% restante (50.000 €) más los gastos de compra.\n\n**Ejemplo 3 — Rentabilidad bruta, neta y cash-on-cash.** Compra: precio 200.000 € + gastos de adquisición (ITP, notaría, registro) 20.000 € → inversión total **220.000 €**. Se financia con hipoteca de 160.000 € (LTV 80%), por lo que el **equity** aportado = 220.000 − 160.000 = **60.000 €**. Renta bruta anual 14.000 €; gastos de explotación 3.000 € → NOI = **11.000 €**.\n  - Rentabilidad **bruta** = 14.000 / 200.000 = **7%**.\n  - Rentabilidad **neta** = 11.000 / 220.000 = **5%**.\n  - Con un servicio de la deuda (cuota de hipoteca) de 7.400 €/año, el flujo de caja antes de impuestos = 11.000 − 7.400 = 3.600 €. **Cash-on-cash** = 3.600 / 60.000 = **6%**. El apalancamiento eleva el retorno sobre el capital propio por encima de la rentabilidad neta.\n\n**Ejemplo 4 — Ganancia patrimonial en la venta (IRPF).** Inmueble adquirido por 200.000 € con 20.000 € de gastos e impuestos deducibles → valor de adquisición **220.000 €**. Se vende por 300.000 € con 10.000 € de gastos de venta → valor de transmisión **290.000 €**. Ganancia patrimonial = 290.000 − 220.000 = **70.000 €**, que tributa en la **base del ahorro** por tramos (a modo ilustrativo: 6.000 × 19% + 44.000 × 21% + 20.000 × 23% = 1.140 + 9.240 + 4.600 = **14.980 €** de cuota; tipo medio ≈ 21,4%). Además se liquida la plusvalía municipal (IIVTNU) sobre el suelo.\n\n#### 12. Errores frecuentes\n- Confundir el **80%** de reparto de dividendos de las **SOCIMI** con el **70%** de inversión mínima en inmuebles de los **FII** (RD 1082/2012): son magnitudes y vehículos distintos.\n- Incluir la **cuota de la hipoteca** en el cálculo del **NOI**: el NOI es *antes* de deuda; el servicio de la deuda solo entra en el flujo de caja y en el cash-on-cash.\n- Suponer que cap rate y valor se mueven en el mismo sentido: la relación es **inversa** (menor cap rate → mayor valor).\n- Aplicar **IVA** a la vivienda de **segunda mano**: la usada tributa por **ITP**; solo la primera entrega del promotor lleva IVA (10%) + AJD.\n- Calcular el **cash-on-cash** sobre la inversión total en lugar de sobre el **capital propio (equity)** realmente aportado.\n- Creer que la reducción del **60%** se aplica a cualquier alquiler: solo al de **vivienda** y sobre el rendimiento neto **positivo**.\n\n#### 13. Claves de examen\n- Memoriza la fórmula **Valor = Renta Neta Anual / Cap Rate** y su despeje (Cap Rate = NOI / Valor).\n- **SOCIMI**: IS 0%, cotiza, reparte al menos el 80% de las rentas de alquiler, el 50% de las plusvalías y el 100% de los dividendos de filiales; gravamen especial del 19% (Ley 11/2009) a socios con participación >= 5% infragravados, y del 15% (Ley 11/2021) sobre beneficios no distribuidos.\n- **FII**: IIC no financiera, al menos el 70% del activo en inmuebles urbanos en alquiler, liquidez al menos anual; la **SII** es una sociedad anónima con personalidad jurídica.\n- **Sistema francés**: cuota constante. **Sistema lineal**: amortización de capital constante y cuota total decreciente.\n- **Método residual** para suelo y solares; **coste de reposición** ante falta de comparables u obra nueva especial.\n- Distingue la tributación por fases: compra (IVA+AJD / ITP), tenencia (IBI), alquiler (IRPF, reducción 60% vivienda) y venta (ganancia patrimonial en base del ahorro + IIVTNU).'
