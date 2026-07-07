import pytest
from backend.database import generar_examen, obtener_preguntas_test

def test_generar_examen_efa_completo():
    examen = generar_examen("EFA Completo")
    
    assert examen["tipo_examen"] == "EFA Completo"
    assert len(examen["preguntas_test"]) == 50
    assert examen["incluye_practica"] is True
    assert examen["pregunta_practica"] is not None
    assert len(examen["ids_originales_test"]) == 50
    
    # Verificar la distribución
    modulos = [q["modulo"] for q in examen["preguntas_test"]]
    # Contar ocurrencias
    counts = {m: modulos.count(m) for m in set(modulos)}
    
    assert counts.get("M1", 0) == 13
    assert counts.get("M2", 0) == 5
    assert counts.get("M3", 0) == 9
    assert counts.get("M4", 0) == 4
    assert counts.get("M5", 0) == 3
    assert counts.get("M8", 0) == 5
    assert counts.get("M9", 0) == 4
    assert counts.get("M10", 0) == 3

def test_generar_examen_eip():
    examen = generar_examen("EIP")
    
    assert examen["tipo_examen"] == "EIP"
    assert len(examen["preguntas_test"]) == 40
    assert examen["incluye_practica"] is False
    assert examen["pregunta_practica"] is None
    
    modulos = [q["modulo"] for q in examen["preguntas_test"]]
    counts = {m: modulos.count(m) for m in set(modulos)}
    
    assert counts.get("M1", 0) == 10
    assert counts.get("M2", 0) == 4
    assert counts.get("M3", 0) == 7

def test_generar_examen_error():
    with pytest.raises(ValueError, match="Tipo de examen no reconocido"):
        generar_examen("Examen Inventado")
