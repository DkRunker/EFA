import os
import uuid
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Any

from backend.database import (
    generar_examen,
    listar_examenes_oficiales,
    PREGUNTAS_TEST,
    PREGUNTAS_PRACTICAS,
    APUNTES_TEORICOS,
    SECCIONES_TEORICAS,
)
from backend.evaluator import evaluar_respuesta_desarrollo
from backend import usuarios
from backend.formulas import (
    calcular_gordon_shapiro,
    calcular_sharpe,
    calcular_treynor,
    calcular_jensen,
    calcular_tae,
    calcular_precio_bono,
    calcular_irpf_ahorro,
    calcular_duracion_bono,
    calcular_tipo_forward,
    calcular_tipo_cambio_forward,
    calcular_ratio_informacion,
    calcular_ratio_sortino,
    calcular_cartera_dos_activos,
    calcular_valoracion_inmobiliaria,
    calcular_amortizacion_francesa
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

class UserAuth(BaseModel):
    username: str
    password: str

@app.post("/api/auth/register")
def api_register(user: UserAuth):
    if not user.username.strip() or not user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario y contraseña son obligatorios."
        )
    if not usuarios.registrar(user.username, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario ya existe."
        )
    return {"message": "Usuario registrado con éxito."}

@app.post("/api/auth/login")
def api_login(user: UserAuth):
    if not usuarios.verificar(user.username, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos."
        )
    return {"username": user.username, "token": f"mock-token-{uuid.uuid4().hex[:8]}"}


@app.get("/api/auth/existe/{username}")
def api_usuario_existe(username: str):
    """Permite a la interfaz saber si debe ofrecer iniciar sesión o registrarse."""
    return {"username": username, "existe": usuarios.existe(username)}

class StartExamRequest(BaseModel):
    tipo_examen: str

class SubmitExamRequest(BaseModel):
    session_id: str
    respuestas_test: dict[str, int]  # { "question_id": selected_option_index }
    respuestas_practica: dict[str, str]  # { "question_id": student_answer_text }

class CalculateFormulaRequest(BaseModel):
    formula: str
    params: dict[str, Any]

@app.get("/api/exams/oficiales")
def api_listar_examenes_oficiales():
    """Convocatorias oficiales EFPA que pueden reproducirse íntegras."""
    return {"examenes": listar_examenes_oficiales()}


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
            "explicacion": original.explicacion,
            "fuente": original.fuente
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
        elif formula == "duracion_bono":
            return calcular_duracion_bono(nominal=p["nominal"], cupon_anual_pct=p["cupon_anual_pct"], n_anos=p["n_anos"], tir=p["tir"], frecuencia=p.get("frecuencia", 1))
        elif formula == "tipo_forward":
            val = calcular_tipo_forward(s1=p["s1"], s2=p["s2"], t1=p["t1"], t2=p["t2"])
            return {"result": val}
        elif formula == "tipo_cambio_forward":
            val = calcular_tipo_cambio_forward(spot=p["spot"], r_dom=p["r_dom"], r_for=p["r_for"], dias=int(p["dias"]))
            return {"result": val}
        elif formula == "ratio_informacion":
            val = calcular_ratio_informacion(rp=p["rp"], rb=p["rb"], tracking_error=p["tracking_error"])
            return {"result": val}
        elif formula == "ratio_sortino":
            val = calcular_ratio_sortino(rp=p["rp"], rf=p["rf"], downside_deviation=p["downside_deviation"])
            return {"result": val}
        elif formula == "cartera_dos_activos":
            return calcular_cartera_dos_activos(w1=p["w1"], w2=p["w2"], r1=p["r1"], r2=p["r2"], sigma1=p["sigma1"], sigma2=p["sigma2"], correlacion=p["correlacion"])
        elif formula == "valoracion_inmobiliaria":
            val = calcular_valoracion_inmobiliaria(renta_neta=p["renta_neta"], cap_rate=p["cap_rate"])
            return {"result": val}
        elif formula == "amortizacion_francesa":
            return calcular_amortizacion_francesa(nominal=p["nominal"], tin=p["tin"], n_anos=p["n_anos"], frecuencia=p.get("frecuencia", 12))
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


@app.get("/api/study/secciones/{modulo_id}")
def api_get_secciones_modulo(modulo_id: str):
    """Teoría estructurada por secciones (intro + secciones con cuerpo y ejercicios)."""
    if modulo_id not in SECCIONES_TEORICAS:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Secciones para el módulo {modulo_id} no encontradas."
        )
    data = SECCIONES_TEORICAS[modulo_id]
    return {"modulo": modulo_id, "intro": data["intro"], "secciones": data["secciones"]}


# --- Servido del frontend compilado (modo portable) ---
# Si existe el build del frontend (frontend/dist), se sirve como aplicación web
# en la raíz "/", de modo que backend y frontend corran en el mismo origen (puerto).
# Las rutas /api/* declaradas arriba tienen prioridad sobre este montaje.
# La ruta puede forzarse con la variable de entorno EFA_FRONTEND_DIST (empaquetado portable).
_FRONTEND_DIST = os.environ.get("EFA_FRONTEND_DIST") or os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "frontend", "dist"
)
if os.path.isdir(_FRONTEND_DIST):
    app.mount("/", StaticFiles(directory=_FRONTEND_DIST, html=True), name="frontend")
