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

APUNTES = '### M5: Pensiones y Jubilación\n\nLa planificación financiera de la jubilación combina las prestaciones públicas de la seguridad social y el ahorro previsional privado a través de planes de pensiones e instrumentos alternativos.\n\n#### 1. Sistema Público de Pensiones en España\nEl sistema es de reparto (las cotizaciones de los trabajadores activos sufragan las pensiones de los jubilados actuales) y está sujeto a reformas periódicas que vinculan la cuantía de la pensión a la edad de jubilación obligatoria (progresiva hasta los 67 años en 2027) y los años cotizados. La base reguladora de la pensión contributiva se calcula con las bases de cotización de los últimos 25 años.\n\n#### 2. Planes y Fondos de Pensiones Privados\nSon instituciones de previsión social complementarias. Sus aportaciones son acumulativas y permanecen bloqueadas en un Fondo de Pensiones hasta la ocurrencia de contingencias (jubilación, incapacidad laboral, dependencia o fallecimiento).\n- **Sistemas**: Individual (contratado por el ciudadano), de Empleo (promovido por una empresa para sus empleados) y Asociado (promovido por una asociación).\n- **Modalidades**:\n  - *Aportación definida*: Se conoce la aportación a realizar, pero el beneficio final dependerá de la evolución de las inversiones. El partícipe asume el riesgo financiero.\n  - *Prestación definida*: Se garantiza una cuantía de jubilación determinada. El promotor asume el riesgo actuarial y de rentabilidad. Solo permitido en planes de empleo.\n\n#### 3. Supuestos Excepcionales de Liquidez\nPor ley, los planes de pensiones son ilíquidos, pero se pueden rescatar de forma anticipada bajo los siguientes supuestos excepcionales:\n1. Desempleo de larga duración (agotar prestaciones contributivas).\n2. Enfermedad grave del partícipe, cónyuge o descendientes directos.\n3. Antigüedad de las aportaciones superior a 10 años (disponible para aportaciones antiguas).\n\n#### 4. Fiscalidad del Plan de Pensiones en España\n- **Aportaciones**: Las aportaciones anuales reducen directamente la base imponible general del IRPF del contribuyente, con el límite del menor de: 1.500 € anuales (ampliables en planes de empleo) o el 30% de los rendimientos netos del trabajo y actividades económicas.\n- **Rescate**: Todas las prestaciones recibidas de un plan de pensiones (sea en capital, renta o mixto) tributan en el IRPF de forma íntegra como **rendimientos del trabajo** en la base general, aplicando el tipo de gravamen marginal del contribuyente. Existe una reducción transitoria del 40% para el cobro en forma de capital de derechos acumulados con anterioridad al 31 de diciembre de 2006, siempre que se rescate en los plazos legalmente fijados tras la jubilación.\n\n#### 5. La teoría de los tres pilares\nLa previsión social se estructura en tres pilares complementarios:\n- **Primer pilar (público y obligatorio)**: pensión contributiva de la Seguridad Social, financiada por reparto. Incluye también las pensiones no contributivas (asistenciales) para quienes carecen de cotización suficiente.\n- **Segundo pilar (empresarial)**: previsión social complementaria promovida por las empresas para sus empleados (planes de pensiones de empleo, PPSE y seguros colectivos).\n- **Tercer pilar (individual y voluntario)**: ahorro-previsión privado del ciudadano (planes de pensiones individuales, PPA, PIAS, seguros de vida-ahorro, etc.).\n\n#### 6. Reparto vs. capitalización\n- **Sistema de reparto**: las cotizaciones de los activos financian las pensiones de los actuales pensionistas (solidaridad intergeneracional). Es el modelo del sistema público español y es sensible a la demografía (envejecimiento, ratio cotizantes/pensionistas).\n- **Sistema de capitalización**: cada partícipe acumula un fondo con sus propias aportaciones y su rentabilidad, del que percibirá su prestación futura. Es el modelo de los planes de pensiones privados.\n\n#### 7. Definición: Plan vs. Fondo de Pensiones\n- **Plan de Pensiones**: es el contrato o instrumento jurídico que define el derecho de las personas a percibir prestaciones y las obligaciones de contribuir.\n- **Fondo de Pensiones**: es el patrimonio (vehículo financiero, sin personalidad jurídica) creado para dar cumplimiento a los planes integrados en él. Un fondo puede integrar varios planes. La gestión corresponde a una Entidad Gestora y la custodia a una Entidad Depositaria.\n\n#### 8. Principios rectores (cinco principios básicos)\nTodo plan de pensiones debe cumplir:\n1. **No discriminación**: acceso garantizado a cualquier persona que cumpla las condiciones de vinculación.\n2. **Capitalización**: se financian mediante sistemas financieros y actuariales de capitalización.\n3. **Irrevocabilidad de aportaciones** del promotor.\n4. **Atribución de derechos**: las contribuciones generan derechos consolidados para el partícipe.\n5. **Integración obligatoria** en un fondo de pensiones.\n\n#### 9. Elementos personales\n- **Promotor**: crea/insta el plan (empresa, asociación o entidad financiera).\n- **Partícipes**: personas físicas en cuyo interés se crea el plan y que realizan (o en cuyo nombre se realizan) las aportaciones.\n- **Partícipes en suspenso**: han cesado en las aportaciones pero mantienen sus derechos consolidados.\n- **Beneficiarios**: personas con derecho a percibir las prestaciones, hayan sido o no partícipes.\n\n#### 10. Modalidades de los planes de pensiones\n- **Por el sujeto promotor**: individual, de empleo y asociado.\n- **Por las obligaciones estipuladas**: aportación definida, prestación definida (solo empleo) y mixtos.\n- **Por la vocación inversora**: renta fija, renta fija mixta, renta variable, renta variable mixta y garantizados.\n\n#### 11. PPES/PPSE y PEPP\n- **Planes de Pensiones de Empleo Simplificados (PPES/PPSE)**: creados para facilitar la previsión del segundo pilar a autónomos, pymes y empleados públicos, con tramitación simplificada. Los autónomos pueden aportar un límite adicional específico (hasta 4.250 € anuales) sobre el límite general.\n- **Producto Paneuropeo de Pensiones Individuales (PEPP)**: producto de ahorro-previsión voluntario de ámbito europeo, portable entre países de la UE, con un producto básico de bajo coste (comisión máxima limitada) y transparencia armonizada.\n\n#### 12. Contingencias cubiertas\nLas prestaciones solo pueden percibirse al producirse una contingencia:\n1. **Jubilación** (o edad equivalente si no cabe el acceso a la jubilación).\n2. **Incapacidad laboral permanente** total, absoluta o gran invalidez.\n3. **Fallecimiento** del partícipe o beneficiario (genera prestaciones de viudedad, orfandad o a favor de herederos).\n4. **Dependencia severa o gran dependencia** del partícipe.\nLa prestación puede cobrarse en forma de **capital** (pago único), **renta** (financiera o actuarial), **mixta** o mediante disposiciones sin periodicidad regular.\n\n#### 13. PPA (Planes de Previsión Asegurados) y su comparación con el PP\nEl **PPA** es un seguro de vida-ahorro cuyo tomador, asegurado y beneficiario es el propio contribuyente y que, a efectos fiscales y de contingencias/liquidez, se asimila a un plan de pensiones (mismos límites de reducción, mismas contingencias y supuestos de liquidez, movilización recíproca con PP). La diferencia esencial: el **PPA garantiza contractualmente un tipo de interés mínimo** (rentabilidad asegurada), mientras que el plan de pensiones individual de aportación definida **no garantiza** rentabilidad (el partícipe asume el riesgo de la inversión). Ambos comparten el mismo límite conjunto de reducción en la base imponible general.\n\n#### 14. Planificación financiera de la jubilación\nEl objetivo es cubrir la pérdida de poder adquisitivo al pasar de rentas de activo a rentas de clase pasiva.\n- **Tasa de reemplazo (o de sustitución)**: mide qué porcentaje de los últimos ingresos por trabajo cubre la primera pensión.\n$$ \\text{Tasa de reemplazo} = \\frac{\\text{Primera pensión}}{\\text{Último salario}} \\times 100 $$\n- **Déficit de jubilación**: diferencia entre los ingresos necesarios (presupuesto de gasto en la jubilación) y los recursos previsibles (pensión pública + rentas del ahorro acumulado).\n$$ \\text{Déficit} = \\text{Necesidades de renta} - \\text{Recursos disponibles (pensión pública + ahorro)} $$\n- **Capitalización del ahorro**: el capital acumulado por aportaciones periódicas constantes (renta pospagable) al tipo de interés $i$ durante $n$ periodos:\n$$ C_n = A \\cdot \\frac{(1+i)^n - 1}{i} $$\ndonde $A$ es la aportación periódica. Un capital único $C_0$ crece por capitalización compuesta hasta:\n$$ C_n = C_0 \\cdot (1+i)^n $$\nLas fases recomendadas de planificación son: iniciar el ahorro cuanto antes (efecto del interés compuesto), revisar periódicamente las variables financiero-fiscales y ajustar el perfil de riesgo reduciéndolo a medida que se acerca la jubilación.\n\n#### 15. Intuición de los conceptos clave\n- **Reparto vs. capitalización**: en el *reparto* no hay ahorro individual; lo que cotizas hoy paga la pensión del jubilado de hoy, y confías en que mañana otros paguen la tuya (pacto intergeneracional, sensible a la demografía). En la *capitalización* cada euro que aportas se invierte a tu nombre y crece con interés compuesto: tu pensión sale de tu propia hucha. El sistema público es reparto; los planes privados, capitalización.\n- **Tasa de reemplazo**: es la \"foto\" del salto de nivel de vida al jubilarte. Si cobrabas 100 y la pensión es 70, tu tasa es 70% y tienes un hueco del 30% que llenar con ahorro. Cuanto más alto tu salario, menor suele ser la tasa pública (la pensión tiene un tope máximo), así que los sueldos altos necesitan MÁS ahorro privado.\n- **Sistemas de planes (tres pilares)**: pilar 1 = lo que te da el Estado (obligatorio); pilar 2 = lo que te da tu empresa (planes de empleo); pilar 3 = lo que te das a ti mismo (planes individuales, PPA, PIAS). Se complementan, no se excluyen.\n- **Contingencias**: el plan es una hucha \"con candado\" que solo se abre ante la jubilación, la incapacidad permanente, el fallecimiento o la dependencia severa. Todo lo demás (paro, enfermedad grave, antigüedad >10 años) son \"llaves de emergencia\" (supuestos de liquidez), no contingencias.\n- **Fiscalidad (idea nuclear: DIFERIMIENTO, no exención)**: al aportar rebajas tu base imponible hoy (ahorras tu tipo marginal); al rescatar, todo lo cobrado tributa como rendimiento del trabajo. No es un regalo fiscal, es un aplazamiento: ganas si tu tipo marginal en la jubilación es menor que cuando aportaste, y ganas por el interés compuesto del dinero que Hacienda te \"prestó\" de forma diferida.\n\n#### 16. Ejemplos resueltos\n**Ejemplo 1 - Tasa de reemplazo.** Último salario bruto 40.000 €/año; primera pensión 26.000 €/año.\n$$ \\text{Tasa} = \\frac{26.000}{40.000} \\times 100 = 65\\,\\% $$\nInterpretación: la pensión cubre el 65% del último sueldo; hay un hueco del 35% (14.000 €/año) que debe cubrir el ahorro privado.\n\n**Ejemplo 2 - Capital necesario para la jubilación (valor actual de una renta).** Se quiere complementar la pensión con una renta pospagable de 10.000 €/año durante 20 años, a un tipo del 3%. El capital que hay que tener acumulado en la fecha de jubilación es el valor actual de esa renta:\n$$ C_0 = A \\cdot \\frac{1-(1+i)^{-n}}{i} = 10.000 \\cdot \\frac{1-(1,03)^{-20}}{0,03} \\approx 148.775\\ \\text{€} $$\nEs decir, se necesitan unos 148.775 € el día de la jubilación para poder retirar 10.000 € al año durante 20 años.\n\n**Ejemplo 3 - Déficit de jubilación.** Necesidades de renta estimadas: 30.000 €/año. Pensión pública prevista: 20.000 €/año.\n$$ \\text{Déficit anual} = 30.000 - 20.000 = 10.000\\ \\text{€/año} $$\nEse déficit anual de 10.000 € es lo que debe generar el ahorro privado (con el Ejemplo 2, para 20 años al 3%, exige un capital de ~148.775 €).\n\n**Ejemplo 4 - Aportación con reducción fiscal.** Un contribuyente con tipo marginal del 37% aporta 1.500 € a su plan.\n$$ \\text{Ahorro fiscal} = 1.500 \\times 0,37 = 555\\ \\text{€} \\quad\\Rightarrow\\quad \\text{coste neto} = 1.500 - 555 = 945\\ \\text{€} $$\nAporta 1.500 € pero le \"cuestan\" 945 € tras el ahorro en IRPF. Ojo: es diferimiento; al rescatar tributará como rendimiento del trabajo.\n\n**Ejemplo 5 - Acumulación por aportaciones periódicas (valor final de una renta pospagable).** Se aportan 2.000 € al final de cada año durante 25 años a un 4%:\n$$ C_n = A \\cdot \\frac{(1+i)^n - 1}{i} = 2.000 \\cdot \\frac{(1,04)^{25}-1}{0,04} \\approx 83.292\\ \\text{€} $$\nSolo se han desembolsado 50.000 € (2.000 × 25); los ~33.292 € restantes son fruto del interés compuesto.\n\n**Ejemplo 6 - Capitalización de un capital único.** 20.000 € invertidos hoy al 4% durante 25 años:\n$$ C_n = C_0 \\cdot (1+i)^n = 20.000 \\cdot (1,04)^{25} \\approx 53.317\\ \\text{€} $$\nEl capital se multiplica por ~2,67 sin aportar un euro más: el poder del tiempo y el interés compuesto.\n\n#### 17. Errores frecuentes\n- **Creer que la reducción del 40% en el rescate es una exención o que se aplica a todo el plan.** Solo afecta a la parte de derechos correspondiente a aportaciones **anteriores a 31/12/2006**, cobrada en forma de **capital** y dentro de los plazos (año de la jubilación y los dos siguientes).\n- **Pensar que el rescate tributa en la base del ahorro (19-28%).** No: siempre tributa como **rendimiento del trabajo en la base general**, al tipo marginal.\n- **Confundir el límite financiero con el límite fiscal.** El límite de **reducción** en IRPF es 1.500 € (o el 30% de los rendimientos netos, el menor), ampliable en planes de empleo; no es el máximo que puedes aportar en términos absolutos en todos los productos de ahorro.\n- **Creer que la prestación por fallecimiento tributa en el Impuesto de Sucesiones.** Nunca: tributa en el **IRPF del beneficiario** como rendimiento del trabajo.\n- **Invertir la tasa de reemplazo.** Es pensión / último salario, no salario / pensión.\n- **Confundir aportación definida con prestación definida.** En aportación definida el riesgo lo asume el **partícipe**; en prestación definida (solo planes de empleo) lo asume el **promotor**.\n- **Mezclar contingencias con supuestos de liquidez.** El paro de larga duración, la enfermedad grave y la antigüedad >10 años NO son contingencias, son supuestos excepcionales de disposición anticipada.\n\n#### 18. Claves de examen\n- **Límite general de reducción**: 1.500 € o 30% de rendimientos netos del trabajo y actividades (el menor).\n- **Ampliaciones**: hasta +8.500 € por contribuciones empresariales a planes de empleo; +4.250 € para autónomos en PPES; +1.000 € al plan del cónyuge (si sus rentas netas < 8.000 €).\n- **Base reguladora** de la pensión pública: bases de cotización de los **últimos 25 años**; edad ordinaria progresiva hasta 67 años (2027).\n- **Contingencias**: jubilación, incapacidad permanente (total/absoluta/gran invalidez), fallecimiento y dependencia severa/gran dependencia.\n- **Supuestos de liquidez extraordinaria**: desempleo de larga duración, enfermedad grave y antigüedad de aportaciones > 10 años.\n- **Traspasos** entre planes (y con PPA): **neutralidad fiscal** (sin retención ni tributación) y conservan la antigüedad.\n- **MEI**: cotización adicional finalista para nutrir el fondo de reserva de la Seguridad Social.\n- **Fórmulas**: valor final de renta pospagable $C_n = A\\,[(1+i)^n-1]/i$; valor actual de renta $C_0 = A\\,[1-(1+i)^{-n}]/i$; capitalización de capital único $C_n = C_0(1+i)^n$; tasa de reemplazo = pensión/último salario.'
