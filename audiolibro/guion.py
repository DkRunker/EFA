"""Convierte la teoría (backend/content/m1..m10.py) en un "guion de audio": texto plano pensado
para leerse en voz alta con un motor TTS.

- Fórmulas LaTeX -> español hablado ("sigma sub p al cuadrado", "a entre b"...).
- Tablas -> narradas fila a fila ("Componente: Inversión; Símbolo: I; ...").
- Gráficas (```grafica) -> descritas a partir de sus datos.
- Tooltips [[término::def]] -> solo el término; [[sim:...]] se omiten.
- Recuadros :::ejemplo / :::error -> anunciados ("Ejemplo resuelto." ... ).
- Los ejercicios NO se incluyen: el audio es para repasar la teoría.

Salida: audiolibro_generado/guion/mN/NN-slug.txt, un fichero por sección (capítulo del libro).
Cada párrafo va separado por una línea en blanco; `sintetizar.py` lo trocea por párrafos.

Uso:  python audiolibro/guion.py [m1 ... m10 | todos]
NUNCA incluir los contenidos con licencia (examenes_reales.py, practicas_libro.py).
"""
from __future__ import annotations

import importlib
import re
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SALIDA = REPO / 'audiolibro_generado' / 'guion'
sys.path.insert(0, str(REPO / 'backend'))

# ---------------------------------------------------------------------------
# Fórmulas: LaTeX -> español hablado
# ---------------------------------------------------------------------------

LETRAS = {
    'a': 'a', 'b': 'be', 'c': 'ce', 'd': 'de', 'e': 'e', 'f': 'efe', 'g': 'ge', 'h': 'hache',
    'i': 'i', 'j': 'jota', 'k': 'ka', 'l': 'ele', 'm': 'eme', 'n': 'ene', 'o': 'o', 'p': 'pe',
    'q': 'cu', 'r': 'erre', 's': 'ese', 't': 'te', 'u': 'u', 'v': 'uve', 'w': 'uve doble',
    'x': 'equis', 'y': 'i griega', 'z': 'zeta',
}
GRIEGAS = {
    'alpha': 'alfa', 'beta': 'beta', 'gamma': 'gamma', 'delta': 'delta', 'epsilon': 'épsilon',
    'varepsilon': 'épsilon', 'theta': 'zeta', 'lambda': 'lambda', 'mu': 'mu', 'nu': 'nu',
    'pi': 'pi', 'rho': 'ro', 'sigma': 'sigma', 'tau': 'tau', 'phi': 'fi', 'varphi': 'fi',
    'omega': 'omega', 'Gamma': 'gamma', 'Delta': 'incremento de', 'Theta': 'zeta',
    'Sigma': 'sigma', 'Phi': 'fi', 'Omega': 'omega', 'Pi': 'pi', 'chi': 'ji', 'eta': 'eta',
    'kappa': 'kappa', 'psi': 'psi', 'xi': 'xi', 'zeta': 'dseta',
}
OPERADORES = {
    'times': ' por ', 'cdot': ' por ', 'div': ' entre ', 'pm': ' más o menos ', 'mp': ' menos o más ',
    'approx': ' aproximadamente igual a ', 'simeq': ' aproximadamente igual a ', 'sim': ' del orden de ',
    'le': ' menor o igual que ', 'leq': ' menor o igual que ', 'ge': ' mayor o igual que ',
    'geq': ' mayor o igual que ', 'neq': ' distinto de ', 'ne': ' distinto de ',
    'Rightarrow': ', entonces, ', 'Longrightarrow': ', entonces, ', 'rightarrow': ' da ',
    'to': ' tiende a ', 'Leftrightarrow': ', equivale a, ', 'Longleftrightarrow': ', equivale a, ',
    'infty': ' infinito ', 'dots': ', etcétera, ', 'ldots': ', etcétera, ', 'cdots': ', etcétera, ',
    'mid': ' tal que ', 'in': ' perteneciente a ', 'partial': ' derivada parcial de ',
    'ln': ' logaritmo neperiano de ', 'log': ' logaritmo de ', 'exp': ' exponencial de ',
    'max': ' el máximo de ', 'min': ' el mínimo de ', '%': ' por ciento', '{': '', '}': '',
    'lvert': ' valor absoluto de ', 'rvert': ', ', 'lceil': ' redondeo hacia arriba de ', 'rceil': ', ',
    'quad': ', ', 'qquad': '. ', ',': ' ', ';': ' ', ' ': ' ', '!': '', ':': ' ', '\\': '. ',
    '&': ' ', '$': ' dólares', '#': '',
}
IGNORADOS = {'left', 'right', 'big', 'bigl', 'bigr', 'Big', 'Bigl', 'Bigr', 'displaystyle',
             'textstyle', 'mathrm', 'mathbf', 'mathit', 'boldsymbol', 'operatorname', 'limits',
             'nolimits', 'text', 'textbf', 'textit', 'mathcal', 'begin', 'end'}
FUNCIONES = {'Cov': 'la covarianza de', 'Var': 'la varianza de', 'E': 'el valor esperado de',
             'N': 'la normal de', 'VA': 'el valor actual de', 'VF': 'el valor final de'}
POTENCIAS = {'2': 'al cuadrado', '3': 'al cubo'}


class _Lector:
    """Parser recursivo mínimo de LaTeX matemático (el subconjunto que usa la teoría)."""

    def __init__(self, s: str):
        self.s = s
        self.i = 0

    def fin(self) -> bool:
        return self.i >= len(self.s)

    def ver(self) -> str:
        return self.s[self.i] if self.i < len(self.s) else ''

    def grupo_crudo(self) -> str:
        """Devuelve el LaTeX de un argumento: {…} o un único token."""
        while self.ver() == ' ':
            self.i += 1
        if self.ver() == '{':
            prof, ini = 0, self.i
            while not self.fin():
                c = self.s[self.i]
                if c == '\\':
                    self.i += 2
                    continue
                if c == '{':
                    prof += 1
                elif c == '}':
                    prof -= 1
                    if prof == 0:
                        self.i += 1
                        return self.s[ini + 1:self.i - 1]
                self.i += 1
            return self.s[ini + 1:]
        if self.ver() == '\\':
            m = re.compile(r'\\([a-zA-Z]+|.)').match(self.s, self.i)
            self.i = m.end()
            return m.group(0)
        c = self.ver()
        self.i += 1
        return c

    def leer(self) -> str:
        out: list[str] = []
        while not self.fin():
            c = self.ver()
            if c == '\\':
                m = re.compile(r'\\([a-zA-Z]+|.)').match(self.s, self.i)
                self.i = m.end()
                out.append(self.comando(m.group(1)))
            elif c == '{':
                out.append(hablar_latex(self.grupo_crudo()))
            elif c == '^':
                self.i += 1
                arg = self.grupo_crudo().strip()
                if arg in POTENCIAS:
                    out.append(' ' + POTENCIAS[arg] + ' ')
                elif arg in ('*', '\\ast', '\\star'):
                    out.append(' estrella ')
                elif arg in ("'", '\\prime'):
                    out.append(' prima ')
                else:
                    out.append(' elevado a ' + hablar_latex(arg) + ', ')
            elif c == '_':
                self.i += 1
                arg = self.grupo_crudo().strip()
                texto = re.sub(r'\\(text|mathrm)\{([^{}]*)\}', r'\2', arg).replace(',', ' ')
                if re.fullmatch(r'[A-Za-zÁÉÍÓÚáéíóúñ]{3,}( ?\d)?', texto.strip()):
                    out.append(' ' + texto.strip() + ' ')          # PIB_{real} -> "PIB real"
                else:
                    out.append(' sub ' + hablar_latex(arg.replace(',', ' ')) + ' ')
            elif c in '+':
                self.i += 1
                out.append(' más ')
            elif c == '-':
                self.i += 1
                out.append(' menos ')
            elif c == '=':
                self.i += 1
                out.append(' igual a ')
            elif c == '<':
                self.i += 1
                out.append(' menor que ')
            elif c == '>':
                self.i += 1
                out.append(' mayor que ')
            elif c == '/':
                self.i += 1
                out.append(' entre ')
            elif c == '*':
                self.i += 1
                out.append(' por ')
            elif c == '|':
                self.i += 1
                out.append(', ')
            elif c in '()[]':
                self.i += 1
                out.append(' ')
            elif c == '€':
                self.i += 1
                out.append(' euros ')
            elif c == '%':
                self.i += 1
                out.append(' por ciento ')
            elif c == '!':
                self.i += 1
                out.append(' factorial ')
            elif c == '~' or c == '&':
                self.i += 1
                out.append(' ')
            elif c.isdigit() or (c in ',.' and self.i + 1 < len(self.s) and self.s[self.i + 1].isdigit()):
                m = re.compile(r'[\d.,]*\d|\d').match(self.s, self.i)
                self.i = m.end()
                out.append(' ' + m.group(0) + ' ')
            elif c.isalpha():
                m = re.compile(r'[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+').match(self.s, self.i)
                self.i = m.end()
                out.append(' ' + self.palabra(m.group(0)) + ' ')
            else:
                self.i += 1
                out.append(' ' if c.isspace() else c)
        return ''.join(out)

    def palabra(self, w: str) -> str:
        sig = self.s[self.i:self.i + 1]
        if w in FUNCIONES and sig == '(':
            return FUNCIONES[w]
        if len(w) == 1:
            return LETRAS.get(w.lower(), w)
        return w

    def comando(self, nombre: str) -> str:
        if nombre in ('frac', 'dfrac', 'tfrac'):
            num, den = self.grupo_crudo(), self.grupo_crudo()
            n, d = hablar_latex(num), hablar_latex(den)
            if _simple(num) and _simple(den):
                return f' {n} entre {d} '
            return f', el cociente entre {n}, y {d}, '
        if nombre == 'sqrt':
            return ' la raíz cuadrada de ' + hablar_latex(self.grupo_crudo()) + ', '
        if nombre in ('sum', 'prod'):
            nombre_op = 'el sumatorio' if nombre == 'sum' else 'el producto'
            desde = hasta = ''
            while self.ver() in ('_', '^', ' '):
                c = self.ver()
                self.i += 1
                if c == '_':
                    desde = hablar_latex(self.grupo_crudo())
                elif c == '^':
                    hasta = hablar_latex(self.grupo_crudo())
            if desde and hasta:
                return f', {nombre_op}, para {desde} hasta {hasta}, de '
            return f', {nombre_op} de '
        if nombre == 'bar':
            return ' ' + hablar_latex(self.grupo_crudo()) + ' media '
        if nombre == 'hat':
            return ' ' + hablar_latex(self.grupo_crudo()) + ' estimada '
        if nombre in ('acute', 'tilde', 'vec', 'overline'):
            return ' ' + hablar_latex(self.grupo_crudo()) + ' '
        if nombre in ('text', 'textbf', 'textit', 'mathrm', 'mathbf', 'operatorname', 'mathit'):
            return ' ' + _texto_de_formula(self.grupo_crudo()) + ' '
        if nombre == 'underbrace':
            cuerpo = hablar_latex(self.grupo_crudo())
            if self.ver() == '_':
                self.i += 1
                etiqueta = hablar_latex(self.grupo_crudo())
                return f' {cuerpo}, es decir, {etiqueta}, '
            return ' ' + cuerpo + ' '
        if nombre == 'xrightarrow':
            return ' da, ' + hablar_latex(self.grupo_crudo()) + ', '
        if nombre in ('begin', 'end'):
            self.grupo_crudo()
            return '. '
        if nombre in GRIEGAS:
            return ' ' + GRIEGAS[nombre] + ' '
        if nombre in OPERADORES:
            return OPERADORES[nombre]
        if nombre in IGNORADOS:
            return ' '
        return ' ' + nombre + ' '


def _simple(tex: str) -> bool:
    """Un argumento 'simple' se lee sin anunciar el cociente: 5, R, 1,04, \\sigma_p..."""
    t = re.sub(r'\\(text|mathrm)\{[^{}]*\}', 'X', tex.strip())
    t = re.sub(r'\{,\}', ',', t)
    return not re.search(r'[+\-=]|\\frac|\\sum|\\sqrt|\\times|\\cdot', t) and len(t) <= 14


def _texto_de_formula(t: str) -> str:
    t = t.replace('\\%', ' por ciento').replace('\\,', ' ').replace('\\ ', ' ').replace('{,}', ',')
    return re.sub(r'\\[a-zA-Z]+', ' ', t)


def hablar_latex(tex: str) -> str:
    tex = tex.replace('{,}', ',').replace('{.}', '.')
    return _Lector(tex).leer()


def formula_hablada(tex: str) -> str:
    s = hablar_latex(tex)
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r'\s+([,.])', r'\1', s)
    s = re.sub(r'([,.])(\s*[,.])+', r'\1', s)
    s = re.sub(r'^[\s,.]+|[\s,]+$', '', s)
    # "menos 0,50 por ciento" al principio suena bien; "igual a menos" también. Nada más que hacer.
    return s


# ---------------------------------------------------------------------------
# Prosa: markdown propio -> texto hablado
# ---------------------------------------------------------------------------

ABREVIATURAS = [
    (r'\bp\. ?ej\.', 'por ejemplo'), (r'\bvs\.', 'frente a'), (r'\bpp\.', 'puntos porcentuales'),
    (r'\bp\.p\.', 'puntos porcentuales'), (r'\bpb\b', 'puntos básicos'), (r'\bp\.b\.', 'puntos básicos'),
    (r'\bart\.', 'artículo'), (r'\bArt\.', 'Artículo'), (r'\bapdo\.', 'apartado'),
    (r'\baprox\.', 'aproximadamente'), (r'\bnº', 'número'), (r'\bNº', 'Número'), (r'\bnúm\.', 'número'),
    (r'\bM€', 'millones de euros'), (r'\bmill\.', 'millones'), (r'\bmm\b', 'miles de millones'),
    (r'\bk€', 'mil euros'), (r'\bUd\.', 'usted'), (r'\bEE\. ?UU\.', 'Estados Unidos'),
    (r'\bSr\.', 'señor'), (r'\bi\. ?e\.', 'es decir'), (r'\betc\.', 'etcétera'),
]
SIMBOLOS = [
    ('≈', ' aproximadamente '), ('→', ', lo que lleva a, '), ('⇒', ', entonces, '), ('←', ' '),
    ('↑', ' sube '), ('↓', ' baja '), ('×', ' por '), ('≤', ' menor o igual que '),
    ('≥', ' mayor o igual que '), ('≠', ' distinto de '), ('±', ' más o menos '), ('–', ', '),
    ('—', ', '), ('…', '...'), ('•', ''), ('✅', ''), ('❌', ''), ('⚠️', ''), ('⚠', ''), ('💡', ''),
    ('📌', ''), ('🎯', ''), ('👉', ''), ('✔', ''), ('✗', ''), ('→', ', '), ('ª', 'ª'),
]


def _num_con_signos(t: str) -> str:
    """'5 %' -> '5 por ciento'; '1.000 €' -> '1.000 euros'; '$' sueltos -> 'dólares'."""
    t = re.sub(r'(\d)\s*%', r'\1 por ciento', t)
    t = re.sub(r'%', ' por ciento', t)
    t = re.sub(r'(\d)\s*€', r'\1 euros', t)
    t = re.sub(r'€\s*(\d[\d.,]*)', r'\1 euros', t)
    t = t.replace('€', 'euros')
    t = re.sub(r'(\d)\s*\$', r'\1 dólares', t)
    return t


def prosa(t: str) -> str:
    """Texto en línea (sin fórmulas ya): limpia marcas y lo deja listo para el TTS."""
    t = re.sub(r'\[\[sim:[^\]]*\]\]', '', t)
    t = re.sub(r'\[\[([^:\]]+)::[^\]]*\]\]', r'\1', t)
    t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)          # enlaces markdown
    t = re.sub(r'\*\*(.+?)\*\*', r'\1', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'\1', t)
    t = re.sub(r'(?<!\w)_(?!\s)(.+?)(?<!\s)_(?!\w)', r'\1', t)
    t = t.replace('`', '')
    for a, b in SIMBOLOS:
        t = t.replace(a, b)
    for pat, rep in ABREVIATURAS:
        t = re.sub(pat, rep, t)
    t = _num_con_signos(t)
    t = re.sub(r'\s*/\s*año\b', ' al año', t)
    t = re.sub(r'"([^"]+)"', r'\1', t)
    t = re.sub(r'\s=\s', ': ', t)                              # "P1 = precio..." en prosa
    t = re.sub(r'\.{2,}', '…', t)                              # se protege de la limpieza de puntos
    t = re.sub(r'[ \t]+', ' ', t)
    t = re.sub(r'([(¿¡])\s+', r'\1', t)
    t = re.sub(r'\s+([,.;:)])', r'\1', t)
    t = re.sub(r',\s*,', ',', t)
    return t.strip()


def con_formulas(t: str) -> str:
    """Sustituye $…$ y $$…$$ por su lectura y limpia la prosa."""
    trozos = re.split(r'(\$\$.+?\$\$|\$[^$\n]+?\$)', t, flags=re.S)
    out = []
    for tr in trozos:
        if tr.startswith('$$'):
            out.append(' ' + formula_hablada(tr[2:-2]) + '. ')
        elif tr.startswith('$') and tr.endswith('$') and len(tr) > 1:
            out.append(' ' + formula_hablada(tr[1:-1]) + ' ')
        else:
            out.append(prosa(tr))
    s = ' '.join(out)
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r'\s+([,.;:?!)])', r'\1', s)
    s = re.sub(r'\.\s*\.', '.', s)
    s = re.sub(r'([,;:])\s*\.', '.', s)
    s = re.sub(r'([(¿¡])\s+', r'\1', s)
    s = re.sub(r'\(\s*\)', '', s)
    return s.replace('…', '...').strip()


def _frase(s: str) -> str:
    s = s.strip()
    if s and s[-1] not in '.:;?!':
        s += '.'
    return s


# --- Tablas ---------------------------------------------------------------

def _celdas(fila: str) -> list[str]:
    fila = fila.strip()
    if fila.startswith('|'):
        fila = fila[1:]
    if fila.endswith('|'):
        fila = fila[:-1]
    # '|' dentro de fórmulas: protegerlo antes de dividir
    return [c.strip() for c in re.split(r'(?<!\\)\|', fila)]


def tabla_hablada(lineas: list[str]) -> list[str]:
    filas = [_celdas(l) for l in lineas if not re.match(r'^\s*\|?\s*:?-{2,}', l)]
    if not filas:
        return []
    cab = [con_formulas(c) for c in filas[0]]
    parrafos = [f'Tabla con {len(filas) - 1} filas. Columnas: {", ".join(c for c in cab if c)}.']
    for fila in filas[1:]:
        partes = []
        for j, celda in enumerate(fila):
            v = con_formulas(celda)
            if not v or v in ('-', '—'):
                continue
            nombre = cab[j] if j < len(cab) else ''
            partes.append(f'{nombre}: {v}' if (nombre and j > 0) else v)
        if partes:
            parrafos.append(_frase('; '.join(partes)))
    parrafos.append('Fin de la tabla.')
    return parrafos


# --- Gráficas -------------------------------------------------------------

def _num(v: str) -> str:
    return v.strip().replace('.', ',') if re.fullmatch(r'-?\d+\.\d+', v.strip()) else v.strip()


def grafica_hablada(bloque: str) -> list[str]:
    campos: dict[str, str] = {}
    series: list[tuple[str, list[str]]] = []
    for l in bloque.splitlines():
        if ':' not in l:
            continue
        k, v = l.split(':', 1)
        k, v = k.strip().lower(), v.strip()
        if k == 'serie':
            nombre, _, datos = v.partition('|')
            series.append((nombre.strip(), [d.strip() for d in datos.split(',') if d.strip()]))
        else:
            campos[k] = v
    tipo = campos.get('tipo', 'barras')
    titulo = prosa(campos.get('titulo', ''))
    eje_x = campos.get('x') or campos.get('categorias') or campos.get('etiquetas') or ''
    xs = [x.strip() for x in re.split(r',(?![^(]*\))', eje_x) if x.strip()]
    out = [f'Gráfica{": " + titulo if titulo else ""}.']
    if tipo == 'payoff':
        pos = campos.get('posicion', 'compra')
        out.append(_frase(prosa(f'Resultado al vencimiento de la {pos} de una {campos.get("opcion", "opción")}, '
                                f'con precio de ejercicio {_num(campos.get("strike", ""))} '
                                f'y prima {_num(campos.get("prima", ""))}')))
    elif tipo == 'oferta_demanda':
        out.append(_frase(prosa(f'Se cruzan la curva de {campos.get("demanda", "demanda").lower()} y la de '
                                f'{campos.get("oferta", "oferta").lower()}; en el eje horizontal, '
                                f'{campos.get("ejex", "la cantidad").lower()}, y en el vertical, '
                                f'{campos.get("ejey", "el precio").lower()}')))
    for nombre, datos in series:
        datos = [_num(d) for d in datos]
        if tipo in ('lineas', 'líneas', 'linea', 'area') and len(datos) > 4:
            if len(xs) == len(datos):
                eje = campos.get('ejex', '').lower() or 'eje horizontal'
                out.append(_frase(prosa(f'{nombre}: pasa de {datos[0]} a {datos[-1]} '
                                        f'({eje}: de {xs[0]} a {xs[-1]})')))
            else:
                out.append(_frase(prosa(f'Curva {nombre}')))
        elif xs and len(xs) == len(datos):
            pares = ', '.join(f'{prosa(x)}, {d}' for x, d in zip(xs, datos))
            out.append(_frase(prosa(f'{nombre}: {pares}') if nombre else prosa(pares)))
        elif datos:
            out.append(_frase(prosa(f'{nombre}: {", ".join(datos)}')))
    if campos.get('ejey') and series and (xs or tipo == 'barras'):
        out.append(_frase(f'Valores en {prosa(campos["ejey"]).lower()}'))
    if campos.get('nota'):
        out.append(_frase(con_formulas(campos['nota'])))
    return out


# --- Documento ------------------------------------------------------------

CALLOUTS = {'ejemplo': ('Ejemplo resuelto.', 'Fin del ejemplo.'),
            'error': ('Error frecuente.', 'Fin del aviso.'),
            'clave': ('Idea clave.', ''), 'nota': ('Nota.', ''), 'recuerda': ('Recuerda.', '')}


def markdown_hablado(md: str) -> list[str]:
    """Devuelve la lista de párrafos hablados de un cuerpo de sección."""
    md = md.replace('\r\n', '\n')
    lineas = md.split('\n')
    parrafos: list[str] = []
    buf: list[str] = []
    cierre_callout: list[str] = []

    def vaciar():
        if buf:
            t = con_formulas(' '.join(x.strip() for x in buf))
            if t:
                parrafos.append(_frase(t))
            buf.clear()

    i = 0
    while i < len(lineas):
        l = lineas[i]
        s = l.strip()
        if s.startswith('```'):
            vaciar()
            lang = s[3:].strip()
            j = i + 1
            while j < len(lineas) and not lineas[j].strip().startswith('```'):
                j += 1
            if lang == 'grafica':
                parrafos.extend(grafica_hablada('\n'.join(lineas[i + 1:j])))
            i = j + 1
            continue
        if s.startswith('$$') and not (s.endswith('$$') and len(s) > 4):
            vaciar()
            j = i + 1
            while j < len(lineas) and '$$' not in lineas[j]:
                j += 1
            bloque = '\n'.join(lineas[i:j + 1])
            parrafos.append(_frase(con_formulas(bloque)))
            i = j + 1
            continue
        m = re.match(r'^:::\s*(\w+)', s)
        if m:
            vaciar()
            ini, fin = CALLOUTS.get(m.group(1).lower(), ('', ''))
            if ini:
                parrafos.append(ini)
            cierre_callout.append(fin)
            i += 1
            continue
        if s == ':::':
            vaciar()
            if cierre_callout:
                fin = cierre_callout.pop()
                if fin:
                    parrafos.append(fin)
            i += 1
            continue
        if s.startswith('|'):
            vaciar()
            j = i
            while j < len(lineas) and lineas[j].strip().startswith('|'):
                j += 1
            parrafos.extend(tabla_hablada(lineas[i:j]))
            i = j
            continue
        h = re.match(r'^(#{1,6})\s+(.*)', s)
        if h:
            vaciar()
            titulo = con_formulas(h.group(2)).rstrip('.')
            titulo = re.sub(r'^(\d+(\.\d+)*)\.?\s+', r'Apartado \1. ', titulo)
            parrafos.append('§ ' + _frase(titulo))       # '§' = pausa larga antes (lo quita sintetizar.py)
            i += 1
            continue
        if not s or re.fullmatch(r'-{3,}|\*{3,}', s):
            vaciar()
            i += 1
            continue
        li = re.match(r'^(\s*)([-*+]|\d+[.)])\s+(.*)', l)
        if li:
            vaciar()
            buf.append(li.group(3))
            # continuaciones del mismo punto (líneas sangradas sin viñeta)
            while i + 1 < len(lineas) and lineas[i + 1].startswith('  ') and lineas[i + 1].strip() \
                    and not re.match(r'^\s*([-*+]|\d+[.)])\s+', lineas[i + 1]):
                i += 1
                buf.append(lineas[i])
            vaciar()
            i += 1
            continue
        buf.append(re.sub(r'^>\s?', '', s))
        i += 1
    vaciar()
    return [p for p in parrafos if re.search(r'\w', p)]


def slug(t: str) -> str:
    t = unicodedata.normalize('NFD', t.lower())
    t = re.sub(r'[\u0300-\u036f]', '', t)
    return re.sub(r'[^a-z0-9]+', '-', t).strip('-')[:60]


def limpiar_titulo(t: str) -> str:
    return re.sub(r'^\s*(\d+(\.\d+)*[.)]?\s+)', '', re.sub(r'[#*]', '', t)).strip()


def guion_modulo(clave: str) -> list[Path]:
    mod = importlib.import_module(f'content.{clave}')
    n = int(clave[1:])
    carpeta = SALIDA / clave
    carpeta.mkdir(parents=True, exist_ok=True)
    for viejo in carpeta.glob('*.txt'):
        viejo.unlink()
    ficheros = []
    intro = re.sub(r'^\s*#\s+M\d+[^\n]*\n', '', mod.INTRO)
    piezas = [('00', 'Introducción', intro)] + [
        (f'{k:02d}', limpiar_titulo(s['titulo']), s['cuerpo']) for k, s in enumerate(mod.SECCIONES, 1)]
    for num, titulo, cuerpo in piezas:
        cab = (f'Módulo {n}: {mod.NOMBRE}. Introducción.' if num == '00'
               else f'Módulo {n}. Capítulo {int(num)}: {prosa(titulo)}.')
        parrafos = [cab] + markdown_hablado(cuerpo)
        f = carpeta / f'{num}-{slug(titulo)}.txt'
        f.write_text('\n\n'.join(parrafos) + '\n', encoding='utf-8')
        ficheros.append(f)
    return ficheros


def main(args: list[str]) -> None:
    claves = [f'm{i}' for i in range(1, 11)] if (not args or 'todos' in args) else args
    total = 0
    for c in claves:
        fs = guion_modulo(c)
        chars = sum(len(f.read_text(encoding='utf-8')) for f in fs)
        total += chars
        print(f'{c}: {len(fs)} ficheros, {chars:,} caracteres (~{chars / 15 / 3600:.1f} h de audio)')
    print(f'Total: {total:,} caracteres (~{total / 15 / 3600:.1f} h)')


if __name__ == '__main__':
    main(sys.argv[1:])
