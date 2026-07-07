# Especificación del Evaluador de Respuestas Prácticas (.specify/evaluator.md)

Este documento especifica el motor de evaluación para las respuestas de desarrollo práctico del examen EFA (Parte II). El motor debe calificar tanto la exactitud numérica como la calidad cualitativa del razonamiento financiero.

## Criterios de Aceptación (Gherkin)

### 1. Evaluación con Modelo de Lenguaje (Con API Key)
```gherkin
Feature: Evaluación cualitativa y cuantitativa mediante LLM

  Scenario: Respuesta con explicación correcta y número exacto
    Given una pregunta práctica de valoración de Gordon-Shapiro
    And una rúbrica oficial que exige:
      - Obtener el denominador de 0.04 (o 4% de prima de descuento neta)
      - Obtener el precio teórico de 100 €
      - Explicar la relación inversa entre el crecimiento y el precio
    And la respuesta redactada por el alumno: "El denominador ke - g es 0.12 - 0.08 = 0.04. Al descontar el dividendo de 4 € entre 0.04, obtenemos un precio teórico de 100 €. Si la tasa g subiera, el denominador disminuiría y el precio teórico de la acción se incrementaría."
    When se ejecuta la evaluación por LLM
    Then el puntaje total obtenido debe ser del 100%
    And el veredicto debe calificar la explicación cualitativa como "Excelente"
    And se deben listar los puntos de la rúbrica cumplidos

  Scenario: Respuesta con número incorrecto por error en el denominador
    Given una pregunta de valoración de Gordon-Shapiro
    And la respuesta redactada por el alumno: "El precio es 4 / 0.12 = 33.33 €"
    When se ejecuta la evaluación por LLM
    Then el puntaje total obtenido debe ser inferior al 50%
    And la retroalimentación debe identificar el error de distractor (no restar la tasa de crecimiento 'g' en el denominador)
```

### 2. Evaluación por Reglas Deterministas (Sin API Key / Fallback)
```gherkin
Feature: Evaluación de respaldo (Fallback) basada en reglas fijas

  Scenario: Detección de números clave y palabras clave
    Given una pregunta con valor de referencia numérico de 100.0
    And palabras clave requeridas: ["denominador", "descuento", "crecimiento"]
    And la respuesta del alumno: "El precio descontado es 100 € debido al crecimiento de dividendos y la tasa ke."
    When se ejecuta la evaluación por reglas
    Then el resultado debe indicar aprobado (Score >= 70%)
    And la retroalimentación debe señalar el acierto del valor numérico 100.0 y las palabras clave encontradas
```
