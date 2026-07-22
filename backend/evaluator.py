import os
import re
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Cargamos variables del archivo .env si existe
load_dotenv()

# Intentamos importar genai desde google-genai
try:
    from google import genai
    from google.genai import types
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

class EvaluacionReporte(BaseModel):
    score: float = Field(..., description="Puntuación de 0.0 a 1.0 de la respuesta.")
    aprobado: bool = Field(..., description="Indica si la respuesta es aprobada (score >= 0.70).")
    comentario_cualitativo: str = Field(..., description="Retroalimentación detallada pedagógica sobre la explicación financiera del alumno.")
    puntos_cumplidos: list[str] = Field(..., description="Puntos de la rúbrica cumplidos por el alumno.")
    puntos_fallidos: list[str] = Field(..., description="Puntos de la rúbrica fallidos o no mencionados.")


def _interpretar_numero(token: str):
    """Devuelve los valores float plausibles de un token numérico.

    Contempla las dos convenciones que conviven en el contenido:
    - Español: punto = separador de miles, coma = decimal ("27.400,50").
    - Anglosajón: coma = separador de miles, punto = decimal ("27,400.50").
    Devuelve un conjunto de candidatos; basta con que uno esté dentro de la
    tolerancia para dar el valor por acertado.
    """
    token = token.strip()
    candidatos = set()

    def _add(s: str):
        try:
            candidatos.add(float(s))
        except ValueError:
            pass

    # Interpretación española: quitar puntos (miles), coma -> punto (decimal)
    _add(token.replace(".", "").replace(",", "."))
    # Interpretación anglosajona: quitar comas (miles), punto decimal
    _add(token.replace(",", ""))
    # Solo dígitos, por si acaso ("27400")
    solo_digitos = re.sub(r"[^\d-]", "", token)
    if solo_digitos not in ("", "-"):
        _add(solo_digitos)

    return candidatos


def _evaluar_por_reglas(
    pregunta_enunciado: str,
    respuesta_alumno: str,
    rubrica: dict,
    valor_esperado: float = None,
    tolerancia: float = 0.01
) -> dict:
    """
    Evaluación de respaldo (fallback) determinista basada en expresiones regulares 
    y coincidencia de palabras clave de la rúbrica.
    """
    respuesta_normalizada = respuesta_alumno.lower()

    # 1. Verificar valor numérico esperado
    valor_correcto = False
    comentario_valor = ""

    if valor_esperado is not None:
        # Buscamos todos los tokens numéricos (dígitos con puntos y comas). El
        # español de España usa el punto como separador de miles y la coma como
        # decimal ("27.400,50"), mientras que en formato anglosajón es al revés
        # ("27,400.50"). Como en el contenido conviven ambos, para cada token
        # probamos las dos interpretaciones y damos por bueno si ALGUNA coincide.
        for token in re.findall(r'-?\d[\d.,]*\d|-?\d', respuesta_alumno):
            for val in _interpretar_numero(token):
                if abs(val - valor_esperado) <= tolerancia:
                    valor_correcto = True
                    break
            if valor_correcto:
                break

        if valor_correcto:
            comentario_valor = f"Acierto en el valor numérico esperado ({valor_esperado})."
        else:
            comentario_valor = f"No se encontró el valor numérico esperado ({valor_esperado}) con la tolerancia permitida."
            
    # 2. Verificar palabras clave
    palabras_clave = rubrica.get("palabras_clave", [])
    palabras_encontradas = []
    palabras_faltantes = []
    
    for pc in palabras_clave:
        if pc.lower() in respuesta_normalizada:
            palabras_encontradas.append(pc)
        else:
            palabras_faltantes.append(pc)
            
    ratio_palabras = len(palabras_encontradas) / len(palabras_clave) if palabras_clave else 1.0
    
    # 3. Calcular score mixto
    # Si hay valor esperado, cuenta el 50% de la nota, y el 50% las palabras clave.
    # Si no hay valor esperado, 100% palabras clave.
    if valor_esperado is not None:
        score = (0.5 if valor_correcto else 0.0) + (0.5 * ratio_palabras)
    else:
        score = ratio_palabras
        
    aprobado = score >= 0.70
    
    # Mapeo simple de puntos de rúbrica basados en palabras encontradas
    puntos_rubrica = rubrica.get("puntos_rubrica", [])
    puntos_cumplidos = []
    puntos_fallidos = []
    
    # Mapeo heurístico básico para llenar la rúbrica en fallback
    for i, punto in enumerate(puntos_rubrica):
        # Si el alumno acertó el valor y es el primer punto, o si tenemos palabras clave asociadas
        if i == 0 and valor_esperado is not None:
            if valor_correcto:
                puntos_cumplidos.append(punto)
            else:
                puntos_fallidos.append(punto)
        else:
            # Asignamos al azar/proporción según palabras clave encontradas
            if ratio_palabras > 0.5:
                puntos_cumplidos.append(punto)
            else:
                puntos_fallidos.append(punto)
                
    comentario = (
        f"Evaluación determinista (Fallback). {comentario_valor} "
        f"Palabras clave encontradas: {', '.join(palabras_encontradas) if palabras_encontradas else 'ninguna'}. "
        f"Faltan términos clave: {', '.join(palabras_faltantes) if palabras_faltantes else 'ninguno'}."
    )
    
    return {
        "score": round(score, 2),
        "aprobado": aprobado,
        "comentario_cualitativo": comentario,
        "puntos_cumplidos": puntos_cumplidos,
        "puntos_fallidos": puntos_fallidos,
        "es_evaluacion_ia": False
    }


def evaluar_respuesta_desarrollo(
    pregunta_enunciado: str,
    respuesta_alumno: str,
    rubrica: dict,
    valor_esperado: float = None,
    tolerancia: float = 0.01
) -> dict:
    """
    Evalúa la respuesta de desarrollo del alumno.
    Utiliza Gemini API (gemini-2.5-flash) si la API key está disponible y la librería genai está instalada.
    De lo contrario, realiza un fallback determinista.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if HAS_GENAI and api_key:
        try:
            client = genai.Client(api_key=api_key)
            
            prompt = f"""
            Actúa como un tribunal oficial evaluador del examen de certificación EFA.
            Evalúa de forma rigurosa la respuesta práctica redactada por el alumno para la siguiente pregunta.
            
            Enunciado de la pregunta:
            {pregunta_enunciado}
            
            Respuesta redactada por el alumno:
            {respuesta_alumno}
            
            Valor de referencia numérico correcto (si aplica): {valor_esperado if valor_esperado is not None else "N/A"} (Tolerancia: {tolerancia})
            
            Rúbrica oficial a evaluar:
            {chr(10).join(f"- {p}" for p in rubrica.get("puntos_rubrica", []))}
            Palabras clave de control que deben estar integradas semánticamente: {', '.join(rubrica.get("palabras_clave", []))}
            
            Instrucciones especiales:
            1. Compara el valor numérico obtenido por el alumno con el valor de referencia. Si el alumno cometió un error de cálculo, identifícalo (por ejemplo, si usó un distractor común como no restar el crecimiento en el denominador de Gordon-Shapiro).
            2. Evalúa cualitativamente si explica correctamente el fundamento financiero. El tribunal no solo valida el número, sino también la coherencia del razonamiento.
            3. Devuelve la puntuación (de 0.0 a 1.0), indicando si aprueba (umbral mínimo 0.70).
            """
            
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=EvaluacionReporte,
                    temperature=0.2
                )
            )
            
            # El SDK google-genai retorna la respuesta estructurada directamente en response.parsed si se usó response_schema
            if hasattr(response, 'parsed') and response.parsed:
                report = response.parsed
                return {
                    "score": report.score,
                    "aprobado": report.aprobado,
                    "comentario_cualitativo": report.comentario_cualitativo,
                    "puntos_cumplidos": report.puntos_cumplidos,
                    "puntos_fallidos": report.puntos_fallidos,
                    "es_evaluacion_ia": True
                }
            else:
                # Si fallara la conversión parsed, parsear JSON manualmente
                import json
                data = json.loads(response.text)
                return {
                    "score": float(data.get("score", 0.0)),
                    "aprobado": bool(data.get("aprobado", False)),
                    "comentario_cualitativo": str(data.get("comentario_cualitativo", "")),
                    "puntos_cumplidos": list(data.get("puntos_cumplidos", [])),
                    "puntos_fallidos": list(data.get("puntos_fallidos", [])),
                    "es_evaluacion_ia": True
                }
                
        except Exception as e:
            # Si hay cualquier error al llamar a la API de Gemini, hacemos fallback a reglas
            pass
            
    # Fallback por reglas si no hay API key o falló la llamada
    return _evaluar_por_reglas(
        pregunta_enunciado=pregunta_enunciado,
        respuesta_alumno=respuesta_alumno,
        rubrica=rubrica,
        valor_esperado=valor_esperado,
        tolerancia=tolerancia
    )
