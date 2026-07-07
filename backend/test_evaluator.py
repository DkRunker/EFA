import pytest
from backend.evaluator import evaluar_respuesta_desarrollo

def test_evaluar_respuesta_fallback_exito():
    # Simulamos caso exitoso sin API key (fallback por reglas)
    rubrica = {
        "palabras_clave": ["denominador", "crecimiento", "descuento"],
        "puntos_rubrica": [
            "Calcular correctamente el denominador de Gordon-Shapiro (ke - g).",
            "Obtener el precio teórico correcto.",
            "Explicar cualitativamente el efecto del crecimiento en el precio."
        ]
    }
    
    respuesta = "Calculamos el denominador ke - g = 0.04. Al aplicar el descuento, el precio teórico es 100. Un mayor crecimiento (g) aumenta el precio."
    
    res = evaluar_respuesta_desarrollo(
        pregunta_enunciado="Calcule el precio teórico usando Gordon-Shapiro con D1=4, ke=12%, g=8%",
        respuesta_alumno=respuesta,
        rubrica=rubrica,
        valor_esperado=100.0,
        tolerancia=0.1
    )
    
    assert res["score"] >= 0.70
    assert res["aprobado"] is True
    assert "100" in res["comentario_cualitativo"]
    assert res["es_evaluacion_ia"] is False  # Puesto que no hay API key en el test

def test_evaluar_respuesta_fallback_fracaso():
    # Caso con error numérico y sin palabras clave
    rubrica = {
        "palabras_clave": ["denominador", "crecimiento", "descuento"],
        "puntos_rubrica": ["Obtener precio de 100"]
    }
    respuesta = "El precio es 50 porque no sé cómo restar el crecimiento."
    
    res = evaluar_respuesta_desarrollo(
        pregunta_enunciado="Gordon-Shapiro",
        respuesta_alumno=respuesta,
        rubrica=rubrica,
        valor_esperado=100.0
    )
    
    assert res["score"] < 0.50
    assert res["aprobado"] is False
    assert res["es_evaluacion_ia"] is False
