import pytest
from backend.formulas import (
    calcular_gordon_shapiro,
    calcular_sharpe,
    calcular_treynor,
    calcular_jensen,
    calcular_tae,
    calcular_precio_bono,
    calcular_irpf_ahorro,
    calcular_duracion_bono,
    calcular_tipo_forward,
    calcular_tipo_cambio_forward,
    calcular_ratio_informacion,
    calcular_ratio_sortino,
    calcular_cartera_dos_activos,
    calcular_valoracion_inmobiliaria,
    calcular_amortizacion_francesa
)

# 1. Tests Gordon-Shapiro
def test_gordon_shapiro_exito():
    res = calcular_gordon_shapiro(d1=4.00, ke=0.12, g=0.08)
    assert res["denominador"] == pytest.approx(0.04)
    assert res["precio_teorico"] == pytest.approx(100.00)

def test_gordon_shapiro_error_ke_menor_o_igual_g():
    with pytest.raises(ValueError, match="La rentabilidad exigida .* debe ser mayor que la tasa de crecimiento"):
        calcular_gordon_shapiro(d1=2.00, ke=0.10, g=0.10)
    with pytest.raises(ValueError, match="La rentabilidad exigida .* debe ser mayor que la tasa de crecimiento"):
        calcular_gordon_shapiro(d1=2.00, ke=0.08, g=0.10)

# 2. Tests Sharpe, Treynor y Jensen
def test_sharpe():
    res = calcular_sharpe(rp=0.15, rf=0.03, sigma_p=0.08)
    assert res == pytest.approx(1.50)

def test_treynor():
    res = calcular_treynor(rp=0.15, rf=0.03, beta_p=1.2)
    assert res == pytest.approx(0.10)

def test_jensen():
    res = calcular_jensen(rp=0.15, rf=0.03, beta_p=1.2, rm=0.10)
    assert res == pytest.approx(0.036)

# 3. Tests TAE
def test_tae():
    res = calcular_tae(tin=0.06, m=12)
    assert res == pytest.approx(0.061678, abs=1e-6)

# 4. Tests Precio de un Bono
def test_precio_bono():
    res = calcular_precio_bono(nominal=1000.0, cupon_anual_pct=0.05, n_anos=3, tir=0.04)
    assert res == pytest.approx(1027.75, abs=1e-2)

# 5. Tests IRPF Ahorro España 2026
def test_irpf_ahorro_70k():
    res = calcular_irpf_ahorro(base_liquidable=70000.0)
    assert res["cuota_total"] == pytest.approx(14980.0)
    assert res["desglose"] == [
        {"tramo": "hasta 6.000 €", "tipo": 0.19, "base_tramo": 6000.0, "cuota_tramo": 1140.0},
        {"tramo": "de 6.000 a 50.000 €", "tipo": 0.21, "base_tramo": 44000.0, "cuota_tramo": 9240.0},
        {"tramo": "de 50.000 a 200.000 €", "tipo": 0.23, "base_tramo": 20000.0, "cuota_tramo": 4600.0},
        {"tramo": "de 200.000 a 300.000 €", "tipo": 0.27, "base_tramo": 0.0, "cuota_tramo": 0.0},
        {"tramo": "más de 300.000 €", "tipo": 0.28, "base_tramo": 0.0, "cuota_tramo": 0.0}
    ]

def test_irpf_ahorro_bajo():
    res = calcular_irpf_ahorro(base_liquidable=5000.0)
    assert res["cuota_total"] == pytest.approx(5000.0 * 0.19)

def test_irpf_ahorro_alto():
    # 400.000 €
    # - 6.000 * 0.19 = 1.140
    # - 44.000 * 0.21 = 9.240
    # - 150.000 * 0.23 = 34.500
    # - 100.000 * 0.27 = 27.000
    # - 100.000 * 0.28 = 28.000
    # Total = 1.140 + 9.240 + 34.500 + 27.000 + 28.000 = 99.880 €
    res = calcular_irpf_ahorro(base_liquidable=400000.0)
    assert res["cuota_total"] == pytest.approx(99880.0)


# 6. Tests Duración y Convexidad del Bono
def test_duracion_bono():
    res = calcular_duracion_bono(nominal=1000.0, cupon_anual_pct=0.05, n_anos=3, tir=0.04, frecuencia=1)
    assert res["precio"] == pytest.approx(1027.75, abs=1e-2)
    assert res["macaulay"] == pytest.approx(2.86, abs=1e-2)
    assert res["modificada"] == pytest.approx(2.75, abs=1e-2)
    assert res["convexidad"] == pytest.approx(10.41, abs=1e-2)


# 7. Tests Tipo Forward
def test_tipo_forward():
    res = calcular_tipo_forward(s1=0.03, s2=0.04, t1=1.0, t2=2.0)
    assert res == pytest.approx(0.0501, abs=1e-4)


# 8. Tests Tipo de Cambio Forward
def test_tipo_cambio_forward():
    res = calcular_tipo_cambio_forward(spot=1.10, r_dom=0.035, r_for=0.02, dias=180)
    assert res == pytest.approx(1.108168, abs=1e-5)


# 9. Tests Ratios Sharpe, Treynor, Jensen e Información/Sortino
def test_ratio_informacion():
    res = calcular_ratio_informacion(rp=0.10, rb=0.08, tracking_error=0.04)
    assert res == pytest.approx(0.50)


def test_ratio_sortino():
    res = calcular_ratio_sortino(rp=0.12, rf=0.02, downside_deviation=0.05)
    assert res == pytest.approx(2.00)


# 10. Tests Cartera de Dos Activos
def test_cartera_dos_activos():
    res = calcular_cartera_dos_activos(w1=0.6, w2=0.4, r1=0.10, r2=0.15, sigma1=0.08, sigma2=0.12, correlacion=-0.5)
    assert res["retorno_cartera"] == pytest.approx(0.12)
    assert res["volatilidad_cartera"] == pytest.approx(0.048)


# 11. Tests Valoración Inmobiliaria
def test_valoracion_inmobiliaria():
    res = calcular_valoracion_inmobiliaria(renta_neta=12000.0, cap_rate=0.06)
    assert res == pytest.approx(200000.0)


# 12. Tests Amortización Francesa
def test_amortizacion_francesa():
    res = calcular_amortizacion_francesa(nominal=100000.0, tin=0.03, n_anos=20, frecuencia=12)
    assert res["cuota_periodica"] == pytest.approx(554.60, abs=1e-2)
