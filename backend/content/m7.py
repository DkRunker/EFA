# Módulo M7 — Crédito y Financiación
# PREGUNTAS: cada tupla es (enunciado, [4 opciones], indice_respuesta_correcta, explicacion)
# Ampliar apuntes y preguntas conforme al temario oficial EFPA. NO borrar términos ya existentes.
NOMBRE = 'Crédito y Financiación'

PREGUNTAS = [
    (
        '¿Qué coste financiero se incluye obligatoriamente en el cálculo de la TAE de una hipoteca pero no en el TIN?',
        ['Comisiones de apertura y gastos de tasación/seguros vinculados', 'Los intereses ordinarios', 'La amortización del capital', 'La prima por pago anticipado'],
        0,
        'La TAE (Tasa Anual Equivalente) refleja el coste efectivo total del préstamo, incluyendo comisiones obligatorias y seguros vinculados, a diferencia del TIN.',
    ),
    (
        'Si solicitamos un préstamo con sistema de amortización francés (cuota constante), ¿cómo evoluciona la proporción de intereses y capital dentro de la cuota?',
        ['Los intereses decrecen a lo largo del tiempo y el capital amortizado crece', 'El capital amortizado decrece y los intereses crecen', 'La proporción de intereses y capital se mantiene constante en todas las cuotas', 'Los intereses se pagan íntegramente en la última cuota junto al vencimiento'],
        0,
        'Al amortizarse capital mensualmente, la base sobre la que se calculan los intereses es menor en cada periodo, aumentando el capital amortizado neto en cada cuota.',
    ),
    (
        'Un préstamo hipotecario con interés variable referenciado al Euríbor a 12 meses tiene una cláusula suelo del 1.5%. Si el Euríbor cotiza al -0.5% y el diferencial es del 1.0%, ¿cuál será el tipo de interés aplicado al cliente?',
        ['1.50% debido a la cláusula suelo', '0.50% neto', '1.00% debido al Euríbor negativo', '2.00% sumando el valor absoluto del Euríbor'],
        0,
        'La suma de Euríbor y diferencial es: -0.5% + 1.0% = 0.50%. Dado que el contrato tiene una cláusula suelo del 1.50%, el tipo aplicado es este límite mínimo.',
    ),
    (
        'Utilizando el sistema de amortización francés, ¿cómo se calcula la cuota de intereses de un periodo t?',
        ['Multiplicando el capital vivo pendiente al final del periodo anterior por el tipo de interés del periodo', 'Dividiendo el TIN anual entre el número de años pendientes de pago', 'Multiplicando la cuota constante mensual por la Beta de la hipoteca', 'Es un valor fijo idéntico al capital principal amortizado en el primer mes'],
        0,
        'Intereses del periodo t = Capital pendiente periodo (t-1) * i. La cuota de amortización de principal de ese mes es la cuota total menos ese interés.',
    ),
    (
        'Bajo la regulación de la Ley de Contratos de Crédito Inmobiliario (LCCI), ¿qué plazo mínimo de antelación exige la ley para que el cliente visite al notario a firmar el acta previa?',
        ['Como mínimo 24 horas antes de la firma de la escritura del préstamo hipotecario', 'Al menos 10 días antes del inicio de la campaña comercial del banco', '3 días naturales posteriores a la tasación del inmueble', 'No es obligatoria la visita al notario antes del día de la firma oficial de la escritura'],
        0,
        'La LCCI exige que el prestatario comparezca ante el notario elegido al menos 24 horas antes de la firma para recibir asesoramiento gratuito sobre las cláusulas y firmar el acta previa.',
    ),
    (
        '¿Cuál es el tipo de interés de demora máximo legal que puede aplicar una entidad bancaria a un préstamo hipotecario residencial según la LCCI?',
        ['El interés ordinario (TIN) más un máximo de 3 puntos porcentuales', 'Un interés máximo del 25% anual fijado por la ley de usura', 'El triple del interés legal del dinero aplicable en ese ejercicio fiscal', 'No hay límite legal, se rige por lo firmado en las cláusulas abusivas del contrato'],
        0,
        'La LCCI limita los intereses de demora: serán el interés nominal ordinario más un máximo del 3% (3 puntos porcentuales), no permitiéndose pacto en contrario.',
    ),
    (
        'Si un banco ofrece un TIN del 4.0% con liquidación de intereses trimestral (m=4), ¿cuál será la TAE equivalente de la hipoteca?',
        ['4.06%', '4.00%', '4.12%', '3.98%'],
        0,
        'TAE = (1 + 0.04/4)^4 - 1 = (1.01)^4 - 1 = 1.040604 - 1 = 4.06%.',
    ),
    (
        'En un préstamo de amortización de sistema Americano, ¿cómo se distribuyen las cuotas?',
        ['Cuotas de solo intereses periódicos y devolución del 100% del principal en el último periodo', 'Cuotas constantes decrecientes compuestas únicamente de principal amortizado', 'Cuotas crecientes donde se amortiza principal en todos los periodos y los intereses se capitalizan', 'No existen cuotas periódicas, se liquida capital e intereses en un pago a los 10 años de carencia'],
        0,
        'El método americano carece de amortización ordinaria de principal durante la vida del préstamo; el prestatario paga cuotas de intereses y devuelve el principal de golpe al final.',
    ),
    (
        'En la concesión de un préstamo con sistema de amortización americano, ¿qué suele constituir el deudor de forma paralela para garantizar la devolución del principal al vencimiento?',
        ['Un fondo de amortización (sinking fund) invertido a una tasa de interés capitalizable', 'Un seguro de vida de capital decreciente vinculado al saldo vivo de la cuenta corriente', 'Una hipoteca inversa sobre una vivienda de protección oficial libre de cargas', 'Una fianza solidaria ilimitada emitida por el banco central del país emisor'],
        0,
        'El sinking fund permite al prestatario acumular de forma progresiva el capital necesario para liquidar la amortización íntegra de principal al vencimiento.',
    ),
    (
        'Bajo las directrices de la LCCI, ¿quién debe abonar por ley los gastos de tasación del inmueble en un préstamo hipotecario residencial?',
        ['El cliente prestatario (tomador del préstamo)', 'El banco prestamista en su totalidad y de forma obligatoria', 'Se distribuye al 50% entre el cliente y la entidad financiera otorgante', 'Queda exento de pago si se firma un seguro de amortización de capital constante'],
        0,
        'La Ley 5/2019 (LCCI) asigna al cliente (prestatario) únicamente los gastos de tasación y las copias de escrituras que solicite, asumiendo el banco los gastos de notaría, registro, gestoría e IAJD.',
    ),
    (
        'En relación con los préstamos hipotecarios a tipo de interés variable, ¿qué es el diferencial aplicado?',
        ['El margen porcentual fijo que se suma al índice de referencia (ej. Euríbor) para obtener el tipo de interés nominal aplicado', 'La comisión anual de gestión cobrada por la entidad por administrar la cartera hipotecaria', 'El coste total de las primas de los seguros vinculados a la hipoteca expresadas en porcentaje', 'La penalización cobrada al cliente por realizar amortizaciones anticipadas parciales'],
        0,
        'El tipo de interés final aplicado en préstamos variables se compone de la suma del índice de referencia (variable) y el diferencial pactado (fijo).',
    ),
    (
        'En un préstamo personal no hipotecario, ¿con qué tipo de garantía responde principalmente el deudor en caso de impago?',
        ['Garantía personal universal e ilimitada (responde con todos sus bienes presentes y futuros)', 'Únicamente con el bien adquirido mediante la financiación obtenida del préstamo', 'Con la vivienda habitual declarada como bien inembargable de antemano', 'Con un aval bancario obligatorio equivalente al 100% de los intereses futuros devengados'],
        0,
        'Los préstamos personales se otorgan con garantía personal según el artículo 1911 del Código Civil (responsabilidad patrimonial universal).',
    ),
    (
        'Al comparar dos préstamos bancarios de igual importe y plazo, ¿por qué el préstamo con liquidación mensual de intereses tiene una TAE superior que el de liquidación trimestral si ambos tienen el mismo TIN?',
        ['Porque la frecuencia de liquidación mensual incrementa el efecto de capitalización compuesta intrayear de los intereses cobrados', 'Porque la comisión de apertura se duplica automáticamente en préstamos mensuales', 'Porque la liquidación mensual exige contratar un seguro de vida obligatorio decreciente', 'Es incorrecto, la liquidación trimestral siempre genera una TAE superior al devengar antes'],
        0,
        'A mayor frecuencia de capitalización de flujos de pago (mensual vs trimestral), mayor es la reinversión y por ende mayor la TAE (Tasa Anual Equivalente).',
    ),
    (
        'En el sistema de amortización italiano o lineal (cuota de capital constante), ¿cómo evoluciona la cuota total (término amortizativo) a lo largo de la vida del préstamo?',
        ['Es decreciente, porque se amortiza el mismo principal cada periodo y los intereses disminuyen al bajar el capital vivo', 'Es constante en todos los periodos, igual que en el sistema francés', 'Es creciente, porque los intereses se capitalizan y se suman al principal', 'Es cero hasta el vencimiento, donde se paga todo el capital de una vez'],
        0,
        'En el sistema lineal se amortiza el mismo importe de principal ($C_0/n$) en cada periodo. Como el capital vivo decrece linealmente, los intereses también decrecen y la cuota total resulta decreciente. Se paga más al principio que en el sistema francés.',
    ),
    (
        'Una vivienda se tasa en 200.000 EUR y el banco concede un préstamo hipotecario de 150.000 EUR. ¿Cuál es el Loan to Value (LTV) de la operación?',
        ['75%', '133%', '50.000 EUR', '80%, el máximo legal'],
        0,
        'El LTV = Importe del préstamo / Valor de tasación = 150.000 / 200.000 = 0,75 = 75%. Un LTV más bajo implica menor riesgo para la entidad, ya que la garantía cubre holgadamente el importe prestado.',
    ),
    (
        'Un cliente tiene ingresos netos mensuales de 2.000 EUR y las cuotas de sus préstamos suman 800 EUR al mes. Según el criterio prudencial habitual, ¿es asumible su nivel de endeudamiento?',
        ['No es recomendable: su ratio de esfuerzo es del 40%, superior al límite prudencial del 30-35% de los ingresos netos', 'Sí, porque cualquier ratio inferior al 50% se considera siempre asumible', 'No se puede calcular sin conocer el valor de tasación del inmueble', 'Sí, porque las cuotas son inferiores a los ingresos netos totales'],
        0,
        'El ratio de esfuerzo = Cuotas / Ingresos netos = 800 / 2.000 = 40%. Al superar el umbral prudencial del 30-35%, la entidad consideraría el endeudamiento excesivo respecto a su capacidad de pago.',
    ),
    (
        'Un inversor financia un proyecto con deuda al 4% de coste y el proyecto rinde un 9%. ¿Qué efecto tiene el apalancamiento financiero sobre la rentabilidad de sus recursos propios?',
        ['Apalancamiento positivo: al superar la rentabilidad del activo (9%) al coste de la deuda (4%), aumenta la rentabilidad de los recursos propios (ROE)', 'Apalancamiento negativo: la deuda siempre reduce la rentabilidad final del inversor', 'Neutro: el apalancamiento no afecta a la rentabilidad de los fondos propios', 'Positivo solo si el coste de la deuda supera a la rentabilidad del activo'],
        0,
        'El apalancamiento es positivo cuando la rentabilidad del activo (9%) supera el coste de la deuda (4%). El diferencial favorable se traslada a los recursos propios, elevando el ROE por encima del ROA, aunque incrementando el riesgo financiero.',
    ),
    (
        'En una operación de crédito (línea o póliza de crédito), ¿sobre qué importe paga intereses el cliente?',
        ['Solo sobre el saldo efectivamente dispuesto, más una comisión de disponibilidad por la parte no dispuesta', 'Sobre el límite total concedido, se disponga o no de él', 'Sobre el doble del importe dispuesto en concepto de riesgo', 'No paga intereses, solo una comisión fija de apertura'],
        0,
        'A diferencia del préstamo (donde se entrega y se cobra interés por todo el capital), en el crédito el cliente dispone según necesidad y paga intereses solo por lo dispuesto, añadiéndose una comisión de disponibilidad sobre el saldo no utilizado.',
    ),
    (
        'Un préstamo tiene un TIN del 12% con liquidación mensual (m=12). ¿Cuál es su TAE?',
        ['12.00%', '12.36%', '12.68%', '13.00%'],
        2,
        'TAE = (1 + 0.12/12)^12 - 1 = (1.01)^12 - 1 = 1.12683 - 1 = 12.68%. La TAE supera al TIN por la capitalización compuesta intraanual.',
    ),
    (
        'Un préstamo por el sistema francés de 1.000 EUR a un tipo del 10% por periodo y 2 periodos. ¿Cuál es la cuota constante (término amortizativo)?',
        ['500.00 EUR', '576.19 EUR', '550.00 EUR', '605.00 EUR'],
        1,
        'C = C0·i/(1-(1+i)^-n) = 1.000·0,10/(1-(1,10)^-2) = 100/(1-0,82645) = 100/0,17355 = 576,19 EUR.',
    ),
    (
        'En un préstamo de 120.000 EUR por el sistema italiano (lineal) a 240 meses, ¿cuál es la cuota de amortización de principal (constante) de cada mes?',
        ['1.000 EUR', '250 EUR', '750 EUR', '500 EUR'],
        3,
        'En el sistema lineal se amortiza el mismo principal cada periodo: C0/n = 120.000/240 = 500 EUR. Los intereses decrecen al bajar el capital vivo, por lo que la cuota total es decreciente.',
    ),
    (
        'Se invierten 10.000 EUR a un tipo del 5% en capitalización simple durante 4 años. ¿Cuál es el capital final?',
        ['10.500 EUR', '11.000 EUR', '12.000 EUR', '12.155 EUR'],
        2,
        'En capitalización simple: Cn = C0·(1 + i·n) = 10.000·(1 + 0,05·4) = 10.000·1,20 = 12.000 EUR. Los intereses se calculan siempre sobre el capital inicial.',
    ),
    (
        'Se invierten 10.000 EUR a un tipo del 5% en capitalización compuesta durante 4 años. ¿Cuál es el capital final (aprox.)?',
        ['12.155 EUR', '12.000 EUR', '11.576 EUR', '12.500 EUR'],
        0,
        'En capitalización compuesta: Cn = C0·(1+i)^n = 10.000·(1,05)^4 = 10.000·1,21551 = 12.155 EUR. Supera al régimen simple (12.000) por el interés sobre interés.',
    ),
    (
        'Una vivienda se tasa en 300.000 EUR y el banco concede un préstamo de 240.000 EUR. ¿Cuál es el Loan to Value (LTV)?',
        ['60%', '75%', '125%', '80%'],
        3,
        'LTV = Importe del préstamo / Valor de tasación = 240.000 / 300.000 = 0,80 = 80%. Coincide con el límite habitual para vivienda habitual.',
    ),
    (
        'Un cliente tiene ingresos netos mensuales de 3.000 EUR y sus cuotas de deuda suman 750 EUR al mes. ¿Cómo valora su ratio de esfuerzo?',
        ['No es asumible: el ratio es del 40%, por encima del umbral prudencial', 'Es asumible: el ratio es del 25%, dentro del umbral prudencial del 30-35%', 'No es asumible: el ratio es del 33% y supera el máximo legal', 'Es asumible porque cualquier ratio inferior al 50% se admite siempre'],
        1,
        'Ratio de esfuerzo = Cuotas / Ingresos netos = 750 / 3.000 = 25%. Al estar por debajo del umbral prudencial del 30-35%, el endeudamiento se considera asumible.',
    ),
    (
        'Según la LCCI, ¿con qué antelación mínima debe entregarse al prestatario la Ficha Europea de Información Normalizada (FEIN) antes de la firma?',
        ['24 horas', '3 días naturales', '10 días', '1 mes'],
        2,
        'La LCCI exige entregar la FEIN (oferta vinculante) y la FiAE con al menos 10 días de antelación a la firma. La visita al notario para el acta previa es al menos 24 horas antes.',
    ),
    (
        'Una inversión de 200.000 EUR se financia con 50.000 EUR de recursos propios y 150.000 EUR de deuda al 4%. El activo rinde un 8%. ¿Cuál es el ROE (rentabilidad de los recursos propios)?',
        ['20%', '8%', '12%', '16%'],
        0,
        'Beneficio del activo = 200.000·0,08 = 16.000; intereses = 150.000·0,04 = 6.000; beneficio neto = 10.000. ROE = 10.000 / 50.000 = 20%. Como el activo (8%) supera el coste de la deuda (4%), el apalancamiento es positivo y eleva el ROE sobre el ROA.',
    ),
    (
        'En un préstamo hipotecario a tipo variable, ¿qué representa el IRPH como índice de referencia?',
        ['La comisión de apertura media cobrada por las entidades de crédito', 'Un tipo medio de los préstamos hipotecarios concedidos por las entidades', 'El tipo del mercado interbancario del euro a 12 meses', 'El límite mínimo aplicable por una cláusula suelo'],
        1,
        'El IRPH (Índice de Referencia de Préstamos Hipotecarios) es un tipo medio de los préstamos hipotecarios de las entidades. El tipo interbancario a 12 meses es el Euríbor.',
    ),
    (
        'En un préstamo con un periodo de carencia de capital, ¿qué paga el prestatario durante dicho periodo?',
        ['Ni principal ni intereses, capitalizándose estos últimos', 'La cuota completa igual que en el sistema francés ordinario', 'Únicamente la comisión de disponibilidad sobre el saldo no dispuesto', 'Solo los intereses, sin amortizar principal'],
        3,
        'En la carencia de capital solo se pagan intereses y no se amortiza principal. Cuando no se paga ni principal ni intereses (capitalizándose estos) se trata de carencia total.',
    ),
    (
        'Al comparar leasing y renting como formas de financiación del uso de un bien, ¿cuál es la diferencia esencial?',
        ['El leasing incluye opción de compra al vencimiento y el renting normalmente no', 'El renting es siempre a más largo plazo y con garantía hipotecaria', 'El leasing no permite deducciones fiscales y el renting sí', 'El renting exige la constitución de un fondo de amortización (sinking fund)'],
        0,
        'El leasing (arrendamiento financiero) es un alquiler con opción de compra al vencimiento; el renting es un alquiler de uso que no suele incluir opción de compra e incorpora servicios como mantenimiento y seguros.',
    ),
]

APUNTES = '### M7: Crédito y Financiación\n\nLa financiación bancaria a particulares y empresas requiere del análisis del coste real del crédito, garantías y sistemas de amortización de préstamos.\n\n#### 1. TIN vs TAE\n1. **TIN (Tipo de Interés Nominal)**: Tipo de interés acordado de forma simple. No contempla la periodicidad de los pagos de intereses ni las comisiones.\n2. **TAE (Tasa Anual Equivalente)**: Tasa efectiva anual de interés compuesto. Incluye el tipo nominal, la frecuencia de las liquidaciones intrayear, las comisiones bancarias de apertura, los seguros obligatorios vinculados y otros gastos de formalización:\n   $$TAE = \\left(1 + \\frac{TIN}{m}\\right)^m - 1$$\n   Donde $m$ es el número de liquidaciones en el año. La TAE permite comparar el coste real de diferentes alternativas de crédito de forma objetiva. A igualdad de TIN, una mayor frecuencia de liquidación ($m$ mayor) genera una TAE mayor por el efecto de la capitalización compuesta. Las comisiones y gastos suben la TAE por encima del TIN, mientras que el TIN solo iguala a la TAE si $m=1$ y no existen comisiones ni gastos.\n\n#### 2. Sistemas de Amortización de Préstamos\n- **Sistema Francés (Cuota Constante)**: Es el método de amortización más utilizado en España. La cuota total (término amortizativo) es constante durante toda la vida del préstamo. En las primeras cuotas, el componente de intereses es muy elevado debido a que el capital pendiente es máximo; a lo largo de la vida del préstamo, los intereses disminuyen progresivamente y la amortización del principal aumenta de forma geométrica. La cuota constante se calcula como:\n   $$C = C_0 \\cdot \\frac{i}{1-(1+i)^{-n}}$$\n   Donde $C_0$ es el capital inicial (principal), $i$ el tipo de interés del periodo y $n$ el número total de cuotas. La cuota de intereses de cada periodo $t$ se obtiene multiplicando el capital vivo pendiente al cierre del periodo anterior por $i$; la amortización de principal de ese periodo es la diferencia entre la cuota constante y esos intereses.\n- **Sistema Italiano o Lineal (Cuota de Capital Constante)**: También llamado de amortización constante o de cuota lineal. Se amortiza el mismo importe de principal en cada periodo ($C_0/n$). Como el capital vivo decrece de forma lineal, los intereses también decrecen y, por tanto, la cuota total (principal + intereses) es decreciente en el tiempo. Se paga más al principio que con el sistema francés.\n- **Sistema Alemán**: Variante en la que los intereses del primer periodo se pagan de forma anticipada. En sentido amplio, se asocia también a la amortización de capital constante.\n- **Sistema Americano (Al Vencimiento o Bullet)**: Durante la vida del préstamo solo se abonan cuotas de intereses (constantes si el tipo es fijo). La totalidad del principal se reembolsa en un único pago al final del plazo. Es habitual que el deudor constituya en paralelo un fondo de amortización (sinking fund), invirtiendo periódicamente una cuota que capitaliza a un tipo de interés para acumular el capital necesario al vencimiento.\n- **Sistema de Cuota Creciente**: El término amortizativo crece a una tasa constante en cada periodo (progresión geométrica o aritmética). Permite cuotas iniciales más bajas, adaptándose a rentas que se esperan crecientes en el tiempo.\n\n#### 3. Capitalización Simple y Compuesta\n- **Capitalización simple**: Los intereses se calculan siempre sobre el capital inicial y no se acumulan al principal (no generan nuevos intereses). Se usa en operaciones a corto plazo (< 1 año): $$C_n = C_0 \\cdot (1 + i \\cdot n)$$\n- **Capitalización compuesta**: Los intereses se acumulan al capital al final de cada periodo y generan nuevos intereses (interés sobre interés). Se usa a largo plazo y es la base de la TAE: $$C_n = C_0 \\cdot (1+i)^n$$\n\n#### 4. Tipos de Operaciones de Financiación\n- **Préstamo**: La entidad entrega de una sola vez la totalidad del capital, que el cliente devuelve según un cuadro de amortización. Los intereses se pagan sobre todo el capital dispuesto.\n- **Crédito (línea/póliza)**: La entidad pone a disposición un límite máximo del que el cliente dispone según necesidad, pagando intereses solo por lo efectivamente dispuesto (más una comisión de disponibilidad por el saldo no dispuesto). Es renovable y flexible.\n- **Préstamo personal**: Garantía personal (responsabilidad patrimonial universal del art. 1911 CC: el deudor responde con todos sus bienes presentes y futuros). Suele ser a corto/medio plazo, importe menor y tipo más alto.\n- **Préstamo hipotecario**: Garantía real sobre un inmueble. Plazos largos, importes altos y tipos más bajos por la mayor garantía. Otros productos: crédito al consumo, leasing, renting, tarjetas de crédito, hipoteca inversa (permite a mayores obtener liquidez de su vivienda) e hipotecas/préstamos verdes (vinculados a criterios ESG o eficiencia energética).\n\n#### 5. Tipos de Interés: Fijo, Variable y Mixto\n- **Fijo**: El TIN permanece constante toda la vida del préstamo. Cuota estable y previsible; sin riesgo de subidas de tipos.\n- **Variable**: El tipo se revisa periódicamente sumando un índice de referencia más un diferencial fijo: tipo aplicado = índice + diferencial.\n- **Mixto**: Un primer periodo a tipo fijo y el resto a tipo variable.\n- **Índices de referencia**: El **Euríbor** (Euro Interbank Offered Rate, tipo del mercado interbancario, habitualmente a 12 meses) es el índice más usado. El **IRPH** (Índice de Referencia de Préstamos Hipotecarios) es un tipo medio de los préstamos hipotecarios de las entidades. Las **cláusulas suelo** fijan un tipo mínimo aplicable aunque el índice + diferencial resulte inferior.\n\n#### 6. Carencia y Comisiones\n- **Carencia de capital**: Durante un periodo inicial solo se pagan intereses, sin amortizar principal.\n- **Carencia total**: No se paga ni principal ni intereses durante el periodo de carencia (los intereses se suelen capitalizar).\n- **Comisiones**: apertura (al formalizar), estudio, amortización anticipada/reembolso (compensa a la entidad, limitada por la LCCI), subrogación (cambio de deudor o de acreedor), y comisión de disponibilidad (en líneas de crédito).\n\n#### 7. Regulación Hipotecaria en España (LCCI)\nLa Ley 5/2019, de Contratos de Crédito Inmobiliario (LCCI), otorga mayor protección al prestatario minorista:\n- Exige la entrega obligatoria de la Ficha Europea de Información Normalizada (FEIN, oferta vinculante 10 días) y la Ficha de Advertencias Estandarizadas (FiAE) con al menos 10 días de antelación a la firma.\n- El prestatario debe acudir al notario para recibir asesoramiento gratuito y firmar el acta previa al menos 24 horas antes de la firma de la escritura.\n- Los gastos de notaría, registro, gestoría e IAJD los asume el banco; el cliente solo paga la tasación y las copias que solicite.\n- Interés de demora máximo: interés remuneratorio ordinario + 3 puntos porcentuales.\n- Limita las comisiones de amortización anticipada (reembolso) y prohíbe las ventas vinculadas de seguros o productos, salvo ventas combinadas autorizadas.\n- Endurece las cláusulas de vencimiento anticipado (impago mínimo de 12 cuotas o 3% del capital en la primera mitad; 15 cuotas o 7% en la segunda mitad).\n\n#### 8. Análisis del Riesgo del Particular\n- **Riesgo de crédito**: probabilidad de que el deudor no atienda sus obligaciones. Los modelos de pérdida esperada usan: probabilidad de impago (PD), severidad (LGD, pérdida en caso de impago), exposición (EAD) y rating.\n- **Scoring**: modelo estadístico que puntúa la solvencia del solicitante a partir de sus características (ingresos, historial, estabilidad).\n- **Capacidad de pago**: ingresos netos recurrentes disponibles para atender la deuda.\n- **Ratio de endeudamiento / esfuerzo**: proporción de los ingresos destinada al pago de cuotas. Como norma prudencial, la cuota (o el total de deudas) no debería superar el 30-35% de los ingresos netos: $$Ratio\\ esfuerzo = \\frac{Cuotas\\ de\\ deuda}{Ingresos\\ netos}$$\n- **Loan to Value (LTV)**: relación entre el importe del préstamo y el valor de tasación de la garantía. Cuanto menor el LTV, menor el riesgo para la entidad: $$LTV = \\frac{Importe\\ del\\ préstamo}{Valor\\ de\\ tasación}$$\n   En hipotecas de vivienda habitual suele limitarse al 80% del valor de tasación.\n- **Factores del nivel de riesgo**: plazo, importe, modalidad, conocimiento del cliente y garantías aportadas.\n\n#### 9. Garantías y Avales\n- **Garantías reales**: recaen sobre un bien concreto. Hipoteca (inmuebles) y prenda o pignoración (bienes muebles o activos financieros). En la pignoración de activos financieros se pondera el riesgo del activo aportado.\n- **Garantías personales**: el patrimonio del deudor y, en su caso, de un **avalista/fiador**, que responde solidariamente de la deuda si el titular no paga.\n- **Nuda propiedad**: propiedad de un bien sin el derecho de uso y disfrute (que corresponde al usufructuario); puede aportarse como garantía.\n- **Ratio de cobertura de garantía**: relación entre el valor de la garantía y el importe del riesgo, mide el colchón disponible ante impago.\n\n#### 10. Apalancamiento Financiero\nEl apalancamiento consiste en emplear deuda (recursos ajenos) para financiar una inversión y así amplificar la rentabilidad de los recursos propios. El efecto es **positivo** cuando la rentabilidad del activo (o del proyecto) supera el coste de la deuda, elevando la rentabilidad financiera (ROE) por encima de la económica (ROA). Es **negativo** cuando el coste de la deuda supera la rentabilidad del activo, amplificando las pérdidas. A mayor endeudamiento, mayor rentabilidad potencial pero también mayor riesgo financiero y coste de oportunidad. El **ratio de endeudamiento** relaciona los recursos ajenos con los propios (o con el total de la operación): $$Ratio\\ endeudamiento = \\frac{Recursos\\ ajenos}{Recursos\\ propios}$$\n\n#### 11. Leasing, Renting e Hipoteca Inversa\n- **Leasing (arrendamiento financiero)**: alquiler con **opción de compra** al vencimiento. Habitual para bienes de inversión de empresas y autónomos, con ventajas fiscales.\n- **Renting**: alquiler de uso a medio plazo que **no suele incluir opción de compra** y engloba servicios (mantenimiento, seguros). Muy usado en vehículos y equipos.\n- **Hipoteca inversa**: producto para **personas mayores (habitualmente 65 o más años) o dependientes** que obtienen liquidez (renta periódica o pago único) con la garantía de su vivienda **sin perder la propiedad**; la deuda se cancela normalmente por los herederos tras el fallecimiento.\n- **Préstamos e hipotecas verdes (ESG)**: financiación vinculada a criterios de sostenibilidad (por ejemplo, eficiencia energética del inmueble) que puede ofrecer mejores condiciones al prestatario.\n\n#### 12. Gestión de la Insolvencia\nCuando el deudor deja de atender sus pagos, la operación se clasifica según la antigüedad del impago:\n- **Morosidad temprana**: primeros retrasos o impagos leves; todavía es posible negociar una solución (refinanciación) antes de la clasificación contable.\n- **Morosidad contable (dudoso)**: la operación se clasifica como dudosa por razón de la morosidad (habitualmente a partir de 90 días de impago), obligando a la entidad a dotar provisiones.\n- **Soluciones**: carencia temporal, ampliación de plazo, reunificación de deudas, quita o dación en pago.\n- **Vencimiento anticipado y procedimiento judicial**: si el impago supera los umbrales de la LCCI (12 cuotas o 3% del capital en la primera mitad del préstamo; 15 cuotas o 7% en la segunda mitad), la entidad puede declarar el vencimiento anticipado e iniciar la ejecución hipotecaria.\n\n#### 13. Ejemplos Resueltos\n**Ejemplo 1 — TAE a partir del TIN con capitalización mensual.** Un préstamo tiene un TIN del 6% con liquidación mensual ($m=12$).\n$$TAE = \\left(1+\\frac{0{,}06}{12}\\right)^{12}-1 = (1{,}005)^{12}-1 = 1{,}06168-1 = 0{,}0617 = 6{,}17\\%$$\nLa TAE (6,17%) supera al TIN (6%) por el efecto de la capitalización compuesta intraanual.\n\n**Ejemplo 2 — Cuota del sistema francés.** Hipoteca de $C_0=150.000$ EUR, TIN 3% anual, 25 años ($n=300$ meses), tipo mensual $i=0{,}03/12=0{,}0025$.\n$$C = 150.000\\cdot\\frac{0{,}0025}{1-(1{,}0025)^{-300}} = \\frac{375}{1-0{,}4728} = \\frac{375}{0{,}5272} \\approx 711\\ \\text{EUR/mes}$$\nLa primera cuota de intereses es $150.000\\cdot0{,}0025=375$ EUR y la amortización de principal $711-375=336$ EUR; en las cuotas siguientes los intereses bajan y el principal amortizado sube.\n\n**Ejemplo 3 — Ratio de esfuerzo/endeudamiento.** Cliente con ingresos netos de 2.500 EUR/mes que ya paga 300 EUR de otras deudas y solicita una hipoteca con cuota de 600 EUR.\n$$Ratio = \\frac{300+600}{2.500} = \\frac{900}{2.500} = 0{,}36 = 36\\%$$\nSupera el umbral prudencial del 35%, por lo que la operación sería dudosa salvo aportación de garantías o ingresos adicionales.\n\n**Ejemplo 4 — Loan to Value (LTV).** Vivienda tasada en 225.000 EUR con un préstamo de 180.000 EUR.\n$$LTV = \\frac{180.000}{225.000} = 0{,}80 = 80\\%$$\nCoincide con el límite habitual del 80% para vivienda habitual; por encima, la entidad exigiría garantías adicionales.\n\n**Ejemplo 5 — Apalancamiento financiero.** Inversión de 100.000 EUR financiada con 40.000 EUR de recursos propios y 60.000 EUR de deuda al 5%. El activo rinde un 10%. Beneficio del activo $=100.000\\cdot0{,}10=10.000$; intereses $=60.000\\cdot0{,}05=3.000$; beneficio neto $=7.000$.\n$$ROE = \\frac{7.000}{40.000} = 0{,}175 = 17{,}5\\%$$\nComo la rentabilidad del activo (10%) supera el coste de la deuda (5%), el apalancamiento es positivo y eleva el ROE (17,5%) por encima del ROA (10%), aunque incrementa el riesgo financiero.\n\n#### 14. Errores Frecuentes y Claves de Examen\n- **TIN vs TAE**: el TIN no incluye comisiones ni la frecuencia de liquidación; la TAE sí. A igual TIN, más liquidaciones al año ($m$ mayor) implican TAE mayor. El TIN solo iguala a la TAE si $m=1$ y no hay comisiones ni gastos.\n- **Francés vs lineal**: en el francés la CUOTA es constante (intereses decrecientes, principal creciente); en el lineal/italiano la AMORTIZACIÓN DE PRINCIPAL es constante y la cuota total es decreciente. No los confundas.\n- **Fórmula de la cuota francesa**: el exponente es negativo, $1-(1+i)^{-n}$; usa el tipo del periodo (mensual) y $n$ en meses, no el anual.\n- **Cláusula suelo**: el tipo aplicado es el MÁXIMO entre (índice + diferencial) y el suelo. Con Euríbor negativo nunca se aplica por debajo del suelo pactado.\n- **Reparto de gastos LCCI**: el cliente solo paga la tasación y las copias que solicite; el banco asume notaría, registro, gestoría e IAJD. Acta notarial: al menos 24 horas antes; FEIN/FiAE: al menos 10 días antes.\n- **Ratio de esfuerzo**: umbral prudencial 30-35% sobre ingresos NETOS. Interés de demora hipotecario LCCI: remuneratorio + 3 puntos porcentuales.\n- **Apalancamiento**: positivo cuando la rentabilidad del activo supera el coste de la deuda; amplifica tanto ganancias como pérdidas y eleva el riesgo financiero.\n- **Crédito vs préstamo**: en el crédito se pagan intereses solo por lo dispuesto (más comisión de disponibilidad); en el préstamo, por todo el capital entregado.'
