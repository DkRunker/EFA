"""Comprobaciones del banco de casos prácticos y del evaluador por reglas."""
import re

from backend.content.practicas import PRACTICAS as PRACTICAS_PROPIAS
from backend.evaluator import _interpretar_numero, evaluar_respuesta_desarrollo

# Los casos importados del libro no se versionan: en un clon del repositorio
# puede haber solo los propios. Comprobamos el banco tal y como lo monta la
# aplicación, que es lo que de verdad ve el alumno.
try:
    from backend.content.practicas_libro import PRACTICAS_LIBRO
except ImportError:
    PRACTICAS_LIBRO = []

PRACTICAS = list(PRACTICAS_PROPIAS) + list(PRACTICAS_LIBRO)

MODULOS = {f"M{i}" for i in range(1, 11)}


def test_estructura_de_los_casos():
    assert len(PRACTICAS) >= 35
    ids = [c["id"] for c in PRACTICAS]
    assert len(ids) == len(set(ids)), "ids duplicados"

    for c in PRACTICAS:
        assert c["modulo"] in MODULOS, f"{c['id']}: módulo inválido"
        assert len(c["enunciado"]) >= 60, f"{c['id']}: enunciado corto"
        assert len(c["rubrica"]) >= 3, f"{c['id']}: rúbrica insuficiente"
        assert len(c["palabras_clave"]) >= 4, f"{c['id']}: pocas palabras clave"
        assert len(c["explicacion"]) >= 80, f"{c['id']}: explicación corta"
        assert c["valor_esperado"] is None or isinstance(c["valor_esperado"], (int, float))
        # el enunciado no debe filtrar la solución
        assert not re.search(r"(?i)\brespuesta:", c["enunciado"]), f"{c['id']}: filtra respuesta"


def test_todos_los_modulos_tienen_varios_casos():
    """El simulador elige un caso al azar; con uno solo repetiría siempre."""
    from collections import Counter
    por_mod = Counter(c["modulo"] for c in PRACTICAS)
    for mod in MODULOS:
        assert por_mod[mod] >= 2, f"{mod}: solo {por_mod[mod]} caso(s), el simulador repetiría"


def test_interpretador_de_numeros_bilingue():
    # español: punto = miles, coma = decimal
    assert 27400 in _aprox(_interpretar_numero("27.400"), 27400)
    assert any(abs(v - 27400.5) < 0.01 for v in _interpretar_numero("27.400,50"))
    assert any(abs(v - 0.70) < 0.01 for v in _interpretar_numero("0,70"))
    # anglosajón: coma = miles, punto = decimal
    assert any(abs(v - 1234.56) < 0.01 for v in _interpretar_numero("1,234.56"))
    assert any(abs(v - 100.0) < 0.01 for v in _interpretar_numero("100.00"))


def _aprox(valores, objetivo):
    return {v for v in valores if abs(v - objetivo) < 0.5}


def test_cada_caso_numerico_aprueba_con_su_solucion():
    """Responder con la propia explicación del caso debe puntuar como aprobado."""
    for c in PRACTICAS:
        if c["valor_esperado"] is None:
            continue
        rep = evaluar_respuesta_desarrollo(
            c["enunciado"], c["explicacion"],
            {"puntos_rubrica": c["rubrica"], "palabras_clave": c["palabras_clave"]},
            c["valor_esperado"], c["tolerancia"],
        )
        assert rep["score"] >= 0.70, f"{c['id']}: la solución correcta solo saca {rep['score']}"


def test_respuesta_vacia_suspende():
    numerico = next(c for c in PRACTICAS if c["valor_esperado"] is not None)
    rep = evaluar_respuesta_desarrollo(
        numerico["enunciado"], "No lo sé.",
        {"puntos_rubrica": numerico["rubrica"], "palabras_clave": numerico["palabras_clave"]},
        numerico["valor_esperado"], numerico["tolerancia"],
    )
    assert rep["aprobado"] is False
