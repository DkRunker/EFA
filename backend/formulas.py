def calcular_gordon_shapiro(d1: float, ke: float, g: float) -> dict:
    """
    Calcula el precio teórico de una acción usando el modelo de Gordon-Shapiro.
    P0 = D1 / (ke - g)
    """
    if ke <= g:
        raise ValueError("La rentabilidad exigida (ke) debe ser mayor que la tasa de crecimiento (g).")
    denominador = ke - g
    precio_teorico = d1 / denominador
    return {
        "denominador": denominador,
        "precio_teorico": precio_teorico
    }


def calcular_sharpe(rp: float, rf: float, sigma_p: float) -> float:
    """
    Calcula el Ratio de Sharpe.
    Sharpe = (Rp - Rf) / sigma_p
    """
    if sigma_p <= 0:
        raise ValueError("La volatilidad de la cartera (sigma_p) debe ser mayor que cero.")
    return (rp - rf) / sigma_p


def calcular_treynor(rp: float, rf: float, beta_p: float) -> float:
    """
    Calcula el Ratio de Treynor.
    Treynor = (Rp - Rf) / beta_p
    """
    if beta_p == 0:
        raise ValueError("La Beta de la cartera (beta_p) no puede ser cero.")
    return (rp - rf) / beta_p


def calcular_jensen(rp: float, rf: float, beta_p: float, rm: float) -> float:
    """
    Calcula el Alfa de Jensen.
    Alfa = Rp - [Rf + beta_p * (Rm - Rf)]
    """
    return rp - (rf + beta_p * (rm - rf))


def calcular_tae(tin: float, m: int) -> float:
    """
    Calcula la Tasa Anual Equivalente (TAE) a partir del TIN y los periodos.
    TAE = (1 + TIN/m)^m - 1
    """
    if m <= 0:
        raise ValueError("El número de periodos de liquidación al año (m) debe ser mayor que cero.")
    return (1 + tin / m) ** m - 1


def calcular_precio_bono(nominal: float, cupon_anual_pct: float, n_anos: int, tir: float) -> float:
    """
    Calcula el precio actual de un bono de renta fija.
    P = Sum(C / (1+tir)^t) + Nominal / (1+tir)^n
    """
    if n_anos <= 0:
        raise ValueError("El vencimiento (n_anos) debe ser mayor que cero.")
    cupon = nominal * cupon_anual_pct
    precio = 0.0
    for t in range(1, n_anos + 1):
        precio += cupon / ((1 + tir) ** t)
    precio += nominal / ((1 + tir) ** n_anos)
    return precio


def calcular_irpf_ahorro(base_liquidable: float) -> dict:
    """
    Calcula la cuota del IRPF del ahorro en España para 2026.
    Tramos:
      - Hasta 6.000 €: 19%
      - De 6.000 € a 50.000 €: 21%
      - De 50.000 € a 200.000 €: 23%
      - De 200.000 € a 300.000 €: 27%
      - Más de 300.000 €: 28%
    """
    tramos = [
        {"tramo": "hasta 6.000 €", "limite": 6000.0, "tipo": 0.19},
        {"tramo": "de 6.000 a 50.000 €", "limite": 44000.0, "tipo": 0.21},
        {"tramo": "de 50.000 a 200.000 €", "limite": 150000.0, "tipo": 0.23},
        {"tramo": "de 200.000 a 300.000 €", "limite": 100000.0, "tipo": 0.27},
        {"tramo": "más de 300.000 €", "limite": float("inf"), "tipo": 0.28}
    ]
    
    desglose = []
    restante = base_liquidable
    cuota_total = 0.0
    
    for t in tramos:
        if restante <= 0:
            base_tramo = 0.0
        else:
            base_tramo = min(restante, t["limite"])
            restante -= base_tramo
            
        cuota_tramo = base_tramo * t["tipo"]
        cuota_total += cuota_tramo
        
        desglose.append({
            "tramo": t["tramo"],
            "tipo": t["tipo"],
            "base_tramo": base_tramo,
            "cuota_tramo": cuota_tramo
        })
        
    return {
        "cuota_total": cuota_total,
        "desglose": desglose
    }


def calcular_duracion_bono(nominal: float, cupon_anual_pct: float, n_anos: int, tir: float, frecuencia: int = 1) -> dict:
    """
    Calcula el precio actual, la Duración de Macaulay, la Duración Modificada y la Convexidad de un bono.
    """
    if n_anos <= 0:
        raise ValueError("El vencimiento (n_anos) debe ser mayor que cero.")
    if frecuencia <= 0:
        raise ValueError("La frecuencia de cupones debe ser mayor que cero.")
    
    t_total = n_anos * frecuencia
    tir_periodo = tir / frecuencia
    cupon_periodo = nominal * (cupon_anual_pct / frecuencia)
    
    precio = 0.0
    suma_ponderada = 0.0
    suma_convexidad = 0.0
    
    for i in range(1, t_total + 1):
        t_anos = i / frecuencia
        factor_descuento = (1 + tir_periodo) ** i
        valor_actual_flujo = cupon_periodo / factor_descuento
        precio += valor_actual_flujo
        suma_ponderada += t_anos * valor_actual_flujo
        suma_convexidad += (t_anos * (t_anos + 1 / frecuencia)) * (cupon_periodo / ((1 + tir_periodo) ** (i + 2)))
        
    factor_descuento_nominal = (1 + tir_periodo) ** t_total
    valor_actual_nominal = nominal / factor_descuento_nominal
    precio += valor_actual_nominal
    suma_ponderada += n_anos * valor_actual_nominal
    suma_convexidad += (n_anos * (n_anos + 1 / frecuencia)) * (nominal / ((1 + tir_periodo) ** (t_total + 2)))
    
    macaulay = suma_ponderada / precio
    modificada = macaulay / (1 + tir_periodo)
    convexidad = suma_convexidad / precio
    
    return {
        "precio": precio,
        "macaulay": macaulay,
        "modificada": modificada,
        "convexidad": convexidad
    }


def calcular_tipo_forward(s1: float, s2: float, t1: float, t2: float) -> float:
    """
    Calcula el tipo de interés forward implícito f(t1, t2) a partir de los tipos spot s1 y s2.
    f(t1, t2) = ((1 + s2)^t2 / (1 + s1)^t1)^(1 / (t2 - t1)) - 1
    """
    if t1 <= 0 or t2 <= 0:
        raise ValueError("Los plazos de tiempo deben ser mayores que cero.")
    if t2 <= t1:
        raise ValueError("El plazo final (t2) debe ser mayor que el plazo inicial (t1).")
    return ((1 + s2) ** t2 / (1 + s1) ** t1) ** (1 / (t2 - t1)) - 1


def calcular_tipo_cambio_forward(spot: float, r_dom: float, r_for: float, dias: int) -> float:
    """
    Calcula el tipo de cambio forward a plazo según la paridad de tipos de interés (base 360).
    F = S * (1 + r_dom * d/360) / (1 + r_for * d/360)
    """
    if spot <= 0:
        raise ValueError("El tipo de cambio Spot debe ser mayor que cero.")
    if dias <= 0:
        raise ValueError("El plazo en días debe ser mayor que cero.")
    factor_dom = 1 + r_dom * (dias / 360)
    factor_for = 1 + r_for * (dias / 360)
    return spot * (factor_dom / factor_for)


def calcular_ratio_informacion(rp: float, rb: float, tracking_error: float) -> float:
    """
    Calcula el Ratio de Información.
    IR = (Rp - Rb) / Tracking Error
    """
    if tracking_error <= 0:
        raise ValueError("El Tracking Error debe ser mayor que cero.")
    return (rp - rb) / tracking_error


def calcular_ratio_sortino(rp: float, rf: float, downside_deviation: float) -> float:
    """
    Calcula el Ratio de Sortino.
    Sortino = (Rp - Rf) / Downside Deviation
    """
    if downside_deviation <= 0:
        raise ValueError("La desviación a la baja (downside deviation) debe ser mayor que cero.")
    return (rp - rf) / downside_deviation


def calcular_cartera_dos_activos(w1: float, w2: float, r1: float, r2: float, sigma1: float, sigma2: float, correlacion: float) -> dict:
    """
    Calcula la rentabilidad esperada y la volatilidad (desviación típica) de una cartera de dos activos.
    """
    if not (-1.0 <= correlacion <= 1.0):
        raise ValueError("El coeficiente de correlación debe estar entre -1.0 y 1.0.")
    if sigma1 < 0 or sigma2 < 0:
        raise ValueError("Las desviaciones estándar no pueden ser negativas.")
    if abs(w1 + w2 - 1.0) > 0.01:
        raise ValueError("Las ponderaciones de la cartera (w1 + w2) deben sumar 1.0.")
        
    retorno = w1 * r1 + w2 * r2
    varianza = (w1**2 * sigma1**2) + (w2**2 * sigma2**2) + (2 * w1 * w2 * sigma1 * sigma2 * correlacion)
    volatilidad = varianza ** 0.5
    
    return {
        "retorno_cartera": retorno,
        "volatilidad_cartera": volatilidad
    }


def calcular_valoracion_inmobiliaria(renta_neta: float, cap_rate: float) -> float:
    """
    Estima el valor de un inmueble usando el método de capitalización de rentas.
    Valor = Renta Neta Anual / Cap Rate
    """
    if cap_rate <= 0:
        raise ValueError("La tasa de capitalización (Cap Rate) debe ser mayor que cero.")
    return renta_neta / cap_rate


def calcular_amortizacion_francesa(nominal: float, tin: float, n_anos: int, frecuencia: int = 12) -> dict:
    """
    Calcula la cuota periódica y totales de un préstamo por el sistema francés (cuota constante).
    """
    if nominal <= 0:
        raise ValueError("El importe nominal del préstamo debe ser mayor que cero.")
    if n_anos <= 0:
        raise ValueError("El plazo en años debe ser mayor que cero.")
    if frecuencia <= 0:
        raise ValueError("La frecuencia de pagos al año debe ser mayor que cero.")
        
    i = tin / frecuencia
    p = n_anos * frecuencia
    
    if i == 0:
        cuota = nominal / p
    else:
        cuota = nominal * (i / (1 - (1 + i) ** (-p)))
        
    return {
        "cuota_periodica": cuota,
        "total_pagado": cuota * p,
        "total_intereses": (cuota * p) - nominal
    }

