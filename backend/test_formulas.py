import pytest
from backend.formulas import (
    calcular_gordon_shapiro,
    calcular_sharpe,
    calcular_treynor,
    calcular_jensen,
    calcular_tae,
    calcular_precio_bono,
    calcular_irpf_ahorro
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
