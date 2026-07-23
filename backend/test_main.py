import pytest
from fastapi.testclient import TestClient
from backend.main import app

from backend.conftest import cabeceras_auth

# Los endpoints exigen sesión iniciada: el cliente la lleva puesta.
client = TestClient(app, headers=cabeceras_auth())

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
    assert response.json()["precio_teorico"] == pytest.approx(100.0)

def test_api_auth_register_and_login():
    # 1. Registrar un usuario nuevo
    reg_response = client.post("/api/auth/register", json={"username": "simulado", "password": "password123"})
    assert reg_response.status_code == 200
    assert reg_response.json()["message"] == "Usuario registrado con éxito."

    # 2. Registrar el mismo usuario otra vez (debe dar error 400)
    reg_dup = client.post("/api/auth/register", json={"username": "simulado", "password": "password123"})
    assert reg_dup.status_code == 400
    assert "ya existe" in reg_dup.json()["detail"]

    # 3. Hacer login correcto
    login_response = client.post("/api/auth/login", json={"username": "simulado", "password": "password123"})
    assert login_response.status_code == 200
    assert login_response.json()["username"] == "simulado"
    assert "token" in login_response.json()

    # 4. Hacer login incorrecto (contraseña errónea)
    login_err = client.post("/api/auth/login", json={"username": "simulado", "password": "password_error"})
    assert login_err.status_code == 401
    assert "incorrectos" in login_err.json()["detail"]

def test_api_study_apuntes():
    # 1. Obtener todos los apuntes
    response = client.get("/api/study/apuntes")
    assert response.status_code == 200
    data = response.json()
    assert "M1" in data
    assert "M3" in data
    assert "M10" in data
    
    # 2. Obtener un apunte específico
    resp_m3 = client.get("/api/study/apuntes/M3")
    assert resp_m3.status_code == 200
    assert "Frontera Eficiente" in resp_m3.json()["apuntes"]
    assert resp_m3.json()["modulo"] == "M3"

    # 3. Módulo inválido
    resp_inv = client.get("/api/study/apuntes/M11")
    assert resp_inv.status_code == 404

