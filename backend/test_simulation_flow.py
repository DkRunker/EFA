import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_simulated_student_flow():
    print("\n--- INICIO DE SIMULACIÓN DE ESTUDIANTE SIN CONOCIMIENTOS PREVIOS ---")
    
    # 1. REGISTRO
    print("[1] Registrando al estudiante 'estudiante_novato'...")
    reg_res = client.post("/api/auth/register", json={
        "username": "estudiante_novato",
        "password": "segura_password_456"
    })
    assert reg_res.status_code == 200
    print("-> Registro exitoso:", reg_res.json())

    # 2. LOGIN
    print("[2] Iniciando sesión...")
    login_res = client.post("/api/auth/login", json={
        "username": "estudiante_novato",
        "password": "segura_password_456"
    })
    assert login_res.status_code == 200
    token_data = login_res.json()
    print("-> Login exitoso. Token recibido:", token_data["token"])

    # 3. ESTUDIO (Sandbox de Fórmulas)
    # El alumno estudia Gordon-Shapiro
    print("[3] Estudiando Gordon-Shapiro en el Sandbox...")
    calc_gs = client.post("/api/formulas/calculate", json={
        "formula": "gordon_shapiro",
        "params": {"d1": 5.0, "ke": 0.15, "g": 0.10}
    })
    assert calc_gs.status_code == 200
    res_gs = calc_gs.json()
    assert res_gs["precio_teorico"] == pytest.approx(100.0)
    print("-> Precio Teórico calculado:", res_gs["precio_teorico"])

    # El alumno estudia IRPF Ahorro España 2026
    print("[3.b] Estudiando liquidación de IRPF Ahorro...")
    calc_irpf = client.post("/api/formulas/calculate", json={
        "formula": "irpf_ahorro",
        "params": {"base_liquidable": 20000.0}
    })
    assert calc_irpf.status_code == 200
    res_irpf = calc_irpf.json()
    # 6.000 * 19% + 14.000 * 21% = 1.140 + 2.940 = 4.080
    assert res_irpf["cuota_total"] == pytest.approx(4080.0)
    print("-> Cuota total de IRPF calculada para 20.000 €:", res_irpf["cuota_total"])

    # 4. INICIAR EXAMEN (EFA Completo)
    print("[4] Iniciando simulación de examen 'EFA Completo'...")
    start_res = client.post("/api/exams/start", json={
        "tipo_examen": "EFA Completo"
    })
    assert start_res.status_code == 200
    exam_session = start_res.json()
    session_id = exam_session["session_id"]
    print("-> Examen iniciado. ID Sesión:", session_id)
    print(f"-> Cargadas {len(exam_session['preguntas_test'])} preguntas de test y 1 pregunta práctica.")

    # 5. REALIZAR EXAMEN (El alumno no sabe y responde de forma aleatoria/errónea)
    print("[5] El alumno responde al test (elige la opción 2 para todas por falta de conocimientos)...")
    respuestas_test = {str(q["id"]): 2 for q in exam_session["preguntas_test"]}
    
    # Responde a la práctica con un texto vacío/sin fórmulas
    id_prac = exam_session["pregunta_practica"]["id"]
    print(f"[5.b] El alumno responde a la pregunta de desarrollo práctica {id_prac} sin razonar...")
    respuestas_practica = {
        str(id_prac): "No tengo conocimientos previos sobre esta materia. El precio teórico es cero y no sé calcular el IRPF."
    }

    # 6. ENTREGAR EXAMEN
    print("[6] Entregando examen para calificar...")
    submit_res = client.post("/api/exams/submit", json={
        "session_id": session_id,
        "respuestas_test": respuestas_test,
        "respuestas_practica": respuestas_practica
    })
    assert submit_res.status_code == 200
    report = submit_res.json()
    
    print("\n--- INFORME DE CALIFICACIÓN RECIBIDO ---")
    print("Tipo de examen:", report["tipo_examen"])
    print(f"Nota Test: {report['nota_test_pct']}% (Aciertos: {report['aciertos_test']}/{report['total_test']})")
    print("Nota Práctica:", report["nota_practica_pct"], "%")
    print("Aprobado General:", report["aprobado_general"])
    print("Veredicto Cualitativo del Tribunal:")
    if report["evaluacion_practica"]:
        print("  - Comentario:", report["evaluacion_practica"]["comentario_cualitativo"])
        print("  - Puntos cumplidos:", report["evaluacion_practica"]["puntos_cumplidos"])
        print("  - Puntos fallidos:", report["evaluacion_practica"]["puntos_fallidos"])
    
    # Aserciones lógicas
    assert report["aprobado_general"] is False  # Definitivamente suspende
    assert report["nota_practica_pct"] < 50.0  # Su respuesta práctica es muy deficiente
    print("-> El flujo de examen e integración de resultados funciona a la perfección sin ningún tipo de error.")
    print("--- FIN DE SIMULACIÓN EXITOSA ---")
