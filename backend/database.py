# Banco de preguntas oficial y simulado para preparación EFA
#
# El contenido vive en el paquete backend/content/ (un módulo por tema: m1..m10, más practicas).
# Este fichero ensambla ese contenido y expone la API pública histórica:
#   PREGUNTAS_TEST, PREGUNTAS_PRACTICAS, APUNTES_TEORICOS, generar_examen, ...
import random
from pydantic import BaseModel

from backend.content import (
    m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, practicas,
)


class PreguntaTest(BaseModel):
    id: int
    modulo: str  # M1 a M10
    tipo: str = "test"
    enunciado: str
    opciones: list[str]
    respuesta_correcta: int  # Índice de 0 a 3
    explicacion: str


class PreguntaPractica(BaseModel):
    id: int
    modulo: str
    tipo: str = "practico"
    enunciado: str
    rubrica: list[str]
    palabras_clave: list[str]
    valor_esperado: float | None = None
    tolerancia: float = 0.01
    explicacion: str


# Orden canónico de módulos (M1..M10) y su fuente de contenido.
_MODULOS = [
    ("M1", m1), ("M2", m2), ("M3", m3), ("M4", m4), ("M5", m5),
    ("M6", m6), ("M7", m7), ("M8", m8), ("M9", m9), ("M10", m10),
]

NOMBRES_MODULOS: dict[str, str] = {code: mod.NOMBRE for code, mod in _MODULOS}

# Ensamblado del banco de preguntas tipo test con ids secuenciales estables.
#
# Los contenidos se redactan situando a menudo la opción correcta en primera posición.
# Para que la representación canónica del banco no tenga sesgo posicional (independientemente
# del barajado adicional que aplica generar_examen en cada sesión), reordenamos las opciones
# de cada pregunta de forma DETERMINISTA (semilla = id) para que sea estable y reproducible.
PREGUNTAS_TEST: list[PreguntaTest] = []
_qid = 1
for _code, _mod in _MODULOS:
    for _enunciado, _opciones, _correcta, _explicacion in _mod.PREGUNTAS:
        _opts = list(_opciones)
        _texto_correcto = _opts[_correcta]
        random.Random(_qid).shuffle(_opts)
        PREGUNTAS_TEST.append(
            PreguntaTest(
                id=_qid,
                modulo=_code,
                enunciado=_enunciado,
                opciones=_opts,
                respuesta_correcta=_opts.index(_texto_correcto),
                explicacion=_explicacion,
            )
        )
        _qid += 1

# Ensamblado del banco de preguntas prácticas.
PREGUNTAS_PRACTICAS: list[PreguntaPractica] = [
    PreguntaPractica(**p) for p in practicas.PRACTICAS
]

# Teoría estructurada por secciones (INTRO + SECCIONES) de cada módulo.
# Cada sección: {"titulo", "cuerpo", "ejercicios": [...]}.
SECCIONES_TEORICAS: dict[str, dict] = {
    code: {"intro": mod.INTRO, "secciones": mod.SECCIONES} for code, mod in _MODULOS
}


def _ensamblar_apuntes(mod) -> str:
    """Reconstruye el markdown completo (compatibilidad) desde INTRO + SECCIONES."""
    partes = [mod.INTRO]
    for s in mod.SECCIONES:
        partes.append(f"## {s['titulo']}\n\n{s['cuerpo']}")
    return "\n\n".join(partes)


# Apuntes teóricos por módulo (derivados de la estructura por secciones).
APUNTES_TEORICOS: dict[str, str] = {code: _ensamblar_apuntes(mod) for code, mod in _MODULOS}


def obtener_preguntas_test():
    return PREGUNTAS_TEST


def obtener_preguntas_practicas():
    return PREGUNTAS_PRACTICAS


def obtener_todos_apuntes() -> dict[str, str]:
    return APUNTES_TEORICOS


def generar_examen(tipo_examen: str) -> dict:
    """
    Compone un examen simulado según la estructura del plan EFA:
    - EIP: 40 test.
    - EFA Nivel II: 40 test + 1 caso práctico.
    - EFA Completo: 50 test + 1 caso práctico.
    Respeta las ponderaciones de los 10 módulos oficiales en las preguntas tipo test.
    """
    incluye_practica = False

    if tipo_examen == "EFA Completo":
        n_test = 50
        incluye_practica = True
    elif tipo_examen == "EFA Nivel II":
        n_test = 40
        incluye_practica = True
    elif tipo_examen == "EIP":
        n_test = 40
        incluye_practica = False
    else:
        raise ValueError("Tipo de examen no reconocido")

    # Ponderaciones de test por módulo (para 40 o 50 preguntas).
    # Para 50: M1=13, M2=5, M3=9, M4=4, M5=3, M6=2, M7=2, M8=5, M9=4, M10=3 -> 50
    # Para 40: M1=10, M2=4, M3=7, M4=3, M5=2, M6=2, M7=2, M8=4, M9=3, M10=3 -> 40
    if n_test == 50:
        distribucion = {"M1": 13, "M2": 5, "M3": 9, "M4": 4, "M5": 3, "M6": 2, "M7": 2, "M8": 5, "M9": 4, "M10": 3}
    else:
        distribucion = {"M1": 10, "M2": 4, "M3": 7, "M4": 3, "M5": 2, "M6": 2, "M7": 2, "M8": 4, "M9": 3, "M10": 3}

    test_seleccionadas = []
    for mod_code, cant in distribucion.items():
        pool = [q for q in PREGUNTAS_TEST if q.modulo == mod_code]
        seleccion = random.sample(pool, min(len(pool), cant))
        test_seleccionadas.extend(seleccion)

    # Barajamos las de test.
    random.shuffle(test_seleccionadas)

    # Seleccionamos práctica si corresponde.
    practica_seleccionada = None
    if incluye_practica:
        practica_seleccionada = random.choice(PREGUNTAS_PRACTICAS)

    # Para enviar al alumno, eliminamos la respuesta correcta y mezclamos las opciones.
    preguntas_test_alumno = []
    mapa_respuestas_correctas = {}  # {str(q.id): nueva_correcta}

    for q in test_seleccionadas:
        opciones_originales = list(q.opciones)
        correcta_texto = opciones_originales[q.respuesta_correcta]

        opciones_mezcladas = list(opciones_originales)
        random.shuffle(opciones_mezcladas)
        nueva_correcta = opciones_mezcladas.index(correcta_texto)

        mapa_respuestas_correctas[str(q.id)] = nueva_correcta

        preguntas_test_alumno.append({
            "id": q.id,
            "modulo": q.modulo,
            "tipo": q.tipo,
            "enunciado": q.enunciado,
            "opciones": opciones_mezcladas,
        })

    return {
        "tipo_examen": tipo_examen,
        "n_preguntas_test": len(test_seleccionadas),
        "preguntas_test": preguntas_test_alumno,
        "incluye_practica": incluye_practica,
        "pregunta_practica": {
            "id": practica_seleccionada.id,
            "modulo": practica_seleccionada.modulo,
            "tipo": practica_seleccionada.tipo,
            "enunciado": practica_seleccionada.enunciado,
        } if practica_seleccionada else None,
        "ids_originales_test": [q.id for q in test_seleccionadas],
        "id_practica_original": practica_seleccionada.id if practica_seleccionada else None,
        "respuestas_correctas_test": mapa_respuestas_correctas,
    }
