"""Pruebas de consistencia del banco de contenidos EFA.

Garantizan que el temario, las preguntas tipo test y los casos prácticos estén
bien formados y sean internamente coherentes: opciones válidas, respuestas
correctas en rango, distribución de examen alcanzable por módulo y valores
numéricos de las prácticas reproducibles con las fórmulas deterministas.
"""
import collections

import pytest

import backend.database as db
from backend import formulas

MODULOS = [f"M{i}" for i in range(1, 11)]

DISTRIBUCIONES = [
    {"M1": 13, "M2": 5, "M3": 9, "M4": 4, "M5": 3, "M6": 2, "M7": 2, "M8": 5, "M9": 4, "M10": 3},  # 50
    {"M1": 10, "M2": 4, "M3": 7, "M4": 3, "M5": 2, "M6": 2, "M7": 2, "M8": 4, "M9": 3, "M10": 3},  # 40
]


def _cuenta_por_modulo():
    return collections.Counter(q.modulo for q in db.PREGUNTAS_TEST)


def test_preguntas_test_bien_formadas():
    for q in db.PREGUNTAS_TEST:
        assert len(q.opciones) == 4, f"Q{q.id} no tiene 4 opciones"
        assert len(set(q.opciones)) == 4, f"Q{q.id} tiene opciones duplicadas"
        assert 0 <= q.respuesta_correcta < 4, f"Q{q.id} índice fuera de rango"
        assert q.enunciado.strip(), f"Q{q.id} sin enunciado"
        assert q.explicacion.strip(), f"Q{q.id} sin explicación"


def test_ids_unicos():
    ids = [q.id for q in db.PREGUNTAS_TEST]
    assert len(ids) == len(set(ids))
    pids = [p.id for p in db.PREGUNTAS_PRACTICAS]
    assert len(pids) == len(set(pids))


@pytest.mark.parametrize("distribucion", DISTRIBUCIONES)
def test_distribucion_examen_alcanzable(distribucion):
    cnt = _cuenta_por_modulo()
    for modulo, necesarias in distribucion.items():
        assert cnt[modulo] >= necesarias, (
            f"El módulo {modulo} tiene {cnt[modulo]} preguntas, "
            f"insuficientes para las {necesarias} de un examen."
        )


def test_apuntes_completos():
    for modulo in MODULOS:
        assert modulo in db.APUNTES_TEORICOS
        assert len(db.APUNTES_TEORICOS[modulo]) >= 3000, f"Apuntes de {modulo} demasiado cortos"


def test_valores_practicas_reproducibles():
    """Cada práctica con valor_esperado numérico se reproduce con formulas.py."""
    calculados = {
        1004: round(formulas.calcular_precio_bono(1000, 0.05, 4, 0.06), 2),
        1005: round(formulas.calcular_tipo_forward(0.03, 0.04, 1, 2) * 100, 2),
        1006: round(formulas.calcular_tipo_cambio_forward(1.10, 0.04, 0.02, 180), 4),
        1007: round(formulas.calcular_duracion_bono(1000, 0.05, 3, 0.05, 1)["macaulay"], 2),
        1008: round(formulas.calcular_cartera_dos_activos(0.6, 0.4, 0.10, 0.06, 0.20, 0.10, 0.30)["volatilidad_cartera"] * 100, 2),
        1009: round(formulas.calcular_jensen(0.14, 0.03, 1.3, 0.10) * 100, 2),
        1010: round(formulas.calcular_valoracion_inmobiliaria(24000, 0.05), 2),
        1011: round(formulas.calcular_tae(0.12, 12) * 100, 2),
        1012: round(formulas.calcular_amortizacion_francesa(150000, 0.04, 25, 12)["cuota_periodica"], 2),
        1013: round(formulas.calcular_irpf_ahorro(30000)["cuota_total"], 2),
        1014: round(formulas.calcular_irpf_ahorro(250000)["cuota_total"], 2),
        1015: round(formulas.calcular_ratio_sortino(0.12, 0.02, 0.08), 2),
        1016: round(formulas.calcular_precio_bono(1000, 0.04, 5, 0.03), 2),
        1017: round(formulas.calcular_duracion_bono(1000, 0.06, 4, 0.06, 1)["modificada"], 2),
        1018: round(formulas.calcular_cartera_dos_activos(0.5, 0.5, 0.08, 0.04, 0.10, 0.10, -1.0)["volatilidad_cartera"] * 100, 2),
        1019: round(formulas.calcular_ratio_informacion(0.11, 0.08, 0.05), 2),
        1020: round(formulas.calcular_valoracion_inmobiliaria(36000, 0.06), 2),
        1021: round(formulas.calcular_tae(0.06, 12) * 100, 2),
        1022: round(formulas.calcular_amortizacion_francesa(200000, 0.05, 30, 12)["cuota_periodica"], 2),
        1023: round(formulas.calcular_irpf_ahorro(100000)["cuota_total"], 2),
    }
    por_id = {p.id: p for p in db.PREGUNTAS_PRACTICAS}
    for pid, valor in calculados.items():
        prac = por_id[pid]
        assert abs(valor - prac.valor_esperado) <= prac.tolerancia, (
            f"Práctica {pid}: fórmula={valor} vs esperado={prac.valor_esperado}"
        )


def test_practicas_conceptuales_evaluables():
    """Las prácticas conceptuales (sin valor numérico) se aprueban con una respuesta
    que integre sus palabras clave (evaluador por reglas, umbral 0.70)."""
    from backend.evaluator import evaluar_respuesta_desarrollo
    for p in db.PREGUNTAS_PRACTICAS:
        if p.valor_esperado is None:
            respuesta = p.explicacion + " " + " ".join(p.palabras_clave)
            res = evaluar_respuesta_desarrollo(
                pregunta_enunciado=p.enunciado,
                respuesta_alumno=respuesta,
                rubrica={"puntos_rubrica": p.rubrica, "palabras_clave": p.palabras_clave},
                valor_esperado=None,
                tolerancia=p.tolerancia,
            )
            assert res["aprobado"], f"Práctica conceptual {p.id} no aprobable con sus palabras clave"
