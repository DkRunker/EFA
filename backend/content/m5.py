# Módulo M5 — Pensiones y Planificación de la Jubilación
# PREGUNTAS: cada tupla es (enunciado, [4 opciones], indice_respuesta_correcta, explicacion)
# Ampliar apuntes y preguntas conforme al temario oficial EFPA. NO borrar términos ya existentes.
NOMBRE = 'Pensiones y Planificación de la Jubilación'

PREGUNTAS = [
    (
        '¿Cuál es el límite máximo general de aportación anual con derecho a reducción fiscal en planes de pensiones individuales?',
        ['1.500 € al año', '8.000 € al año', '10.000 € al año', '2.000 € al año'],
        0,
        'En España (salvo regímenes especiales), el límite general de aportación y reducción fiscal a planes de pensiones individuales es de 1.500 € anuales.',
    ),
    (
        '¿Bajo qué supuesto excepcional regulado por ley se puede rescatar un plan de pensiones por antigüedad de las aportaciones?',
        ['Aportaciones con una antigüedad mínima de 10 años', 'Aportaciones de más de 5 años si el partícipe cambia de residencia fiscal', 'Aportaciones con antigüedad de 15 años solo si el partícipe no tiene vivienda en propiedad', 'No existe supuesto por antigüedad, solo se permite el rescate por jubilación'],
        0,
        'La normativa del IRPF en España permite rescatar los derechos consolidados correspondientes a aportaciones con al menos 10 años de antigüedad.',
    ),
    (
        'En un plan de pensiones de prestación definida, ¿quién asume el riesgo actuarial y financiero de la jubilación?',
        ['El promotor del plan de pensiones (generalmente la empresa)', 'El partícipe de forma exclusiva', 'La sociedad gestora de fondos de pensiones', 'El consorcio de compensación de seguros'],
        0,
        'En los planes de prestación definida, el promotor se compromete a una cuantía de prestación fija, asumiendo cualquier déficit del fondo.',
    ),
    (
        '¿Cómo tributa el rescate en forma de capital de las aportaciones realizadas a un plan de pensiones con anterioridad al 31 de diciembre de 2006?',
        ['Se benefician de una reducción del 40% sobre el importe rescatado si se ejerce dentro del plazo legal', 'Tributan exentas de IRPF al clasificarse como rentas no sujetas', 'Tributan en la base del ahorro aplicando el tipo fijo del 19%', 'Se reducen un 50% de la cuota tributaria si el partícipe está jubilado'],
        0,
        'Los derechos consolidados anteriores a 2007 pueden acogerse a una reducción de integración del 40% si se rescatan en el año de jubilación o los dos siguientes.',
    ),
    (
        'En la base reguladora para el cálculo de la pensión de jubilación pública en España, ¿cuántos años de cotización se computan actualmente?',
        ['Los últimos 25 años de cotizaciones del trabajador', 'Toda la vida laboral del cotizante sin excepciones', 'Los mejores 10 años seleccionados por el propio trabajador', 'Los últimos 15 años de cotización reducidos por el IPC medio de la eurozona'],
        0,
        'Actualmente, la base reguladora de la pensión contributiva se calcula a partir de las bases de cotización de los últimos 25 años.',
    ),
    (
        'En España, ¿cuál es el límite máximo de aportación anual que un contribuyente puede realizar al plan de pensiones de su cónyuge con derecho a reducción fiscal?',
        ['1.000 € al año si el cónyuge no tiene rendimientos del trabajo superiores a 8.000 €', '1.500 € al año sin requisitos de rentas del cónyuge', '8.000 € al año siempre que tengan régimen de gananciales', 'No está permitida la reducción fiscal por aportaciones a favor del cónyuge'],
        0,
        'Se permite aportar e integrar hasta 1.000 € anuales al plan del cónyuge si este tiene rentas netas de trabajo y actividades inferiores a 8.000 € anuales.',
    ),
    (
        'Para aplicar la reducción transitoria del 40% en el rescate en forma de capital de planes de pensiones para derechos anteriores a 2007, ¿cuál es el plazo para jubilaciones ocurridas a partir de 2018?',
        ['El año de la contingencia (jubilación) y los dos ejercicios fiscales siguientes', 'El mes posterior a la fecha oficial de jubilación exclusivamente', 'Durante los 5 años naturales posteriores a la jubilación del contribuyente', 'No existe plazo, la reducción se mantiene de por vida sobre esos derechos consolidados'],
        0,
        'La ley limita el incentivo del 40% al año de la contingencia (jubilación) y a los dos ejercicios fiscales siguientes.',
    ),
    (
        '¿Cómo influye el sistema de Planes de Pensiones de Empleo Simplificados (PPES) en el límite general de reducción de aportaciones para autónomos?',
        ['Permite a los autónomos aportar hasta 4.250 € anuales adicionales al plan simplificado, sumando un límite total de 5.750 € al año', 'Exime a los autónomos de tributar por sus rendimientos de actividades económicas', 'Reduce a la mitad el tipo marginal del IRPF para las aportaciones superiores a 1.500 €', 'Permite traspasar fondos a SOCIMIs sin devengo de retención fiscal en el IRPF'],
        0,
        'La ley amplía en 4.250 € el límite general de 1.500 € para aportaciones de trabajadores autónomos a planes de empleo simplificados de su colectivo.',
    ),
    (
        '¿Qué ocurre con los derechos consolidados de un plan de pensiones en caso de fallecimiento del partícipe?',
        ['Los derechos se integran en el patrimonio de los beneficiarios designados (o herederos) y tributan como rendimientos del trabajo en su IRPF', 'Pasan a tributar directamente en el Impuesto sobre Sucesiones y Donaciones (ISD)', 'Son confiscados de forma automática por la entidad gestora al extinguirse la relación actuarial', 'Quedan exentos de tributar si los beneficiarios son descendientes de primer grado menores de edad'],
        0,
        'Las prestaciones por fallecimiento de planes de pensiones nunca tributan por ISD; tributan siempre en el IRPF de los perceptores como rendimientos del trabajo.',
    ),
    (
        'En el cálculo de la pensión de jubilación pública en España, ¿cómo influye el Mecanismo de Equidad Intergeneracional (MEI)?',
        ['Adapta la cuantía inicial de la pensión e incrementa de forma transitoria las cotizaciones para nutrir el fondo de reserva', 'Duplica las bases de cotización de los partícipe menores de 45 años', 'Aumenta la pensión en un 4.0% fijo por cada año trabajado en el sector público', 'Reduce la edad oficial de jubilación contributiva si la tasa de natalidad sube'],
        0,
        "El MEI consiste en una aportación adicional en la cotización para nutrir la hucha de las pensiones y hacer frente a las jubilaciones del 'baby boom'.",
    ),
    (
        'En los planes de pensiones individuales, ¿cuál de las siguientes contingencias permite el rescate de los derechos consolidados?',
        ['Jubilación, incapacidad laboral permanente (total, absoluta o gran invalidez), fallecimiento o dependencia severa/gran dependencia', 'El despido disciplinario del trabajador con derecho a indemnización ordinaria', 'La adquisición de la vivienda habitual por parte de los beneficiarios directos del plan', 'El traslado definitivo de la sede social de la entidad gestora al extranjero'],
        0,
        'Estas son las contingencias tasadas legalmente en la normativa de planes de pensiones para habilitar el rescate ordinario.',
    ),
    (
        '¿Cuál es el límite máximo conjunto de aportación que puede deducirse un trabajador autónomo que aporta a un plan de pensiones de empleo simplificado y a un plan individual?',
        ['5.750 € al año (1.500 € de límite general + 4.250 € de límite específico de empleo simplificado)', '1.500 € al año como tope máximo absoluto sin excepciones de colectivo', '8.500 € al año equivalente al límite de aportación de planes sectoriales de empleo', '10.000 € anuales condicionados al volumen de rendimientos netos de actividades'],
        0,
        'El límite de reducción en el IRPF para autónomos es de 1.500 € para aportaciones individuales, ampliables en hasta 4.250 € adicionales por aportaciones a planes de empleo simplificados.',
    ),
    (
        '¿Qué es un plan de pensiones de aportación definida?',
        ['Un plan donde se conoce de antemano el importe de las aportaciones periódicas, pero no el rendimiento futuro ni la cuantía de la prestación final', 'Un plan que asegura por contrato una rentabilidad real neta superior a la inflación media europea', 'Un plan gestionado en exclusiva por un sindicato o comité de empresa con aportaciones voluntarias de los clientes', 'Un plan cuyos gastos y comisiones están definidos y garantizados al 0.05% anual'],
        0,
        'En aportación definida el partícipe asume el riesgo financiero de la evolución del fondo, conociéndose solo la aportación periódica comprometida.',
    ),
    (
        'En España, ¿cómo tributa en el IRPF el traspaso de derechos consolidados entre planes de pensiones de diferentes gestoras?',
        ['El traspaso está exento de retención e impuesto (neutralidad fiscal) y conserva la antigüedad de las aportaciones', 'Tributa inmediatamente al tipo fijo de retención a cuenta de actividades profesionales (15%)', 'Se le aplica el gravamen de la escala del ahorro sobre los rendimientos implícitos acumulados', 'Se permite la exención solo si el traspaso se completa en un plazo máximo de 24 horas'],
        0,
        'Al igual que con los fondos de inversión, la legislación española permite la libre movilización entre planes de pensiones sin devengo fiscal.',
    ),
    (
        'Según la teoría de los tres pilares de la previsión social, ¿a qué pilar corresponde un plan de pensiones individual contratado voluntariamente por un ciudadano?',
        ['Al tercer pilar (previsión privada e individual)', 'Al primer pilar (sistema público obligatorio)', 'Al segundo pilar (previsión social empresarial)', 'A ningún pilar, ya que los planes individuales quedan fuera del esquema de previsión'],
        0,
        'El primer pilar es la pensión pública de reparto; el segundo es la previsión empresarial (planes de empleo); el tercero es el ahorro-previsión privado y voluntario, donde se enmarca el plan de pensiones individual.',
    ),
    (
        '¿Qué mide la tasa de reemplazo (o de sustitución) en la planificación de la jubilación?',
        ['El porcentaje que representa la primera pensión respecto del último salario percibido', 'El número de años que restan hasta alcanzar la edad legal de jubilación', 'La proporción de cotizantes activos por cada pensionista del sistema de reparto', 'El porcentaje de las aportaciones que reduce la base imponible del IRPF'],
        0,
        'La tasa de reemplazo relaciona la primera pensión con el último salario (pensión / último salario x 100) y estima la pérdida de poder adquisitivo al jubilarse.',
    ),
    (
        '¿Cuál es la diferencia esencial entre un Plan de Previsión Asegurado (PPA) y un plan de pensiones individual de aportación definida?',
        ['El PPA garantiza contractualmente un tipo de interés mínimo, mientras que el plan de aportación definida no garantiza rentabilidad', 'El PPA no permite reducir la base imponible del IRPF, a diferencia del plan de pensiones', 'El PPA puede rescatarse libremente en cualquier momento sin necesidad de contingencia', 'El PPA tributa en la base del ahorro, mientras que el plan de pensiones tributa como rendimiento del trabajo'],
        0,
        'El PPA es un seguro que asimila su fiscalidad, contingencias y liquidez al plan de pensiones, pero se distingue por ofrecer una rentabilidad mínima garantizada por contrato.',
    ),
    (
        'En un sistema público de pensiones basado en el reparto, ¿cómo se financian las pensiones de los jubilados actuales?',
        ['Con las cotizaciones sociales de los trabajadores en activo en ese momento', 'Con un fondo de capitalización individual acumulado por cada pensionista a lo largo de su vida laboral', 'Exclusivamente con los rendimientos de las inversiones del fondo de reserva', 'Con las aportaciones voluntarias que realizan las empresas a los planes de empleo'],
        0,
        'En el sistema de reparto existe solidaridad intergeneracional: las cotizaciones de los activos sufragan las pensiones vigentes, lo que lo hace sensible a la evolución demográfica.',
    ),
    (
        'Un partícipe que ha cesado de realizar aportaciones a su plan de pensiones pero mantiene sus derechos consolidados en el fondo, ¿qué figura de los elementos personales representa?',
        ['Partícipe en suspenso', 'Beneficiario', 'Promotor', 'Entidad depositaria'],
        0,
        'El partícipe en suspenso es aquel que ha dejado de aportar pero conserva sus derechos consolidados; el beneficiario percibe prestaciones y el promotor insta la creación del plan.',
    ),
    (
        'Un ahorrador aporta cantidades constantes al final de cada año a un producto de previsión que capitaliza a un tipo de interés compuesto. ¿Qué expresión permite obtener el capital acumulado al cabo de n años?',
        ['El valor final de una renta pospagable: C = A · [(1+i)^n − 1] / i', 'El descuento simple del salario medio de los últimos 25 años', 'El producto del número de años por la aportación anual, sin capitalización', 'La tasa de reemplazo multiplicada por el último salario percibido'],
        0,
        'La acumulación de aportaciones periódicas constantes que capitalizan responde al valor final de una renta (pospagable), C = A · [(1+i)^n − 1] / i, donde se aprecia el efecto del interés compuesto.',
    ),
    (
        'Un trabajador percibía un último salario bruto de 40.000 €/año y su primera pensión de jubilación es de 26.000 €/año. ¿Cuál es su tasa de reemplazo?',
        ['150%', '65%', '35%', '26%'],
        1,
        'La tasa de reemplazo = primera pensión / último salario × 100 = 26.000 / 40.000 × 100 = 65%. El 35% restante (14.000 €/año) es el hueco que debería cubrir el ahorro privado.',
    ),
    (
        'Un contribuyente con un tipo marginal del IRPF del 37% aporta 1.500 € a su plan de pensiones. ¿Cuál es el ahorro fiscal aproximado que obtiene ese ejercicio?',
        ['1.500 €', '405 €', '555 €', '0 €, porque las aportaciones no reducen la base imponible'],
        2,
        'La aportación reduce la base imponible general, por lo que el ahorro fiscal equivale a la aportación por el tipo marginal: 1.500 × 0,37 = 555 €. El coste neto real de la aportación es 945 €. No obstante, es un diferimiento: al rescatar tributará como rendimiento del trabajo.',
    ),
    (
        'Un ahorrador aporta 3.000 € al final de cada año durante 20 años a un tipo de interés compuesto del 5% anual. ¿Cuál es el capital acumulado aproximado al final?',
        ['60.000 €', '≈ 99.200 €', '≈ 33.000 €', '150.000 €'],
        1,
        'Es el valor final de una renta pospagable: C = A·[(1+i)^n − 1]/i = 3.000 · [(1,05)^20 − 1]/0,05 ≈ 3.000 × 33,066 ≈ 99.200 €. Se aportan 60.000 € y el resto (~39.200 €) es efecto del interés compuesto.',
    ),
    (
        'Se desea disponer de una renta pospagable de 12.000 €/año durante 15 años a partir de la jubilación, con un tipo del 4%. ¿Qué capital hay que tener acumulado en la fecha de jubilación?',
        ['180.000 €', '≈ 12.000 €', '≈ 133.400 €', '≈ 240.000 €'],
        2,
        'El capital necesario es el valor actual de la renta: C0 = A·[1 − (1+i)^−n]/i = 12.000 · [1 − (1,04)^−15]/0,04 ≈ 12.000 × 11,118 ≈ 133.400 €.',
    ),
    (
        'Las necesidades de renta estimadas para la jubilación son de 28.000 €/año y la pensión pública prevista es de 19.000 €/año. ¿Cuál es el déficit anual de jubilación a cubrir con ahorro privado?',
        ['47.000 €', '9.000 €', '19.000 €', '0 €, no existe déficit'],
        1,
        'El déficit de jubilación es la diferencia entre las necesidades de renta y los recursos disponibles: 28.000 − 19.000 = 9.000 €/año. Ese importe es el que debe generar el ahorro-previsión privado.',
    ),
    (
        '¿Cuál de las siguientes es una característica del Producto Paneuropeo de Pensiones Individuales (PEPP)?',
        ['Es un plan de prestación definida obligatorio para los funcionarios', 'Garantiza por ley una rentabilidad mínima del 4% anual a todos los partícipes', 'Solo puede contratarse por las empresas para sus empleados del segundo pilar', 'Es un producto de previsión voluntario portable entre países de la UE, con un producto básico de bajo coste y comisión máxima limitada'],
        3,
        'El PEPP es un producto de ahorro-previsión individual (tercer pilar), voluntario, de ámbito europeo y portable entre Estados miembros, con un "PEPP básico" de bajo coste (comisión limitada) y transparencia armonizada.',
    ),
    (
        '¿Cuál es la diferencia conceptual entre un Plan de Pensiones y un Fondo de Pensiones?',
        ['El Plan es el patrimonio invertido y el Fondo es el contrato jurídico', 'Ambos términos son sinónimos y no existe diferencia jurídica', 'El Plan es el contrato que define derechos y obligaciones; el Fondo es el patrimonio, sin personalidad jurídica, que da cumplimiento a los planes integrados en él', 'El Fondo lo gestiona el partícipe y el Plan lo gestiona la Seguridad Social'],
        2,
        'El Plan de Pensiones es el instrumento jurídico (contrato) que regula derechos y obligaciones; el Fondo de Pensiones es el patrimonio, carente de personalidad jurídica, creado para dar cumplimiento a los planes. Un mismo fondo puede integrar varios planes.',
    ),
    (
        '¿Cuál de los siguientes es uno de los cinco principios básicos que debe cumplir todo Plan de Pensiones?',
        ['Revocabilidad de las aportaciones del promotor en cualquier momento', 'Capitalización de las aportaciones mediante sistemas financiero-actuariales', 'Discriminación positiva a favor de los partícipes de mayor renta', 'Integración voluntaria y opcional en un fondo de pensiones'],
        1,
        'Los cinco principios son: no discriminación, capitalización, irrevocabilidad de las aportaciones del promotor, atribución de derechos e integración obligatoria en un fondo. Por tanto, la capitalización es uno de ellos.',
    ),
    (
        '¿Cuál de los siguientes NO es un supuesto excepcional de disposición anticipada (liquidez) de un plan de pensiones?',
        ['Desempleo de larga duración', 'Enfermedad grave del partícipe', 'Aportaciones con más de 10 años de antigüedad', 'Adquisición de la primera vivienda habitual'],
        3,
        'Los supuestos excepcionales de liquidez son el desempleo de larga duración, la enfermedad grave y la antigüedad de las aportaciones superior a 10 años. La compra de vivienda NO es un supuesto de disposición anticipada de planes de pensiones.',
    ),
    (
        'En el IRPF, las prestaciones percibidas de un plan de pensiones (ya sea en forma de capital o de renta) tributan como...',
        ['Rendimientos del capital mobiliario en la base del ahorro', 'Ganancias patrimoniales al tipo fijo del 19%', 'Rendimientos del trabajo en la base general, al tipo marginal del contribuyente', 'Rentas exentas de tributación en todos los casos'],
        2,
        'Todas las prestaciones de planes de pensiones tributan como rendimientos del trabajo en la base general del IRPF, al tipo marginal. Solo existe la reducción transitoria del 40% para derechos anteriores a 2007 rescatados en forma de capital dentro de plazo.',
    ),
    (
        'Se invierten hoy 20.000 € en un producto que capitaliza a un interés compuesto del 4% anual durante 25 años, sin nuevas aportaciones. ¿Cuál es el capital final aproximado?',
        ['≈ 53.300 €', '20.000 €', '≈ 500.000 €', '≈ 25.000 €'],
        0,
        'Capitalización compuesta de un capital único: Cn = C0·(1+i)^n = 20.000 · (1,04)^25 ≈ 20.000 × 2,666 ≈ 53.300 €. El capital se multiplica por ~2,67 solo por el efecto del tiempo y el interés compuesto.',
    ),
]


INTRO = '# M5: Pensiones y Jubilación\n\nUn día dejarás de trabajar, pero seguirás necesitando ingresos para vivir. ¿De dónde saldrán? De dos sitios: la pensión pública (lo que te paga el Estado) y el ahorro que hayas ido acumulando por tu cuenta. Este módulo trata de cómo funciona cada uno y de cómo planificar para que no te falte dinero al jubilarte.'


SECCIONES = [
    {
        'titulo': 'Sistema público de pensiones en España',
        'cuerpo': 'El sistema público español es de [[sistema de reparto::modelo de pensiones en el que lo que cotizan los trabajadores de hoy paga directamente las pensiones de los jubilados de hoy. No hay una hucha personal: es un pacto entre generaciones]]: las cotizaciones de los trabajadores en activo pagan las pensiones de los jubilados actuales. Está sujeto a reformas que vinculan la cuantía a la edad de jubilación (progresiva hasta los 67 años en 2027) y a los años cotizados. La [[base reguladora::media de los sueldos por los que has cotizado durante un número de años (hoy los últimos 25 en España); sobre ella se calcula la cuantía de tu pensión pública]] de la pensión contributiva se calcula con las bases de cotización de los últimos 25 años.',
        'ejercicios': [],
    },
    {
        'titulo': 'Planes y fondos de pensiones privados',
        'cuerpo': 'Como la pensión pública puede no bastar, existe el ahorro privado. Un [[plan de pensiones::producto de ahorro a largo plazo para la jubilación; el dinero queda "con candado" hasta que ocurre una contingencia (jubilarse, incapacidad, dependencia o fallecimiento) y ofrece ventajas fiscales al aportar]] es una institución de previsión social complementaria. Sus aportaciones se acumulan y quedan bloqueadas en un fondo hasta que ocurre una contingencia (jubilación, incapacidad, dependencia o fallecimiento).\n- **Sistemas**: Individual (lo contrata el ciudadano), de Empleo (lo promueve una empresa para sus empleados) y Asociado (lo promueve una asociación).\n- **Modalidades**:\n  - *[[aportación definida::modalidad de plan en la que sabes cuánto aportas, pero no cuánto cobrarás: la prestación final depende de cómo vayan las inversiones. El riesgo lo asume el partícipe]]*: se conoce la aportación, pero el resultado final depende de las inversiones. El partícipe asume el riesgo.\n  - *[[prestación definida::modalidad en la que se garantiza de antemano la cuantía que cobrarás; el riesgo de que las inversiones no basten lo asume quien promueve el plan. Solo se permite en planes de empleo]]*: se garantiza una cuantía de jubilación. El promotor asume el riesgo. Solo en planes de empleo.',
        'ejercicios': [],
    },
    {
        'titulo': 'Supuestos excepcionales de liquidez',
        'cuerpo': 'Los planes son ilíquidos por ley (no puedes sacar el dinero cuando quieras), pero hay "llaves de emergencia" para rescatarlos antes:\n1. Desempleo de larga duración (tras agotar prestaciones contributivas).\n2. Enfermedad grave del partícipe, cónyuge o descendientes directos.\n3. Antigüedad de las aportaciones superior a 10 años.',
        'ejercicios': [],
    },
    {
        'titulo': 'Fiscalidad del plan de pensiones en España',
        'cuerpo': 'La ventaja fiscal es la gran razón para usar planes de pensiones, pero conviene entenderla bien:\n- **Aportaciones**: reducen directamente la [[base imponible general::parte de tu renta sobre la que se calcula el IRPF, que incluye sueldos y otras rentas; se le aplica una escala progresiva por tramos. Reducirla hace pagar menos impuestos]] del IRPF. Límite: el menor de 1.500 € anuales (ampliables en planes de empleo) o el 30% de los rendimientos netos del trabajo y actividades.\n- **Rescate**: todo lo que recibes (en capital, renta o mixto) tributa íntegramente como [[rendimientos del trabajo::tipo de renta en el IRPF que incluye los sueldos y también las prestaciones de los planes de pensiones; tributa en la base general al tipo marginal, no en la del ahorro]] en la base general, al [[tipo marginal::porcentaje de impuesto que se aplica al último tramo de tu renta; es el tipo más alto que pagas y sube conforme ganas más]] del contribuyente. Existe una reducción transitoria del 40% para el cobro en forma de capital de derechos anteriores al 31/12/2006, si se rescata en los plazos legales.\n\nLa idea nuclear: es un [[diferimiento fiscal::aplazamiento del pago de impuestos a un momento futuro. No es un ahorro definitivo: pagarás al rescatar, pero mientras tanto el dinero crece y puede que entonces tu tipo sea menor]], no una exención. Al aportar rebajas tu base hoy; al rescatar, pagas. Ganas si tu tipo marginal en la jubilación es menor que cuando aportaste, y por el interés compuesto entretanto.',
        'ejercicios': [],
    },
    {
        'titulo': 'La teoría de los tres pilares',
        'cuerpo': 'La previsión social se apoya en tres patas que se complementan:\n- **Primer pilar (público y obligatorio)**: la pensión de la Seguridad Social, por reparto. Incluye las pensiones no contributivas para quien no cotizó lo suficiente.\n- **Segundo pilar (empresarial)**: lo que promueven las empresas para sus empleados (planes de empleo, PPSE, seguros colectivos).\n- **Tercer pilar (individual y voluntario)**: el ahorro privado de cada uno (planes individuales, PPA, PIAS, seguros de vida-ahorro).\n\nResumen: pilar 1 = lo que te da el Estado; pilar 2 = lo que te da tu empresa; pilar 3 = lo que te das a ti mismo.',
        'ejercicios': [],
    },
    {
        'titulo': 'Reparto frente a capitalización',
        'cuerpo': '- **Sistema de reparto**: los activos financian a los pensionistas de hoy (solidaridad intergeneracional). Es el modelo público español, muy sensible a la demografía (envejecimiento, ratio cotizantes/pensionistas).\n- **[[sistema de capitalización::modelo en el que cada persona acumula su propio fondo con sus aportaciones y la rentabilidad que generan; su pensión sale de esa hucha personal. Es el modelo de los planes privados]]**: cada partícipe acumula su propio fondo. Es el modelo de los planes privados.',
        'ejercicios': [],
    },
    {
        'titulo': 'Plan frente a fondo de pensiones',
        'cuerpo': 'No es lo mismo (aunque suene igual):\n- **Plan de Pensiones**: el contrato o instrumento jurídico que define derechos y obligaciones.\n- **[[fondo de pensiones::patrimonio (el "saco de dinero") donde se integran las aportaciones de uno o varios planes para invertirlas. No tiene personalidad jurídica; lo gestiona una gestora y lo custodia un depositario]]**: el patrimonio creado para dar cumplimiento a los planes. Un fondo puede integrar varios planes. Lo gestiona una Entidad Gestora y lo custodia un Depositario.',
        'ejercicios': [],
    },
    {
        'titulo': 'Principios rectores (cinco principios básicos)',
        'cuerpo': 'Todo plan debe cumplir:\n1. **No discriminación**: acceso garantizado a quien cumpla las condiciones.\n2. **Capitalización**: se financian con sistemas financieros y actuariales de capitalización.\n3. **Irrevocabilidad** de las aportaciones del promotor.\n4. **Atribución de derechos**: las contribuciones generan [[derechos consolidados::el dinero que un partícipe ha acumulado en su plan y que le pertenece; puede trasladarlo a otro plan aunque no pueda cobrarlo hasta una contingencia]] para el partícipe.\n5. **Integración obligatoria** en un fondo de pensiones.',
        'ejercicios': [],
    },
    {
        'titulo': 'Elementos personales',
        'cuerpo': '- **Promotor**: crea el plan (empresa, asociación o entidad financiera).\n- **Partícipes**: personas en cuyo interés se crea el plan y que realizan las aportaciones.\n- **Partícipes en suspenso**: han dejado de aportar pero mantienen sus derechos consolidados.\n- **Beneficiarios**: quienes tienen derecho a cobrar las prestaciones, hayan sido o no partícipes.',
        'ejercicios': [],
    },
    {
        'titulo': 'Modalidades de los planes de pensiones',
        'cuerpo': '- **Por el promotor**: individual, de empleo y asociado.\n- **Por las obligaciones**: aportación definida, prestación definida (solo empleo) y mixtos.\n- **Por la vocación inversora**: renta fija, renta fija mixta, renta variable, renta variable mixta y garantizados.',
        'ejercicios': [],
    },
    {
        'titulo': 'PPES/PPSE y PEPP',
        'cuerpo': '- **Planes de Pensiones de Empleo Simplificados (PPES/PPSE)**: facilitan la previsión del segundo pilar a autónomos, pymes y empleados públicos. Los autónomos pueden aportar un límite adicional (hasta 4.250 € anuales) sobre el general.\n- **[[PEPP (Producto Paneuropeo de Pensiones Individuales)::producto de ahorro para la jubilación de ámbito europeo, que se puede llevar de un país de la UE a otro, con una versión básica de bajo coste y reglas de transparencia comunes]]**: producto de ahorro-previsión voluntario europeo, portable entre países de la UE, con una versión básica de bajo coste y transparencia armonizada.',
        'ejercicios': [],
    },
    {
        'titulo': 'Contingencias cubiertas',
        'cuerpo': 'Las prestaciones solo se cobran al ocurrir una [[contingencia::hecho previsto por la ley que da derecho a cobrar el plan de pensiones: jubilación, incapacidad permanente, fallecimiento o dependencia severa. Sin uno de ellos, el dinero no se puede rescatar (salvo llaves de emergencia)]]:\n1. **Jubilación** (o edad equivalente).\n2. **Incapacidad laboral permanente** total, absoluta o gran invalidez.\n3. **Fallecimiento** del partícipe o beneficiario (viudedad, orfandad o herederos).\n4. **Dependencia severa o gran dependencia** del partícipe.\n\nLa prestación se cobra en forma de **capital** (pago único), **renta**, **mixta** o mediante disposiciones sin periodicidad regular.',
        'ejercicios': [],
    },
    {
        'titulo': 'PPA y su comparación con el plan de pensiones',
        'cuerpo': 'El **PPA** (Plan de Previsión Asegurado) es un seguro de vida-ahorro que, a efectos fiscales, de contingencias y de liquidez, se asimila a un plan de pensiones (mismos límites de reducción, mismas contingencias, movilización recíproca). La diferencia esencial: el **PPA garantiza contractualmente un tipo de interés mínimo**, mientras que el plan de pensiones individual de aportación definida **no garantiza** rentabilidad. Ambos comparten el mismo límite conjunto de reducción en la base imponible general.',
        'ejercicios': [],
    },
    {
        'titulo': 'Planificación financiera de la jubilación',
        'cuerpo': 'El objetivo es evitar un bajón brusco del nivel de vida al pasar de trabajar a estar jubilado.\n- **[[tasa de reemplazo::porcentaje del último sueldo que cubre la primera pensión. Si cobrabas 100 y la pensión es 70, la tasa es del 70%; el 30% restante es el hueco a cubrir con ahorro]] (o de sustitución)**: qué porcentaje de los últimos ingresos por trabajo cubre la primera pensión.\n$$ \\text{Tasa de reemplazo} = \\frac{\\text{Primera pensión}}{\\text{Último salario}} \\times 100 $$\n- **Déficit de jubilación**: diferencia entre los ingresos que necesitarás y los recursos previsibles (pensión pública + rentas del ahorro).\n$$ \\text{Déficit} = \\text{Necesidades de renta} - \\text{Recursos disponibles (pensión pública + ahorro)} $$\n- **Capitalización del ahorro**: el capital acumulado por aportaciones periódicas constantes (renta pospagable) al tipo $i$ durante $n$ periodos, aprovechando el [[interés compuesto::mecanismo por el que los intereses generan a su vez más intereses; con el tiempo, el crecimiento se acelera. Es el gran aliado del ahorro a largo plazo]]:\n$$ C_n = A \\cdot \\frac{(1+i)^n - 1}{i} $$\ndonde $A$ es la aportación periódica. Un capital único $C_0$ crece por capitalización compuesta hasta:\n$$ C_n = C_0 \\cdot (1+i)^n $$\nRecomendaciones: empezar a ahorrar cuanto antes (interés compuesto), revisar periódicamente las variables y reducir el riesgo a medida que se acerca la jubilación.',
        'ejercicios': [],
    },
    {
        'titulo': 'Intuición de los conceptos clave',
        'cuerpo': '- **Reparto frente a capitalización**: en el reparto, lo que cotizas hoy paga la pensión del jubilado de hoy (pacto intergeneracional, sensible a la demografía). En la capitalización, cada euro que aportas se invierte a tu nombre y crece con interés compuesto. El sistema público es reparto; los planes privados, capitalización.\n- **Tasa de reemplazo**: es la "foto" del salto de nivel de vida al jubilarte. Cuanto más alto tu salario, menor suele ser la tasa pública (la pensión tiene tope), así que los sueldos altos necesitan MÁS ahorro privado.\n- **Contingencias frente a liquidez**: el plan es una hucha con candado que solo se abre ante jubilación, incapacidad permanente, fallecimiento o dependencia severa. El paro, la enfermedad grave y la antigüedad de más de 10 años son "llaves de emergencia", no contingencias.\n- **Fiscalidad (diferimiento, no exención)**: al aportar rebajas tu base hoy; al rescatar, todo lo cobrado tributa como rendimiento del trabajo. Ganas si tu tipo marginal en la jubilación es menor que al aportar.',
        'ejercicios': [],
    },
    {
        'titulo': 'Ejemplos resueltos',
        'cuerpo': '**Ejemplo 1 — Tasa de reemplazo.** Último salario bruto 40.000 €/año; primera pensión 26.000 €/año.\n$$ \\text{Tasa} = \\frac{26.000}{40.000} \\times 100 = 65\\,\\% $$\nLa pensión cubre el 65%; hay un hueco del 35% (14.000 €/año) a cubrir con ahorro privado.\n\n**Ejemplo 2 — Capital necesario (valor actual de una renta).** Se quiere complementar la pensión con 10.000 €/año durante 20 años, al 3%. El capital necesario en la jubilación es el valor actual de esa renta:\n$$ C_0 = A \\cdot \\frac{1-(1+i)^{-n}}{i} = 10.000 \\cdot \\frac{1-(1,03)^{-20}}{0,03} \\approx 148.775\\ \\text{€} $$\n\n**Ejemplo 3 — Déficit de jubilación.** Necesidades: 30.000 €/año. Pensión pública: 20.000 €/año.\n$$ \\text{Déficit anual} = 30.000 - 20.000 = 10.000\\ \\text{€/año} $$\nEse déficit es lo que debe generar el ahorro privado.\n\n**Ejemplo 4 — Aportación con reducción fiscal.** Un contribuyente con tipo marginal del 37% aporta 1.500 €.\n$$ \\text{Ahorro fiscal} = 1.500 \\times 0,37 = 555\\ \\text{€} \\quad\\Rightarrow\\quad \\text{coste neto} = 945\\ \\text{€} $$\nAporta 1.500 € pero le "cuestan" 945 € tras el ahorro en IRPF. Es diferimiento: al rescatar tributará como rendimiento del trabajo.\n\n**Ejemplo 5 — Acumulación por aportaciones periódicas.** Se aportan 2.000 € al final de cada año durante 25 años al 4%:\n$$ C_n = A \\cdot \\frac{(1+i)^n - 1}{i} = 2.000 \\cdot \\frac{(1,04)^{25}-1}{0,04} \\approx 83.292\\ \\text{€} $$\nSolo se desembolsan 50.000 €; los ~33.292 € restantes son fruto del interés compuesto.\n\n**Ejemplo 6 — Capitalización de un capital único.** 20.000 € hoy al 4% durante 25 años:\n$$ C_n = C_0 \\cdot (1+i)^n = 20.000 \\cdot (1,04)^{25} \\approx 53.317\\ \\text{€} $$\nEl capital se multiplica por ~2,67 sin aportar un euro más.',
        'ejercicios': [],
    },
    {
        'titulo': 'Errores frecuentes',
        'cuerpo': '- **Creer que la reducción del 40% del rescate es una exención o que se aplica a todo el plan.** Solo afecta a derechos por aportaciones anteriores al 31/12/2006, cobrados en forma de capital y en plazo.\n- **Pensar que el rescate tributa en la base del ahorro (19-28%).** No: siempre como **rendimiento del trabajo en la base general**, al tipo marginal.\n- **Confundir el límite financiero con el fiscal.** El de reducción en IRPF es 1.500 € (o el 30% de los rendimientos netos, el menor), ampliable en planes de empleo.\n- **Creer que la prestación por fallecimiento tributa en Sucesiones.** Nunca: tributa en el IRPF del beneficiario como rendimiento del trabajo.\n- **Invertir la tasa de reemplazo.** Es pensión / último salario, no al revés.\n- **Confundir aportación definida con prestación definida.** En aportación definida el riesgo lo asume el partícipe; en prestación definida (solo empleo), el promotor.\n- **Mezclar contingencias con supuestos de liquidez.** El paro, la enfermedad grave y la antigüedad de más de 10 años NO son contingencias.',
        'ejercicios': [],
    },
    {
        'titulo': 'Claves de examen',
        'cuerpo': '- **Límite general de reducción**: 1.500 € o 30% de rendimientos netos del trabajo y actividades (el menor).\n- **Ampliaciones**: hasta +8.500 € por contribuciones empresariales a planes de empleo; +4.250 € para autónomos en PPES; +1.000 € al plan del cónyuge (si sus rentas netas < 8.000 €).\n- **Base reguladora** pública: bases de cotización de los últimos 25 años; edad ordinaria progresiva hasta 67 años (2027).\n- **Contingencias**: jubilación, incapacidad permanente, fallecimiento y dependencia severa/gran dependencia.\n- **Supuestos de liquidez extraordinaria**: desempleo de larga duración, enfermedad grave y antigüedad de aportaciones > 10 años.\n- **Traspasos** entre planes (y con PPA): neutralidad fiscal (sin retención ni tributación) y conservan la antigüedad.\n- **[[MEI (Mecanismo de Equidad Intergeneracional)::cotización adicional creada para reforzar el fondo de reserva de la Seguridad Social y ayudar a sostener las pensiones ante el envejecimiento de la población]]**: cotización adicional finalista para nutrir el fondo de reserva de la Seguridad Social.\n- **Fórmulas**: valor final de renta pospagable $C_n = A\\,[(1+i)^n-1]/i$; valor actual de renta $C_0 = A\\,[1-(1+i)^{-n}]/i$; capitalización de capital único $C_n = C_0(1+i)^n$; tasa de reemplazo = pensión/último salario.',
        'ejercicios': [],
    },
]
