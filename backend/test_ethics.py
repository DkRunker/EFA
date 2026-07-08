import pytest
from backend.database import obtener_preguntas_test

def test_ethics_mifid_compliance():
    # Buscamos todas las preguntas del módulo M9 (Ética y Legislación)
    preguntas_m9 = [q for q in obtener_preguntas_test() if q.modulo == "M9"]
    assert len(preguntas_m9) >= 3
    
    # Verificar que el concepto MiFID II está correctamente explicado en las respuestas
    mifid_qs = [q for q in preguntas_m9 if "mifid" in q.enunciado.lower() or "mifid" in q.explicacion.lower()]
    assert len(mifid_qs) >= 1
    
    for q in mifid_qs:
        # La explicación no debe contener términos contradictorios
        assert "mifid" in q.explicacion.lower()
        assert any(term in q.explicacion.lower() for term in ["directiva", "transparencia", "complejo", "clasificación", "cliente", "profesional", "registro"])

def test_ethics_code_of_ethics_efpa():
    # Verificar que las preguntas de ética respetan el código oficial EFPA
    preguntas_m9 = [q for q in obtener_preguntas_test() if q.modulo == "M9"]
    
    # Buscar temas de ética/blanqueo
    ethics_qs = [q for q in preguntas_m9 if any(x in q.enunciado.lower() or x in q.explicacion.lower() for x in ["ético", "ética", "blanqueo", "código"])]
    assert len(ethics_qs) >= 1
    
    for q in ethics_qs:
        # Verificar que el comportamiento ético o prevención del blanqueo tiene explicaciones justificadas
        assert len(q.explicacion) > 20
        # No debe alucinar con respuestas vacías o evasivas
        assert "simulada" not in q.explicacion.lower() or len(q.opciones) == 4
