# Especificación del Simulador de Exámenes (.specify/simulator.md)

Este documento especifica el generador de exámenes simulados y la API REST del backend de la plataforma EFA.

## Criterios de Aceptación (Gherkin)

### 1. Generación del Examen EFA Completo
```gherkin
Feature: Simulación de Examen EFA Completo

  Scenario: Compilación de examen EFA Completo respetando ponderación oficial
    Given que un alumno inicia una simulación de examen para "EFA Completo"
    And la base de datos contiene al menos:
      - 20 preguntas del módulo M1
      - 10 preguntas de M2
      - 15 preguntas de M3
      - 8 preguntas de M4, M5, M8, M9, M10, M6, M7
      - 5 preguntas prácticas de desarrollo
    When el motor de generación compila el cuestionario
    Then el examen resultante debe tener exactamente 50 preguntas tipo test
    And debe incluir al menos 1 pregunta práctica de desarrollo
    And el peso de las preguntas tipo test por módulo debe ser aproximadamente:
      | Módulo | Cantidad Esperada | Peso Oficial |
      | M1     | 12-13 preguntas   | 25.0%        |
      | M2     | 5 preguntas       | 10.0%        |
      | M3     | 8-9 preguntas     | 17.5%        |
      | M4     | 3-4 preguntas     | 7.5%         |
      | M5     | 2-3 preguntas     | 5.0%         |
      | M6     | 2-3 preguntas     | 5.0%         |
      | M7     | 2-3 preguntas     | 5.0%         |
      | M8     | 5 preguntas       | 10.0%        |
      | M9     | 3-4 preguntas     | 7.5%         |
      | M10    | 3-4 preguntas     | 7.5%         |
```

### 2. Calificación del Examen EFA Completo
```gherkin
Feature: Calificación y Feedback de Examen EFA Completo

  Scenario: Aprobado independiente en ambas partes
    Given un examen entregado con:
      - 38 aciertos de 50 en la Parte I (Test) -> 76% (Aprobado >= 70%)
      - 1 respuesta práctica calificada con 0.85 -> 85% (Aprobada >= 70%)
    When se calcula la calificación del examen
    Then el resultado general debe ser "APROBADO"

  Scenario: Suspenso por suspender la parte práctica
    Given un examen entregado con:
      - 45 aciertos de 50 en la Parte I (Test) -> 90% (Aprobado)
      - 1 respuesta práctica calificada con 0.50 -> 50% (Suspenso)
    When se calcula la calificación del examen
    Then el resultado general debe ser "SUSPENDIDO"
    And debe detallar que se suspendió la parte práctica
```
