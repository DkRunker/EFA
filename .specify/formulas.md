# Especificación del Motor de Fórmulas Financieras (.specify/formulas.md)

Este documento especifica el comportamiento esperado de las funciones matemáticas del motor de cálculo determinista para la preparación del examen EFA.

## Criterios de Aceptación (Gherkin)

### 1. Valoración por Gordon-Shapiro
```gherkin
Feature: Valoración de activos por Descuento de Dividendos (Gordon-Shapiro)

  Scenario: Cálculo exitoso del precio teórico
    Given un dividendo esperado el próximo año (D1) de 4.00
    And una rentabilidad exigida (ke) del 12.0% (0.12)
    And una tasa de crecimiento constante (g) del 8.0% (0.08)
    When se ejecuta la fórmula de Gordon-Shapiro
    Then el precio teórico resultante debe ser exactamente 100.00
    And el denominador neto (ke - g) debe ser 0.04

  Scenario: Error cuando la tasa de crecimiento es igual o mayor a la rentabilidad exigida
    Given un dividendo esperado de 2.00
    And una rentabilidad exigida (ke) del 10.0% (0.10)
    And una tasa de crecimiento (g) del 10.0% (0.10)
    When se ejecuta la fórmula de Gordon-Shapiro
    Then debe lanzarse un error indicando que ke debe ser mayor que g
```

### 2. Ratios de Sharpe, Treynor y Alfa de Jensen
```gherkin
Feature: Ratios de Rentabilidad Ajustada al Riesgo (Módulo de Gestión de Carteras)

  Scenario: Cálculo del Ratio de Sharpe
    Given una rentabilidad de la cartera (Rp) del 15.0% (0.15)
    And una tasa libre de riesgo (Rf) del 3.0% (0.03)
    And una volatilidad de la cartera (sigma_p) del 8.0% (0.08)
    When se calcula el Ratio de Sharpe
    Then el resultado debe ser exactamente 1.50

  Scenario: Cálculo del Ratio de Treynor
    Given una rentabilidad de la cartera (Rp) del 15.0% (0.15)
    And una tasa libre de riesgo (Rf) del 3.0% (0.03)
    And una Beta de la cartera (beta_p) de 1.2
    When se calcula el Ratio de Treynor
    Then el resultado debe ser exactamente 0.10 (ó 10%)

  Scenario: Cálculo del Alfa de Jensen
    Given una rentabilidad de la cartera (Rp) del 15.0% (0.15)
    And una tasa libre de riesgo (Rf) del 3.0% (0.03)
    And una Beta de la cartera (beta_p) de 1.2
    And una rentabilidad del mercado (Rm) del 10.0% (0.10)
    When se calcula el Alfa de Jensen
    Then el alfa resultante debe ser exactamente 0.036 (3.6%)
```

### 3. Equivalencia TIN y TAE (Interés Compuesto)
```gherkin
Feature: Cálculo de la Tasa Anual Equivalente (TAE)

  Scenario: Conversión de TIN a TAE con capitalización mensual
    Given un Tipo de Interés Nominal (TIN) del 6.0% (0.06)
    And un número de periodos de liquidación al año (m) de 12 (mensual)
    When se calcula la TAE
    Then la TAE resultante debe ser aproximadamente del 6.1678% (0.061678)
```

### 4. Valoración de Renta Fija (Precio de un Bono)
```gherkin
Feature: Precio de un Bono mediante Cupón y TIR

  Scenario: Precio de un bono anual con vencimiento a 3 años
    Given un valor nominal (N) de 1000.00
    And un cupón anual del 5.0% (50.00)
    And un vencimiento (n) de 3 años
    And una TIR (y) del 4.0% (0.04)
    When se calcula el precio actual del bono
    Then el precio debe ser aproximadamente 1027.75
```

### 5. Liquidación de Impuestos (Escala del Ahorro IRPF España 2026)
```gherkin
Feature: Liquidación del Impuesto de la Renta sobre el Ahorro

  Scenario: Base liquidable de 70,000 €
    Given una base imponible del ahorro de 70000.00 €
    When se calcula la cuota del IRPF del ahorro aplicando la escala 2026:
      | Tramo inferior | Tramo superior | Tipo gravamen |
      | 0 €            | 6.000 €        | 19%           |
      | 6.000 €        | 50.000 €       | 21%           |
      | 50.000 €       | 200.000 €      | 23%           |
      | 200.000 €      | 300.000 €      | 27%           |
      | 300.000 €      | en adelante    | 28%           |
    Then la cuota tributaria resultante debe ser exactamente 14,980.00 €
    # Desglose:
    # - Primeros 6.000 € al 19% = 1.140 €
    # - Siguientes 44.000 € (de 6k a 50k) al 21% = 9.240 €
    # - Restantes 20.000 € (de 50k a 70k) al 23% = 4.600 €
    # - Total = 1.140 + 9.240 + 4.600 = 14.980 €
```
