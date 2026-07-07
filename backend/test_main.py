from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_api_start_exam_efa_completo():
    response = client.post("/api/exams/start", json={"tipo_examen": "EFA Completo"})
    assert response.status_code == 200
    data = response.json()
    assert "session_id" in data
    assert data["tipo_examen"] == "EFA Completo"
    assert len(data["preguntas_test"]) == 50
    assert data["incluye_practica"] is True
    assert data["pregunta_practica"] is not None

def test_api_start_exam_invalid():
    response = client.post("/api/exams/start", json={"tipo_examen": "Examen Invalido"})
    assert response.status_code == 400
    assert "detail" in response.json()

def test_api_submit_exam_complete_flow():
    # 1. Iniciar examen
    response = client.post("/api/exams/start", json={"tipo_examen": "EFA Completo"})
    assert response.status_code == 200
    exam_data = response.json()
    session_id = exam_data["session_id"]
    
    # 2. Responder (simulamos responder la primera opción 0 a todas y vaciar la práctica)
    respuestas_test = {str(q["id"]): 0 for q in exam_data["preguntas_test"]}
    respuesta_practica = {
        str(exam_data["pregunta_practica"]["id"]): "El precio teórico es de 100 €. Denominador es 0.04."
    }
    
    submit_response = client.post("/api/exams/submit", json={
        "session_id": session_id,
        "respuestas_test": respuestas_test,
        "respuestas_practica": respuesta_practica
    })
    
    assert submit_response.status_code == 200
    report = submit_response.json()
    assert "aprobado_general" in report
    assert "nota_test_pct" in report
    assert "nota_practica_pct" in report
    assert "evaluacion_practica" in report

def test_api_formulas_calculate():
    response = client.post("/api/formulas/calculate", json={
        "formula": "gordon_shapiro",
        "params": {"d1": 4.0, "ke": 0.12, "g": 0.08}
    })
    assert response.status_code == 200
    assert response.json()["precio_teorico"] == 100.0
