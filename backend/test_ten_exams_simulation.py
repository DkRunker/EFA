import pytest
import random
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_student_lifecycle_with_ten_exams():
    print("\n\n=== INICIANDO SIMULACIÓN DE CICLO COMPLETO CON 10 EXÁMENES ===")
    
    # 1. REGISTRO
    username = f"estudiante_estudioso_{random.randint(1000, 9999)}"
    print(f"\n[Fase 1] Registrando nuevo usuario: {username}...")
    reg_res = client.post("/api/auth/register", json={
        "username": username,
        "password": "password_segura_123"
    })
    assert reg_res.status_code == 200
    print("-> Registro exitoso:", reg_res.json()["message"])

    # 2. LOGIN
    print(f"\n[Fase 2] Iniciando sesión para {username}...")
    login_res = client.post("/api/auth/login", json={
        "username": username,
        "password": "password_segura_123"
    })
    assert login_res.status_code == 200
    token = login_res.json()["token"]
    print("-> Login exitoso. Token obtenido:", token)

    # 3. ESTUDIO COMPLETO DE TODO LO QUE OFRECE LA WEB
    print("\n[Fase 3] Simulando ESTUDIO COMPLETO de los 10 módulos del temario...")
    # El estudiante lee consecutivamente los 10 temas
    for i in range(1, 11):
        mod_id = f"M{i}"
        resp_note = client.get(f"/api/study/apuntes/{mod_id}")
        assert resp_note.status_code == 200
        note_data = resp_note.json()
        print(f"  - Leído Tema {i} ({mod_id}). Título/Sección: {note_data['apuntes'][:50].strip()}...")
        
    print("\n[Fase 3.b] Simulando PRÁCTICA en el Sandbox para todas las fórmulas...")
    formulas_a_estudiar = [
        ("gordon_shapiro", {"d1": 5.0, "ke": 0.15, "g": 0.10}),
        ("sharpe", {"rp": 0.12, "rf": 0.02, "sigma_p": 0.10}),
        ("treynor", {"rp": 0.12, "rf": 0.02, "beta_p": 1.2}),
        ("jensen", {"rp": 0.12, "rf": 0.02, "beta_p": 1.2, "rm": 0.09}),
        ("tae", {"tin": 0.08, "m": 4}),
        ("precio_bono", {"nominal": 1000.0, "cupon_anual_pct": 0.06, "n_anos": 5, "tir": 0.05}),
        ("irpf_ahorro", {"base_liquidable": 120000.0})
    ]
    for formula, params in formulas_a_estudiar:
        calc_resp = client.post("/api/formulas/calculate", json={
            "formula": formula,
            "params": params
        })
        assert calc_resp.status_code == 200
        print(f"  - Sandbox de {formula} calculado con éxito.")

    # 4. EXÁMENES (REALIZA 10 EXÁMENES)
    print("\n[Fase 4] Iniciando la ronda de 10 exámenes...")
    
    # Distribución de tipos de examen
    tipos_examen = [
        "EIP", "EIP", "EIP",
        "EFA Nivel II", "EFA Nivel II", "EFA Nivel II",
        "EFA Completo", "EFA Completo", "EFA Completo", "EFA Completo"
    ]
    
    intentos_aprobados = 0
    from backend.database import PREGUNTAS_TEST

    for i, tipo in enumerate(tipos_examen, 1):
        print(f"\n--- Examen #{i} / 10 ({tipo}) ---")
        
        # Iniciar examen
        start_res = client.post("/api/exams/start", json={"tipo_examen": tipo})
        assert start_res.status_code == 200
        session_data = start_res.json()
        session_id = session_data["session_id"]
        
        # Responder preguntas de test
        es_estudioso_en_este = (i % 2 == 0) # Exámenes pares: aprobados (estudiados), Exámenes impares: suspendidos
        
        respuestas_test = {}
        for q in session_data["preguntas_test"]:
            if es_estudioso_en_este:
                # Buscamos el original para responder correctamente
                original_q = next(x for x in PREGUNTAS_TEST if x.id == q["id"])
                respuestas_test[str(q["id"])] = original_q.respuesta_correcta
            else:
                respuestas_test[str(q["id"])] = 2 # Falta de conocimientos
                
        # Responder pregunta práctica
        respuestas_practica = {}
        if session_data["pregunta_practica"]:
            id_prac = session_data["pregunta_practica"]["id"]
            if es_estudioso_en_este:
                if id_prac == 1001:
                    respuestas_practica[str(id_prac)] = (
                        "Para resolver Gordon-Shapiro, calculamos el denominador ke - g = 0.12 - 0.08 = 0.04. "
                        "El precio teórico P0 inicial es 4.00 / 0.04 = 100.00 €. Si g sube al 9.0% (0.09), "
                        "el precio teórico es de 4.00 / 0.03 = 133.33 €. La tasa de crecimiento de dividendos tiene "
                        "una relación directa y aumenta el precio."
                    )
                elif id_prac == 1002:
                    respuestas_practica[str(id_prac)] = (
                        "El Ratio de Sharpe es de 1.50, calculado como (0.15 - 0.03) / 0.08 = 1.50. "
                        "El Ratio de Treynor es de 0.10 (10%), calculado como (0.15 - 0.03) / 1.2. "
                        "El Ratio de Sharpe mide el riesgo total (volatilidad), mientras que Treynor mide el riesgo sistemático (Beta). "
                        "Si la cartera no está bien diversificada, puede penalizar en Sharpe pero verse aceptable en Treynor."
                    )
                elif id_prac == 1003:
                    respuestas_practica[str(id_prac)] = (
                        "La cuota tributaria en el IRPF del ahorro se calcula por tramos: Tramo 1 (hasta 6.000 €) al 19% = 1.140 €. "
                        "Tramo 2 (hasta 50.000 €) al 21% por 44.000 € = 9.240 €. Tramo 3 (de 50.000 a 70.000 €) al 23% por 20.000 € = 4.600 €. "
                        "La cuota total del ahorro en el IRPF es de 1.140 + 9.240 + 4.600 = 14980.0 €."
                    )
            else:
                respuestas_practica[str(id_prac)] = "No tengo conocimientos suficientes para resolver este caso práctico."

        # Entregar examen
        submit_res = client.post("/api/exams/submit", json={
            "session_id": session_id,
            "respuestas_test": respuestas_test,
            "respuestas_practica": respuestas_practica
        })
        assert submit_res.status_code == 200
        report = submit_res.json()
        
        # Mostrar resumen
        aprobado_gen = report["aprobado_general"]
        if aprobado_gen:
            intentos_aprobados += 1
            
        print(f"  - Resultado: {'APROBADO' if aprobado_gen else 'SUSPENDIDO'}")
        print(f"  - Nota Test: {report['nota_test_pct']}% (Aciertos: {report['aciertos_test']}/{report['total_test']})")
        if report["nota_practica_pct"] is not None:
            print(f"  - Nota Práctica: {report['nota_practica_pct']}%")
            if report["evaluacion_practica"]:
                print(f"  - Comentario del tribunal: {report['evaluacion_practica']['comentario_cualitativo'][:100]}...")

    print(f"\n=== FIN DE SIMULACIÓN COMPLETA DE 10 EXÁMENES ===")
    print(f"Total exámenes realizados: 10")
    print(f"Total exámenes aprobados: {intentos_aprobados} / 10")
    print("=========================================================")
    
    # Validamos que los 5 exámenes estudiados hayan sido aprobados y los 5 no estudiados hayan sido suspendidos
    assert intentos_aprobados == 5
