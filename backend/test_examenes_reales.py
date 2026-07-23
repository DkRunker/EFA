"""Comprobaciones del banco importado de exámenes oficiales EFPA."""
import re

import pytest

from backend.database import (
    EXAMENES_OFICIALES,
    PREGUNTAS_TEST,
    generar_examen,
    listar_examenes_oficiales,
)

# El banco importado es contenido con licencia y no se versiona: en un clon del
# repositorio puede no estar. Estas pruebas solo aplican si está presente.
try:
    from backend.content.examenes_reales import PREGUNTAS_EXAMEN
except ImportError:
    PREGUNTAS_EXAMEN = None

pytestmark = pytest.mark.skipif(
    PREGUNTAS_EXAMEN is None,
    reason="no está el banco importado de exámenes (contenido con licencia)",
)

MODULOS = {f"M{i}" for i in range(1, 11)}


def test_estructura_de_cada_pregunta():
    assert len(PREGUNTAS_EXAMEN) > 1000

    for i, p in enumerate(PREGUNTAS_EXAMEN):
        assert p["modulo"] in MODULOS, f"{i}: módulo inválido {p['modulo']!r}"
        assert len(p["opciones"]) == 4, f"{i}: no tiene 4 opciones"
        assert 0 <= p["correcta"] <= 3, f"{i}: índice correcto fuera de rango"
        assert len(p["enunciado"]) >= 15, f"{i}: enunciado demasiado corto"
        # las cuatro opciones deben ser distintas entre sí
        assert len({o.lower() for o in p["opciones"]}) == 4, f"{i}: opciones repetidas"
        assert p["fuente"], f"{i}: sin fuente"


def test_todas_tienen_explicacion_util():
    """Ninguna pregunta puede quedarse sin explicación real del porqué."""
    for i, p in enumerate(PREGUNTAS_EXAMEN):
        assert len(p["explicacion"]) >= 30, f"{i}: explicación ausente o trivial"
        # no debe colarse el texto de relleno que se usó durante la importación
        assert "repasa el apartado correspondiente" not in p["explicacion"], (
            f"{i}: explicación de relleno sin contenido"
        )


def test_no_arrastra_datos_personales_del_pdf():
    """La marca de agua del PDF (datos de un tercero) no debe estar en el contenido."""
    correo = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
    for i, p in enumerate(PREGUNTAS_EXAMEN):
        texto = " ".join([p["enunciado"], p["explicacion"], *p["opciones"]])
        assert not correo.search(texto), f"{i}: contiene un correo electrónico"
        assert "uso exclusivo de" not in texto.lower(), f"{i}: contiene la marca de agua"


def test_preguntas_integradas_en_el_banco_general():
    assert len(PREGUNTAS_TEST) > 1500
    ids = [q.id for q in PREGUNTAS_TEST]
    assert len(ids) == len(set(ids)), "hay ids duplicados en el banco"

    importadas = [q for q in PREGUNTAS_TEST if q.fuente != "Banco propio"]
    assert len(importadas) == len(PREGUNTAS_EXAMEN)

    # cada módulo conserva preguntas suficientes para componer un simulacro
    for mod in MODULOS:
        assert sum(1 for q in PREGUNTAS_TEST if q.modulo == mod) >= 13


def test_examenes_oficiales_reproducibles():
    disponibles = listar_examenes_oficiales()
    assert len(disponibles) >= 5

    for ex in disponibles:
        assert ex["n_preguntas"] >= 20
        examen = generar_examen(ex["id"])
        assert examen["n_preguntas_test"] == ex["n_preguntas"]
        assert examen["incluye_practica"] is False
        # las preguntas van sin la respuesta correcta
        for q in examen["preguntas_test"]:
            assert "respuesta_correcta" not in q
            assert len(q["opciones"]) == 4
        # el mapa de correctas apunta a una opción válida de cada pregunta
        assert len(examen["respuestas_correctas_test"]) == ex["n_preguntas"]
        assert all(0 <= v <= 3 for v in examen["respuestas_correctas_test"].values())


def test_barajado_conserva_la_respuesta_correcta():
    """Al barajar las opciones, el índice correcto debe seguir señalando el mismo texto."""
    nombre = next(iter(EXAMENES_OFICIALES))
    examen = generar_examen("Oficial: " + nombre)
    por_id = {q.id: q for q in PREGUNTAS_TEST}

    for q in examen["preguntas_test"]:
        original = por_id[q["id"]]
        texto_correcto = original.opciones[original.respuesta_correcta]
        idx = examen["respuestas_correctas_test"][str(q["id"])]
        assert q["opciones"][idx] == texto_correcto


def test_examen_oficial_desconocido_da_error():
    with pytest.raises(ValueError):
        generar_examen("Oficial: convocatoria inexistente")
