// Renderizado de la teoría (markdown propio + fórmulas + gráficas SVG).
// Funciones PURAS (texto -> HTML/SVG), sin React: las usa la web (App.tsx) y
// también el generador del libro (scripts/libro.ts), para que ambos se vean igual.

// ===== Motor de gráficas SVG (sin librerías externas, temático claro/oscuro) =====
// Se activa con un bloque ```grafica ... ``` dentro de la teoría. Tipos:
// lineas, barras, oferta_demanda, payoff. Devuelve un <svg> como cadena.
const GRAF_COLORES = ['var(--primary)', 'var(--secondary)', 'var(--warning)', 'var(--success)', 'var(--error)'];

function _escSvg(s: string): string {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function _parseGrafica(spec: string): { p: Record<string, string>; series: { nombre: string; valores: number[] }[] } {
  const p: Record<string, string> = {};
  const series: { nombre: string; valores: number[] }[] = [];
  for (const raw of spec.split('\n')) {
    const l = raw.trim();
    const idx = l.indexOf(':');
    if (!l || idx < 0) continue;
    const key = l.slice(0, idx).trim().toLowerCase();
    const val = l.slice(idx + 1).trim();
    if (key === 'serie') {
      const partes = val.split('|');
      series.push({
        nombre: (partes[0] || '').trim(),
        valores: (partes[1] || '').split(',').map(s => parseFloat(s.trim().replace(',', '.'))).filter(n => !isNaN(n)),
      });
    } else {
      p[key] = val;
    }
  }
  return { p, series };
}

const GRAF_W = 660, GRAF_H = 380, GRAF_L = 58, GRAF_R = 22, GRAF_T = 40, GRAF_B = 52;
const GRAF_PW = GRAF_W - GRAF_L - GRAF_R, GRAF_PH = GRAF_H - GRAF_T - GRAF_B;

function _grafMarco(titulo: string, ejex: string, ejey: string): string {
  let s = '';
  if (titulo) s += `<text x="${GRAF_W / 2}" y="22" text-anchor="middle" font-size="16" font-weight="600" fill="var(--text-primary)">${_escSvg(titulo)}</text>`;
  // ejes
  s += `<line x1="${GRAF_L}" y1="${GRAF_T}" x2="${GRAF_L}" y2="${GRAF_T + GRAF_PH}" stroke="var(--text-muted)" stroke-width="1.2"/>`;
  s += `<line x1="${GRAF_L}" y1="${GRAF_T + GRAF_PH}" x2="${GRAF_L + GRAF_PW}" y2="${GRAF_T + GRAF_PH}" stroke="var(--text-muted)" stroke-width="1.2"/>`;
  if (ejex) s += `<text x="${GRAF_L + GRAF_PW / 2}" y="${GRAF_H - 8}" text-anchor="middle" font-size="12" fill="var(--text-secondary)">${_escSvg(ejex)}</text>`;
  if (ejey) s += `<text x="16" y="${GRAF_T + GRAF_PH / 2}" text-anchor="middle" font-size="12" fill="var(--text-secondary)" transform="rotate(-90 16 ${GRAF_T + GRAF_PH / 2})">${_escSvg(ejey)}</text>`;
  return s;
}

function _grafLeyenda(nombres: string[]): string {
  if (nombres.filter(n => n).length < 2) return '';
  let s = '';
  let x = GRAF_L + 4;
  const y = GRAF_T - 22;
  nombres.forEach((n, i) => {
    if (!n) return;
    s += `<rect x="${x}" y="${y}" width="14" height="10" rx="2" fill="${GRAF_COLORES[i % GRAF_COLORES.length]}"/>`;
    s += `<text x="${x + 19}" y="${y + 9}" font-size="12" fill="var(--text-secondary)">${_escSvg(n)}</text>`;
    x += 30 + n.length * 7;
  });
  return s;
}

function _svgWrap(inner: string, caption: string): string {
  const cap = caption ? `<figcaption class="grafica-cap">${_escSvg(caption)}</figcaption>` : '';
  return `<figure class="grafica"><svg viewBox="0 0 ${GRAF_W} ${GRAF_H}" role="img" xmlns="http://www.w3.org/2000/svg">${inner}</svg>${cap}</figure>`;
}

function _grafLineasBarras(tipo: string, p: Record<string, string>, series: { nombre: string; valores: number[] }[]): string {
  const xs = (p['x'] || '').split(',').map(s => s.trim()).filter(Boolean);
  const n = Math.max(xs.length, ...series.map(s => s.valores.length), 1);
  const todos = series.flatMap(s => s.valores);
  let ymin = Math.min(0, ...todos), ymax = Math.max(...todos, 0);
  if (ymin === ymax) ymax = ymin + 1;
  const pad = (ymax - ymin) * 0.08; ymax += pad; if (ymin < 0) ymin -= pad;
  const sy = (v: number) => GRAF_T + GRAF_PH - ((v - ymin) / (ymax - ymin)) * GRAF_PH;
  let g = _grafMarco(p['titulo'] || '', p['ejex'] || '', p['ejey'] || '');
  // rejilla y + etiquetas y
  for (let k = 0; k <= 4; k++) {
    const v = ymin + (k / 4) * (ymax - ymin), y = sy(v);
    g += `<line x1="${GRAF_L}" y1="${y.toFixed(1)}" x2="${GRAF_L + GRAF_PW}" y2="${y.toFixed(1)}" stroke="var(--border-color)" stroke-width="1"/>`;
    g += `<text x="${GRAF_L - 6}" y="${(y + 4).toFixed(1)}" text-anchor="end" font-size="11" fill="var(--text-muted)">${(Math.round(v * 100) / 100)}</text>`;
  }
  if (tipo === 'barras') {
    const grupo = GRAF_PW / n;
    const bw = (grupo * 0.7) / Math.max(series.length, 1);
    series.forEach((s, si) => {
      s.valores.forEach((v, i) => {
        const x = GRAF_L + i * grupo + grupo * 0.15 + si * bw;
        const y = sy(v), y0 = sy(0);
        g += `<rect x="${x.toFixed(1)}" y="${Math.min(y, y0).toFixed(1)}" width="${bw.toFixed(1)}" height="${Math.abs(y0 - y).toFixed(1)}" fill="${GRAF_COLORES[si % GRAF_COLORES.length]}" opacity="0.85"/>`;
      });
    });
    xs.forEach((xl, i) => { g += `<text x="${(GRAF_L + i * grupo + grupo / 2).toFixed(1)}" y="${GRAF_T + GRAF_PH + 16}" text-anchor="middle" font-size="11" fill="var(--text-muted)">${_escSvg(xl)}</text>`; });
  } else {
    const sx = (i: number) => GRAF_L + (n <= 1 ? GRAF_PW / 2 : (i / (n - 1)) * GRAF_PW);
    series.forEach((s, si) => {
      const pts = s.valores.map((v, i) => `${sx(i).toFixed(1)},${sy(v).toFixed(1)}`).join(' ');
      const col = GRAF_COLORES[si % GRAF_COLORES.length];
      g += `<polyline points="${pts}" fill="none" stroke="${col}" stroke-width="2.4" stroke-linejoin="round"/>`;
      s.valores.forEach((v, i) => { g += `<circle cx="${sx(i).toFixed(1)}" cy="${sy(v).toFixed(1)}" r="3" fill="${col}"/>`; });
    });
    xs.forEach((xl, i) => { g += `<text x="${sx(i).toFixed(1)}" y="${GRAF_T + GRAF_PH + 16}" text-anchor="middle" font-size="11" fill="var(--text-muted)">${_escSvg(xl)}</text>`; });
  }
  g += _grafLeyenda(series.map(s => s.nombre));
  return _svgWrap(g, p['nota'] || '');
}

function _grafOfertaDemanda(p: Record<string, string>): string {
  const x0 = GRAF_L, x1 = GRAF_L + GRAF_PW, y0 = GRAF_T, y1 = GRAF_T + GRAF_PH;
  let g = _grafMarco(p['titulo'] || 'Oferta y demanda', p['ejex'] || 'Cantidad', p['ejey'] || 'Precio');
  // demanda (pendiente negativa) y oferta (positiva), cruce en el centro
  g += `<line x1="${x0 + 10}" y1="${y0 + 20}" x2="${x1 - 10}" y2="${y1 - 20}" stroke="${GRAF_COLORES[0]}" stroke-width="2.6"/>`;
  g += `<line x1="${x0 + 10}" y1="${y1 - 20}" x2="${x1 - 10}" y2="${y0 + 20}" stroke="${GRAF_COLORES[1]}" stroke-width="2.6"/>`;
  const cx = (x0 + x1) / 2, cy = (y0 + y1) / 2;
  g += `<line x1="${x0}" y1="${cy}" x2="${cx}" y2="${cy}" stroke="var(--border-color)" stroke-dasharray="4 3"/>`;
  g += `<line x1="${cx}" y1="${cy}" x2="${cx}" y2="${y1}" stroke="var(--border-color)" stroke-dasharray="4 3"/>`;
  g += `<circle cx="${cx}" cy="${cy}" r="4.5" fill="var(--text-primary)"/>`;
  g += `<text x="${x1 - 8}" y="${y1 - 24}" text-anchor="end" font-size="13" font-weight="600" fill="${GRAF_COLORES[0]}">${_escSvg(p['demanda'] || 'Demanda')}</text>`;
  g += `<text x="${x1 - 8}" y="${y0 + 30}" text-anchor="end" font-size="13" font-weight="600" fill="${GRAF_COLORES[1]}">${_escSvg(p['oferta'] || 'Oferta')}</text>`;
  g += `<text x="${cx + 8}" y="${cy - 8}" font-size="11" fill="var(--text-secondary)">E</text>`;
  return _svgWrap(g, p['nota'] || '');
}

function _grafPayoff(p: Record<string, string>): string {
  const K = parseFloat(p['strike'] || '100'), prima = parseFloat(p['prima'] || '5');
  const opcion = (p['opcion'] || 'call').toLowerCase(), pos = (p['posicion'] || 'compra').toLowerCase();
  const xmin = Math.max(0, K * 0.4), xmax = K * 1.6;
  const puntos = [xmin, K, xmax];
  const payoff = (S: number) => {
    let intr = opcion === 'call' ? Math.max(S - K, 0) : Math.max(K - S, 0);
    let r = intr - prima;
    return pos === 'venta' ? -r : r;
  };
  const ys = puntos.map(payoff);
  let ymin = Math.min(...ys), ymax = Math.max(...ys);
  const padY = Math.max((ymax - ymin) * 0.15, prima * 0.5); ymin -= padY; ymax += padY;
  const sx = (S: number) => GRAF_L + ((S - xmin) / (xmax - xmin)) * GRAF_PW;
  const sy = (v: number) => GRAF_T + GRAF_PH - ((v - ymin) / (ymax - ymin)) * GRAF_PH;
  let g = _grafMarco(p['titulo'] || 'Diagrama de resultado', p['ejex'] || 'Precio del subyacente al vencimiento', p['ejey'] || 'Resultado (€)');
  // línea de resultado cero
  const yZero = sy(0);
  g += `<line x1="${GRAF_L}" y1="${yZero.toFixed(1)}" x2="${GRAF_L + GRAF_PW}" y2="${yZero.toFixed(1)}" stroke="var(--border-color)" stroke-width="1.2" stroke-dasharray="5 3"/>`;
  // strike
  g += `<line x1="${sx(K).toFixed(1)}" y1="${GRAF_T}" x2="${sx(K).toFixed(1)}" y2="${GRAF_T + GRAF_PH}" stroke="var(--text-muted)" stroke-dasharray="3 3"/>`;
  g += `<text x="${sx(K).toFixed(1)}" y="${GRAF_T + GRAF_PH + 16}" text-anchor="middle" font-size="11" fill="var(--text-muted)">K=${K}</text>`;
  const pts = puntos.map(S => `${sx(S).toFixed(1)},${sy(payoff(S)).toFixed(1)}`).join(' ');
  g += `<polyline points="${pts}" fill="none" stroke="${GRAF_COLORES[0]}" stroke-width="2.6" stroke-linejoin="round"/>`;
  // punto muerto (breakeven)
  const be = opcion === 'call' ? K + prima : K - prima;
  if (be > xmin && be < xmax) {
    g += `<circle cx="${sx(be).toFixed(1)}" cy="${yZero.toFixed(1)}" r="4" fill="var(--text-primary)"/>`;
    g += `<text x="${sx(be).toFixed(1)}" y="${(yZero - 8).toFixed(1)}" text-anchor="middle" font-size="10" fill="var(--text-secondary)">BE ${Math.round(be * 100) / 100}</text>`;
  }
  return _svgWrap(g, p['nota'] || '');
}

export function renderGrafica(spec: string): string {
  try {
    const { p, series } = _parseGrafica(spec);
    const tipo = (p['tipo'] || 'lineas').toLowerCase();
    if (tipo === 'oferta_demanda') return _grafOfertaDemanda(p);
    if (tipo === 'payoff') return _grafPayoff(p);
    if (tipo === 'barras' || tipo === 'lineas') return _grafLineasBarras(tipo, p, series);
    return `<div class="grafica-error">Gráfica de tipo desconocido: ${_escSvg(tipo)}</div>`;
  } catch {
    return `<div class="grafica-error">No se pudo dibujar la gráfica.</div>`;
  }
}

export function renderMarkdownToHtml(markdown: string): string {
  if (!markdown) return '';

  const mathPlaceholders: string[] = [];
  
  // Token inerte para markdown: solo letras y dígitos, SIN guiones bajos ni
  // asteriscos, para que el procesado de negrita/cursiva (** __ * _) no lo
  // corrompa y la restauración posterior siempre encuentre el marcador exacto.
  const mathToken = (idx: number) => `MATHTKN${idx}MATHEND`;

  // 1. Ocultar fórmulas en bloque $$...$$
  let processed = markdown.replace(/\$\$([\s\S]*?)\$\$/g, (match) => {
    const idx = mathPlaceholders.length;
    mathPlaceholders.push(match);
    return mathToken(idx);
  });

  // 2. Ocultar fórmulas en línea $...$
  processed = processed.replace(/\$([^$\n]+?)\$/g, (match) => {
    const idx = mathPlaceholders.length;
    mathPlaceholders.push(match);
    return mathToken(idx);
  });

  // 2b. Ocultar conceptos con definición: [[término::definición]]
  const conceptos: { term: string; def: string }[] = [];
  const conceptToken = (idx: number) => `CONCEPTTKN${idx}CONCEPTEND`;
  processed = processed.replace(/\[\[([^\]|]+?)::([^\]]+?)\]\]/g, (_m, term, def) => {
    const idx = conceptos.length;
    conceptos.push({ term: String(term).trim(), def: String(def).trim() });
    return conceptToken(idx);
  });

  const lines = processed.split('\n');
  let headingCounter = 0;
  const htmlBlocks: string[] = [];
  
  let inList: 'ul' | 'ol' | null = null;
  let currentListItemLines: string[] = [];
  let paragraphLines: string[] = [];
  let calloutTipo: string | null = null;
  let calloutLines: string[] = [];
  let enGrafica = false;
  let graficaLines: string[] = [];

  const flushParagraph = () => {
    if (paragraphLines.length > 0) {
      const pText = paragraphLines.join(' ');
      const htmlText = renderInlineMarkdown(pText);
      htmlBlocks.push(`<p style="margin-bottom: 12px; color: var(--text-primary);">${htmlText}</p>`);
      paragraphLines = [];
    }
  };

  const flushListItem = () => {
    if (currentListItemLines.length > 0) {
      const itemText = currentListItemLines.join(' ');
      const htmlText = renderInlineMarkdown(itemText);
      const listStyle = inList === 'ul' 
        ? 'margin-left: 24px; margin-bottom: 8px; list-style-type: disc; color: var(--text-primary);' 
        : 'margin-left: 24px; margin-bottom: 8px; list-style-type: decimal; color: var(--text-primary);';
      htmlBlocks.push(`<li style="${listStyle}">${htmlText}</li>`);
      currentListItemLines = [];
    }
  };

  const flushList = () => {
    flushListItem();
    if (inList === 'ul') {
      htmlBlocks.push('</ul>');
    } else if (inList === 'ol') {
      htmlBlocks.push('</ol>');
    }
    inList = null;
  };

  const renderInlineMarkdown = (text: string): string => {
    let res = text;
    // Negrita: **texto**
    res = res.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
    // Negrita: __texto__
    res = res.replace(/__([^_]+)__/g, '<strong>$1</strong>');
    // Cursiva: *texto*
    res = res.replace(/\*([^*]+)\*/g, '<em>$1</em>');
    // Cursiva: _texto_ (evitando conflictos con placeholders)
    res = res.replace(/_([^_]+)_/g, (match, p1) => {
      if (p1.startsWith('MATH_PLACEHOLDER_')) return match;
      return `<em>${p1}</em>`;
    });
    return res;
  };

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const trimmed = line.trim();

    // 2b-bis. Gráficas: bloque ```grafica ... ```
    if (!enGrafica && /^```\s*grafica\s*$/.test(trimmed)) {
      flushList();
      flushParagraph();
      enGrafica = true;
      graficaLines = [];
      continue;
    }
    if (enGrafica && trimmed === '```') {
      htmlBlocks.push(renderGrafica(graficaLines.join('\n')));
      enGrafica = false;
      continue;
    }
    if (enGrafica) {
      graficaLines.push(line);
      continue;
    }

    // 2c. Callouts intercalados: :::ejemplo / :::error ... :::
    if (trimmed === ':::ejemplo' || trimmed === ':::error') {
      flushList();
      flushParagraph();
      calloutTipo = trimmed.slice(3);
      calloutLines = [];
      continue;
    }
    if (trimmed === ':::' && calloutTipo) {
      const titulo = calloutTipo === 'ejemplo' ? '📝 Ejemplo resuelto' : '⚠️ Error frecuente';
      const innerHtml = renderMarkdownToHtml(calloutLines.join('\n'));
      htmlBlocks.push(
        `<div class="callout callout-${calloutTipo}"><div class="callout-titulo">${titulo}</div>${innerHtml}</div>`
      );
      calloutTipo = null;
      continue;
    }
    if (calloutTipo) {
      calloutLines.push(line);
      continue;
    }

    // 2c-bis. Citas markdown: bloques de líneas que empiezan por "> "
    if (/^>\s?/.test(trimmed)) {
      flushList();
      flushParagraph();
      const citaLineas: string[] = [];
      let k = i;
      while (k < lines.length && /^>\s?/.test(lines[k].trim())) {
        citaLineas.push(lines[k].trim().replace(/^>\s?/, ''));
        k++;
      }
      const interior = renderMarkdownToHtml(citaLineas.join('\n'));
      htmlBlocks.push(
        `<blockquote style="border-left:4px solid var(--secondary);background:rgba(0,229,255,0.05);margin:12px 0;padding:8px 14px;border-radius:0 8px 8px 0;">${interior}</blockquote>`
      );
      i = k - 1;
      continue;
    }

    // 2d. Tablas markdown: fila de cabecera "| a | b |" seguida de separador "| --- | --- |"
    if (
      trimmed.startsWith('|') && trimmed.endsWith('|') &&
      i + 1 < lines.length && /^\|[\s:|-]+\|$/.test(lines[i + 1].trim())
    ) {
      flushList();
      flushParagraph();
      const parseRow = (l: string) =>
        l.trim().replace(/^\|/, '').replace(/\|$/, '').split('|').map((celda) => renderInlineMarkdown(celda.trim()));
      const cabecera = parseRow(trimmed);
      let j = i + 2;
      const filas: string[][] = [];
      while (j < lines.length && lines[j].trim().startsWith('|') && lines[j].trim().endsWith('|')) {
        filas.push(parseRow(lines[j]));
        j++;
      }
      const th = 'border:1px solid var(--border-color);padding:8px 11px;text-align:left;color:var(--text-primary);background:var(--surface-soft);';
      const td = 'border:1px solid var(--border-color);padding:8px 11px;color:var(--text-primary);vertical-align:top;';
      let tabla = '<div style="overflow-x:auto;margin:12px 0;"><table style="border-collapse:collapse;width:100%;font-size:0.95rem;">';
      tabla += '<thead><tr>' + cabecera.map((h) => `<th style="${th}">${h}</th>`).join('') + '</tr></thead><tbody>';
      for (const fila of filas) {
        tabla += '<tr>' + fila.map((c) => `<td style="${td}">${c}</td>`).join('') + '</tr>';
      }
      tabla += '</tbody></table></div>';
      htmlBlocks.push(tabla);
      i = j - 1;
      continue;
    }

    // 3. Caso especial: Fórmulas en bloque que están solas en su línea
    if (trimmed.startsWith('MATHTKN') && trimmed.endsWith('MATHEND')) {
      const match = trimmed.match(/^MATHTKN(\d+)MATHEND$/);
      if (match) {
        const idx = parseInt(match[1], 10);
        const originalMath = mathPlaceholders[idx];
        if (originalMath && originalMath.startsWith('$$')) {
          flushList();
          flushParagraph();
          htmlBlocks.push(`<div class="math-block">${trimmed}</div>`);
          continue;
        }
      }
    }

    // 4. Encabezados (# a ######)
    const headerMatch = trimmed.match(/^(#{1,6})\s+(.*)$/);
    if (headerMatch) {
      flushList();
      flushParagraph();
      const level = headerMatch[1].length;
      const headerText = renderInlineMarkdown(headerMatch[2].replace(/\s+#+$/, ''));
      const headingId = `hb-${headingCounter++}`;

      let style = 'margin-top: 24px; margin-bottom: 12px; font-weight: 600; color: var(--text-primary); scroll-margin-top: 24px;';
      if (level === 1) style += 'font-size: 1.8rem; border-bottom: 2px solid var(--border-color); padding-bottom: 8px;';
      else if (level === 2) style += 'font-size: 1.5rem; border-bottom: 1px solid var(--border-color); padding-bottom: 6px;';
      else if (level === 3) style += 'font-size: 1.35rem; border-left: 4px solid var(--primary); padding-left: 12px; margin-bottom: 16px;';
      else if (level === 4) style += 'font-size: 1.2rem; border-left: 3px solid var(--secondary); padding-left: 8px;';
      else style += 'font-size: 1.05rem;';

      htmlBlocks.push(`<h${level} id="${headingId}" style="${style}">${headerText}</h${level}>`);
      continue;
    }

    // 5. Listas de viñetas (bullet points)
    const bulletMatch = line.match(/^(\s*)([-*])\s+(.*)$/);
    if (bulletMatch && !trimmed.startsWith('MATHTKN')) {
      flushParagraph();
      if (inList !== 'ul') {
        flushList();
        inList = 'ul';
        htmlBlocks.push('<ul style="margin-bottom: 12px; padding-left: 0;">');
      } else {
        flushListItem();
      }
      currentListItemLines.push(bulletMatch[3]);
      continue;
    }

    // 6. Listas ordenadas
    const numberedMatch = line.match(/^(\s*)(\d+)\.\s+(.*)$/);
    if (numberedMatch) {
      flushParagraph();
      if (inList !== 'ol') {
        flushList();
        inList = 'ol';
        htmlBlocks.push('<ol style="margin-bottom: 12px; padding-left: 0;">');
      } else {
        flushListItem();
      }
      currentListItemLines.push(numberedMatch[3]);
      continue;
    }

    // 7. Líneas vacías
    if (trimmed === '') {
      flushList();
      flushParagraph();
      continue;
    }

    // 8. Líneas de párrafo normales
    if (inList) {
      currentListItemLines.push(trimmed);
    } else {
      paragraphLines.push(trimmed);
    }
  }

  flushList();
  flushParagraph();

  // 9. Restaurar las fórmulas matemáticas originales en el HTML.
  // IMPORTANTE: se usa una FUNCIÓN de reemplazo para que las secuencias "$$"
  // de las fórmulas no se interpreten como patrones especiales de String.replace
  // (que colapsarían "$$" en un solo "$" y romperían las fórmulas de bloque).
  let finalHtml = htmlBlocks.join('\n');
  for (let i = 0; i < mathPlaceholders.length; i++) {
    finalHtml = finalHtml.replaceAll(`MATHTKN${i}MATHEND`, () => mathPlaceholders[i]);
  }

  // 10. Restaurar los conceptos como elementos interactivos (tooltip + acordeón por clic)
  const escaparHtml = (s: string) =>
    s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  for (let i = 0; i < conceptos.length; i++) {
    const { term, def } = conceptos[i];
    const span = `<span class="concepto" tabindex="0" role="button">${escaparHtml(term)}<span class="concepto-tip">${escaparHtml(def)}</span></span>`;
    finalHtml = finalHtml.replaceAll(`CONCEPTTKN${i}CONCEPTEND`, () => span);
  }

  return finalHtml;
}

// Limpia un título de sección para mostrarlo en el submenú (sin marcas markdown).
export function limpiarTitulo(t: string): string {
  return t
    .replace(/\[\[([^\]|]+?)::[^\]]+?\]\]/g, '$1')
    .replace(/\[\[sim:[a-z0-9_]+\]\]/g, '')
    .replace(/\$\$?[^$]*?\$\$?/g, '')
    .replace(/[*_`#]/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}
