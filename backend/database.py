# Banco de preguntas oficial y simulado para preparación EFA
#
# El contenido vive en el paquete backend/content/ (un módulo por tema: m1..m10, más practicas).
# Este fichero ensambla ese contenido y expone la API pública histórica:
#   PREGUNTAS_TEST, PREGUNTAS_PRACTICAS, APUNTES_TEORICOS, generar_examen, ...
import random
import re
import unicodedata
from pydantic import BaseModel

from backend.content import (
    m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, practicas,
)

# Banco de preguntas importado de exámenes oficiales. Es contenido con licencia
# y no se versiona, así que puede no estar presente en un clon del repositorio:
# en ese caso la plataforma funciona igual, solo que con el banco propio y sin
# las convocatorias oficiales reproducibles.
try:
    from backend.content import examenes_reales
    _PREGUNTAS_IMPORTADAS = list(examenes_reales.PREGUNTAS_EXAMEN)
except ImportError:  # pragma: no cover - depende de si el fichero está presente
    _PREGUNTAS_IMPORTADAS = []


class PreguntaTest(BaseModel):
    id: int
    modulo: str  # M1 a M10
    tipo: str = "test"
    enunciado: str
    opciones: list[str]
    respuesta_correcta: int  # Índice de 0 a 3
    explicacion: str
    # Procedencia de la pregunta. Las redactadas para la plataforma llevan
    # "Banco propio"; las importadas indican el examen oficial de origen.
    fuente: str = "Banco propio"


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

# Preguntas procedentes de exámenes oficiales EFPA y de los simuladores oficiales.
# Se añaden al mismo banco (con su fuente) para que los simulacros puedan usarlas.
# Aquí NO reordenamos: el orden de las opciones es el del examen original y
# generar_examen ya baraja en cada sesión.
for _p in _PREGUNTAS_IMPORTADAS:
    PREGUNTAS_TEST.append(
        PreguntaTest(
            id=_qid,
            modulo=_p["modulo"],
            enunciado=_p["enunciado"],
            opciones=list(_p["opciones"]),
            respuesta_correcta=_p["correcta"],
            explicacion=_p["explicacion"],
            fuente=_p["fuente"],
        )
    )
    _qid += 1


# Exámenes sintéticos de elaboración propia (versionados, sin licencia). Son
# simulacros completos con dificultad similar o superior a la de los oficiales;
# se incorporan como convocatorias reproducibles con fuente "Simulacro sintético ...".
try:
    from backend.content import examenes_sinteticos as _examenes_sinteticos
    _EXAMENES_SINTETICOS = list(_examenes_sinteticos.EXAMENES_SINTETICOS)
except ImportError:  # pragma: no cover
    _EXAMENES_SINTETICOS = []

for _ex in _EXAMENES_SINTETICOS:
    _fuente = "Simulacro sintético " + _ex["nombre"]
    for _p in _ex["preguntas"]:
        PREGUNTAS_TEST.append(
            PreguntaTest(
                id=_qid,
                modulo=_p["modulo"],
                enunciado=_p["enunciado"],
                opciones=list(_p["opciones"]),
                respuesta_correcta=_p["correcta"],
                explicacion=_p.get("explicacion", ""),
                fuente=_fuente,
            )
        )
        _qid += 1


# Además del banco propio (PREGUNTAS de cada módulo) y de las preguntas importadas
# de exámenes oficiales, incorporamos al banco de simulacros los EJERCICIOS TIPO
# TEST (opción múltiple) que hay repartidos por las SECCIONES de la teoría. Así los
# simulacros disponen de muchísimo más fondo. Los ejercicios numéricos no encajan en
# el formato test y se dejan fuera (siguen usándose en la teoría). Se deduplica por
# enunciado normalizado frente a todo lo ya incorporado.
def _norm_enunciado(_s: str) -> str:
    _s = "".join(c for c in unicodedata.normalize("NFD", _s or "") if unicodedata.category(c) != "Mn")
    return " ".join(_s.lower().split())


_enunciados_vistos = {_norm_enunciado(_q.enunciado) for _q in PREGUNTAS_TEST}
for _code, _mod in _MODULOS:
    for _sec in _mod.SECCIONES:
        for _e in _sec.get("ejercicios", []):
            if _e.get("tipo") != "opcion":
                continue
            _ops = _e.get("opciones")
            _corr = _e.get("correcta")
            if not (isinstance(_ops, list) and len(_ops) == 4
                    and isinstance(_corr, int) and 0 <= _corr < 4):
                continue
            _clave = _norm_enunciado(_e.get("enunciado", ""))
            if not _clave or _clave in _enunciados_vistos:
                continue
            _enunciados_vistos.add(_clave)
            _opts = list(_ops)
            _texto_correcto = _opts[_corr]
            random.Random(_qid).shuffle(_opts)
            PREGUNTAS_TEST.append(
                PreguntaTest(
                    id=_qid,
                    modulo=_code,
                    enunciado=_e["enunciado"],
                    opciones=_opts,
                    respuesta_correcta=_opts.index(_texto_correcto),
                    explicacion=_e.get("explicacion", ""),
                    fuente="Banco propio (teoría)",
                )
            )
            _qid += 1

# Exámenes oficiales completos, agrupados por convocatoria, para poder
# reproducirlos tal cual en el simulador. Se reconocen tanto las convocatorias
# reales ("Examen oficial EFA™ 2018 (1)") como los simulacros que publica EFPA
# ("Simulacro oficial EFPA (Modelo A)"): ambos son exámenes completos.
_PREFIJOS_EXAMEN = ("Examen oficial ", "Simulacro oficial ", "Simulacro sintético ")

EXAMENES_OFICIALES: dict[str, list[int]] = {}
for _q in PREGUNTAS_TEST:
    for _pref in _PREFIJOS_EXAMEN:
        if _q.fuente.startswith(_pref):
            EXAMENES_OFICIALES.setdefault(_q.fuente[len(_pref):], []).append(_q.id)
            break
# Solo consideramos convocatorias con un número razonable de preguntas.
EXAMENES_OFICIALES = {k: v for k, v in EXAMENES_OFICIALES.items() if len(v) >= 20}

# Casos prácticos importados del libro de exámenes: contenido con licencia que
# tampoco se versiona, así que su presencia es opcional igual que la del banco
# de preguntas importado.
try:
    from backend.content import practicas_libro
    _PRACTICAS_IMPORTADAS = list(practicas_libro.PRACTICAS_LIBRO)
except ImportError:  # pragma: no cover - depende de si el fichero está presente
    _PRACTICAS_IMPORTADAS = []

# Ensamblado del banco de preguntas prácticas (propias + importadas si las hay).
PREGUNTAS_PRACTICAS: list[PreguntaPractica] = [
    PreguntaPractica(**p) for p in (list(practicas.PRACTICAS) + _PRACTICAS_IMPORTADAS)
]

# Además de las prácticas propias y las importadas, derivamos casos prácticos de
# cálculo a partir de los EJERCICIOS NUMÉRICOS de las secciones de teoría: tienen un
# valor esperado ya verificado y una explicación con la solución trabajada, así que
# son práctica de cálculo de calidad. Se deduplican por enunciado normalizado. Con
# esto el banco de prácticas pasa de decenas a más de mil casos.
_STOP = {
    "para", "como", "cual", "cuales", "sobre", "entre", "segun", "porque", "cuando",
    "donde", "esta", "este", "esto", "estos", "estas", "unos", "unas", "cada", "muy",
    "mas", "menos", "que", "con", "los", "las", "del", "una", "uno", "por", "sus",
    "sin", "año", "anos", "euros", "euro", "siguiente", "siguientes", "valor",
    "calcula", "calcular", "cuanto", "cuanta", "cuantos", "cuantas", "obtenga",
    "determine", "indique", "aproximadamente", "resultado", "tiene", "tienen",
}


def _palabras_clave(enunciado: str, n: int = 5) -> list[str]:
    _txt = "".join(c for c in unicodedata.normalize("NFD", enunciado or "")
                   if unicodedata.category(c) != "Mn").lower()
    _cand: list[str] = []
    _vistas: set[str] = set()
    for _w in re.findall(r"[a-z]{6,}", _txt):
        if _w in _STOP or _w in _vistas:
            continue
        _vistas.add(_w)
        _cand.append(_w)
        if len(_cand) >= n:
            break
    return _cand


def _rubrica_de(explicacion: str, valor_esperado) -> list[str]:
    _frases = [s.strip() for s in re.split(r"(?<=[.;])\s+", (explicacion or "").strip()) if len(s.strip()) >= 15]
    _puntos = _frases[:3]
    _cierre = f"Llegar al resultado esperado (aprox. {valor_esperado})."
    if not _puntos:
        _puntos = ["Plantear el cálculo con la fórmula adecuada."]
    if _cierre not in _puntos:
        _puntos.append(_cierre)
    return _puntos


_pid = max((p.id for p in PREGUNTAS_PRACTICAS), default=0) + 1
_practicas_vistas = {_norm_enunciado(p.enunciado) for p in PREGUNTAS_PRACTICAS}
for _code, _mod in _MODULOS:
    for _sec in _mod.SECCIONES:
        for _e in _sec.get("ejercicios", []):
            if _e.get("tipo") == "opcion":
                continue
            _val = _e.get("valor_esperado")
            try:
                _val = float(_val)
            except (TypeError, ValueError):
                continue
            _enun = _e.get("enunciado", "")
            if not isinstance(_enun, str) or len(_enun.strip()) < 15:
                continue
            _clave = _norm_enunciado(_enun)
            if not _clave or _clave in _practicas_vistas:
                continue
            _practicas_vistas.add(_clave)
            _tol = _e.get("tolerancia")
            try:
                _tol = float(_tol)
            except (TypeError, ValueError):
                _tol = max(abs(_val) * 0.01, 0.01)
            _expl = _e.get("explicacion", "") or ""
            PREGUNTAS_PRACTICAS.append(
                PreguntaPractica(
                    id=_pid,
                    modulo=_code,
                    tipo="practico",
                    enunciado=_enun,
                    rubrica=_rubrica_de(_expl, _val),
                    palabras_clave=_palabras_clave(_enun),
                    valor_esperado=_val,
                    tolerancia=_tol,
                    explicacion=_expl,
                )
            )
            _pid += 1

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


PREFIJO_OFICIAL = "Oficial: "


def listar_examenes_oficiales() -> list[dict]:
    """Convocatorias oficiales disponibles para reproducir en el simulador."""
    return [
        {
            "id": PREFIJO_OFICIAL + nombre,
            "nombre": nombre,
            "n_preguntas": len(ids),
        }
        for nombre, ids in sorted(EXAMENES_OFICIALES.items())
    ]


def _preparar_para_alumno(preguntas: list[PreguntaTest]) -> tuple[list[dict], dict]:
    """Baraja las opciones y oculta la respuesta correcta."""
    preguntas_alumno = []
    mapa_correctas = {}
    for q in preguntas:
        opciones = list(q.opciones)
        texto_correcto = opciones[q.respuesta_correcta]
        random.shuffle(opciones)
        mapa_correctas[str(q.id)] = opciones.index(texto_correcto)
        preguntas_alumno.append({
            "id": q.id,
            "modulo": q.modulo,
            "tipo": q.tipo,
            "enunciado": q.enunciado,
            "opciones": opciones,
        })
    return preguntas_alumno, mapa_correctas


def _generar_examen_oficial(nombre: str) -> dict:
    """Reproduce una convocatoria oficial completa, en su orden original."""
    ids = EXAMENES_OFICIALES.get(nombre)
    if not ids:
        raise ValueError(f"Examen oficial no encontrado: {nombre}")

    por_id = {q.id: q for q in PREGUNTAS_TEST}
    seleccionadas = [por_id[i] for i in ids]
    preguntas_alumno, mapa_correctas = _preparar_para_alumno(seleccionadas)

    return {
        "tipo_examen": PREFIJO_OFICIAL + nombre,
        "n_preguntas_test": len(seleccionadas),
        "preguntas_test": preguntas_alumno,
        "incluye_practica": False,
        "pregunta_practica": None,
        "ids_originales_test": [q.id for q in seleccionadas],
        "id_practica_original": None,
        "respuestas_correctas_test": mapa_correctas,
    }


def generar_examen(tipo_examen: str) -> dict:
    """
    Compone un examen simulado según la estructura del plan EFA:
    - EIP: 40 test.
    - EFA Nivel II: 40 test + 1 caso práctico.
    - EFA Completo: 50 test + 1 caso práctico.
    Respeta las ponderaciones de los 10 módulos oficiales en las preguntas tipo test.
    """
    incluye_practica = False

    # Convocatoria oficial reproducida tal cual: "Oficial: EFA™ 2018 (1)".
    if tipo_examen.startswith(PREFIJO_OFICIAL):
        return _generar_examen_oficial(tipo_examen[len(PREFIJO_OFICIAL):])

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
