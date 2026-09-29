// Generador del LIBRO de estudio (PDF + EPUB), un volumen por módulo.
//
// Uso (desde frontend/):   node scripts/libro.ts m1            -> PDF + EPUB del M1
//                          node scripts/libro.ts m1 m5 --epub  -> solo EPUB
//                          node scripts/libro.ts todos --pdf   -> solo PDF de los 10
//
// Reutiliza el MISMO renderizado que la web (src/render.ts), así el libro se ve
// igual: fórmulas KaTeX, gráficas SVG, tablas y recuadros. Particularidades del libro:
//   - Los términos con definición [[término::def]] van al GLOSARIO del volumen.
//   - Las calculadoras interactivas [[sim:...]] se omiten (no tienen sentido en papel).
//   - Los ejercicios de cada capítulo van al final del capítulo y las SOLUCIONES al
//     final del volumen.
// Contenido: SOLO la teoría propia (backend/content/m*.py). NUNCA los exámenes con
// licencia. Los PDF/EPUB generados NO se versionan (salen a libro_generado/).
//
// Sin dependencias nuevas: el PDF lo imprime Microsoft Edge (Chromium) sin interfaz
// vía su protocolo de depuración; el EPUB se empaqueta con un escritor ZIP propio.

import { execFileSync, spawn } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import { fileURLToPath, pathToFileURL } from 'node:url';
import katex from 'katex';
import { renderMarkdownToHtml } from '../src/render.ts';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const FRONTEND = path.resolve(AQUI, '..');
const REPO = path.resolve(FRONTEND, '..');
const SALIDA = path.join(REPO, 'libro_generado');
const KATEX_CSS = path.join(FRONTEND, 'node_modules', 'katex', 'dist', 'katex.min.css');
const EDGE_CANDIDATOS = [
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
  'C:/Program Files/Microsoft/Edge/Application/msedge.exe',
];

// Módulos cuyo contenido se apoya en parte en OpenStax (CC BY 4.0): atribución obligatoria.
const ATRIBUCION_OPENSTAX: Record<string, string> = {
  m1: 'Parte de los contenidos de macroeconomía y divisas de este módulo se han elaborado tomando como referencia ' +
      '<em>Principles of Macroeconomics 2e</em> (OpenStax, Rice University), publicado bajo licencia ' +
      'Creative Commons Attribution 4.0 (CC BY 4.0): https://openstax.org/details/books/principles-macroeconomics-2e. ' +
      'El texto de este libro es una redacción propia, no una traducción.',
};

// Colores fijos para las variables CSS del renderizado (muchos lectores de EPUB no
// entienden variables CSS y el papel pide una paleta clara).
const COLORES: Record<string, string> = {
  '--primary': '#1f5fbf',
  '--secondary': '#0e7c86',
  '--warning': '#b86e00',
  '--success': '#2e7d32',
  '--error': '#c62828',
  '--text-primary': '#1a1a1a',
  '--text-secondary': '#444444',
  '--text-muted': '#6b6b6b',
  '--border-color': '#c9ced6',
  '--surface-soft': '#eef1f5',
};

type Modo = 'pdf' | 'epub';
interface Ejercicio {
  enunciado: string;
  tipo?: string;
  opciones?: string[];
  correcta?: number;
  valor_esperado?: number;
  tolerancia?: number;
  explicacion?: string;
}
interface Seccion { titulo: string; cuerpo: string; ejercicios: Ejercicio[] }
interface Modulo { clave: string; numero: number; nombre: string; intro: string; secciones: Seccion[] }
interface Glosario { terminos: Map<string, { termino: string; def: string }> }

// ------------------------------------------------------------------ utilidades

const esc = (s: string) =>
  String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

function slug(s: string): string {
  return s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[^A-Za-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

function numES(v: number): string {
  return Number(v).toLocaleString('es-ES', { maximumFractionDigits: 4 });
}

function resolverColores(html: string): string {
  return html.replace(/var\((--[a-z-]+)\)/g, (m, nombre) => COLORES[nombre] ?? m);
}

// ------------------------------------------------------------------ contenido

function cargarModulo(clave: string): Modulo {
  const n = Number(clave.slice(1));
  const code =
    'import json,sys,importlib\n' +
    `m=importlib.import_module('backend.content.${clave}')\n` +
    "json.dump({'nombre':m.NOMBRE,'intro':m.INTRO,'secciones':[{'titulo':s['titulo'],'cuerpo':s['cuerpo'],'ejercicios':s.get('ejercicios',[])} for s in m.SECCIONES]}, sys.stdout, ensure_ascii=False)";
  const out = execFileSync('python', ['-c', code], {
    cwd: REPO, encoding: 'utf8', maxBuffer: 512 * 1024 * 1024,
    env: { ...process.env, PYTHONIOENCODING: 'utf-8' },
  });
  const d = JSON.parse(out);
  return { clave, numero: n, nombre: d.nombre, intro: d.intro, secciones: d.secciones };
}

// ------------------------------------------------------------------ renderizado de fragmentos

let contadorFragmentos = 0;
const erroresKatex: string[] = [];

// Prepara el markdown de la teoría para el libro: quita las calculadoras, manda los
// términos al glosario (dejando un marcador inerte) y escapa & < > de la prosa para que
// el resultado sea XML válido (EPUB). No toca fórmulas ni bloques de gráfica.
function preparar(md: string, glos: Glosario, terminos: string[]): string {
  if (!md) return '';
  let s = md.replace(/\[\[sim:[a-z0-9_]+\]\]/g, '');

  // términos -> marcador TERMTKN{i}TERMEND (solo letras y dígitos: inmune a ** _ *)
  s = s.replace(/\[\[([^\]|]+?)::([^\]]+?)\]\]/g, (_m, t, d) => {
    const termino = String(t).trim();
    const k = termino.toLocaleLowerCase('es');
    if (!glos.terminos.has(k)) glos.terminos.set(k, { termino, def: String(d).trim() });
    terminos.push(termino);
    return `TERMTKN${terminos.length - 1}TERMEND`;
  });

  // proteger gráficas y fórmulas antes de escapar
  const prot: string[] = [];
  const tok = (x: string) => { prot.push(x); return `PROTTKN${prot.length - 1}PROTEND`; };
  s = s.replace(/```\s*grafica[\s\S]*?```/g, tok);
  s = s.replace(/\$\$[\s\S]*?\$\$/g, tok);
  s = s.replace(/\$[^$\n]+?\$/g, tok);

  // escapar la prosa; conservar el ">" inicial de las citas markdown
  s = s.split('\n').map((linea) => {
    const m = linea.match(/^(\s*>\s?)?([\s\S]*)$/)!;
    const cita = m[1] ?? '';
    return cita + m[2].replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }).join('\n');

  return s.replace(/PROTTKN(\d+)PROTEND/g, (_m, i) => prot[Number(i)]);
}

function renderizarMates(html: string, modo: Modo): string {
  return html.replace(/\$\$([\s\S]*?)\$\$|\$([^$\n]+?)\$/g, (m, bloque, enLinea) => {
    const tex = bloque ?? enLinea;
    const r = katex.renderToString(tex, {
      displayMode: bloque !== undefined,
      throwOnError: false,
      strict: 'ignore',
      output: modo === 'pdf' ? 'html' : 'mathml',
    });
    if (r.includes('katex-error')) erroresKatex.push(m.slice(0, 80));
    return r;
  });
}

// Renderiza un fragmento de markdown de la teoría a HTML/XHTML de libro.
function fragmento(md: string, modo: Modo, glos: Glosario): string {
  const terminos: string[] = [];
  let html = renderMarkdownToHtml(preparar(md, glos, terminos));
  const f = contadorFragmentos++;
  html = html.replace(/id="hb-(\d+)"/g, `id="f${f}-hb-$1"`);
  html = html.replace(/📝 Ejemplo resuelto/g, 'Ejemplo resuelto').replace(/⚠️ Error frecuente/g, 'Error frecuente');
  html = renderizarMates(html, modo);
  html = html.replace(/TERMTKN(\d+)TERMEND/g, (_m, i) => `<span class="termino">${esc(terminos[Number(i)])}</span>`);
  return resolverColores(html);
}

// Igual, pero para textos cortos (opciones, definiciones): sin el <p> envolvente.
function enLinea(md: string, modo: Modo, glos: Glosario): string {
  const h = fragmento(md, modo, glos).trim();
  const m = h.match(/^<p[^>]*>([\s\S]*)<\/p>$/);
  return m && !m[1].includes('<p') ? m[1] : h;
}

// ------------------------------------------------------------------ piezas del libro

const LETRAS = ['A', 'B', 'C', 'D', 'E', 'F'];

function ejerciciosCapitulo(mod: Modulo, ic: number, modo: Modo, glos: Glosario): { html: string; soluciones: string } {
  const ejs = mod.secciones[ic].ejercicios || [];
  if (!ejs.length) return { html: '', soluciones: '' };
  const cap = ic + 1;
  let html = `<section class="ejercicios"><h2 class="ejercicios-titulo">Ejercicios del capítulo ${cap}</h2>`;
  let sol = `<section class="soluciones-cap"><h2>Capítulo ${cap}. ${esc(limpiar(mod.secciones[ic].titulo))}</h2>`;
  ejs.forEach((e, j) => {
    const num = `${cap}.${j + 1}`;
    html += `<div class="ejercicio"><p class="ej-enunciado"><span class="ej-num">${num}</span> ${enLinea(e.enunciado, modo, glos)}</p>`;
    if (e.tipo === 'opcion' && Array.isArray(e.opciones)) {
      html += '<div class="opciones">';
      e.opciones.forEach((o, k) => { html += `<p class="opcion"><span class="letra">${LETRAS[k]})</span> ${enLinea(o, modo, glos)}</p>`; });
      html += '</div>';
      const c = typeof e.correcta === 'number' ? e.correcta : 0;
      sol += `<div class="solucion"><p><span class="ej-num">${num}</span> <strong>Respuesta: ${LETRAS[c]})</strong> ${enLinea(e.opciones[c] ?? '', modo, glos)}</p>`;
    } else {
      const tol = typeof e.tolerancia === 'number' && e.tolerancia > 0 ? ` <span class="tol">(margen ± ${numES(e.tolerancia)})</span>` : '';
      sol += `<div class="solucion"><p><span class="ej-num">${num}</span> <strong>Resultado: ${numES(Number(e.valor_esperado))}</strong>${tol}</p>`;
    }
    if (e.explicacion) sol += `<div class="sol-expl">${fragmento(e.explicacion, modo, glos)}</div>`;
    sol += '</div>';
    html += '</div>';
  });
  html += '</section>';
  sol += '</section>';
  return { html, soluciones: sol };
}

function limpiar(t: string): string {
  return t.replace(/\[\[([^\]|]+?)::[^\]]+?\]\]/g, '$1').replace(/\[\[sim:[a-z0-9_]+\]\]/g, '')
    .replace(/[*_`#]/g, '').replace(/\s+/g, ' ').trim();
}

function tituloLibro(mod: Modulo): string {
  return `Módulo ${mod.numero}. ${mod.nombre}`;
}

// La introducción de cada módulo empieza con su propio "# Mx: nombre", que en el libro
// duplica la portada y el título "Introducción": se quita.
function introSinTitulo(intro: string): string {
  return (intro || '').replace(/^\s*#\s+M\d+:[^\n]*\n+/, '');
}

// Cabecera de capítulo: la etiqueta "Capítulo N" va FUERA del <h1> para que el título
// del marcador de navegación (outline del PDF, índice del EPUB) quede limpio.
function cabeceraCapitulo(n: number, titulo: string): string {
  return `<p class="cap-num">Capítulo ${n}</p><h1 class="cap-titulo">${esc(titulo)}</h1>`;
}

function portada(mod: Modulo): string {
  return `<section class="portada">
  <p class="portada-serie">Preparación de la certificación EFA</p>
  <p class="portada-num">Módulo ${mod.numero}</p>
  <div class="portada-titulo">${esc(mod.nombre)}</div>
  <p class="portada-sub">Manual de estudio · Teoría, ejercicios y soluciones</p>
</section>`;
}

function creditos(mod: Modulo): string {
  const fecha = new Date().toLocaleDateString('es-ES', { day: 'numeric', month: 'long', year: 'numeric' });
  const os_ = ATRIBUCION_OPENSTAX[mod.clave] ? `<p><strong>Atribución.</strong> ${ATRIBUCION_OPENSTAX[mod.clave]}</p>` : '';
  return `<section class="creditos">
  <h1 class="creditos-titulo">Sobre este libro</h1>
  <p>Material de estudio de <strong>elaboración propia</strong> para preparar la certificación EFA, generado a partir de la teoría de la plataforma de estudio.</p>
  <p>No está afiliado a EFPA España ni cuenta con su respaldo. Es un material orientativo: la normativa fiscal y financiera cambia con frecuencia, así que conviene contrastar los datos vigentes. No constituye asesoramiento financiero, fiscal ni jurídico.</p>
  ${os_}
  <p class="creditos-fecha">Edición generada el ${esc(fecha)}.</p>
</section>`;
}

function glosarioHtml(glos: Glosario, modo: Modo): string {
  const lista = [...glos.terminos.values()].sort((a, b) => a.termino.localeCompare(b.termino, 'es'));
  if (!lista.length) return '';
  const vacio: Glosario = { terminos: new Map() }; // las definiciones no alimentan el glosario
  let h = '<section class="glosario"><h1 class="cap-titulo">Glosario</h1><dl>';
  for (const t of lista) h += `<dt>${esc(t.termino)}</dt><dd>${enLinea(t.def, modo, vacio)}</dd>`;
  return h + '</dl></section>';
}

// ------------------------------------------------------------------ PDF

const CSS_PDF = `
@page { size: A4; margin: 22mm 20mm 24mm 20mm; }
html { font-size: 10.5pt; }
body { font-family: Georgia, Cambria, 'Times New Roman', serif; color: #1a1a1a; line-height: 1.55; margin: 0;
       -webkit-print-color-adjust: exact; print-color-adjust: exact; text-align: justify; hyphens: auto; }
h1, h2, h3, h4, h5, h6 { font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; text-align: left; hyphens: manual;
       break-after: avoid; page-break-after: avoid; }
p, li { orphans: 3; widows: 3; }
.portada { height: 240mm; display: flex; flex-direction: column; justify-content: center; text-align: center; break-after: page; }
.portada-serie { font-family: 'Segoe UI', Arial, sans-serif; letter-spacing: .12em; text-transform: uppercase; color: #6b6b6b; font-size: 10pt; }
.portada-num { font-family: 'Segoe UI', Arial, sans-serif; font-size: 60pt; font-weight: 800; color: #1f5fbf; margin: 18mm 0 4mm; }
.portada-sub { color: #444; font-style: italic; }
.creditos { break-after: page; font-size: 9.5pt; color: #333; }
.creditos-fecha { color: #6b6b6b; margin-top: 10mm; }
.indice { break-after: page; }
.indice ol { list-style: none; padding: 0; }
.indice li { margin: 3px 0; border-bottom: 1px dotted #c9ced6; }
.indice a { color: inherit; text-decoration: none; }
.indice .nro { display: inline-block; min-width: 2.2em; font-weight: 700; color: #1f5fbf; }
.indice a { display: flex; align-items: baseline; }
.indice .txt { flex: 1; } .indice .pag { margin-left: 8px; color: #444; font-variant-numeric: tabular-nums; }
.capitulo, .intro, .glosario, .soluciones { break-before: page; }
.cap-titulo { font-size: 21pt; color: #1a1a1a; border-bottom: 3px solid #1f5fbf; padding-bottom: 6px; margin: 0 0 16px; }
.cap-num { font-family: 'Segoe UI', Arial, sans-serif; font-weight: 700; font-size: 10pt; letter-spacing: .1em;
           text-transform: uppercase; color: #1f5fbf; margin: 0 0 2px; break-after: avoid; page-break-after: avoid; }
.portada-titulo { font-family: 'Segoe UI', Arial, sans-serif; font-weight: 700; font-size: 26pt; margin: 0 10mm 8mm; line-height: 1.2; }
.creditos-titulo { font-size: 14pt; margin-top: 0; }
td, th { text-align: left; hyphens: auto; }
figure.grafica { margin: 14px auto; text-align: center; break-inside: avoid; }
figure.grafica svg { width: 14.5cm; max-width: 100%; height: auto; font-family: 'Segoe UI', Arial, sans-serif; }
.grafica-cap { font-size: 8.5pt; color: #6b6b6b; font-style: italic; margin-top: 4px; }
.callout { border-left: 4px solid; border-radius: 4px; padding: 8px 12px 4px; margin: 12px 0; break-inside: avoid; }
.callout-ejemplo { background: #eef4ff; border-color: #1f5fbf; }
.callout-error { background: #fff5e6; border-color: #b86e00; }
.callout-titulo { font-family: 'Segoe UI', Arial, sans-serif; font-weight: 700; font-size: 8.5pt; text-transform: uppercase; letter-spacing: .05em; margin-bottom: 4px; }
.callout-ejemplo .callout-titulo { color: #1f5fbf; } .callout-error .callout-titulo { color: #b86e00; }
.math-block { margin: 10px 0; break-inside: avoid; }
.katex { font-size: 1.05em; } .katex-display { margin: .6em 0; }
table { font-size: 8.8pt; break-inside: auto; } tr { break-inside: avoid; }
.termino { font-weight: 700; }
.ejercicios { margin-top: 18px; border-top: 2px solid #c9ced6; padding-top: 6px; }
.ejercicios-titulo { font-size: 13pt; color: #0e7c86; }
.ejercicio { margin: 0 0 10px; break-inside: avoid; }
.ej-num { font-family: 'Segoe UI', Arial, sans-serif; font-weight: 700; color: #1f5fbf; margin-right: 3px; }
.opciones { margin: 2px 0 0 1.6em; } .opcion { margin: 1px 0; text-align: left; }
.letra { font-weight: 700; margin-right: 3px; }
.soluciones h2 { font-size: 12pt; color: #0e7c86; margin-top: 16px; }
.solucion { margin: 0 0 9px; font-size: 9.3pt; break-inside: avoid; }
.solucion p { margin: 0 0 3px; } .sol-expl { margin-left: 1.6em; color: #333; }
.tol { color: #6b6b6b; font-weight: normal; }
.glosario dl { font-size: 9.5pt; } .glosario dt { font-weight: 700; margin-top: 6px; font-family: 'Segoe UI', Arial, sans-serif; }
.glosario dd { margin: 1px 0 0 1.2em; }
`;

// Números de página de las entradas del índice (se obtienen en una primera impresión).
interface PaginasIndice { intro?: number; caps: (number | null)[]; glosario?: number; soluciones?: number }

// Textos de todos los encabezados del HTML (sin etiquetas), para limpiar los marcadores.
function textosEncabezados(html: string): string[] {
  const des = (s: string) => s.replace(/<[^>]+>/g, '').replace(/&lt;/g, '<').replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"').replace(/&amp;/g, '&').replace(/\s+/g, ' ').trim();
  return [...html.matchAll(/<h([1-6])[^>]*>([\s\S]*?)<\/h\1>/g)].map((m) => des(m[2])).filter(Boolean);
}

// Renderiza el cuerpo del volumen UNA vez y devuelve un constructor del HTML completo,
// al que se le pueden pasar los números de página del índice (segunda pasada).
function htmlPdf(mod: Modulo): { construir: (pags?: PaginasIndice) => string; errores: number; titulos: string[]; encabezados: string[] } {
  const glos: Glosario = { terminos: new Map() };
  const errAntes = erroresKatex.length;
  const titulos = mod.secciones.map((s) => limpiar(s.titulo));
  let cuerpo = `<section class="intro" id="intro"><h1 class="cap-titulo">Introducción</h1>${fragmento(introSinTitulo(mod.intro), 'pdf', glos)}</section>`;
  let soluciones = '';
  mod.secciones.forEach((s, i) => {
    const ej = ejerciciosCapitulo(mod, i, 'pdf', glos);
    cuerpo += `<section class="capitulo" id="cap-${i + 1}">${cabeceraCapitulo(i + 1, titulos[i])}` +
      fragmento(s.cuerpo, 'pdf', glos) + ej.html + '</section>';
    soluciones += ej.soluciones;
  });
  cuerpo += glosarioHtml(glos, 'pdf').replace('<section class="glosario">', '<section class="glosario" id="glosario">');
  cuerpo += `<section class="soluciones" id="soluciones"><h1 class="cap-titulo">Soluciones de los ejercicios</h1>${soluciones}</section>`;

  const construir = (pags?: PaginasIndice) => {
    const pag = (p?: number | null) => (p ? `<span class="pag">${p}</span>` : '');
    const entrada = (href: string, nro: string, txt: string, p?: number | null) =>
      `<li><a href="${href}"><span class="nro">${nro}</span><span class="txt">${esc(txt)}</span>${pag(p)}</a></li>`;
    let indice = '<nav class="indice"><h1 class="cap-titulo">Índice</h1><ol>';
    indice += entrada('#intro', '', 'Introducción', pags?.intro);
    titulos.forEach((t, i) => { indice += entrada(`#cap-${i + 1}`, String(i + 1), t, pags?.caps[i]); });
    indice += entrada('#glosario', '', 'Glosario', pags?.glosario);
    indice += entrada('#soluciones', '', 'Soluciones de los ejercicios', pags?.soluciones) + '</ol></nav>';
    return `<!doctype html><html lang="es"><head><meta charset="utf-8"><title>${esc(tituloLibro(mod))}</title>
<link rel="stylesheet" href="${pathToFileURL(KATEX_CSS).href}"><style>${CSS_PDF}</style></head><body>${portada(mod)}${creditos(mod)}${indice}${cuerpo}</body></html>`;
  };
  const encabezados = [...textosEncabezados(cuerpo), 'Sobre este libro', 'Índice'];
  return { construir, errores: erroresKatex.length - errAntes, titulos, encabezados };
}

// Con PyMuPDF (si está instalado): reescribe los marcadores del PDF con los títulos
// correctos (Chromium pega las palabras de los títulos que ocupan dos líneas), numera
// los capítulos en el marcador, y devuelve en qué página empieza cada parte del índice.
function ajustarPdf(pdfFile: string, titulos: string[], encabezados: string[]): PaginasIndice | null {
  const cfg = path.join(os.tmpdir(), `libro-cfg-${process.pid}.json`);
  fs.writeFileSync(cfg, JSON.stringify({ pdf: pdfFile, capitulos: titulos, encabezados }));
  const code = `
import json, sys, os, re
try:
    import pymupdf
except ImportError:
    print("SIN_PYMUPDF"); sys.exit(0)
cfg = json.load(open(sys.argv[1], encoding="utf-8"))
doc = pymupdf.open(cfg["pdf"])
ns = lambda s: re.sub(r"\\s+", "", s)
mapa = {}
for t in cfg["encabezados"]:
    mapa.setdefault(ns(t), t)
caps = {ns(t): i for i, t in enumerate(cfg["capitulos"])}
res = {"caps": [None] * len(cfg["capitulos"])}
nuevo, prev = [], 0
for lvl, tit, pag in doc.get_toc(simple=True):
    k = ns(tit)
    limpio = mapa.get(k, tit)
    if lvl == 1 and k in caps:
        i = caps[k]
        limpio = f"{i + 1}. {cfg['capitulos'][i]}"
        if res["caps"][i] is None:
            res["caps"][i] = pag
    elif lvl == 1 and limpio == "Introducción":
        res.setdefault("intro", pag)
    elif lvl == 1 and limpio == "Glosario":
        res.setdefault("glosario", pag)
    elif lvl == 1 and limpio == "Soluciones de los ejercicios":
        res.setdefault("soluciones", pag)
    lvl = max(1, min(lvl, prev + 1)); prev = lvl
    nuevo.append([lvl, limpio, pag])
doc.set_toc(nuevo)
tmp = cfg["pdf"] + ".tmp"
doc.save(tmp, garbage=3, deflate=True)
doc.close()
os.replace(tmp, cfg["pdf"])
print(json.dumps(res))
`;
  try {
    const out = execFileSync('python', ['-c', code, cfg], { encoding: 'utf8', env: { ...process.env, PYTHONIOENCODING: 'utf-8' } }).trim();
    if (out.includes('SIN_PYMUPDF')) { console.log('   (sin PyMuPDF: índice sin números de página y marcadores sin retocar)'); return null; }
    return JSON.parse(out.split('\n').pop()!);
  } finally {
    fs.rmSync(cfg, { force: true });
  }
}

async function imprimirPdf(htmlFile: string, pdfFile: string, pie: string): Promise<void> {
  const edge = EDGE_CANDIDATOS.find((p) => fs.existsSync(p));
  if (!edge) throw new Error('No se encuentra Microsoft Edge para imprimir el PDF.');
  const perfil = fs.mkdtempSync(path.join(os.tmpdir(), 'edge-libro-'));
  const puerto = 9300 + Math.floor(Math.random() * 600);
  const proc = spawn(edge, ['--headless=new', `--remote-debugging-port=${puerto}`, `--user-data-dir=${perfil}`,
    '--no-first-run', '--no-default-browser-check', '--disable-extensions', '--allow-file-access-from-files', 'about:blank'],
  { stdio: 'ignore' });
  try {
    let listo = false;
    for (let i = 0; i < 80 && !listo; i++) {
      try { await (await fetch(`http://127.0.0.1:${puerto}/json/version`)).json(); listo = true; } catch { await sleep(250); }
    }
    if (!listo) throw new Error('Edge no respondió en el puerto de depuración.');
    const pest = await (await fetch(`http://127.0.0.1:${puerto}/json/new?${encodeURIComponent(pathToFileURL(htmlFile).href)}`, { method: 'PUT' })).json();
    const ws = new WebSocket(pest.webSocketDebuggerUrl);
    await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
    let sig = 0;
    const pendientes = new Map<number, { res: (v: any) => void; rej: (e: Error) => void }>();
    ws.onmessage = (ev) => {
      const m = JSON.parse(String(ev.data));
      const p = m.id !== undefined ? pendientes.get(m.id) : undefined;
      if (p) { pendientes.delete(m.id); if (m.error) p.rej(new Error(JSON.stringify(m.error))); else p.res(m.result); }
    };
    const cdp = (method: string, params: object = {}) => new Promise<any>((res, rej) => {
      const id = ++sig; pendientes.set(id, { res, rej }); ws.send(JSON.stringify({ id, method, params }));
    });
    for (let i = 0; i < 480; i++) {
      const r = await cdp('Runtime.evaluate', { expression: 'document.readyState', returnByValue: true });
      if (r.result.value === 'complete') break;
      await sleep(250);
    }
    await cdp('Runtime.evaluate', { expression: 'document.fonts.ready.then(() => 1)', awaitPromise: true });
    const pdf = await cdp('Page.printToPDF', {
      printBackground: true,
      preferCSSPageSize: true,
      displayHeaderFooter: true,
      headerTemplate: '<span></span>',
      footerTemplate: `<div style="font-size:7.5pt;width:100%;margin:0 20mm;display:flex;justify-content:space-between;color:#888;font-family:Georgia,serif;"><span>${esc(pie)}</span><span class="pageNumber"></span></div>`,
      generateDocumentOutline: true,
      generateTaggedPDF: true,
    });
    fs.writeFileSync(pdfFile, Buffer.from(pdf.data, 'base64'));
    ws.close();
  } finally {
    proc.kill();
    await sleep(300);
    try { fs.rmSync(perfil, { recursive: true, force: true }); } catch { /* Edge puede tardar en soltar el perfil */ }
  }
}

// ------------------------------------------------------------------ EPUB

const CSS_EPUB = `
body { font-family: Georgia, 'Times New Roman', serif; line-height: 1.5; color: #1a1a1a; }
h1, h2, h3, h4, h5, h6 { font-family: sans-serif; line-height: 1.25; }
.portada { text-align: center; margin-top: 30%; }
.portada-serie { text-transform: uppercase; letter-spacing: .1em; color: #6b6b6b; font-size: .8em; }
.portada-num { font-size: 3em; font-weight: bold; color: #1f5fbf; margin: 1em 0 .2em; }
.portada-titulo { font-family: sans-serif; font-weight: bold; font-size: 1.8em; }
.portada-sub { font-style: italic; color: #444; }
.cap-titulo { border-bottom: 3px solid #1f5fbf; padding-bottom: .3em; }
.cap-num { font-family: sans-serif; font-weight: bold; font-size: .8em; letter-spacing: .1em; text-transform: uppercase; color: #1f5fbf; margin: 0; }
td, th { text-align: left; }
figure.grafica { margin: 1em 0; text-align: center; }
figure.grafica svg { width: 100%; height: auto; font-family: sans-serif; }
.grafica-cap { font-size: .8em; color: #6b6b6b; font-style: italic; }
.callout { border-left: 4px solid #1f5fbf; padding: .5em .8em; margin: 1em 0; background: #eef4ff; }
.callout-error { border-left-color: #b86e00; background: #fff5e6; }
.callout-titulo { font-family: sans-serif; font-weight: bold; font-size: .8em; text-transform: uppercase; }
.math-block { margin: .8em 0; text-align: center; }
table { border-collapse: collapse; font-size: .85em; }
.termino { font-weight: bold; }
.ejercicios { margin-top: 1.5em; border-top: 2px solid #c9ced6; }
.ej-num { font-weight: bold; color: #1f5fbf; }
.opciones { margin-left: 1.5em; } .letra { font-weight: bold; }
.solucion { margin-bottom: .8em; font-size: .95em; } .sol-expl { margin-left: 1.5em; }
.tol { color: #6b6b6b; font-weight: normal; }
.glosario dt { font-weight: bold; margin-top: .5em; } .glosario dd { margin-left: 1.2em; }
`;

function xhtml(titulo: string, cuerpo: string): string {
  return `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="es" lang="es">
<head><meta charset="UTF-8"/><title>${esc(titulo)}</title><link rel="stylesheet" type="text/css" href="estilo.css"/></head>
<body>${cuerpo}</body>
</html>`;
}

// Escritor ZIP mínimo (stored/deflate) con crc32 de node:zlib.
function crearZip(entradas: { nombre: string; datos: Buffer; guardar?: boolean }[]): Buffer {
  const trozos: Buffer[] = [];
  const central: Buffer[] = [];
  let offset = 0;
  for (const e of entradas) {
    const nombre = Buffer.from(e.nombre, 'utf8');
    const crc = zlib.crc32(e.datos) >>> 0;
    const comp = e.guardar ? e.datos : zlib.deflateRawSync(e.datos, { level: 9 });
    const metodo = e.guardar ? 0 : 8;
    const loc = Buffer.alloc(30);
    loc.writeUInt32LE(0x04034b50, 0); loc.writeUInt16LE(20, 4); loc.writeUInt16LE(0x0800, 6);
    loc.writeUInt16LE(metodo, 8); loc.writeUInt16LE(0, 10); loc.writeUInt16LE(0x21, 12);
    loc.writeUInt32LE(crc, 14); loc.writeUInt32LE(comp.length, 18); loc.writeUInt32LE(e.datos.length, 22);
    loc.writeUInt16LE(nombre.length, 26); loc.writeUInt16LE(0, 28);
    trozos.push(loc, nombre, comp);
    const cen = Buffer.alloc(46);
    cen.writeUInt32LE(0x02014b50, 0); cen.writeUInt16LE(20, 4); cen.writeUInt16LE(20, 6); cen.writeUInt16LE(0x0800, 8);
    cen.writeUInt16LE(metodo, 10); cen.writeUInt16LE(0, 12); cen.writeUInt16LE(0x21, 14);
    cen.writeUInt32LE(crc, 16); cen.writeUInt32LE(comp.length, 20); cen.writeUInt32LE(e.datos.length, 24);
    cen.writeUInt16LE(nombre.length, 28); cen.writeUInt16LE(0, 30); cen.writeUInt16LE(0, 32);
    cen.writeUInt16LE(0, 34); cen.writeUInt16LE(0, 36); cen.writeUInt32LE(0, 38); cen.writeUInt32LE(offset, 42);
    central.push(cen, nombre);
    offset += loc.length + nombre.length + comp.length;
  }
  const cd = Buffer.concat(central);
  const fin = Buffer.alloc(22);
  fin.writeUInt32LE(0x06054b50, 0); fin.writeUInt16LE(0, 4); fin.writeUInt16LE(0, 6);
  fin.writeUInt16LE(entradas.length, 8); fin.writeUInt16LE(entradas.length, 10);
  fin.writeUInt32LE(cd.length, 12); fin.writeUInt32LE(offset, 16); fin.writeUInt16LE(0, 20);
  return Buffer.concat([...trozos, cd, fin]);
}

function construirEpub(mod: Modulo): { zip: Buffer; errores: number; ficheros: Map<string, string> } {
  const glos: Glosario = { terminos: new Map() };
  const errAntes = erroresKatex.length;
  const titulos = mod.secciones.map((s) => limpiar(s.titulo));
  const docs: { id: string; href: string; titulo: string; cuerpo: string }[] = [];
  docs.push({ id: 'portada', href: 'portada.xhtml', titulo: tituloLibro(mod), cuerpo: portada(mod) });
  docs.push({ id: 'creditos', href: 'creditos.xhtml', titulo: 'Sobre este libro', cuerpo: creditos(mod) });
  docs.push({ id: 'intro', href: 'intro.xhtml', titulo: 'Introducción', cuerpo: `<section class="intro"><h1 class="cap-titulo">Introducción</h1>${fragmento(introSinTitulo(mod.intro), 'epub', glos)}</section>` });
  let soluciones = '';
  mod.secciones.forEach((s, i) => {
    const ej = ejerciciosCapitulo(mod, i, 'epub', glos);
    const n = String(i + 1).padStart(2, '0');
    docs.push({ id: `cap${n}`, href: `cap${n}.xhtml`, titulo: `${i + 1}. ${titulos[i]}`,
      cuerpo: `<section class="capitulo">${cabeceraCapitulo(i + 1, titulos[i])}${fragmento(s.cuerpo, 'epub', glos)}${ej.html}</section>` });
    soluciones += ej.soluciones;
  });
  const g = glosarioHtml(glos, 'epub');
  if (g) docs.push({ id: 'glosario', href: 'glosario.xhtml', titulo: 'Glosario', cuerpo: g });
  docs.push({ id: 'soluciones', href: 'soluciones.xhtml', titulo: 'Soluciones de los ejercicios',
    cuerpo: `<section class="soluciones"><h1 class="cap-titulo">Soluciones de los ejercicios</h1>${soluciones}</section>` });

  const ficheros = new Map<string, string>();
  for (const d of docs) ficheros.set(d.href, xhtml(d.titulo, d.cuerpo));
  const nav = `<nav epub:type="toc" id="toc"><h1>Índice</h1><ol>${docs.map((d) => `<li><a href="${d.href}">${esc(d.titulo)}</a></li>`).join('')}</ol></nav>`;
  ficheros.set('nav.xhtml', xhtml('Índice', nav));

  const uuid = crypto.createHash('sha1').update('efa-libro-' + mod.clave).digest('hex');
  const id = `urn:uuid:${uuid.slice(0, 8)}-${uuid.slice(8, 12)}-5${uuid.slice(13, 16)}-a${uuid.slice(17, 20)}-${uuid.slice(20, 32)}`;
  const modificado = new Date().toISOString().replace(/\.\d+Z$/, 'Z');
  const props = (href: string) => {
    const c = ficheros.get(href) ?? '';
    const p = [c.includes('<math') ? 'mathml' : '', c.includes('<svg') ? 'svg' : ''].filter(Boolean).join(' ');
    return p ? ` properties="${p}"` : '';
  };
  const opf = `<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="es">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="bookid">${id}</dc:identifier>
<dc:title>${esc('Preparación EFA · ' + tituloLibro(mod))}</dc:title>
<dc:language>es</dc:language>
<dc:creator>Preparación EFA (elaboración propia)</dc:creator>
<meta property="dcterms:modified">${modificado}</meta>
</metadata>
<manifest>
<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
<item id="css" href="estilo.css" media-type="text/css"/>
${docs.map((d) => `<item id="${d.id}" href="${d.href}" media-type="application/xhtml+xml"${props(d.href)}/>`).join('\n')}
</manifest>
<spine>
${docs.map((d) => `<itemref idref="${d.id}"/>`).join('\n')}
</spine>
</package>`;
  const container = `<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>`;

  const entradas = [
    { nombre: 'mimetype', datos: Buffer.from('application/epub+zip'), guardar: true },
    { nombre: 'META-INF/container.xml', datos: Buffer.from(container) },
    { nombre: 'OEBPS/content.opf', datos: Buffer.from(opf) },
    { nombre: 'OEBPS/estilo.css', datos: Buffer.from(CSS_EPUB) },
    ...[...ficheros].map(([href, c]) => ({ nombre: `OEBPS/${href}`, datos: Buffer.from(c) })),
  ];
  return { zip: crearZip(entradas), errores: erroresKatex.length - errAntes, ficheros };
}

// Comprueba que cada XHTML es XML bien formado (lo exige EPUB 3). Usa Python (stdlib).
function validarXhtml(dir: string): string[] {
  const code =
    'import sys,os,xml.etree.ElementTree as ET\n' +
    'errs=[]\n' +
    'for f in sorted(os.listdir(sys.argv[1])):\n' +
    '  if f.endswith(".xhtml"):\n' +
    '    try: ET.parse(os.path.join(sys.argv[1],f))\n' +
    '    except ET.ParseError as e: errs.append(f"{f}: {e}")\n' +
    'print("\\n".join(errs))';
  const out = execFileSync('python', ['-c', code, dir], { encoding: 'utf8', env: { ...process.env, PYTHONIOENCODING: 'utf-8' } });
  return out.split('\n').map((l) => l.trim()).filter(Boolean);
}

// ------------------------------------------------------------------ principal

async function main() {
  const args = process.argv.slice(2);
  const soloPdf = args.includes('--pdf');
  const soloEpub = args.includes('--epub');
  let claves = args.filter((a) => !a.startsWith('--'));
  if (!claves.length) claves = ['m1'];
  if (claves.includes('todos')) claves = Array.from({ length: 10 }, (_, i) => `m${i + 1}`);
  for (const c of claves) if (!/^m([1-9]|10)$/.test(c)) throw new Error(`Módulo no válido: ${c}`);

  fs.mkdirSync(path.join(SALIDA, 'intermedio'), { recursive: true });
  for (const clave of claves) {
    const t0 = Date.now();
    const mod = cargarModulo(clave);
    const base = `EFA-Modulo-${mod.numero}-${slug(mod.nombre)}`;
    const nEj = mod.secciones.reduce((a, s) => a + (s.ejercicios?.length ?? 0), 0);
    console.log(`\n== ${tituloLibro(mod)} (${mod.secciones.length} capítulos, ${nEj} ejercicios)`);

    if (!soloEpub) {
      const { construir, errores, titulos, encabezados } = htmlPdf(mod);
      const htmlFile = path.join(SALIDA, 'intermedio', `${base}.html`);
      const pdfFile = path.join(SALIDA, `${base}.pdf`);
      const pie = `Preparación EFA · Módulo ${mod.numero}`;
      // 1ª pasada: imprimir para saber en qué página cae cada parte.
      fs.writeFileSync(htmlFile, construir());
      await imprimirPdf(htmlFile, pdfFile, pie);
      const pags = ajustarPdf(pdfFile, titulos, encabezados);
      // 2ª pasada: reimprimir con el índice numerado (el índice ocupa lo mismo, no mueve páginas).
      if (pags) {
        fs.writeFileSync(htmlFile, construir(pags));
        await imprimirPdf(htmlFile, pdfFile, pie);
        const pags2 = ajustarPdf(pdfFile, titulos, encabezados);
        if (JSON.stringify(pags2) !== JSON.stringify(pags)) console.log('   ! aviso: el índice cambió entre pasadas; revisar los números de página');
      }
      console.log(`   PDF  -> ${path.relative(REPO, pdfFile)} (${(fs.statSync(pdfFile).size / 1048576).toFixed(1)} MB, fórmulas con error: ${errores}${pags ? ', índice numerado' : ''})`);
    }
    if (!soloPdf) {
      const { zip, errores, ficheros } = construirEpub(mod);
      const dirX = path.join(SALIDA, 'intermedio', `${base}-epub`);
      fs.rmSync(dirX, { recursive: true, force: true });
      fs.mkdirSync(dirX, { recursive: true });
      for (const [href, c] of ficheros) fs.writeFileSync(path.join(dirX, href), c);
      const malos = validarXhtml(dirX);
      const epubFile = path.join(SALIDA, `${base}.epub`);
      fs.writeFileSync(epubFile, zip);
      console.log(`   EPUB -> ${path.relative(REPO, epubFile)} (${(zip.length / 1048576).toFixed(1)} MB, fórmulas con error: ${errores}, XHTML mal formados: ${malos.length})`);
      for (const m of malos.slice(0, 10)) console.log(`      ! ${m}`);
    }
    console.log(`   (${((Date.now() - t0) / 1000).toFixed(1)} s)`);
  }
  if (erroresKatex.length) {
    console.log(`\nFórmulas que KaTeX no pudo renderizar (${erroresKatex.length}):`);
    for (const e of [...new Set(erroresKatex)].slice(0, 15)) console.log(`   · ${e}`);
  }
}

main().catch((e) => { console.error(e); process.exit(1); });
