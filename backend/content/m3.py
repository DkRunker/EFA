# Módulo M3 — Gestión de Carteras
# PREGUNTAS: cada tupla es (enunciado, [4 opciones], indice_respuesta_correcta, explicacion)
# Ampliar apuntes y preguntas conforme al temario oficial EFPA. NO borrar términos ya existentes.
NOMBRE = 'Gestión de Carteras'

PREGUNTAS = [
    (
        'Según el modelo CAPM, ¿cuál es el único riesgo por el que se remunera al inversor?',
        ['Riesgo sistemático o de mercado (Beta)', 'Riesgo no sistemático o diversificable', 'Riesgo de liquidez', 'Riesgo de crédito'],
        0,
        'El CAPM asume que el riesgo específico puede eliminarse mediante diversificación, por lo que el mercado solo remunera el riesgo sistemático (Beta).',
    ),
    (
        '¿Qué representa la frontera eficiente de Markowitz?',
        ['Las carteras con la máxima rentabilidad para cada nivel de riesgo', 'La combinación óptima con activo libre de riesgo', 'La recta del mercado de capitales (CML)', 'Carteras compuestas solo por renta fija'],
        0,
        'La frontera eficiente representa el conjunto de carteras óptimas que ofrecen el mayor rendimiento esperado para una desviación estándar dada.',
    ),
    (
        '¿Cuál es el Ratio de Sharpe de una cartera con una rentabilidad del 10.0%, desviación estándar del 15.0%, si la tasa libre de riesgo es del 2.0%?',
        ['0.53', '0.67', '0.80', '0.12'],
        0,
        'Calculado como (0.10 - 0.02) / 0.15 = 0.533 (redondeado a 0.53).',
    ),
    (
        'Si una cartera tiene una Beta de 1.5, una rentabilidad del 14.0% y la tasa libre de riesgo es del 2.0%, ¿cuál es su Ratio de Treynor?',
        ['8.00%', '9.33%', '12.00%', '6.00%'],
        0,
        'Calculado como (0.14 - 0.02) / 1.5 = 0.08 o 8.00%.',
    ),
    (
        'El modelo CAPM estima una rentabilidad exigida para un activo del 9.0%. Si la tasa libre de riesgo es del 3.0% y la prima de riesgo del mercado es del 5.0%, ¿cuál es la Beta de dicho activo?',
        ['1.20', '1.00', '0.80', '1.50'],
        0,
        'Resolviendo CAPM: 0.09 = 0.03 + Beta * 0.05 => Beta = (0.09 - 0.03) / 0.05 = 1.20.',
    ),
    (
        '¿Qué indica un Alfa de Jensen (α) positivo en una cartera?',
        ['Que la cartera ha batido al mercado generando un exceso de rendimiento ajustado por su riesgo sistemático', 'Que la volatilidad de la cartera es inferior a la del activo libre de riesgo', 'Que la cartera está perfectamente diversificada y tiene Beta cero', 'Que el rendimiento de la cartera ha subido debido al efecto divisa'],
        0,
        'El Alfa de Jensen mide el rendimiento anormal. Si es positivo, la gestión activa aportó valor por encima del CAPM esperado.',
    ),
    (
        'En la teoría de carteras, ¿qué es el riesgo específico o no sistemático?',
        ['El riesgo propio de una empresa o sector que puede ser eliminado mediante la diversificación', 'El riesgo macroeconómico y de mercado que afecta a todos los activos por igual', 'El riesgo asociado a variaciones en los tipos de interés oficiales', 'La volatilidad histórica del índice de referencia o benchmark'],
        0,
        'Es el riesgo particular de un emisor (ej. huelga, fallo de producto). Se diluye al combinar activos no correlacionados.',
    ),
    (
        '¿Qué mide el Tracking Error de un fondo de inversión de gestión activa?',
        ['La desviación estándar de la diferencia de rentabilidades entre el fondo y su benchmark', 'La rentabilidad acumulada del fondo desde su fecha de constitución', 'La comisión total devengada en relación a los costes de transacción', 'El número de veces que el gestor cambia los componentes de la cartera al año'],
        0,
        'Mide la consistencia de la desviación de la cartera frente a su índice. A mayor tracking error, mayor es la gestión activa.',
    ),
    (
        '¿Cuál es la principal diferencia entre la Capital Market Line (CML) y la Security Market Line (SML)?',
        ['La CML utiliza el riesgo total (desviación estándar) y es aplicable solo a carteras eficientes, mientras que la SML utiliza el riesgo sistemático (Beta) y aplica a carteras y activos individuales', 'La CML evalúa activos individuales y la SML carteras eficientes exclusivamente', 'La CML tiene pendiente negativa y la SML tiene pendiente positiva siempre', 'No hay diferencia, son dos nombres para representar la frontera de Markowitz'],
        0,
        'La SML se deriva del CAPM y aplica a todo tipo de activos usando la Beta. La CML nace de la frontera eficiente usando la desviación típica.',
    ),
    (
        'Si combinamos en una cartera un activo con riesgo y el activo libre de riesgo, ¿qué forma tendrá el conjunto de carteras resultantes en el espacio Rentabilidad-Desviación Estándar?',
        ['Una línea recta que conecta el activo libre de riesgo con la cartera de activos con riesgo', 'Una parábola cóncava similar a la frontera eficiente de activos individuales', 'Una elipse cerrada que representa la covarianza negativa de los activos', 'Una línea quebrada con pendiente descendente hacia la volatilidad cero'],
        0,
        'Al combinar un activo sin riesgo (volatilidad cero) con una cartera de riesgo, la correlación es nula y la relación riesgo-retorno es lineal.',
    ),
    (
        '¿Qué diferencia al Ratio de Sortino del Ratio de Sharpe?',
        ['El Ratio de Sortino utiliza en el denominador la desviación estándar de los retornos negativos (downside deviation), penalizando solo la volatilidad perjudicial', 'El Ratio de Sortino utiliza la Beta en vez de la volatilidad como medida de riesgo', 'El Ratio de Sortino calcula la rentabilidad geométrica en vez de la aritmética', 'El Ratio de Sortino descuenta la inflación en lugar de la tasa libre de riesgo'],
        0,
        'El Ratio de Sortino mide el exceso de retorno sobre el riesgo de pérdidas (downside risk), evitando penalizar la volatilidad al alza de la cartera.',
    ),
    (
        'En la gestión de carteras, ¿en qué consiste la asignación táctica de activos (Tactical Asset Allocation - TAA)?',
        ['En realizar desviaciones deliberadas a corto plazo respecto a la asignación estratégica para aprovechar ineficiencias del mercado', 'En fijar la distribución de activos a largo plazo según el perfil de riesgo del inversor', 'En vender todos los activos ilíquidos en momentos de pánico financiero', 'En comprar exclusivamente bonos del Estado y oro para proteger el patrimonio'],
        0,
        'La TAA busca batir al benchmark tomando posiciones dinámicas a corto plazo, a diferencia de la SAA que fija la estructura estratégica a largo plazo.',
    ),
    (
        '¿Qué representa la pendiente de la Security Market Line (SML) en el CAPM?',
        ['La prima de riesgo del mercado (Rm - Rf)', 'La volatilidad del índice del mercado de acciones', 'El tipo de interés libre de riesgo oficial', 'El recíproco de la Beta media de las carteras eficientes'],
        0,
        'La SML grafica E(R) vs Beta. Su intercepto es Rf y su pendiente es (Rm - Rf), que representa el precio del riesgo sistemático.',
    ),
    (
        '¿Cuál es el Ratio de Información de un fondo de inversión si su rentabilidad anual supera a la del benchmark en un 2.0% y tiene un Tracking Error del 4.0%?',
        ['0.50', '2.00', '0.25', '1.00'],
        0,
        'El Ratio de Información es el cociente de (Rentabilidad Activa / Tracking Error) = 2% / 4% = 0.50.',
    ),
    (
        '¿Cuál es la premisa de la Hipótesis de Eficiencia de los Mercados (EMH) en su forma semifuerte?',
        ['Los precios de las acciones reflejan toda la información histórica disponible y toda la información pública actual de forma inmediata', 'Los precios reflejan únicamente la información histórica de volumen y cotizaciones', 'Los precios incorporan absolutamente toda la información, pública y privada (información confidencial)', 'Los mercados son ineficientes y los gestores activos baten siempre al índice'],
        0,
        'La eficiencia semifuerte indica que el análisis fundamental y la información pública ya están descontados en el precio de cotización.',
    ),
    (
        '¿Qué mide el coeficiente de determinación (R-cuadrado o R2) de una cartera frente a su benchmark?',
        ['El porcentaje de variación de la rentabilidad de la cartera explicado por movimientos del índice de referencia', 'La volatilidad total de los retornos históricos no diversificables', 'La ganancia extraordinaria generada de forma independiente a la Beta', 'La covarianza de la rentabilidad residual ajustada por la tasa libre de riesgo'],
        0,
        'El R-cuadrado indica el grado de ajuste con el índice: un valor cercano a 1.0 (o 100%) muestra que el comportamiento depende casi enteramente de la evolución del benchmark.',
    ),
    (
        'En la teoría de carteras, ¿qué representa la recta CML (Capital Market Line)?',
        ['La relación entre la rentabilidad esperada y la desviación típica para carteras eficientes', 'La recta de regresión de los activos individuales ajustados por su riesgo sistemático Beta', 'El límite de apalancamiento máximo permitido por la Security Market Line', 'La frontera de mínima varianza de activos no correlacionados'],
        0,
        'La CML representa las carteras óptimas que combinan la cartera de mercado con el activo libre de riesgo, relacionando retorno esperado con riesgo total (desviación estándar).',
    ),
    (
        'Si la covarianza entre dos activos A y B es positiva, ¿qué ocurrirá con el riesgo total de una cartera equilibrada que combine ambos?',
        ['Se diversificará el riesgo, pero la reducción será menor que si la covarianza fuera negativa o nula', 'El riesgo se incrementará de forma ilimitada por encima de la suma ponderada de riesgos', 'No se producirá ningún efecto de diversificación del riesgo específico', 'El riesgo total se reducirá de forma idéntica a si el coeficiente de correlación fuera -1'],
        0,
        'Siempre que la correlación sea inferior a +1, existirá beneficio de diversificación, pero será más potente cuanto menor o más negativa sea la correlación/covarianza.',
    ),
    (
        'En relación a la asignación de activos, ¿qué caracteriza al Rebalanceo de Cartera (Portfolio Rebalancing)?',
        ['Vender activos que se han apreciado y comprar activos que se han depreciado para restaurar las ponderaciones estratégicas iniciales', 'Vender de forma sistemática los fondos con mayor volatilidad histórica a final del año', 'Incrementar de forma progresiva la exposición a activos de renta variable según avanza la edad del cliente', 'Mantener la cartera inalterada permitiendo que las tendencias del mercado definan los pesos futuros'],
        0,
        'El rebalanceo restaura los pesos de asignación estratégica (SAA) originales, obligando disciplinadamente a recoger beneficios de ganadores y acumular infravalorados.',
    ),
    (
        '¿Cuál es la principal debilidad del Ratio de Sharpe clásico como medida de rentabilidad ajustada al riesgo?',
        ['Trata por igual la volatilidad al alza (favorable) y a la baja (desfavorable) al utilizar la desviación estándar total', 'No permite realizar comparaciones entre fondos con diferentes tasas libres de riesgo', 'Requiere obligatoriamente que la cartera tenga una Beta superior a 1.0 para ser calculado', 'Ignora por completo la rentabilidad media ponderada acumulada del fondo comercializado'],
        0,
        'El Ratio de Sharpe penaliza la volatilidad generada por subidas fuertes de rentabilidad (volatilidad al alza), lo cual es favorable para el inversor, limitación que corrige el Ratio de Sortino.',
    ),
    (
        'Un activo cotiza ofreciendo una rentabilidad esperada del 12%, pero según la SML (CAPM) su rentabilidad exigida es del 9%. ¿Cómo está valorado el activo?',
        ['Infravalorado: se sitúa por encima de la SML y conviene comprarlo', 'Sobrevalorado: se sitúa por debajo de la SML y conviene venderlo', 'En equilibrio: se encuentra exactamente sobre la SML', 'No puede determinarse sin conocer la desviación típica del activo'],
        0,
        'Si la rentabilidad real esperada (12%) supera a la exigida por el CAPM (9%), el activo ofrece más de lo debido para su beta: está infravalorado y se sitúa por encima de la SML. La señal es comprar.',
    ),
    (
        'La Beta de un activo se calcula como el cociente entre:',
        ['La covarianza del activo con el mercado y la varianza del mercado', 'La varianza del activo y la covarianza con el mercado', 'La desviación típica del activo y la del mercado', 'La correlación del activo con el mercado y su propia varianza'],
        0,
        'Beta = Cov(Ri, Rm) / Var(Rm). Mide la sensibilidad del activo a los movimientos del mercado, es decir, su riesgo sistemático.',
    ),
    (
        '¿Qué caracteriza al modelo APT (Arbitrage Pricing Theory) frente al CAPM?',
        ['Explica la rentabilidad esperada mediante varios factores de riesgo y no requiere identificar la cartera de mercado', 'Utiliza un único factor (la beta de mercado) y exige conocer la cartera de mercado', 'Solo es aplicable a carteras situadas sobre la Capital Market Line', 'Sustituye la rentabilidad esperada por la desviación típica como medida de valor'],
        0,
        'El APT de Ross es un modelo multifactorial basado en la ausencia de arbitraje. A diferencia del CAPM (un solo factor y cartera de mercado), utiliza varios factores macroeconómicos y no necesita definir la cartera de mercado.',
    ),
    (
        'Si dos activos con volatilidad positiva tienen un coeficiente de correlación de -1, ¿qué es posible construir combinándolos?',
        ['Una cartera con riesgo nulo eligiendo adecuadamente los pesos', 'Una cartera cuya volatilidad siempre supera la media ponderada', 'Una cartera cuya rentabilidad esperada es negativa', 'Una cartera que replica exactamente la cartera de mercado'],
        0,
        'Con correlación -1 la volatilidad de la cartera es |w1·σ1 - w2·σ2|, que puede anularse con los pesos w1 = σ2/(σ1+σ2). Es el caso de máxima diversificación.',
    ),
    (
        'En la atribución de resultados de una cartera gestionada activamente, ¿qué mide el efecto "asset allocation"?',
        ['El valor añadido por sobreponderar o infraponderar categorías de activos respecto al benchmark', 'El valor añadido por seleccionar títulos concretos mejores que los del índice dentro de cada categoría', 'La comisión de gestión detraída al partícipe durante el periodo', 'La diferencia entre la TIR del inversor y la TGR del gestor'],
        0,
        'La rentabilidad activa total (Rp - Rb) se descompone en asset allocation (decisiones de peso entre categorías) y security selection (elección de títulos dentro de cada categoría). El efecto asset allocation recoge las decisiones de asignación entre clases de activos.',
    ),
    (
        'Según el teorema de separación en el modelo CAPM, todas las carteras eficientes se obtienen combinando:',
        ['El activo libre de riesgo y la cartera de mercado', 'Dos activos con riesgo cualesquiera de la frontera', 'La cartera de mínima varianza y la de máxima rentabilidad', 'Únicamente activos de renta fija y renta variable nacional'],
        0,
        'El teorema de separación establece que toda cartera eficiente de la CML es una combinación del activo sin riesgo y la cartera de mercado (cartera de tangencia), variando solo la proporción según la aversión al riesgo del inversor.',
    ),
    (
        'Comparando la TIR (rentabilidad del inversor) con la TGR (rentabilidad del gestor), ¿qué información se obtiene?',
        ['El acierto o fracaso del inversor en su estrategia de market timing con sus aportaciones y reembolsos', 'El nivel de riesgo sistemático asumido por la cartera durante el periodo', 'El grado de eficiencia semifuerte del mercado en el que opera el fondo', 'La comisión de éxito devengada por la sociedad gestora'],
        0,
        'La TGR (time-weighted) es independiente de los flujos del inversor y mide la habilidad del gestor; la TIR (money-weighted) sí depende de esos flujos. Si la TIR supera a la TGR, el inversor acertó con el momento de sus aportaciones (market timing).',
    ),
    (
        'Bajo la hipótesis de normalidad de las rentabilidades, ¿qué porcentaje aproximado de los resultados se sitúa en el intervalo E(R) ± 1 desviación típica?',
        ['Aproximadamente el 68%', 'Aproximadamente el 95%', 'Aproximadamente el 50%', 'Aproximadamente el 99,7%'],
        0,
        'En una distribución Normal, cerca del 68% de las observaciones caen dentro de E(R) ± 1σ, y alrededor del 95% dentro de E(R) ± 2σ. Este marco permite estimar intervalos de rentabilidad y las colas de pérdida.',
    ),
    (
        '¿Cuál es el Ratio de Sharpe de una cartera con rentabilidad del 12%, desviación típica del 18% y tasa libre de riesgo del 3%?',
        ['0.75', '0.67', '0.50', '0.45'],
        2,
        'Sharpe = (0.12 - 0.03) / 0.18 = 0.09 / 0.18 = 0.50. Mide el exceso de rentabilidad sobre el activo sin riesgo por unidad de riesgo total (volatilidad).',
    ),
    (
        'Una cartera obtiene una rentabilidad del 8%, con una tasa libre de riesgo del 2% y una downside deviation (desviación de las caídas) del 4%. ¿Cuál es su Ratio de Sortino?',
        ['0.75', '1.50', '2.00', '1.00'],
        1,
        'Sortino = (Rp - Rf) / downside deviation = (0.08 - 0.02) / 0.04 = 0.06 / 0.04 = 1.50. A diferencia de Sharpe, solo penaliza la volatilidad de las pérdidas.',
    ),
    (
        'Una cartera tiene una rentabilidad del 13%, beta 1.1, siendo la tasa libre de riesgo del 3% y la rentabilidad del mercado del 10%. ¿Cuál es su Alfa de Jensen?',
        ['1.3%', '3.0%', '2.3%', '-2.3%'],
        2,
        'Rentabilidad exigida por el CAPM = 3% + 1.1 x (10% - 3%) = 3% + 7.7% = 10.7%. Alfa = 13% - 10.7% = +2.3%. El alfa positivo indica valor añadido sobre lo exigido por su riesgo sistemático.',
    ),
    (
        'Un fondo obtiene una rentabilidad del 9% frente al 6% de su benchmark, con un tracking error del 5%. ¿Cuál es su Ratio de Información?',
        ['0.60', '1.50', '0.30', '0.45'],
        0,
        'IR = (Rp - Rb) / Tracking Error = (9% - 6%) / 5% = 3 / 5 = 0.60.',
    ),
    (
        'Una cartera invierte al 50% en dos activos con volatilidades del 20% y del 10% y correlación nula entre ellos. ¿Cuál es la volatilidad de la cartera?',
        ['15.00%', '11.18%', '12.50%', '10.00%'],
        1,
        'σp = raíz(0.5^2·0.20^2 + 0.5^2·0.10^2) = raíz(0.01 + 0.0025) = raíz(0.0125) = 11.18%. Con correlación 0 la volatilidad es inferior a la media ponderada (15%).',
    ),
    (
        'Una cartera invierte un 40% en un activo con beta 0.8 y un 60% en otro con beta 1.2. ¿Cuál es la beta de la cartera?',
        ['1.00', '0.96', '1.04', '1.20'],
        2,
        'La beta de una cartera es la media ponderada de las betas: βp = 0.4·0.8 + 0.6·1.2 = 0.32 + 0.72 = 1.04.',
    ),
    (
        'Una cartera coloca un 60% en un activo con rentabilidad esperada del 10% y un 40% en otro con rentabilidad esperada del 5%. ¿Cuál es la rentabilidad esperada de la cartera?',
        ['7.5%', '8.0%', '9.0%', '6.5%'],
        1,
        'E(Rp) = suma de pesos por rentabilidades = 0.6·10% + 0.4·5% = 6% + 2% = 8%.',
    ),
    (
        'Se estiman tres escenarios para un activo: expansión (prob. 40%, +20%), normal (prob. 40%, +10%) y recesión (prob. 20%, -15%). ¿Cuál es su rentabilidad esperada?',
        ['5.0%', '11.0%', '12.0%', '9.0%'],
        3,
        'E(R) = suma de probabilidad por rentabilidad = 0.4·20% + 0.4·10% + 0.2·(-15%) = 8% + 4% - 3% = 9%.',
    ),
    (
        'Un activo tiene una correlación con el mercado de 0.8, una volatilidad del 30% y el mercado una volatilidad del 20%. ¿Cuál es su beta?',
        ['0.8', '1.2', '1.5', '1.0'],
        1,
        'β = ρ · (σi / σm) = 0.8 · (30% / 20%) = 0.8 · 1.5 = 1.2. Equivale a Cov(i,m)/Var(m).',
    ),
    (
        'Un activo tiene beta 1.2, el mercado una volatilidad del 15% y el riesgo específico (residual) del activo es del 10%. ¿Cuál es aproximadamente su riesgo total (volatilidad)?',
        ['15.0%', '18.0%', '20.6%', '25.0%'],
        2,
        'Riesgo total: σ² = β²·σm² + σε² = 1.2²·0.15² + 0.10² = 0.0324 + 0.01 = 0.0424; σ = raíz(0.0424) = 20.6%.',
    ),
    (
        'Si la volatilidad diaria de un activo es del 1%, ¿cuál es su volatilidad anualizada aproximada (252 sesiones)?',
        ['12.60%', '15.87%', '25.20%', '1.59%'],
        1,
        'La volatilidad escala con la raíz del tiempo: σanual = σdiaria · raíz(252) = 1% · 15.87 = 15.87%.',
    ),
    (
        'Dos activos tienen volatilidades del 20% y del 10% y una correlación de -1. ¿Qué peso debe tener el primer activo para que la cartera tenga riesgo nulo?',
        ['33,3%', '50,0%', '66,7%', '25,0%'],
        0,
        'Con ρ = -1 el riesgo se anula con w1 = σ2 / (σ1 + σ2) = 10 / (20 + 10) = 1/3 = 33,3% (y 66,7% en el segundo).',
    ),
    (
        'Una cartera tiene una rentabilidad esperada del 8% y una volatilidad del 10%, con rentabilidades normalmente distribuidas. ¿En qué intervalo se situará aproximadamente el 95% de los resultados?',
        ['Entre -2% y 18%', 'Entre -12% y 28%', 'Entre -22% y 38%', 'Entre 0% y 16%'],
        1,
        'El 95% de las observaciones cae en E(R) ± 2σ = 8% ± 2·10% = 8% ± 20%, es decir, entre -12% y 28%.',
    ),
    (
        '¿Qué mide el VaR (Value at Risk) de una cartera?',
        ['La rentabilidad media esperada ajustada por la inflación del periodo', 'La pérdida máxima estimada para un horizonte temporal y un nivel de confianza dados', 'La comisión máxima que puede cobrar la gestora al partícipe', 'La beta máxima que puede alcanzar la cartera en un mercado alcista'],
        1,
        'El VaR expresa la pérdida máxima esperada con un nivel de confianza y horizonte determinados (p. ej. con un 95% de confianza no se perderá más del X% en un mes).',
    ),
    (
        '¿Cuál es el objetivo principal de las normas GIPS (Global Investment Performance Standards)?',
        ['Garantizar la comparabilidad, transparencia y representatividad en la presentación de resultados, evitando el cherry picking', 'Fijar las comisiones máximas de gestión de los fondos de inversión', 'Establecer los requisitos de solvencia de las entidades gestoras', 'Definir el nivel de apalancamiento permitido a los fondos alternativos'],
        0,
        'Las GIPS son estándares internacionales de presentación de resultados que buscan comparabilidad y transparencia, impidiendo mostrar selectivamente solo las mejores carteras (cherry picking).',
    ),
    (
        'Si una cartera se sitúa en el primer cuartil de rentabilidad de su categoría, ¿qué significa?',
        ['Que se encuentra entre el 25% de las carteras con peor rentabilidad', 'Que su rentabilidad coincide exactamente con la mediana de la categoría', 'Que se encuentra entre el 25% de las carteras con mejor rentabilidad', 'Que ha obtenido una rentabilidad negativa en el periodo'],
        2,
        'El primer cuartil agrupa al 25% de mejores resultados de la categoría. Los cuartiles y percentiles sitúan la posición relativa de la cartera frente a sus comparables.',
    ),
]


INTRO = '# M3: Gestión de Carteras\n\nHasta ahora hemos visto productos sueltos (bonos, acciones, fondos). Pero un inversor no compra un solo producto: arma una [[cartera::conjunto de todas las inversiones de una persona o entidad tomadas en su conjunto: acciones, bonos, fondos, etc. También se llama portafolio]] (el conjunto de todas sus inversiones). Este módulo trata de cómo combinar esos productos de forma inteligente para lograr la mejor rentabilidad posible con el menor riesgo, y de cómo medir si lo estamos haciendo bien.\n\nLa idea que lo vertebra todo es sencilla y sabia: no pongas todos los huevos en la misma cesta. Combinar activos que no suben y bajan a la vez reduce el riesgo sin renunciar necesariamente a la rentabilidad.'


SECCIONES = [
    {
        'titulo': 'Teoría Moderna de Carteras (Harry Markowitz)',
        'cuerpo': 'Markowitz demostró con matemáticas algo que la sabiduría popular ya intuía: mezclar inversiones distintas reduce el riesgo del conjunto.\n\n**Riesgo y rentabilidad.** La rentabilidad esperada de una cartera es simplemente la media de las rentabilidades de sus activos, ponderada por cuánto dinero pones en cada uno:\n\n$$E(R_p) = \\sum_{i=1}^{N} w_i \\cdot E(R_i)$$\n\nPero con el riesgo pasa algo mágico: el riesgo de la cartera NO es la media de los riesgos. Para dos activos:\n\n$$\\sigma_p = \\sqrt{w_1^2 \\sigma_1^2 + w_2^2 \\sigma_2^2 + 2 w_1 w_2 \\rho_{1,2} \\sigma_1 \\sigma_2}$$\n\ndonde $\\rho_{1,2}$ es el [[coeficiente de correlación::número entre -1 y +1 que mide si dos inversiones se mueven juntas. +1: suben y bajan a la vez; -1: se mueven al revés; 0: no tienen relación]] de rentabilidades. Si $\\rho_{1,2} < 1$, aparece el efecto diversificador que reduce la volatilidad de la cartera por debajo de la media ponderada. ¡Ahí está la magia!\n\n**Frontera Eficiente.** La [[Frontera Eficiente::conjunto de las mejores carteras posibles: aquellas que, para un nivel de riesgo dado, ofrecen la máxima rentabilidad (o el mínimo riesgo para una rentabilidad dada)]] es el conjunto de carteras óptimas que maximizan el rendimiento esperado para cada nivel de volatilidad, o minimizan la volatilidad para cada nivel de rendimiento. Es el "menú" de las mejores carteras; un inversor racional solo elige entre ellas.\n\n**Riesgo sistemático frente a riesgo específico.** Hay dos tipos de riesgo:\n- **[[riesgo específico::riesgo propio de una empresa concreta (una huelga, un mal producto, un fraude). Se puede eliminar diversificando, es decir, teniendo muchas inversiones distintas]] (diversificable)**: propio del emisor. Se reduce y elimina añadiendo activos poco correlacionados.\n- **[[riesgo sistemático::riesgo que afecta a todo el mercado a la vez (una recesión, una subida de tipos, una guerra). No se puede eliminar diversificando. Se mide con la beta]] (de mercado)**: deriva de factores macroeconómicos globales. Afecta a todo el mercado y no se elimina diversificando. Se mide con la beta ($\\beta$).',
        'ejercicios': [],
    },
    {
        'titulo': 'Modelo CAPM',
        'cuerpo': 'El [[CAPM::modelo que calcula qué rentabilidad debes exigir a una inversión según su riesgo de mercado (beta). Cuanto más riesgo de mercado, más rentabilidad debes pedir]] establece la rentabilidad exigida a un activo en función de su riesgo de mercado (su beta):\n\n$$E(R_i) = R_f + \\beta_i \\cdot (E(R_m) - R_f)$$\n\ndonde $R_f$ es la rentabilidad del [[activo libre de riesgo::inversión que se considera sin riesgo de impago, como la deuda pública a corto plazo del Estado; sirve de referencia mínima de rentabilidad]] (por ejemplo, Letras del Estado), $E(R_m)$ la rentabilidad esperada del mercado, y $(E(R_m) - R_f)$ la [[prima de riesgo::rentabilidad extra que un inversor exige por asumir riesgo, por encima de lo que le daría una inversión sin riesgo]] del mercado. Su representación gráfica es la **Security Market Line (SML)**.',
        'ejercicios': [],
    },
    {
        'titulo': 'Ratios de medida de performance (ajuste por riesgo)',
        'cuerpo': 'Ganar un 20% suena genial... hasta que sabes que se asumió un riesgo enorme. Estos ratios miden la rentabilidad teniendo en cuenta el riesgo asumido:\n1. **[[ratio de Sharpe::mide cuánta rentabilidad extra logra una cartera por cada unidad de riesgo total (volatilidad). Cuanto mayor, mejor relación rentabilidad-riesgo]]**: exceso de rentabilidad sobre el activo sin riesgo por unidad de riesgo total.\n   $$Sharpe = \\frac{R_p - R_f}{\\sigma_p}$$\n2. **[[ratio de Treynor::como el Sharpe, pero divide entre la beta (riesgo de mercado) en vez de la volatilidad total. Útil en carteras bien diversificadas]]**: exceso de rentabilidad por unidad de riesgo sistemático (beta).\n   $$Treynor = \\frac{R_p - R_f}{\\beta_p}$$\n3. **[[alfa de Jensen::rentabilidad extra que consigue el gestor por encima de la que le exigía el CAPM según su riesgo. Positivo significa que ha aportado valor real]] ($\\alpha_p$)**: rentabilidad anormal frente a la exigida por el CAPM.\n   $$\\alpha_p = R_p - [R_f + \\beta_p \\cdot (R_m - R_f)]$$\n4. **Ratio de Información**: exceso de rentabilidad frente a un [[benchmark::índice de referencia con el que se compara una cartera para juzgar si lo hace mejor o peor que el mercado]] por unidad de tracking error.\n   $$IR = \\frac{R_p - R_b}{\\text{Tracking Error}}$$\n5. **[[ratio de Sortino::variante del Sharpe que solo castiga las caídas (la volatilidad "mala"), no las subidas. Divide entre la desviación de los rendimientos negativos]]**: exceso de rentabilidad dividido por el Downside Risk (solo las pérdidas).\n   $$Sortino = \\frac{R_p - R_f}{\\sigma_d}$$',
        'ejercicios': [],
    },
    {
        'titulo': 'Rentabilidad y riesgo de un activo',
        'cuerpo': '1. **Rentabilidad histórica frente a esperada**: la histórica es la ya obtenida en el pasado; la esperada $E(R)$ es una estimación futura. La histórica tiene problemas de estimación (tamaño de la muestra, dividendos, periodo).\n2. **Rentabilidad simple** de un periodo (lo que gano contando la subida de precio más lo cobrado):\n   $$R = \\frac{P_1 - P_0 + D}{P_0}$$\n3. **Rentabilidad media histórica**: media aritmética de las rentabilidades de cada subperiodo.\n4. **Rentabilidad esperada por escenarios**: media ponderada por probabilidades:\n   $$E(R) = \\sum_{i=1}^{n} p_i \\cdot R_i$$\n5. **Rentabilidad anualizada**:\n   $$R_{anual} = (1 + R_{periodo})^{\\frac{365}{d}} - 1$$',
        'ejercicios': [],
    },
    {
        'titulo': 'Volatilidad, covarianza y correlación',
        'cuerpo': 'La [[volatilidad::medida de cuánto oscila el precio de una inversión en torno a su media. Es la forma más usada de medir el riesgo: a más volatilidad, más incertidumbre]] es la medida de riesgo más usada.\n1. **Varianza** (histórica): promedio de las desviaciones al cuadrado respecto a la media:\n   $$\\sigma^2 = \\frac{1}{n}\\sum_{i=1}^{n}(R_i - \\bar{R})^2$$\n   La desviación típica o volatilidad es su raíz cuadrada $\\sigma = \\sqrt{\\sigma^2}$. Su desventaja: penaliza por igual las desviaciones al alza (buenas) y a la baja (malas).\n2. **Varianza por escenarios**: $\\sigma^2 = \\sum p_i (R_i - E(R))^2$.\n3. **Volatilidad anualizada**: $\\sigma_{anual} = \\sigma_{periodo} \\cdot \\sqrt{t}$ (por ejemplo, $\\sigma_{anual} = \\sigma_{diaria}\\cdot\\sqrt{252}$).\n4. **[[covarianza::medida de si dos inversiones se mueven en el mismo sentido (positiva) o en sentidos opuestos (negativa). La correlación es su versión estandarizada]]**: cómo se mueven conjuntamente dos activos:\n   $$Cov(A,B) = \\frac{1}{n}\\sum (R_A - \\bar{R}_A)(R_B - \\bar{R}_B)$$\n5. **Coeficiente de correlación**: covarianza estandarizada, entre -1 y +1:\n   $$\\rho_{A,B} = \\frac{Cov(A,B)}{\\sigma_A \\cdot \\sigma_B}$$\n   Cuanto menor (o más negativa) la correlación, mayor el efecto diversificador. Con $\\rho = -1$ se puede construir una cartera de **riesgo nulo** aun combinando dos activos con volatilidad positiva.',
        'ejercicios': [],
    },
    {
        'titulo': 'Diversificación y cartera de dos activos',
        'cuerpo': 'La volatilidad de una cartera de dos activos con riesgo es:\n$$\\sigma_p = \\sqrt{w_1^2 \\sigma_1^2 + w_2^2 \\sigma_2^2 + 2 w_1 w_2 \\sigma_1 \\sigma_2 \\rho_{1,2}}$$\n- Si $\\rho = +1$: $\\sigma_p = w_1\\sigma_1 + w_2\\sigma_2$ (media ponderada, sin diversificación).\n- Si $\\rho = 0$: $\\sigma_p = \\sqrt{w_1^2\\sigma_1^2 + w_2^2\\sigma_2^2}$.\n- Si $\\rho = -1$: $\\sigma_p = |w_1\\sigma_1 - w_2\\sigma_2|$, y el riesgo se anula con $w_1 = \\frac{\\sigma_2}{\\sigma_1+\\sigma_2}$.\nSi un activo es libre de riesgo ($\\sigma_2 = 0$): $\\sigma_p = w_1 \\sigma_1$. El objetivo de diversificar es **reducir el riesgo**, no maximizar la rentabilidad; una cartera puede estar bien diversificada con pocos títulos si su correlación es baja.',
        'ejercicios': [],
    },
    {
        'titulo': 'Hipótesis de normalidad',
        'cuerpo': 'Si las rentabilidades siguen una [[distribución normal::la típica "campana de Gauss"; una forma de repartir las probabilidades en la que los valores se concentran alrededor de la media y los extremos son raros]] (campana de Gauss), quedan definidas por su media y su desviación típica. Aproximadamente el **68%** de las observaciones caen en $E(R) \\pm 1\\sigma$ y el **95%** en $E(R) \\pm 2\\sigma$. Las colas del **16%** (por debajo de $E(R)-1\\sigma$) y del **2,5%** (por debajo de $E(R)-2\\sigma$) permiten estimar rentabilidades extremas. Manteniendo rentabilidad y volatilidad, la probabilidad de perder dinero es **menor a largo plazo** que a corto.',
        'ejercicios': [],
    },
    {
        'titulo': 'Mercados de capitales eficientes',
        'cuerpo': 'Un [[mercado eficiente::mercado en el que los precios reflejan de inmediato toda la información disponible, de modo que es muy difícil ganar de forma sistemática al conjunto]] es aquel cuyos precios reflejan al instante la información disponible. Niveles:\n- **Débil**: los precios recogen toda la información histórica. El análisis técnico no aporta valor.\n- **Semifuerte**: recogen además toda la información pública actual. El análisis fundamental tampoco aporta valor.\n- **Fuerte**: recogen toda la información, incluida la privada/privilegiada. Ni el insider puede batir al mercado; los precios siguen un comportamiento aleatorio (random walk).\n\nExisten **anomalías** (efecto enero o fin de ejercicio, efecto fin de semana, efecto vacaciones, efecto tamaño).',
        'ejercicios': [],
    },
    {
        'titulo': 'Teoría de carteras de Markowitz (detalle)',
        'cuerpo': '- **Cartera factible**: cualquier combinación posible de activos. **Cartera eficiente**: la que, para un nivel de riesgo, da la máxima rentabilidad. La **Frontera Eficiente** es el conjunto de carteras eficientes; tiene forma parabólica (cóncava) en el plano rentabilidad-riesgo, entre la cartera de mínima volatilidad y la de máxima rentabilidad esperada.\n- **Hipótesis del modelo media-varianza**: los inversores son racionales y [[aversión al riesgo::preferencia de la mayoría de los inversores por asumir menos riesgo; para aceptar más riesgo, exigen más rentabilidad a cambio]] aversos al riesgo, y deciden solo en función de la rentabilidad esperada (media) y el riesgo (varianza), para un único horizonte.\n- **Curvas de indiferencia**: combinaciones rentabilidad-riesgo igualmente deseables para un inversor. Para un averso al riesgo son crecientes y convexas. La **cartera óptima** es la de la Frontera Eficiente tangente a la curva de indiferencia más elevada.',
        'ejercicios': [],
    },
    {
        'titulo': 'Modelo de mercado de Sharpe',
        'cuerpo': 'Simplifica el modelo de Markowitz relacionando cada activo con un único factor: el mercado. La **línea característica** de un título es la regresión:\n$$R_i = \\alpha_i + \\beta_i \\cdot R_m + \\varepsilon_i$$\n- **[[beta::número que mide cuánto amplifica un activo los movimientos del mercado. Beta 1,5: si el mercado sube 10%, se espera que el activo suba un 15%. Mide el riesgo de mercado]] ($\\beta$)**: sensibilidad del activo al mercado; mide el riesgo sistemático:\n  $$\\beta_i = \\frac{Cov(R_i, R_m)}{\\sigma_m^2}$$\n  Clasificación: $\\beta > 1$ agresivo, $\\beta = 1$ neutro, $0 < \\beta < 1$ defensivo, $\\beta < 0$ contrario al mercado.\n- **Alfa ($\\alpha$)**: rentabilidad del título independiente del mercado (ordenada en el origen).\n- **Coeficiente de determinación ($R^2$)**: porcentaje de la variabilidad del título explicado por el mercado; mide la bondad del ajuste.\n- **Descomposición del riesgo total**:\n  $$\\sigma_i^2 = \\underbrace{\\beta_i^2 \\sigma_m^2}_{\\text{sistemático}} + \\underbrace{\\sigma_{\\varepsilon}^2}_{\\text{no sistemático}}$$\n  En una cartera bien diversificada el riesgo no sistemático tiende a cero y solo permanece el sistemático.\n- **Beta de una cartera**: media ponderada de las betas: $\\beta_p = \\sum w_i \\beta_i$.',
        'ejercicios': [],
    },
    {
        'titulo': 'CAPM: CML y SML',
        'cuerpo': '**Hipótesis del CAPM**: expectativas homogéneas, un único periodo, poder prestar y endeudarse al tipo sin riesgo, ausencia de costes e impuestos, y mercado eficiente.\n- **Capital Market Line (CML)**: es la Frontera Eficiente cuando existe un activo sin riesgo. Relaciona rentabilidad esperada y **riesgo total** ($\\sigma$):\n  $$E(R_p) = R_f + \\frac{E(R_m) - R_f}{\\sigma_m}\\cdot \\sigma_p$$\n  Su pendiente es el **precio del riesgo**. La **cartera de mercado** es la de tangencia entre la CML y la frontera de activos con riesgo; según el **teorema de separación**, todas las carteras eficientes combinan la cartera de mercado y el activo sin riesgo.\n- **Security Market Line (SML)**: representación gráfica del CAPM. Relaciona la rentabilidad exigida con el **riesgo sistemático** ($\\beta$):\n  $$E(R_i) = R_f + \\beta_i (E(R_m) - R_f)$$\n  Intercepto $R_f$ y pendiente igual a la prima de riesgo del mercado. Un activo **por encima** de la SML (rentabilidad real mayor que la exigida) está **infravalorado** (comprar); **por debajo**, **sobrevalorado** (vender). Diferencia clave: la **CML** solo aplica a carteras eficientes usando $\\sigma$; la **SML** aplica a cualquier activo usando $\\beta$.',
        'ejercicios': [],
    },
    {
        'titulo': 'APT (Arbitrage Pricing Theory)',
        'cuerpo': 'El [[APT::modelo alternativo al CAPM que explica la rentabilidad de un activo por su sensibilidad a varios factores de riesgo (inflación, tipos, producción...), no solo al mercado]] de Ross es multifactorial. La rentabilidad esperada se explica por la sensibilidad a varios factores de riesgo:\n$$E(R_i) = R_f + \\beta_{i1}\\lambda_1 + \\beta_{i2}\\lambda_2 + \\dots + \\beta_{ik}\\lambda_k$$\ndonde $\\lambda_k$ es la prima de riesgo de cada factor. No requiere identificar la cartera de mercado y se basa en la ausencia de arbitraje.',
        'ejercicios': [],
    },
    {
        'titulo': 'Otros modelos: Graham y Dodd',
        'cuerpo': 'Análisis fundamental del *value investing*: una acción está infravalorada cuando cotiza por debajo de su [[valor intrínseco::valor "real" o justo que se estima para una acción según sus fundamentales (beneficios, activos...), al margen de lo que marque el mercado en un momento dado]] (bajos PER y precio/valor contable, con margen de seguridad). Inconveniente: la subjetividad al estimar el valor intrínseco.',
        'ejercicios': [],
    },
    {
        'titulo': 'Proceso de asignación de activos (Asset Allocation)',
        'cuerpo': 'Decidir qué porcentaje de la cartera va a acciones, cuánto a bonos y cuánto a liquidez es la decisión que más influye en el resultado final.\n- **Gestión pasiva**: replica un índice (tracking error bajo). **Gestión activa**: busca batir al benchmark (tracking error alto).\n- **[[asignación estratégica::reparto objetivo de la cartera entre tipos de activo (acciones, bonos, liquidez) a largo plazo, según el perfil de riesgo del inversor]] (SAA)**: pesos objetivo a largo plazo por tipo de activo, sector y geografía. Incluye el [[rebalanceo::ajuste periódico de la cartera para volver a los pesos objetivo, vendiendo lo que ha subido y comprando lo que ha bajado]] periódico o la estrategia de comprar y mantener (buy & hold).\n- **Asignación táctica (TAA)**: desviaciones a corto plazo de la SAA para aprovechar coyunturas. Se apoya en el security selection y el [[market timing::intento de acertar el mejor momento para entrar y salir del mercado. Muy difícil de lograr de forma consistente]] (elegir el momento de entrada/salida).\n- **Benchmark**: debe ser inequívoco, medible, replicable, apropiado al estilo y conocido de antemano.\n- **ESG**: los factores ambientales, sociales y de gobernanza se integran en la asignación y la selección.',
        'ejercicios': [],
    },
    {
        'titulo': 'Medición de rentabilidad',
        'cuerpo': '- **Rentabilidad simple** del periodo (ya vista).\n- **TIR (rentabilidad del inversor)**: tasa que iguala aportaciones y reembolsos; depende de los flujos monetarios (money-weighted).\n- **TGR (rentabilidad del gestor)**: rentabilidad time-weighted, independiente de los flujos que decide el inversor; mide la habilidad del gestor.\n- Comparando **TIR y TGR** se evalúa el acierto del inversor en el market timing: si TIR > TGR, el inversor acertó con el momento de sus aportaciones.',
        'ejercicios': [],
    },
    {
        'titulo': 'Tracking Error, VaR y comparación con el benchmark',
        'cuerpo': '- **[[tracking error::medida de cuánto se separa la rentabilidad de una cartera de la de su índice de referencia. Bajo indica gestión pasiva; alto, gestión activa]] (TE)**: desviación típica de la diferencia de rentabilidades entre cartera y benchmark.\n- **[[VaR (Value at Risk)::estimación de la pérdida máxima que puede sufrir una cartera en un plazo dado con cierta probabilidad. Ejemplo: "con un 95% de confianza no perderé más del 4% en un mes"]]**: pérdida máxima estimada para un horizonte y un nivel de confianza dados.\n- **Batir al benchmark**: una cartera lo bate si logra mejor Sharpe, mejor Treynor o un alfa de Jensen positivo.',
        'ejercicios': [],
    },
    {
        'titulo': 'Atribución de resultados',
        'cuerpo': 'La rentabilidad total añadida por el gestor es $R_p - R_b$. Se descompone en:\n- **Asset Allocation (asignación)**: valor añadido por sobreponderar o infraponderar categorías de activos frente al benchmark.\n- **Security Selection (selección)**: valor añadido por elegir, dentro de cada categoría, títulos que baten al benchmark.',
        'ejercicios': [],
    },
    {
        'titulo': 'Información al cliente: cuartiles, percentiles y GIPS',
        'cuerpo': '- **Cuartil/percentil**: posición relativa de la cartera dentro de su categoría (primer cuartil = mejor 25%). Se aplica a rentabilidades y a medidas de riesgo.\n- **Normas [[GIPS::estándares internacionales para presentar los resultados de las inversiones de forma comparable y transparente, evitando que las gestoras muestren solo sus mejores carteras]]**: estándares internacionales de presentación de resultados; persiguen comparabilidad, transparencia y representatividad, evitando el cherry picking.',
        'ejercicios': [],
    },
    {
        'titulo': 'Intuición de los conceptos clave',
        'cuerpo': '- **Diversificación**: combinar activos que no se mueven al unísono reduce el riesgo total sin sacrificar (proporcionalmente) rentabilidad. El beneficio aparece siempre que $\\rho < 1$ y crece cuanto más baja o negativa sea la correlación. No depende de tener muchos títulos, sino de que estén poco correlacionados.\n- **Frontera eficiente**: es el "menú" de las mejores carteras posibles; para un riesgo dado, ninguna ofrece más rentabilidad.\n- **CAPM / SML**: la rentabilidad exigida crece linealmente con la beta. La pendiente $(R_m-R_f)$ es el "precio" del riesgo sistemático.\n- **CML**: aplica solo a carteras eficientes y mide el riesgo con la volatilidad total $\\sigma$, no con la beta.\n- **Beta**: amplificador de los movimientos del mercado. $\\beta = 1{,}5$: si el mercado se mueve un 10%, se espera un 15% en el mismo sentido.\n- **Ratios de un vistazo**: Sharpe usa riesgo total ($\\sigma$); Treynor y Jensen usan riesgo sistemático ($\\beta$); el Ratio de Información compara frente al benchmark; Sortino solo penaliza el riesgo de caídas.',
        'ejercicios': [],
    },
    {
        'titulo': 'Ejemplos resueltos paso a paso',
        'cuerpo': '**Ejemplo 1 (Ratio de Sharpe).** Cartera con $R_p=12\\%$, $\\sigma_p=18\\%$ y $R_f=3\\%$.\n$$Sharpe = \\frac{0{,}12-0{,}03}{0{,}18} = 0{,}50$$\nPor cada unidad de riesgo total se obtienen 0,50 unidades de exceso de rentabilidad.\n\n**Ejemplo 2 (Ratio de Treynor).** $R_p=11\\%$, $\\beta_p=1{,}2$, $R_f=2\\%$.\n$$Treynor = \\frac{0{,}11-0{,}02}{1{,}2} = 0{,}075 = 7{,}5\\%$$\n\n**Ejemplo 3 (Alfa de Jensen).** $R_p=13\\%$, $\\beta_p=1{,}1$, $R_f=3\\%$, $R_m=10\\%$.\nRentabilidad exigida por el CAPM: $3\\% + 1{,}1\\,(10\\%-3\\%) = 10{,}7\\%$.\n$$\\alpha_p = 13\\% - 10{,}7\\% = +2{,}3\\%$$\nAlfa positivo: el gestor batió lo que exigía su riesgo sistemático.\n\n**Ejemplo 4 (Ratio de Información).** Cartera $R_p=9\\%$, benchmark $R_b=6\\%$, tracking error $=5\\%$.\n$$IR = \\frac{9\\%-6\\%}{5\\%} = 0{,}60$$\n\n**Ejemplo 5 (Ratio de Sortino).** $R_p=8\\%$, $R_f=2\\%$, downside deviation $\\sigma_d=4\\%$.\n$$Sortino = \\frac{0{,}08-0{,}02}{0{,}04} = 1{,}5$$\nCon la $\\sigma$ total (mayor) el Sharpe sería menor: Sortino premia a las carteras cuya volatilidad procede sobre todo de subidas.\n\n**Ejemplo 6 (Cartera de dos activos y el papel de la correlación).** Pesos $w_1=w_2=0{,}5$, con $\\sigma_1=20\\%$ y $\\sigma_2=10\\%$.\n- $\\rho=+1$: $\\sigma_p = 0{,}5\\cdot20\\% + 0{,}5\\cdot10\\% = 15\\%$ (sin diversificación).\n- $\\rho=0$: $\\sigma_p = \\sqrt{0{,}5^2\\cdot0{,}20^2 + 0{,}5^2\\cdot0{,}10^2} = 11{,}18\\%$.\n- $\\rho=-1$: $\\sigma_p = |0{,}5\\cdot20\\% - 0{,}5\\cdot10\\%| = 5\\%$.\nCon $\\rho=-1$ la cartera de riesgo nulo se logra con $w_1=\\frac{\\sigma_2}{\\sigma_1+\\sigma_2}=33{,}3\\%$ en el activo 1.\n\n**Ejemplo 7 (Beta por covarianza y por correlación).**\n- Por covarianza: $Cov(i,m)=0{,}024$ y $\\sigma_m^2=0{,}020$ $\\Rightarrow$ $\\beta = 1{,}2$.\n- Por correlación: $\\beta = \\rho_{i,m}\\dfrac{\\sigma_i}{\\sigma_m}$. Con $\\rho=0{,}8$, $\\sigma_i=30\\%$ y $\\sigma_m=20\\%$: $\\beta = 0{,}8\\cdot\\frac{30}{20} = 1{,}2$.\n\n**Ejemplo 8 (Beta y rentabilidad esperada de una cartera).** 40% en un activo de $\\beta=0{,}8$ y 60% en otro de $\\beta=1{,}2$:\n$$\\beta_p = 0{,}4\\cdot0{,}8 + 0{,}6\\cdot1{,}2 = 1{,}04$$\nRentabilidad esperada por escenarios (expansión 40% → +20%, normal 40% → +10%, recesión 20% → -15%):\n$$E(R)=0{,}4\\cdot20\\% + 0{,}4\\cdot10\\% + 0{,}2\\cdot(-15\\%) = 9\\%$$',
        'ejercicios': [],
    },
    {
        'titulo': 'Errores frecuentes y claves de examen',
        'cuerpo': '- **Riesgo total frente a sistemático**: Sharpe y la CML usan la volatilidad total ($\\sigma$); Treynor, Jensen y la SML usan la beta ($\\beta$). Confundirlos es el error más típico.\n- **CML frente a SML**: la CML solo describe carteras eficientes (eje X = $\\sigma$); la SML vale para cualquier activo (eje X = $\\beta$).\n- **Infra/sobrevalorado**: rentabilidad esperada **por encima** de la SML → infravalorado (comprar); por debajo → sobrevalorado (vender).\n- **Diversificación**: reduce solo el riesgo no sistemático; el sistemático permanece. Muchos títulos no garantizan diversificación si están muy correlacionados.\n- **Correlación**: hay beneficio diversificador siempre que $\\rho<1$; la cartera de riesgo nulo exige $\\rho=-1$ exacta.\n- **Sharpe frente a Sortino**: Sharpe penaliza también la volatilidad al alza; Sortino solo la del downside.\n- **TIR frente a TGR**: la TGR (time-weighted) mide al gestor; la TIR (money-weighted) incorpora los flujos del inversor. Si TIR > TGR, el inversor acertó con el market timing.\n- **Alfa positivo**: mide valor añadido frente al CAPM, no rentabilidad absoluta.\n- **Unidades**: expresa rentabilidades y sigmas en la misma base; mezclarlas descuadra los ratios.\n- **Beta de la cartera**: es la media ponderada de las betas, nunca la suma.',
        'ejercicios': [],
    },
]
