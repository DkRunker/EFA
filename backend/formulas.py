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
