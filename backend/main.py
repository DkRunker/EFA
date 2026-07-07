import uuid
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any

from backend.database import generar_examen, PREGUNTAS_TEST, PREGUNTAS_PRACTICAS, APUNTES_TEORICOS
from backend.evaluator import evaluar_respuesta_desarrollo
from backend.formulas import (
    calcular_gordon_shapiro,
    calcular_sharpe,
    calcular_treynor,
    calcular_jensen,
    calcular_tae,
    calcular_precio_bono,
    calcular_irpf_ahorro
)

app = FastAPI(title="EFA Prep Platform API", version="1.0.0")

# Permitir CORS para desarrollo local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Almacenamiento en memoria de sesiones de examen activas
active_sessions: dict[str, dict] = {}
users_db: dict[str, str] = {}

class UserAuth(BaseModel):
    username: str
    password: str

@app.post("/api/auth/register")
def api_register(user: UserAuth):
    if user.username in users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario ya existe."
        )
    users_db[user.username] = user.password
    return {"message": "Usuario registrado con éxito."}

@app.post("/api/auth/login")
def api_login(user: UserAuth):
    if user.username not in users_db or users_db[user.username] != user.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos."
        )
    return {"username": user.username, "token": f"mock-token-{uuid.uuid4().hex[:8]}"}

class StartExamRequest(BaseModel):
    tipo_examen: str

class SubmitExamRequest(BaseModel):
    session_id: str
    respuestas_test: dict[str, int]  # { "question_id": selected_option_index }
    respuestas_practica: dict[str, str]  # { "question_id": student_answer_text }

class CalculateFormulaRequest(BaseModel):
    formula: str
    params: dict[str, Any]

@app.post("/api/exams/start")
def api_start_exam(req: StartExamRequest):
    try:
        examen = generar_examen(req.tipo_examen)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        
    session_id = str(uuid.uuid4())
    
    # Almacenamos el examen completo (con respuestas correctas) indexado por session_id
    active_sessions[session_id] = {
        "tipo_examen": examen["tipo_examen"],
        "ids_originales_test": examen["ids_originales_test"],
        "id_practica_original": examen["id_practica_original"],
        "respuestas_correctas_test": examen["respuestas_correctas_test"],
        "opciones_mezcladas_test": {str(q["id"]): q["opciones"] for q in examen["preguntas_test"]}
    }
    
    # Retornamos el examen limpio al frontend
    return {
        "session_id": session_id,
        "tipo_examen": examen["tipo_examen"],
        "preguntas_test": examen["preguntas_test"],
        "incluye_practica": examen["incluye_practica"],
        "pregunta_practica": examen["pregunta_practica"]
    }

@app.post("/api/exams/submit")
def api_submit_exam(req: SubmitExamRequest):
    session = active_sessions.get(req.session_id)
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Sesión de examen no encontrada o caducada."
        )
        
    tipo_examen = session["tipo_examen"]
    ids_test = session["ids_originales_test"]
    id_practica = session["id_practica_original"]
    
    # 1. Calificar Parte I (Test)
    aciertos = 0
    total_test = len(ids_test)
    desglose_test = []
    
    for qid in ids_test:
        # Encontrar pregunta original
        original = next(q for q in PREGUNTAS_TEST if q.id == qid)
        # Obtener respuesta del alumno (la clave en JSON del dict es string)
        alumno_ans = req.respuestas_test.get(str(qid))
        
        es_correcta = False
        correct_ans_index = session["respuestas_correctas_test"].get(str(qid))
        if alumno_ans is not None and alumno_ans == correct_ans_index:
            es_correcta = True
            aciertos += 1
            
        desglose_test.append({
            "id": original.id,
            "modulo": original.modulo,
            "enunciado": original.enunciado,
            "opciones": session["opciones_mezcladas_test"].get(str(qid)),
            "respuesta_alumno": alumno_ans,
            "respuesta_correcta": correct_ans_index,
            "es_correcta": es_correcta,
            "explicacion": original.explicacion
        })
        
    nota_test_pct = (aciertos / total_test) * 100 if total_test > 0 else 0.0
    aprobado_test = nota_test_pct >= 70.0
    
    # 2. Calificar Parte II (Práctica de Desarrollo) si aplica
    nota_practica_pct = None
    aprobado_practica = None
    evaluacion_report = None
    
    if id_practica is not None:
        original_prac = next(q for q in PREGUNTAS_PRACTICAS if q.id == id_practica)
        alumno_text = req.respuestas_practica.get(str(id_practica), "")
        
        # Llamar al evaluador
        eval_res = evaluar_respuesta_desarrollo(
            pregunta_enunciado=original_prac.enunciado,
            respuesta_alumno=alumno_text,
            rubrica={
                "puntos_rubrica": original_prac.rubrica,
                "palabras_clave": original_prac.palabras_clave
            },
            valor_esperado=original_prac.valor_esperado,
            tolerancia=original_prac.tolerancia
        )
        
        nota_practica_pct = eval_res["score"] * 100
        aprobado_practica = eval_res["aprobado"]
        evaluacion_report = eval_res
        
    # 3. Determinar aprobado general
    # EIP: solo test >= 70%
    # EFA Completo / Nivel II: test >= 70% Y practica >= 70%
    if tipo_examen in ["EFA Completo", "EFA Nivel II"]:
        aprobado_general = aprobado_test and (aprobado_practica is True)
    else:
        aprobado_general = aprobado_test
        
    # Borrar la sesión para liberar memoria
    active_sessions.pop(req.session_id, None)
    
    return {
        "tipo_examen": tipo_examen,
        "nota_test_pct": round(nota_test_pct, 2),
        "aciertos_test": aciertos,
        "total_test": total_test,
        "aprobado_test": aprobado_test,
        "nota_practica_pct": round(nota_practica_pct, 2) if nota_practica_pct is not None else None,
        "aprobado_practica": aprobado_practica,
        "aprobado_general": aprobado_general,
        "evaluacion_practica": evaluacion_report,
        "desglose_test": desglose_test
    }

@app.post("/api/formulas/calculate")
def api_calculate_formula(req: CalculateFormulaRequest):
    formula = req.formula
    p = req.params
    
    try:
        if formula == "gordon_shapiro":
            return calcular_gordon_shapiro(d1=p["d1"], ke=p["ke"], g=p["g"])
        elif formula == "sharpe":
            val = calcular_sharpe(rp=p["rp"], rf=p["rf"], sigma_p=p["sigma_p"])
            return {"result": val}
        elif formula == "treynor":
            val = calcular_treynor(rp=p["rp"], rf=p["rf"], beta_p=p["beta_p"])
            return {"result": val}
        elif formula == "jensen":
            val = calcular_jensen(rp=p["rp"], rf=p["rf"], beta_p=p["beta_p"], rm=p["rm"])
            return {"result": val}
        elif formula == "tae":
            val = calcular_tae(tin=p["tin"], m=p["m"])
            return {"result": val}
        elif formula == "precio_bono":
            val = calcular_precio_bono(nominal=p["nominal"], cupon_anual_pct=p["cupon_anual_pct"], n_anos=p["n_anos"], tir=p["tir"])
            return {"result": val}
        elif formula == "irpf_ahorro":
            return calcular_irpf_ahorro(base_liquidable=p["base_liquidable"])
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Fórmula no soportada")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@app.get("/api/study/apuntes")
def api_get_todos_apuntes():
    return APUNTES_TEORICOS

@app.get("/api/study/apuntes/{modulo_id}")
def api_get_apunte_modulo(modulo_id: str):
    if modulo_id not in APUNTES_TEORICOS:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Apuntes para el módulo {modulo_id} no encontrados."
        )
    return {"modulo": modulo_id, "apuntes": APUNTES_TEORICOS[modulo_id]}
