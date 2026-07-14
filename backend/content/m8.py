# Módulo M8 — Fiscalidad
# PREGUNTAS: cada tupla es (enunciado, [4 opciones], indice_respuesta_correcta, explicacion)
# Ampliar apuntes y preguntas conforme al temario oficial EFPA. NO borrar términos ya existentes.
NOMBRE = 'Fiscalidad'

PREGUNTAS = [
    (
        '¿A partir de qué importe anual la tarifa del ahorro estatal del IRPF español aplica el tipo del 21%?',
        ['6.000 €', '50.000 €', '200.000 €', '3.000 €'],
        0,
        'La escala del ahorro aplica un 19% hasta 6.000 €, y un 21% a partir de ese límite hasta 50.000 €.',
    ),
    (
        '¿Qué límite existe en el IRPF para compensar saldos negativos de ganancias y pérdidas patrimoniales con el saldo de rendimientos del capital mobiliario en la base del ahorro?',
        ['Un máximo del 25% del saldo positivo de los rendimientos del capital mobiliario', 'Un máximo del 10% sin posibilidad de trasladar el exceso a ejercicios futuros', 'Se pueden compensar al 100% sin ningún límite cuantitativo', 'No está permitida la compensación cruzada entre estos dos compartimentos'],
        0,
        'La ley del IRPF permite la compensación cruzada en la base del ahorro con un límite del 25% del saldo positivo del compartimento opuesto.',
    ),
    (
        '¿Cuál es el tratamiento fiscal en el Impuesto sobre el Patrimonio de los planes de pensiones individuales en España?',
        ['Están totalmente exentos de declarar en el Impuesto sobre el Patrimonio', 'Tributan por su valor de rescate consolidado al final del año fiscal', 'Están exentos solo si el partícipe no supera los 65 años de edad', 'Tributan en el impuesto al 50% de su valor neto patrimonial'],
        0,
        'Los derechos consolidados en planes de pensiones son bienes inembargables y están exentos del Impuesto sobre el Patrimonio por carecer de liquidez inmediata.',
    ),
    (
        'Un inversor persona física vende acciones de una empresa española con ganancias patrimoniales. ¿Qué retención fiscal a cuenta del IRPF se le aplica en el momento de la venta?',
        ['0% (las ventas de acciones cotizadas no están sujetas a retención a cuenta)', '19% de retención directa aplicada por el bróker español', '21% de retención sobre el importe total de la transmisión', 'Un tipo del 15% que luego se liquida en el impuesto de transmisiones patrimoniales'],
        0,
        'Las ganancias patrimoniales por transmisión de acciones no sufren retención a cuenta (a diferencia de fondos de inversión), debiendo declararse en la renta anual.',
    ),
    (
        'En relación a la exención por reinversión en vivienda habitual en el IRPF, ¿de qué plazo dispone el contribuyente para reinvertir el importe obtenido por la venta de su vivienda habitual?',
        ['Un plazo máximo de 2 años, anteriores o posteriores a la fecha de la venta', 'Un año a contar desde el devengo del impuesto', 'Debe realizarse de forma inmediata y simultánea ante notario', '5 años siempre que se justifique ante la AEAT la adquisición del suelo'],
        0,
        'La reinversión de la ganancia patrimonial para vivienda habitual debe producirse en un plazo no superior a dos años desde la enajenación.',
    ),
    (
        '¿Cómo tributan en el IRPF los dividendos distribuidos por una sociedad cotizada a una persona física residente en España?',
        ['Como rendimientos del capital mobiliario en la base del ahorro, sujetos a retención (generalmente del 19%)', 'Como ganancias patrimoniales sujetas a una escala progresiva en la base general', 'Están exentos los primeros 1.500 € y el resto tributa al tipo marginal del trabajo', 'Tributan en la base general reduciéndose en la base imponible del ahorro'],
        0,
        'Los dividendos son rendimientos de capital mobiliario que tributan en la base imponible del ahorro y sufren una retención en origen del 19%.',
    ),
    (
        '¿Cuál es el tipo de gravamen aplicable en el IRPF del ahorro español a un rendimiento de capital mobiliario de 250.000 €?',
        ['Se aplica una escala progresiva: 19% por los primeros 6.000 €, 21% hasta 50.000 €, 23% hasta 200.000 € y 27% por el exceso hasta 250.000 €', 'Un tipo impositivo único del 23% sobre la totalidad del rendimiento neto', 'Se integra al tipo marginal del contribuyente en la base general con retención del 19%', 'Se aplica un tipo reducido de retención del 15% al declararse de forma independiente'],
        0,
        'La base del ahorro es progresiva. Al superar los 200.000 € y hasta los 300.000 €, el tipo aplicable sobre ese tramo es del 27% (para 2026).',
    ),
    (
        'En una operación bursátil de Script Dividend, si el accionista elige recibir nuevas acciones liberadas en lugar de cobrar efectivo, ¿cuál es el tratamiento fiscal?',
        ['Las nuevas acciones no tributan en el momento de la entrega; reducen el valor de adquisición de las acciones de origen diferiendo la ganancia fiscal hasta la venta', 'Tributan inmediatamente como rendimiento de capital mobiliario al tipo del 19%', 'Tributan como ganancia patrimonial sujeta a retención a cuenta aplicada por Iberclear', 'Se consideran rentas exentas hasta un límite máximo de 12.000 € anuales'],
        0,
        'Recibir acciones liberadas no genera tributación inmediata en el IRPF. El coste de adquisición global se reparte entre más títulos, bajando el precio de adquisición unitario.',
    ),
    (
        'Si un contribuyente mayor de 65 años vende un local comercial generando una plusvalía de 50.000 €, ¿qué requisito exige la ley para que quede exenta de tributar en el IRPF?',
        ['Reinvertir el importe total de la transmisión en la constitución de una renta vitalicia asegurada en un plazo máximo de 6 meses, con un tope de 240.000 €', 'Estar exento de forma automática sin condiciones por tener más de 65 años de edad', 'Reinvertir la ganancia en adquirir acciones de una SOCIMI cotizada en el Mercado Alternativo', 'No está permitida la exención en locales comerciales, se limita solo a la vivienda habitual'],
        0,
        'Los mayores de 65 años pueden excluir de gravamen la ganancia por venta de cualquier bien (locales, acciones) si destinan el dinero a una renta vitalicia en 6 meses (tope 240.000 €).',
    ),
    (
        '¿Qué ocurre fiscalmente en el IRPF si una persona física vende participaciones de un fondo de inversión con pérdidas y compra acciones de la misma categoría en un plazo inferior a dos meses?',
        ['Se aplica la regla de incorporación de pérdidas de lavado (wash sale), no permitiéndose compensar la pérdida hasta la venta futura de las nuevas participaciones', 'Se le aplica una penalización administrativa del 15% aplicada de oficio por la AEAT', 'La plusvalía de otras operaciones se reduce a la mitad automáticamente', 'Se permite compensar la pérdida de forma normal al tratarse de activos financieros diferentes'],
        0,
        'La regla de lavado de fondos impide deducir pérdidas patrimoniales si se recompran valores homogéneos en los 2 meses anteriores o posteriores (o 1 año para valores no cotizados).',
    ),
    (
        'En la transmisión de participaciones de fondos de inversión, ¿qué criterio de ordenación temporal de entradas y salidas se aplica por ley en España para determinar el coste fiscal?',
        ['Criterio FIFO (First-In, First-Out)', 'Criterio LIFO (Last-In, First-Out)', 'Precio Medio Ponderado (PMP) calculado diariamente por la gestora', 'Criterio libre elegido por el propio contribuyente en su autoliquidación'],
        0,
        'En España, la venta de acciones y participaciones de fondos de inversión sigue obligatoriamente el criterio FIFO: se consideran transmitidas primero las adquiridas en fecha más antigua.',
    ),
    (
        'En el Impuesto sobre la Renta de las Personas Físicas (IRPF) en España, ¿cómo tributan los rendimientos procedentes del capital inmobiliario (alquileres de viviendas habituales)?',
        ['En la base imponible general progresiva, pudiendo aplicar reducciones sobre el rendimiento neto si se cumplen los requisitos legales', 'En la base imponible del ahorro aplicando la escala del 19% al 28%', 'Están exentas en su totalidad si el arrendatario es menor de 35 años de edad', 'Tributan mediante una cuota fija anual del 10% retenida por el pagador mercantil'],
        0,
        'Los rendimientos del alquiler de viviendas habituales se integran en la base general progresiva (no en la del ahorro) con reducciones fiscales si procede (ej. 50% o 60% según fecha).',
    ),
    (
        'En el Impuesto sobre el Patrimonio en España, ¿cuál es el límite del mínimo exento de carácter general fijado por la ley estatal?',
        ['700.000 € por contribuyente (más hasta 300.000 € exentos por vivienda habitual)', '1.000.000 € netos consolidados sin exención por vivienda habitual', '500.000 € conjuntos aplicables únicamente a la base liquidable general', 'No existe mínimo exento estatal, depende exclusivamente de las provincias autonómicas'],
        0,
        'La ley estatal del IP establece un mínimo exento general de 700.000 € (modificable por las Comunidades Autónomas) y una exención de hasta 300.000 € para la vivienda habitual del sujeto pasivo.',
    ),
    (
        'En el Impuesto sobre Sucesiones y Donaciones (ISD) español, ¿cuál es la principal diferencia entre sucesiones y donaciones a efectos de reducciones y tarifas?',
        ['Sucesiones grava las adquisiciones mortis causa (fallecimiento) y donaciones las transmisiones gratuitas inter vivos, teniendo reducciones fiscales diferentes', 'Donaciones no tributa si el donatario es descendiente directo menor de edad', 'Sucesiones aplica un tipo de interés de demora del 5.0% y donaciones está exenta de retenciones', 'Sucesiones integra los activos en la base del ahorro del IRPF y donaciones en la base general'],
        0,
        'Son dos modalidades del mismo tributo. Sucesiones (mortis causa) suele contar con mayores reducciones familiares (Grupo I y II) y bonificaciones que donaciones (inter vivos).',
    ),
    (
        'En relación con los Planes de Ahorro a Largo Plazo (PALP), ¿cómo tributan los rendimientos de capital mobiliario generados a los 5 años?',
        ['Están exentos de tributación si se aporta un máximo de 5.000 € anuales durante al menos 5 años y se cumple el plazo', 'Tributan al tipo del 19% en el IRPF sin retención de la entidad financiera', 'Se integran en la base imponible general aplicando una reducción del 40%', 'Sufren un gravamen diferido hasta el momento de jubilación definitiva del tomador'],
        0,
        'Los Seguros Individuales de Ahorro a Largo Plazo (SIALP) o Depósitos Individuales de Ahorro a Largo Plazo (CIALP) eximen del IRPF de intereses si la inversión dura 5 años y las aportaciones son <= 5.000 €/año.',
    ),
    (
        'En relación a la fiscalidad de la renta fija, ¿cómo tributan los cupones percibidos por un inversor persona física residente en España?',
        ['Como rendimientos del capital mobiliario en la base del ahorro, sujetos a retención a cuenta (generalmente del 19%)', 'Como ganancias patrimoniales sujetas a la escala progresiva del trabajo en la base general', 'Están exentos si proceden de emisiones del Tesoro Público (letras y bonos)', 'Tributan al tipo fijo del 1% en el Impuesto sobre Transmisiones Patrimoniales corporativo'],
        0,
        'Los cupones de bonos y obligaciones tributan como rendimientos de capital mobiliario integrados en la base del ahorro con retención del 19%.',
    ),
    (
        'Un contribuyente obtiene en el ejercicio una base liquidable del ahorro de 60.000 €. Aplicando la escala del ahorro vigente (19% hasta 6.000 €; 21% de 6.000 a 50.000 €; 23% de 50.000 a 200.000 €), ¿cuál es la cuota íntegra del ahorro?',
        ['12.680 €', '13.800 €', '11.400 €', '12.600 €'],
        0,
        'Se aplica por tramos: 6.000×19% = 1.140 €; 44.000×21% = 9.240 €; 10.000×23% = 2.300 €. Total = 12.680 €. No se aplica un tipo único sobre toda la base, sino una escala progresiva.',
    ),
    (
        '¿Cómo tributan en el IRPF las aportaciones y las prestaciones de un plan de pensiones individual?',
        ['Las aportaciones reducen la base imponible general (con límites); las prestaciones tributan como rendimientos del trabajo en la base general', 'Las aportaciones reducen la base del ahorro y las prestaciones tributan como ganancias patrimoniales', 'Ni aportaciones ni prestaciones tienen efecto fiscal hasta la jubilación', 'Las aportaciones son deducibles en cuota al 40% y las prestaciones están exentas'],
        0,
        'Las aportaciones a planes de pensiones reducen la base imponible general (límite general de 1.500 € anuales de aportación individual). Las prestaciones (rescate) tributan íntegramente como rendimientos del trabajo en la base general, no en la del ahorro.',
    ),
    (
        'En el régimen de diferimiento por traspaso entre fondos de inversión aplicable a personas físicas residentes, ¿qué efecto fiscal tiene traspasar el capital de un fondo a otro sin reembolsar?',
        ['No se genera ganancia ni pérdida patrimonial en el momento del traspaso; la tributación se difiere hasta el reembolso definitivo', 'Se tributa por la ganancia acumulada pero con una bonificación del 50%', 'Se aplica una retención del 19% sobre la plusvalía latente en cada traspaso', 'El traspaso tributa como rendimiento del capital mobiliario en la base del ahorro'],
        0,
        'El régimen de diferimiento (traspaso) permite mover el capital entre IIC sin tributar, conservando el valor y fecha de adquisición originales. La ganancia solo tributa cuando se reembolsa finalmente a efectivo.',
    ),
    (
        'En el Impuesto sobre Sociedades español, ¿cuál es el tipo de gravamen general aplicable a la base imponible de la mayoría de las entidades?',
        ['25%', '19%', '30%', '15% sin excepciones'],
        0,
        'El tipo general del Impuesto sobre Sociedades es del 25%. Existen tipos reducidos (por ejemplo, para entidades de nueva creación o de reducida dimensión) y el tipo especial del 1% para las Instituciones de Inversión Colectiva que cumplan los requisitos.',
    ),
    (
        'Si en un ejercicio el saldo de ganancias y pérdidas patrimoniales de la base del ahorro resulta negativo tras la compensación interna y la compensación cruzada, ¿qué puede hacer el contribuyente con el saldo negativo restante?',
        ['Compensarlo con saldos positivos de la base del ahorro de los 4 ejercicios siguientes', 'Solicitar su devolución directa a la AEAT en efectivo', 'Trasladarlo indefinidamente sin límite temporal', 'Compensarlo con rendimientos del trabajo de la base general'],
        0,
        'Las pérdidas patrimoniales no compensadas en el ejercicio pueden trasladarse y compensarse en los 4 ejercicios siguientes, dentro de la base del ahorro. No pueden compensarse con rentas de la base general.',
    ),
    (
        'En el IRPF, la percepción en forma de capital diferido de un seguro de vida-ahorro (por ejemplo, un unit linked rescatado por el propio tomador), ¿cómo tributa?',
        ['Como rendimiento del capital mobiliario en la base del ahorro por la diferencia entre el capital percibido y las primas satisfechas', 'Como ganancia patrimonial en la base general', 'Como rendimiento del trabajo sujeto a la escala general', 'Está exento por tratarse de un seguro de vida'],
        0,
        'El rescate de un seguro de vida-ahorro o unit linked por el propio tomador genera rendimiento del capital mobiliario (capital percibido menos primas pagadas), que se integra en la base del ahorro y tributa según la escala 19%-28%.',
    ),
    (
        'Una persona física obtiene rentas por el alquiler de un local comercial de su propiedad. ¿En qué base imponible del IRPF se integran estos rendimientos del capital inmobiliario?',
        ['En la base imponible del ahorro, aplicando la escala del 19% al 28%', 'En la base imponible general, tributando al tipo marginal progresivo del contribuyente', 'Están totalmente exentos por tratarse de un local comercial', 'Tributan de forma independiente en el Impuesto sobre Sucesiones y Donaciones'],
        1,
        'Los rendimientos del capital inmobiliario (alquileres) se integran siempre en la base imponible general y tributan a la escala progresiva del contribuyente, no en la base del ahorro.',
    ),
    (
        'Cuando una sociedad abona un dividendo a un accionista persona física residente, ¿qué porcentaje de retención a cuenta del IRPF practica el pagador con carácter general?',
        ['21%', '23%', '19%', '0%, los dividendos nunca soportan retención'],
        2,
        'Los rendimientos del capital mobiliario, como los dividendos, soportan una retención a cuenta del 19% en el momento de su abono, que después se descuenta de la cuota final del IRPF.',
    ),
    (
        'Una persona física recibe una subvención pública para la adquisición de un bien. Al no derivar de la transmisión de un elemento patrimonial, ¿en qué base tributa esta ganancia patrimonial?',
        ['En la base del ahorro, dentro del compartimento de ganancias y pérdidas patrimoniales', 'En la base del ahorro, dentro del compartimento de rendimientos del capital mobiliario', 'No tributa en el IRPF por tratarse de una ayuda pública', 'En la base imponible general, porque no procede de una transmisión'],
        3,
        'Solo las ganancias patrimoniales que derivan de la transmisión de elementos patrimoniales se integran en la base del ahorro. Las que no derivan de transmisión (premios, subvenciones) se integran en la base general.',
    ),
    (
        'Un inversor compró 100 acciones de una compañía en 2018 y otras 100 de la misma compañía en 2022. Si ahora vende 100 acciones, ¿cuáles se consideran transmitidas a efectos fiscales?',
        ['Las adquiridas en 2018, en aplicación de la regla FIFO', 'Las adquiridas en 2022, en aplicación de la regla LIFO', 'Las que elija libremente el inversor en su autoliquidación', 'Una combinación al precio medio ponderado de ambas compras'],
        0,
        'En valores homogéneos rige obligatoriamente el criterio FIFO: se entienden transmitidas primero las acciones adquiridas en la fecha más antigua, es decir, las de 2018.',
    ),
    (
        'En la norma antiaplicación (o de recompra) que impide computar una pérdida patrimonial si se readquieren valores homogéneos, ¿cuál es el plazo aplicable cuando los valores NO cotizan en un mercado organizado?',
        ['2 meses anteriores o posteriores a la transmisión', '1 año anterior o posterior a la transmisión', '6 meses anteriores o posteriores a la transmisión', 'La norma antiaplicación no se aplica a valores no cotizados'],
        1,
        'La norma antiaplicación difiere la pérdida si se recompran valores homogéneos en un plazo de 2 meses para valores cotizados y de 1 año para valores no cotizados.',
    ),
    (
        'En la base imponible general del IRPF, ¿hasta qué porcentaje del saldo positivo de rendimientos puede compensarse el saldo negativo de las ganancias y pérdidas patrimoniales que no derivan de transmisión?',
        ['Un 10% del saldo positivo de rendimientos', 'Un 50% del saldo positivo de rendimientos', 'Un 25% del saldo positivo de rendimientos', 'El 100%, sin ningún límite cuantitativo'],
        2,
        'En la base general, el saldo negativo de ganancias/pérdidas no derivadas de transmisión compensa el saldo positivo de rendimientos con un límite del 25%, análogo al del ahorro.',
    ),
    (
        '¿Cómo tributan los rendimientos obtenidos por una persona física en la amortización de Letras del Tesoro?',
        ['Como ganancia patrimonial con retención del 19% aplicada por el emisor', 'Están totalmente exentos por proceder de deuda pública estatal', 'Como rendimiento del capital mobiliario con retención del 21% en origen', 'Como rendimiento del capital mobiliario en la base del ahorro, sin retención en origen'],
        3,
        'Las Letras del Tesoro generan rendimiento del capital mobiliario que se integra en la base del ahorro, pero constituyen una excepción: no soportan retención a cuenta en origen.',
    ),
    (
        'En un Plan Individual de Ahorro Sistemático (PIAS), ¿qué ventaja fiscal se obtiene si la prestación se percibe en forma de renta vitalicia asegurada?',
        ['La rentabilidad acumulada durante la vida del producto queda exenta de tributación', 'La aportación anual reduce la base imponible general del tomador', 'La prestación tributa como rendimiento del trabajo con reducción del 40%', 'El producto tributa al tipo reducido del 1% propio de las IIC'],
        0,
        'El PIAS permite que la rentabilidad generada quede exenta en el IRPF si la prestación se percibe como renta vitalicia asegurada, cumpliendo los requisitos legales de plazo y aportaciones.',
    ),
    (
        'En el Impuesto sobre Sucesiones y Donaciones, ¿a qué grupo de parentesco pertenecen los descendientes y adoptados menores de 21 años?',
        ['Grupo II', 'Grupo I', 'Grupo III', 'Grupo IV'],
        1,
        'El Grupo I comprende a los descendientes y adoptados menores de 21 años, que son los que gozan de mayores reducciones en el ISD. El Grupo II incluye descendientes de 21 años o más, cónyuge y ascendientes.',
    ),
    (
        'En el Impuesto sobre el Patrimonio, ¿cuál es el límite conjunto que opera entre las cuotas del IRPF y del IP?',
        ['La suma de cuotas no puede exceder el 80% de la base del ahorro del IRPF', 'La suma de cuotas no puede exceder el 50% de la cuota íntegra del IRPF', 'La suma de cuotas de IRPF más IP no puede exceder el 60% de la base imponible del IRPF', 'No existe ningún límite conjunto entre ambos impuestos'],
        2,
        'La suma de las cuotas del IRPF y del IP no puede superar el 60% de la base imponible del IRPF; si se supera, se reduce la cuota del IP hasta un máximo del 80%.',
    ),
    (
        '¿A partir de qué importe de patrimonio neto grava el Impuesto Temporal de Solidaridad de las Grandes Fortunas (ITSGF), complementario del IP?',
        ['700.000 € de patrimonio neto', '300.000 € de patrimonio neto', '1.000.000 € de patrimonio neto', '3.000.000 € de patrimonio neto'],
        3,
        'El ITSGF grava los patrimonios netos superiores a 3.000.000 €. Es complementario del IP y permite deducir la cuota ya satisfecha por este para evitar la doble imposición.',
    ),
    (
        'Un contribuyente tiene una base liquidable del ahorro de 20.000 €. Aplicando la escala del ahorro (19% hasta 6.000 €; 21% de 6.000 a 50.000 €), ¿cuál es la cuota íntegra del ahorro?',
        ['4.080 €', '4.200 €', '3.800 €', '5.000 €'],
        0,
        'Por tramos: 6.000 × 19% = 1.140 € y 14.000 × 21% = 2.940 €. Total = 1.140 + 2.940 = 4.080 €. No se aplica un tipo único a toda la base.',
    ),
    (
        'Una base liquidable del ahorro asciende a 100.000 €. Con la escala del ahorro (19% hasta 6.000 €; 21% de 6.000 a 50.000 €; 23% de 50.000 a 200.000 €), ¿cuál es la cuota íntegra?',
        ['23.000 €', '21.880 €', '20.700 €', '22.500 €'],
        1,
        'Por tramos: 6.000 × 19% = 1.140 €; 44.000 × 21% = 9.240 €; 50.000 × 23% = 11.500 €. Total = 1.140 + 9.240 + 11.500 = 21.880 €.',
    ),
    (
        'Un inversor obtiene una base liquidable del ahorro de 350.000 €. Aplicando la escala completa del ahorro (19%/21%/23%/27% y 28% para el exceso sobre 300.000 €), ¿cuál es la cuota íntegra?',
        ['98.000 €', '84.500 €', '85.880 €', '80.880 €'],
        2,
        'Hasta 300.000 € la cuota es 71.880 € (1.140 + 9.240 + 34.500 + 27.000). El exceso, 50.000 €, tributa al 28%: 50.000 × 28% = 14.000 €. Total = 71.880 + 14.000 = 85.880 €.',
    ),
    (
        'En la base del ahorro, un contribuyente tiene un saldo positivo de rendimientos del capital mobiliario de +8.000 € y un saldo negativo de ganancias y pérdidas patrimoniales de -5.000 €. ¿Cuál es la base del ahorro resultante y el exceso a compensar?',
        ['Base de 3.000 € y ningún exceso pendiente de compensar', 'Base de 8.000 € y exceso de 5.000 € trasladable', 'Base de 5.000 € y exceso de 2.000 € trasladable', 'Base de 6.000 € y exceso de 3.000 € trasladable a los 4 ejercicios siguientes'],
        3,
        'El saldo negativo compensa el positivo solo hasta el 25% de 8.000 € = 2.000 €. Base del ahorro = 8.000 - 2.000 = 6.000 €. El exceso no compensado, 5.000 - 2.000 = 3.000 €, se traslada a los 4 ejercicios siguientes.',
    ),
]


INTRO = '# M8: Fiscalidad de las Inversiones\n\nDe cada euro que ganas con tus inversiones, una parte se la lleva Hacienda. Saber cuánto, cuándo y cómo se paga es tan importante como elegir bien la inversión: a veces, dos productos con la misma rentabilidad dejan resultados muy distintos en el bolsillo por culpa de los impuestos. Este módulo te da el mapa de la fiscalidad del ahorro en España.'


SECCIONES = [
    {
        'titulo': 'Estructura del IRPF en España',
        'cuerpo': 'El [[IRPF::Impuesto sobre la Renta de las Personas Físicas; el principal impuesto que pagan los particulares en España sobre lo que ganan cada año (sueldos, rentas, inversiones)]] separa las rentas del contribuyente en dos "cajas" o bases imponibles:\n1. **[[base imponible general::"caja" del IRPF donde caen los sueldos, pensiones, actividades económicas y alquileres; tributa a una escala progresiva con tipos altos (que pueden superar el 47%)]]**: incluye rendimientos del trabajo (salarios, pensiones), actividades económicas y alquileres. Tributa de forma progresiva según el tipo marginal del contribuyente (que puede superar el 47% según la comunidad).\n2. **[[base imponible del ahorro::"caja" del IRPF donde caen los frutos del capital financiero (dividendos, intereses, cupones y plusvalías por vender activos); tributa a una escala más suave, del 19% al 28%]]**: incluye los rendimientos del capital mobiliario (dividendos, cupones) y las ganancias y pérdidas patrimoniales (ventas de acciones, fondos, inmuebles). Tributa por una escala progresiva del ahorro (España 2026):\n   - Primeros 6.000 €: **19%**\n   - De 6.000 € a 50.000 €: **21%**\n   - De 50.000 € a 200.000 €: **23%**\n   - De 200.000 € a 300.000 €: **27%**\n   - Más de 300.000 €: **28%**',
        'ejercicios': [],
    },
    {
        'titulo': 'Fiscalidad por tipo de activo financiero',
        'cuerpo': '- **Acciones**: los dividendos y las ganancias por venta van a la base del ahorro. Las ganancias por venta **no** llevan retención.\n- **Renta fija (bonos y Letras)**: los cupones son rendimientos de capital mobiliario con retención (19%). Las Letras del Tesoro tributan como RCM en el reembolso, pero están exentas de retención en origen.\n- **Fondos de inversión**: diferimiento por traspaso para personas físicas. Los reembolsos tributan en la base del ahorro con retención obligatoria del 19%.\n- **Derivados (opciones y futuros)**: los resultados se integran como ganancias y pérdidas patrimoniales en la base del ahorro, exentos de retención.',
        'ejercicios': [],
    },
    {
        'titulo': 'Impuesto sobre el Patrimonio (IP) y Sucesiones/Donaciones (ISD)',
        'cuerpo': '- **[[IP (Impuesto sobre el Patrimonio)::impuesto que grava el valor total de lo que posee una persona (su patrimonio neto) a 31 de diciembre, por encima de un mínimo exento. Está cedido a las comunidades autónomas]]**: grava el patrimonio neto a 31 de diciembre. Mínimo exento estatal de 700.000 € (más hasta 300.000 € por vivienda habitual). Los planes de pensiones y seguros que no admiten rescate están exentos. Límite conjunto de cuota IRPF-IP del 60% de las bases del IRPF.\n- **[[ISD (Impuesto sobre Sucesiones y Donaciones)::impuesto que se paga al recibir bienes gratis: por herencia (sucesión) o por regalo en vida (donación). Cedido a las comunidades, con enormes diferencias territoriales]]**: grava las transmisiones gratuitas. Sucesiones (mortis causa) grava herencias y seguros de vida por fallecimiento; Donaciones (inter vivos) grava donaciones y seguros en vida (cuando tomador ≠ beneficiario). Tiene reducciones y bonificaciones autonómicas según el parentesco (Grupos I a IV).',
        'ejercicios': [],
    },
    {
        'titulo': 'Mecanismo de compensación en la base del ahorro',
        'cuerpo': 'La base del ahorro tiene dos compartimentos: los rendimientos del capital mobiliario y las ganancias/pérdidas patrimoniales. Dentro de cada uno se compensan pérdidas y ganancias. Si un compartimento queda negativo, puede compensar el saldo positivo del otro con un **límite máximo del 25%** de ese saldo positivo. Las pérdidas sobrantes se compensan en los **4 ejercicios** siguientes.',
        'ejercicios': [],
    },
    {
        'titulo': 'Exenciones destacadas',
        'cuerpo': '- **Reinversión en vivienda habitual**: la ganancia por vender la vivienda habitual queda exenta si el importe total se reinvierte en otra vivienda habitual en dos años.\n- **Mayores de 65 años**: exención de la plusvalía por venta de la vivienda habitual. Para otros activos, exención si el importe de la venta se destina a constituir una renta vitalicia asegurada en 6 meses (límite 240.000 €).',
        'ejercicios': [],
    },
    {
        'titulo': 'El IRPF como impuesto personal, directo y progresivo',
        'cuerpo': 'El IRPF es **personal** (atiende a las circunstancias personales y familiares), **directo** (recae sobre la renta como muestra directa de capacidad económica) y **[[impuesto progresivo::impuesto en el que el tipo medio crece a medida que aumenta la renta: quien más gana paga proporcionalmente más]]** (el tipo medio crece con la base). El [[hecho imponible::el acto o situación que, según la ley, obliga a pagar un impuesto; en el IRPF, obtener renta]] es la obtención de renta. Existen rentas no sujetas, rentas exentas y opera la presunción de onerosidad. El esquema de liquidación parte de la renta, la clasifica en base general y del ahorro, aplica reducciones (base liquidable), la escala (cuota íntegra), las deducciones (cuota líquida) y las retenciones y pagos a cuenta (cuota diferencial).',
        'ejercicios': [],
    },
    {
        'titulo': 'Rendimientos del capital mobiliario (RCM)',
        'cuerpo': 'Los [[RCM (rendimientos del capital mobiliario)::lo que "paga" un activo financiero por tenerlo, sin necesidad de venderlo: intereses, dividendos, cupones o el rescate de un seguro. Tributan en la base del ahorro]] son las rentas que produce tu capital financiero:\n- **Intereses** de cuentas, depósitos y bonos.\n- **Dividendos** y participaciones en beneficios.\n- **Cupones** de renta fija.\n- Rendimientos de seguros de vida-ahorro y unit linked al rescatar.\n\nTodos se integran en la base del ahorro y llevan una [[retención::cantidad que se descuenta y se adelanta a Hacienda en el momento de cobrar una renta; luego se resta de la cuota final del impuesto. En RCM y fondos suele ser del 19%]] a cuenta del **19%** (salvo excepciones como las Letras del Tesoro). La retención es un anticipo del impuesto. Rendimiento neto = íntegro − gastos deducibles (en RCM, muy limitados: administración y depósito de valores).',
        'ejercicios': [],
    },
    {
        'titulo': 'Rendimientos del capital inmobiliario',
        'cuerpo': 'Proceden del alquiler de inmuebles que **no** sea actividad económica. Se integran en la **base general** (no en la del ahorro) y tributan al tipo marginal.\n- **Gastos deducibles**: intereses de financiación, IBI, conservación y reparación, amortización (3% sobre el mayor del valor catastral de construcción o el coste), suministros, comunidad, seguros. Intereses + reparación no pueden dar rendimiento neto negativo del propio inmueble (el exceso se traslada 4 años).\n- **Reducción por arrendamiento de vivienda**: sobre el rendimiento neto positivo, con carácter general del **60%** (la normativa vigente contempla 50%, 60%, 70% o 90% según zonas tensionadas y condiciones). No aplica a alquiler turístico ni de locales.\n- **[[imputación de rentas inmobiliarias::renta "ficticia" que Hacienda te obliga a declarar por tener un inmueble urbano vacío (que no sea tu vivienda habitual), aunque no lo alquiles: el 2% del valor catastral, o el 1,1% si se revisó hace poco]]**: los inmuebles urbanos no arrendados ni afectos (salvo la vivienda habitual) imputan una renta del **2%** del valor catastral (**1,1%** si se revisó en los últimos 10 años).',
        'ejercicios': [],
    },
    {
        'titulo': 'Ganancias y pérdidas patrimoniales',
        'cuerpo': 'Surgen cuando **vendes** un elemento de tu patrimonio y hay diferencia entre lo que te dan y lo que te costó:\n$$G/P = Valor\\ de\\ transmisi\\acute{o}n - Valor\\ de\\ adquisici\\acute{o}n$$\nLas ganancias por **transmisión** van a la base del ahorro. Las que **no** derivan de transmisión (premios, subvenciones) van a la base general.\n- **[[regla FIFO::regla que, al vender parte de unas acciones o participaciones iguales, considera vendidas primero las que compraste antes (First In, First Out). Determina qué precio de compra se usa para calcular la ganancia]]**: en valores homogéneos se venden primero los adquiridos en fecha más antigua.\n- **[[norma antiaplicación::regla que impide computar la pérdida por vender un valor si se recompra el mismo (o uno igual) en un plazo corto (2 meses en cotizados, 1 año en no cotizados). Evita "vender para apuntarse la pérdida" y recomprar]] (recompra)**: no se computan como pérdidas las de la venta de valores si se han recomprado valores homogéneos **dentro de los 2 meses** anteriores o posteriores (**1 año** en no cotizados). La pérdida queda diferida hasta vender los recomprados. Regla análoga para RCM negativos.\n- **Coeficientes de abatimiento**: régimen transitorio para elementos adquiridos antes del 31-12-1994, con límite de 400.000 € de valor de transmisión acumulado.',
        'ejercicios': [],
    },
    {
        'titulo': 'Integración y compensación de rentas (esquema)',
        'cuerpo': '- **Base general**: se integran y compensan los rendimientos (trabajo, capital inmobiliario, actividades) y las ganancias/pérdidas que no derivan de transmisión. El saldo negativo de estas compensa hasta el **25%** del saldo positivo de rendimientos.\n- **Base del ahorro**: dos compartimentos, RCM y ganancias/pérdidas por transmisión. Cada uno se compensa internamente; si uno es negativo, compensa el positivo del otro con **límite del 25%**. El exceso se traslada a los **4 ejercicios** siguientes.',
        'ejercicios': [],
    },
    {
        'titulo': 'Ejemplos de liquidación por tramos (escala del ahorro)',
        'cuerpo': 'Escala: 19% (hasta 6.000 €), 21% (6.000-50.000 €), 23% (50.000-200.000 €), 27% (200.000-300.000 €), 28% (más de 300.000 €).\n**Ejemplo A — base del ahorro de 10.000 €:**\n$$Cuota = 6.000 \\times 0{,}19 + 4.000 \\times 0{,}21 = 1.140 + 840 = 1.980\\ \\text{€}$$\n**Ejemplo B — base del ahorro de 60.000 €:**\n$$Cuota = 6.000 \\times 0{,}19 + 44.000 \\times 0{,}21 + 10.000 \\times 0{,}23 = 12.680\\ \\text{€}$$\n**Ejemplo C — base del ahorro de 250.000 €:**\n$$Cuota = 6.000 \\times 0{,}19 + 44.000 \\times 0{,}21 + 150.000 \\times 0{,}23 + 50.000 \\times 0{,}27 = 58.380\\ \\text{€}$$',
        'ejercicios': [],
    },
    {
        'titulo': 'Tributación detallada por producto',
        'cuerpo': '- **Depósitos y cuentas**: intereses = RCM, retención 19%, base del ahorro. En IP se declaran por el mayor entre el saldo a 31-12 y el saldo medio del último trimestre.\n- **Acciones**: dividendos = RCM (retención 19%); venta = ganancia/pérdida patrimonial **sin retención**, con FIFO y norma antiaplicación (2 meses). El scrip dividend en acciones liberadas no tributa hasta la venta (reduce el coste unitario); si se vende el derecho, ganancia patrimonial.\n- **Renta fija (bonos, obligaciones, Letras)**: cupones = RCM con retención; transmisión/amortización = **RCM** (no ganancia patrimonial). Letras del Tesoro: RCM sin retención en origen.\n- **Fondos de inversión (IIC)**: reembolso = ganancia/pérdida patrimonial en base del ahorro con **retención del 19%**; [[diferimiento por traspaso::ventaja fiscal de los fondos para personas físicas: cambiar el dinero de un fondo a otro no tributa; solo se paga al reembolsar finalmente a efectivo]] (no tributa el traspaso entre fondos, conservando valor y antigüedad); FIFO.\n- **Planes de pensiones**: las aportaciones **reducen la base general** (límite 1.500 € anuales, ampliable). El exceso no reducido se traslada a los **5 ejercicios** siguientes. Las prestaciones tributan como **rendimientos del trabajo** en la base general (posible reducción del 40% por aportaciones anteriores a 1-1-2007 rescatadas en capital). En caso de fallecimiento, las prestaciones al beneficiario tributan en **IRPF** del beneficiario (no en ISD).\n- **Seguros de vida-ahorro y unit linked**: rescate por el tomador = **RCM** (capital − primas) en base del ahorro. Rentas vitalicias/temporales: solo tributa un porcentaje según edad o duración. **PIAS**: exención si se percibe como renta vitalicia. **SIALP/CIALP**: exención total de la rentabilidad si se mantiene 5 años y la aportación anual no supera 5.000 €.\n- **Derivados (futuros, opciones)**: resultado = ganancia/pérdida patrimonial en base del ahorro, sin retención.',
        'ejercicios': [],
    },
    {
        'titulo': 'Impuesto sobre el Patrimonio (IP) — liquidación',
        'cuerpo': 'Grava el patrimonio neto a 31 de diciembre. **Mínimo exento** general estatal de 700.000 € (más hasta 300.000 € por vivienda habitual). Escala progresiva estatal del **0,2% al 3,5%** (modificable por las CCAA). Exentos los bienes afectos a actividades económicas, las participaciones en empresa familiar que cumplan requisitos y los derechos consolidados en planes de pensiones. **Límite conjunto IRPF+IP**: la suma de cuotas no puede exceder el **60%** de la base imponible del IRPF. El [[ITSGF (Impuesto de Solidaridad de las Grandes Fortunas)::impuesto estatal complementario del Impuesto sobre el Patrimonio que grava los patrimonios netos superiores a 3 millones de euros; se descuenta lo ya pagado por IP]] grava patrimonios netos superiores a 3.000.000 €, deduciéndose la cuota ya pagada por IP.',
        'ejercicios': [],
    },
    {
        'titulo': 'Impuesto sobre Sucesiones y Donaciones (ISD)',
        'cuerpo': 'Impuesto **directo, personal y progresivo** sobre los incrementos patrimoniales obtenidos gratis por personas físicas. Tres hechos imponibles: adquisiciones mortis causa (herencias), inter vivos (donaciones) y percepción de seguros de vida por fallecimiento cuando contratante y beneficiario son distintos. La cuota depende de la base, la escala progresiva, el **coeficiente multiplicador** (según parentesco y patrimonio previo) y las reducciones. Grupos de parentesco: **I** (descendientes < 21 años), **II** (descendientes ≥ 21, cónyuge, ascendientes), **III** (colaterales de 2.º y 3.er grado), **IV** (resto). Cedido a las CCAA, que pueden aplicar bonificaciones muy relevantes (cercanas al 99% para Grupos I y II en muchas).',
        'ejercicios': [],
    },
    {
        'titulo': 'Impuesto sobre Sociedades (IS) — nociones',
        'cuerpo': 'El [[IS (Impuesto sobre Sociedades)::impuesto que pagan las empresas (personas jurídicas) sobre sus beneficios. El tipo general es del 25%; las IIC que cumplen requisitos tributan al 1%]] grava la renta de las personas jurídicas residentes. La base parte del resultado contable, corregido por ajustes fiscales. **Tipo general del 25%**; reducidos para nuevas y de reducida dimensión; **1%** para las IIC que cumplan requisitos. Incentivos: exención por doble imposición de dividendos y plusvalías de participaciones significativas (≥ 5%), deducciones por I+D+i. La renta de la sociedad tributa en IS y, al repartirse como dividendo, tributa de nuevo en el IRPF del socio.',
        'ejercicios': [],
    },
    {
        'titulo': 'Impuesto sobre la Renta de no Residentes (IRNR) — nociones',
        'cuerpo': 'Grava las rentas obtenidas en España por no residentes. La residencia fiscal se determina por permanencia > 183 días o centro de intereses económicos en España. Puede operar con o sin establecimiento permanente. Los [[convenio de doble imposición::acuerdo entre dos países para evitar que una misma renta pague impuestos completos en ambos; reparte el derecho a gravar y limita la retención en el país de origen]]s limitan la tributación en origen. Tipo general del 24% (19% para residentes UE/EEE y para dividendos, intereses y ganancias).',
        'ejercicios': [],
    },
    {
        'titulo': 'Intuición de los conceptos clave',
        'cuerpo': '- **Base general frente a base del ahorro**: dos cajas separadas. En la **general** cae lo que procede de tu esfuerzo o actividad ordinaria (nómina, pensiones, alquileres) y tributa a tipos altos (marginales del 45%-50%). En la del **ahorro** cae el fruto de tu capital financiero (dividendos, intereses, cupones, plusvalías) y tributa más suave (19%-28%). Regla de oro: el trabajo y los alquileres van a la general; el fruto del capital financiero, al ahorro.\n- **RCM**: es lo que te paga el activo por tenerlo (cupón, dividendo, interés, rescate de seguro), sin vender.\n- **Ganancias y pérdidas patrimoniales**: es lo que aflora cuando **transmites** (vendes) el activo.\n- **Compensación**: dentro del ahorro, las pérdidas de una caja pueden tapar ganancias de la otra, pero solo hasta el **25%** del saldo positivo; el resto se guarda **4 años**.\n- **Tributación por producto**: identifica si genera RCM (depósito, bono, dividendo) o ganancia patrimonial (acción vendida, fondo reembolsado, derivado), y si lleva retención (fondos y RCM llevan 19%; venta de acciones y derivados no).\n- **IP e ISD**: IP grava *tener* patrimonio a 31-12; ISD grava *recibir* gratis (herencia o donación). Ambos cedidos a las CCAA, con grandes diferencias territoriales.',
        'ejercicios': [],
    },
    {
        'titulo': 'Más ejemplos resueltos de liquidación por tramos',
        'cuerpo': '**Ejemplo D — base del ahorro de 300.000 €:**\n$$Cuota = 6.000 \\times 0{,}19 + 44.000 \\times 0{,}21 + 150.000 \\times 0{,}23 + 100.000 \\times 0{,}27 = 71.880\\ \\text{€}$$\n**Ejemplo E — base del ahorro de 400.000 €:**\n$$Cuota = 71.880 + 100.000 \\times 0{,}28 = 99.880\\ \\text{€}$$\nEl tramo del 28% solo se aplica al exceso **sobre 300.000 €**, nunca a toda la base. El tipo medio efectivo (99.880 / 400.000 = 24,97%) siempre es inferior al marginal (28%).',
        'ejercicios': [],
    },
    {
        'titulo': 'Ejemplos resueltos de compensación en la base del ahorro',
        'cuerpo': '**Ejemplo F — compensación parcial con exceso trasladable.** Saldo de RCM **+10.000 €** y saldo de ganancias/pérdidas patrimoniales **-4.000 €**.\n- El saldo negativo compensa el positivo de RCM solo hasta el **25%** de 10.000 € = **2.500 €**.\n- Base del ahorro = 10.000 - 2.500 = **7.500 €**.\n- Pérdida no compensada = 4.000 - 2.500 = **1.500 €**, trasladable **4 ejercicios**.\n- Cuota: $$6.000 \\times 0{,}19 + 1.500 \\times 0{,}21 = 1.455\\ \\text{€}$$\n**Ejemplo G — compensación total (el límite del 25% no muerde).** Saldo de RCM **+20.000 €** y saldo patrimonial **-3.000 €**.\n- Límite = 25% de 20.000 € = 5.000 € > 3.000 €, luego se compensa la totalidad.\n- Base del ahorro = 20.000 - 3.000 = **17.000 €**. Sin exceso a trasladar.\n- Cuota: $$6.000 \\times 0{,}19 + 11.000 \\times 0{,}21 = 3.450\\ \\text{€}$$\n**Ejemplo H — solo un compartimento.** Ganancias patrimoniales netas por venta de acciones de **250.000 €** (sin RCM). Escala completa: $$1.140 + 9.240 + 34.500 + 13.500 = 58.380\\ \\text{€}$$',
        'ejercicios': [],
    },
    {
        'titulo': 'Errores frecuentes',
        'cuerpo': '- **Aplicar un tipo único a toda la base del ahorro.** La escala es progresiva por tramos: no se multiplica toda la base por el tipo del último tramo. Es el fallo más habitual.\n- **Confundir base general y del ahorro.** Los **alquileres** y las **prestaciones de planes de pensiones** tributan en la base **general**.\n- **Creer que la venta de acciones lleva retención.** No la lleva; sí los reembolsos de **fondos** (19%) y los RCM.\n- **Confundir RCM con ganancia patrimonial en renta fija.** La transmisión o amortización de un bono genera **RCM**, aunque haya "venta".\n- **Olvidar el límite del 25%** en la compensación cruzada, o pretender compensar pérdidas del ahorro con rentas del trabajo (no se puede).\n- **Aportaciones a planes de pensiones como deducción en cuota.** No: **reducen la base general**, no la cuota.\n- **Ignorar la norma antiaplicación (2 meses / 1 año).**\n- **Olvidar el diferimiento por traspaso de fondos.** Traspasar entre fondos no tributa; solo el reembolso final.\n- **Dar por exento el IP en toda España.** El mínimo exento estatal es 700.000 €, pero cada CCAA puede bonificar casi al 100%.',
        'ejercicios': [],
    },
    {
        'titulo': 'Claves de examen',
        'cuerpo': '- Memoriza la **escala del ahorro**: 19% / 21% / 23% / 27% / 28% con umbrales 6.000 / 50.000 / 200.000 / 300.000 €.\n- Umbrales de compensación: **25%** cruzada y traslado a **4 ejercicios**; las aportaciones no reducidas de planes de pensiones se trasladan **5 ejercicios**.\n- Retenciones típicas: **19%** sobre RCM y sobre reembolsos de fondos; **0%** en venta de acciones y derivados; Letras del Tesoro sin retención en origen.\n- **FIFO** obligatorio en acciones y fondos; **norma antiaplicación** 2 meses (cotizados) / 1 año (no cotizados).\n- Exenciones estrella: **reinversión en vivienda habitual** (2 años), **mayores de 65 años** con renta vitalicia (6 meses, tope 240.000 €), **SIALP/CIALP** (5 años, aportación ≤ 5.000 €/año), **PIAS** (renta vitalicia).\n- IP: mínimo exento **700.000 €** + **300.000 €** vivienda habitual; límite conjunto IRPF+IP **60%**; **ITSGF** para patrimonios netos > **3.000.000 €**.\n- ISD: grupos de parentesco **I-IV**; impuesto **cedido** a las CCAA; los seguros de vida por fallecimiento (tomador ≠ beneficiario) van a **ISD**, no a IRPF.\n- IS: tipo general **25%**; **1%** para IIC que cumplen requisitos.',
        'ejercicios': [],
    },
]
