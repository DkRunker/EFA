import { useState, useEffect, useRef } from 'react';
import { 
  Play, 
  Award, 
  BookOpen, 
  Clock, 
  ArrowRight, 
  ArrowLeft, 
  Send, 
  CheckCircle, 
  XCircle, 
  TrendingUp, 
  AlertTriangle,
  User,
  Lock,
  BookOpen as BookIcon,
  Calculator,
  LogOut
} from 'lucide-react';
import type { ExamenSession, ExamenReport } from './types';
import FormulaSimulator, { FORMULAS, FORMULA_KEYS } from './FormulaSimulator';

function renderMarkdownToHtml(markdown: string): string {
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
      const th = 'border:1px solid var(--border-color);padding:8px 11px;text-align:left;color:#fff;background:rgba(255,255,255,0.05);';
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

      let style = 'margin-top: 24px; margin-bottom: 12px; font-weight: 600; color: #fff; scroll-margin-top: 24px;';
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
function limpiarTitulo(t: string): string {
  return t
    .replace(/\[\[([^\]|]+?)::[^\]]+?\]\]/g, '$1')
    .replace(/\[\[sim:[a-z0-9_]+\]\]/g, '')
    .replace(/\$\$?[^$]*?\$\$?/g, '')
    .replace(/[*_`#]/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

// Tipos de la teoría estructurada por secciones.
interface Ejercicio {
  enunciado: string;
  tipo?: 'numerico' | 'opcion';
  formula?: string;
  valor_esperado?: number;
  tolerancia?: number;
  opciones?: string[];
  correcta?: number;
  explicacion: string;
}
interface Seccion {
  titulo: string;
  cuerpo: string;
  ejercicios: Ejercicio[];
}

// Renderiza el cuerpo de una sección troceándolo en los marcadores [[sim:clave]],
// intercalando bloques de markdown con el simulador de la fórmula correspondiente.
function SeccionCuerpo({ cuerpo }: { cuerpo: string }) {
  const partes = cuerpo.split(/\[\[sim:([a-z0-9_]+)\]\]/);
  return (
    <>
      {partes.map((parte, i) => {
        if (i % 2 === 1) {
          // clave de fórmula capturada
          return FORMULAS[parte] ? <FormulaSimulator key={i} formula={parte} compact /> : null;
        }
        if (!parte.trim()) return null;
        return <div key={i} dangerouslySetInnerHTML={{ __html: renderMarkdownToHtml(parte) }} />;
      })}
    </>
  );
}

// Widget interactivo de un ejercicio: el alumno responde, comprueba y ve la
// solución correcta con la explicación del proceso.
function EjercicioWidget({ ej, n }: { ej: Ejercicio; n: number }) {
  const [valor, setValor] = useState('');
  const [seleccion, setSeleccion] = useState<number | null>(null);
  const [revelado, setRevelado] = useState(false);
  const esNumerico = ej.tipo !== 'opcion';

  let acierto = false;
  if (revelado) {
    if (esNumerico) {
      const num = parseFloat(String(valor).replace(',', '.'));
      acierto = !isNaN(num) && Math.abs(num - (ej.valor_esperado ?? NaN)) <= (ej.tolerancia ?? 0.01);
    } else {
      acierto = seleccion === ej.correcta;
    }
  }
  const solucionTexto = esNumerico
    ? String(ej.valor_esperado)
    : (ej.opciones && ej.correcta != null ? ej.opciones[ej.correcta] : '');

  return (
    <div className="ejercicio">
      <div className="ejercicio-enunciado">
        <strong>Ejercicio {n}. </strong>
        <span dangerouslySetInnerHTML={{ __html: renderMarkdownToHtml(ej.enunciado) }} />
      </div>
      {esNumerico ? (
        <input
          type="text"
          value={valor}
          onChange={(e) => setValor(e.target.value)}
          placeholder="Escribe tu resultado"
          style={{ width: '100%', background: 'rgba(0,0,0,0.3)', border: '1px solid var(--border-color)', padding: '8px 10px', borderRadius: '8px', color: '#fff' }}
        />
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
          {(ej.opciones ?? []).map((op, i) => (
            <label key={i} style={{ display: 'flex', gap: '8px', alignItems: 'center', color: 'var(--text-primary)', cursor: 'pointer' }}>
              <input type="radio" name={`ej-${n}`} checked={seleccion === i} onChange={() => setSeleccion(i)} />
              <span>{op}</span>
            </label>
          ))}
        </div>
      )}
      <button className="btn btn-secondary" style={{ marginTop: '10px', width: 'fit-content' }} onClick={() => setRevelado(true)}>
        Comprobar
      </button>
      {revelado && (
        <div className="ejercicio-solucion">
          <div className={acierto ? 'ejercicio-ok' : 'ejercicio-ko'}>
            {acierto ? '✓ ¡Correcto!' : '✗ Revisa la solución'}
          </div>
          <div style={{ marginTop: '4px' }}><strong>Solución:</strong> {solucionTexto}</div>
          <div style={{ marginTop: '6px' }} dangerouslySetInnerHTML={{ __html: renderMarkdownToHtml(ej.explicacion) }} />
        </div>
      )}
    </div>
  );
}

export default function App() {
  // Autenticación
  const [currentUser, setCurrentUser] = useState<string | null>(null);
  const [authMode, setAuthMode] = useState<'LOGIN' | 'REGISTER'>('LOGIN');
  const [authUsername, setAuthUsername] = useState<string>('');
  const [authPassword, setAuthPassword] = useState<string>('');
  const [authSuccessMsg, setAuthSuccessMsg] = useState<string>('');

  // Navegación principal
  const [screen, setScreen] = useState<'DASHBOARD' | 'SIMULATOR' | 'RESULTS' | 'STUDY'>('DASHBOARD');
  
  // Examen activo
  const [activeExam, setActiveExam] = useState<ExamenSession | null>(null);
  const [answersTest, setAnswersTest] = useState<Record<number, number>>({});
  const [answersPrac, setAnswersPrac] = useState<Record<number, string>>({});
  
  // Temporizador
  const [timer, setTimer] = useState<number>(0);
  const timerIntervalRef = useRef<any>(null);
  
  const [selectedQuestionIndex, setSelectedQuestionIndex] = useState<number>(0);
  const [isSubmitting, setIsSubmitting] = useState<boolean>(false);
  const [activeReport, setActiveReport] = useState<ExamenReport | null>(null);
  const [errorMsg, setErrorMsg] = useState<string>('');

  // Sandbox de Estudio
  const [selectedFormula, setSelectedFormula] = useState<string>('gordon_shapiro');

  // Nuevas variables para apuntes de estudio
  const [studySubTab, setStudySubTab] = useState<'SANDBOX' | 'APUNTES'>('SANDBOX');
  const [selectedApunteModulo, setSelectedApunteModulo] = useState<string>('M1');
  const [seccionesData, setSeccionesData] = useState<{ intro: string; secciones: Seccion[] }>({ intro: '', secciones: [] });

  // Historial e intentos
  const [historial, setHistorial] = useState<Array<{ usuario: string; tipo: string; nota: number; aprobado: boolean; fecha: string }>>(() => {
    const saved = localStorage.getItem('efa_historial_v2');
    return saved ? JSON.parse(saved) : [
      { usuario: "simulado", tipo: "EIP", nota: 78.5, aprobado: true, fecha: "2026-07-01" },
      { usuario: "simulado", tipo: "EFA Completo", nota: 68.0, aprobado: false, fecha: "2026-07-04" }
    ];
  });

  // Efecto KaTeX
  useEffect(() => {
    if (typeof (window as any).renderMathInElement === 'function') {
      const t = setTimeout(() => {
        (window as any).renderMathInElement(document.body, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false },
            { left: '\\(', right: '\\)', display: false },
            { left: '\\[', right: '\\]', display: true }
          ],
          throwOnError: false
        });
      }, 50);
      return () => clearTimeout(t);
    }
  }, [screen, selectedQuestionIndex, activeReport, selectedFormula, currentUser, studySubTab, selectedApunteModulo, seccionesData]);

  // Efecto para cargar la teoría estructurada por secciones
  useEffect(() => {
    if (screen === 'STUDY' && studySubTab === 'APUNTES') {
      setErrorMsg('');
      fetch(`http://localhost:8000/api/study/secciones/${selectedApunteModulo}`)
        .then(res => {
          if (!res.ok) throw new Error('No se pudo cargar la teoría.');
          return res.json();
        })
        .then(data => {
          setSeccionesData({ intro: data.intro, secciones: data.secciones });
        })
        .catch(err => {
          setErrorMsg(err.message || 'Error de conexión');
        });
    }
  }, [screen, studySubTab, selectedApunteModulo]);

  // Secciones del módulo actual (para el submenú lateral) y navegación por scroll
  const seccionesApuntes = seccionesData.secciones.map((s, i) => ({ id: `sec-${i}`, title: limpiarTitulo(s.titulo) }));
  const irASeccion = (id: string) => {
    document.getElementById(id)?.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

  // Temporizador de Examen
  useEffect(() => {
    if (screen === 'SIMULATOR' && timer > 0) {
      timerIntervalRef.current = setInterval(() => {
        setTimer((prev) => {
          if (prev <= 1) {
            clearInterval(timerIntervalRef.current!);
            handleFinalizarExamen(true);
            return 0;
          }
          return prev - 1;
        });
      }, 1000);
    }
    return () => {
      if (timerIntervalRef.current) clearInterval(timerIntervalRef.current);
    };
  }, [screen, timer]);

  // Auth Handler
  const handleAuthSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setErrorMsg('');
    setAuthSuccessMsg('');
    setIsSubmitting(true);
    
    const endpoint = authMode === 'REGISTER' ? 'register' : 'login';
    try {
      const response = await fetch(`http://localhost:8000/api/auth/${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: authUsername, password: authPassword })
      });
      
      if (!response.ok) {
        const errData = await response.json();
        throw new Error(errData.detail || 'Error en la autenticación.');
      }
      
      const data = await response.json();
      
      if (authMode === 'REGISTER') {
        setAuthSuccessMsg('¡Usuario registrado con éxito! Ahora puedes iniciar sesión.');
        setAuthMode('LOGIN');
        setAuthPassword('');
      } else {
        setCurrentUser(data.username);
        setScreen('DASHBOARD');
      }
    } catch (err: any) {
      setErrorMsg(err.message || 'Error de conexión');
    } finally {
      setIsSubmitting(false);
    }
  };

  // Logout
  const handleLogout = () => {
    setCurrentUser(null);
    setScreen('DASHBOARD');
    setAuthUsername('');
    setAuthPassword('');
    setAuthSuccessMsg('');
  };

  // Comienza examen
  const handleStartExam = async (tipo: string) => {
    setErrorMsg('');
    setIsSubmitting(true);
    try {
      const response = await fetch('http://localhost:8000/api/exams/start', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ tipo_examen: tipo })
      });
      
      if (!response.ok) {
        throw new Error('No se pudo iniciar el examen. Verifica el backend.');
      }
      
      const data: ExamenSession = await response.json();
      setActiveExam(data);
      setAnswersTest({});
      setAnswersPrac({});
      setSelectedQuestionIndex(0);
      setTimer(1.5 * 60 * 60);
      setScreen('SIMULATOR');
    } catch (err: any) {
      setErrorMsg(err.message || 'Error de conexión');
    } finally {
      setIsSubmitting(false);
    }
  };

  // Finaliza examen
  const handleFinalizarExamen = async (autoSubmit = false) => {
    if (!activeExam) return;
    if (!autoSubmit && !window.confirm('¿Deseas finalizar y calificar el examen?')) return;
    
    setIsSubmitting(true);
    setErrorMsg('');
    
    try {
      const response = await fetch('http://localhost:8000/api/exams/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          session_id: activeExam.session_id,
          respuestas_test: answersTest,
          respuestas_practica: answersPrac
        })
      });
      
      if (!response.ok) {
        throw new Error('Error al enviar las respuestas.');
      }
      
      const report: ExamenReport = await response.json();
      setActiveReport(report);
      
      const nota_final = report.nota_practica_pct !== null 
        ? (report.nota_test_pct + report.nota_practica_pct) / 2 
        : report.nota_test_pct;
        
      const nuevoIntento = {
        usuario: currentUser || 'Anónimo',
        tipo: report.tipo_examen,
        nota: Math.round(nota_final * 10) / 10,
        aprobado: report.aprobado_general,
        fecha: new Date().toISOString().split('T')[0]
      };
      
      const nuevoHistorial = [nuevoIntento, ...historial];
      setHistorial(nuevoHistorial);
      localStorage.setItem('efa_historial_v2', JSON.stringify(nuevoHistorial));
      
      setScreen('RESULTS');
    } catch (err: any) {
      setErrorMsg(err.message || 'Error al calificar');
    } finally {
      setIsSubmitting(false);
    }
  };


  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins < 10 ? '0' : ''}${mins}:${secs < 10 ? '0' : ''}${secs}`;
  };

  const currentHistorial = historial.filter(h => h.usuario === currentUser);
  const averageScore = currentHistorial.length > 0 
    ? Math.round(currentHistorial.reduce((acc, curr) => acc + curr.nota, 0) / currentHistorial.length) 
    : 0;

  // Si no está autenticado, forzar pantalla de AUTH
  if (!currentUser) {
    return (
      <div className="container fade-in" style={{ maxWidth: '480px', marginTop: '80px' }}>
        <div className="card" style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
          <div style={{ textAlign: 'center' }}>
            <h1 style={{ fontSize: '2rem', background: 'linear-gradient(135deg, var(--secondary) 0%, var(--primary) 100%)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent', display: 'inline-block', marginBottom: '8px' }}>
              EFA Prep Platform
            </h1>
            <p>Accede a tu simulador inteligente oficial</p>
          </div>

          {authSuccessMsg && (
            <div style={{ background: 'rgba(16, 185, 129, 0.15)', border: '1px solid var(--success)', padding: '12px', borderRadius: '8px', color: '#8dfcb9', fontSize: '0.9rem' }}>
              {authSuccessMsg}
            </div>
          )}

          {errorMsg && (
            <div style={{ background: 'rgba(239, 68, 68, 0.15)', border: '1px solid var(--error)', padding: '12px', borderRadius: '8px', color: '#ff8a8a', fontSize: '0.9rem' }}>
              {errorMsg}
            </div>
          )}

          <form onSubmit={handleAuthSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            <div>
              <label style={{ display: 'block', marginBottom: '6px', fontSize: '0.9rem', color: 'var(--text-secondary)' }}>Usuario</label>
              <div style={{ position: 'relative' }}>
                <User size={18} style={{ position: 'absolute', left: '12px', top: '12px', color: 'var(--text-muted)' }} />
                <input
                  type="text"
                  required
                  value={authUsername}
                  onChange={(e) => setAuthUsername(e.target.value)}
                  placeholder="Introduce tu usuario"
                  style={{ width: '100%', padding: '10px 12px 10px 40px', background: 'rgba(0,0,0,0.2)', border: '1px solid var(--border-color)', borderRadius: '8px', color: '#fff' }}
                />
              </div>
            </div>

            <div>
              <label style={{ display: 'block', marginBottom: '6px', fontSize: '0.9rem', color: 'var(--text-secondary)' }}>Contraseña</label>
              <div style={{ position: 'relative' }}>
                <Lock size={18} style={{ position: 'absolute', left: '12px', top: '12px', color: 'var(--text-muted)' }} />
                <input
                  type="password"
                  required
                  value={authPassword}
                  onChange={(e) => setAuthPassword(e.target.value)}
                  placeholder="Introduce tu contraseña"
                  style={{ width: '100%', padding: '10px 12px 10px 40px', background: 'rgba(0,0,0,0.2)', border: '1px solid var(--border-color)', borderRadius: '8px', color: '#fff' }}
                />
              </div>
            </div>

            <button type="submit" className="btn btn-primary" style={{ width: '100%', marginTop: '8px' }} disabled={isSubmitting}>
              {authMode === 'LOGIN' ? 'Iniciar Sesión' : 'Registrarse'}
            </button>
          </form>

          <div style={{ textAlign: 'center', borderTop: '1px solid var(--border-color)', paddingTop: '16px' }}>
            <button 
              style={{ background: 'none', border: 'none', color: 'var(--secondary)', cursor: 'pointer', fontSize: '0.9rem' }}
              onClick={() => {
                setAuthMode(authMode === 'LOGIN' ? 'REGISTER' : 'LOGIN');
                setErrorMsg('');
                setAuthSuccessMsg('');
              }}
            >
              {authMode === 'LOGIN' ? '¿No tienes cuenta? Regístrate aquí' : '¿Ya tienes cuenta? Inicia sesión'}
            </button>
          </div>
        </div>
      </div>
    );
  }

  // APP CON LOGIN ACTIVO
  return (
    <div className="container fade-in">
      <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '40px', borderBottom: '1px solid var(--border-color)', paddingBottom: '20px', flexWrap: 'wrap', gap: '16px' }}>
        <div>
          <h1 style={{ fontSize: '2rem', display: 'flex', alignItems: 'center', gap: '12px' }}>
            <span style={{ background: 'linear-gradient(135deg, var(--secondary) 0%, var(--primary) 100%)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>EFA Prep</span>
            <span style={{ fontSize: '0.85rem', padding: '2px 8px', background: 'var(--primary)', borderRadius: '12px', color: '#fff' }}>Estudiante</span>
          </h1>
        </div>
        
        <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--text-secondary)' }}>
            <User size={16} />
            <span style={{ fontWeight: 500, color: '#fff' }}>{currentUser}</span>
          </div>

          {screen !== 'DASHBOARD' && (
            <button className="btn btn-secondary" style={{ padding: '8px 16px', fontSize: '0.9rem' }} onClick={() => setScreen('DASHBOARD')}>
              Volver al Panel
            </button>
          )}

          <button className="btn btn-danger" style={{ padding: '8px 12px', background: 'rgba(239, 68, 68, 0.1)', border: '1px solid var(--error)', color: 'var(--error)' }} onClick={handleLogout}>
            <LogOut size={16} />
          </button>
        </div>
      </header>

      {errorMsg && (
        <div style={{ background: 'rgba(239, 68, 68, 0.15)', border: '1px solid var(--error)', padding: '16px', borderRadius: '12px', marginBottom: '24px', display: 'flex', gap: '12px', alignItems: 'center', color: '#ff8a8a' }}>
          <AlertTriangle />
          <p style={{ color: '#ff8a8a', fontWeight: 500 }}>{errorMsg}</p>
        </div>
      )}

      {/* PANTALLA: DASHBOARD */}
      {screen === 'DASHBOARD' && (
        <div>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '24px', marginBottom: '40px' }}>
            <div className="card" style={{ display: 'flex', alignItems: 'center', gap: '20px' }}>
              <div style={{ background: 'rgba(138, 43, 226, 0.15)', padding: '16px', borderRadius: '12px' }}>
                <TrendingUp style={{ color: 'var(--primary)', width: '32px', height: '32px' }} />
              </div>
              <div>
                <h3 style={{ fontSize: '1.8rem' }}>{averageScore}%</h3>
                <p>Media de Preparación</p>
              </div>
            </div>
            
            <div className="card" style={{ display: 'flex', alignItems: 'center', gap: '20px' }}>
              <div style={{ background: 'rgba(0, 229, 255, 0.15)', padding: '16px', borderRadius: '12px' }}>
                <Award style={{ color: 'var(--secondary)', width: '32px', height: '32px' }} />
              </div>
              <div>
                <h3 style={{ fontSize: '1.8rem' }}>{currentHistorial.filter(h => h.aprobado).length}</h3>
                <p>Simulaciones Aprobadas</p>
              </div>
            </div>

            <div className="card" style={{ display: 'flex', alignItems: 'center', gap: '20px' }}>
              <div style={{ background: 'rgba(255, 255, 255, 0.05)', padding: '16px', borderRadius: '12px' }}>
                <BookOpen style={{ color: '#fff', width: '32px', height: '32px' }} />
              </div>
              <div>
                <h3 style={{ fontSize: '1.8rem' }}>{currentHistorial.length}</h3>
                <p>Exámenes Realizados</p>
              </div>
            </div>
          </div>

          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '24px' }}>
            <h2 style={{ fontSize: '1.5rem', borderLeft: '4px solid var(--primary)', paddingLeft: '12px' }}>
              Actividades Académicas Disponibles
            </h2>
            <button className="btn btn-accent" onClick={() => setScreen('STUDY')}>
              <Calculator size={18} /> Sandbox de Estudio
            </button>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '24px', marginBottom: '40px' }}>
            <div className="card" style={{ display: 'flex', flexDirection: 'column', justifyContent: 'space-between', minHeight: '260px' }}>
              <div>
                <h3 style={{ marginBottom: '8px', color: '#fff', fontSize: '1.3rem' }}>EIP Nivel I</h3>
                <p style={{ marginBottom: '20px' }}>Simulación del examen oficial de acceso nivel I. 40 preguntas tipo test.</p>
                <div style={{ display: 'flex', gap: '16px', color: 'var(--text-secondary)', fontSize: '0.9rem', marginBottom: '20px' }}>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}><Clock size={16} /> 1h 30m</span>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}><BookIcon size={16} /> 40 Preguntas</span>
                </div>
              </div>
              <button className="btn btn-primary" onClick={() => handleStartExam('EIP')} disabled={isSubmitting}>
                <Play size={18} /> Iniciar Test
              </button>
            </div>

            <div className="card" style={{ display: 'flex', flexDirection: 'column', justifyContent: 'space-between', minHeight: '260px', border: '1px solid rgba(138, 43, 226, 0.2)' }}>
              <div>
                <h3 style={{ marginBottom: '8px', color: '#fff', fontSize: '1.3rem', display: 'flex', justifyContent: 'space-between' }}>
                  EFA Completo
                  <span style={{ fontSize: '0.75rem', padding: '2px 8px', background: 'var(--primary)', borderRadius: '12px', color: '#fff' }}>Oficial</span>
                </h3>
                <p style={{ marginBottom: '20px' }}>Examen de certificación directa EFA. 50 preguntas tipo test y 1 caso práctico de desarrollo fiscal/financiero.</p>
                <div style={{ display: 'flex', gap: '16px', color: 'var(--text-secondary)', fontSize: '0.9rem', marginBottom: '20px' }}>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}><Clock size={16} /> 2h 30m</span>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}><BookIcon size={16} /> 50 Test + 1 Caso</span>
                </div>
              </div>
              <button className="btn btn-accent" onClick={() => handleStartExam('EFA Completo')} disabled={isSubmitting}>
                <Play size={18} /> Iniciar Examen
              </button>
            </div>

            <div className="card" style={{ display: 'flex', flexDirection: 'column', justifyContent: 'space-between', minHeight: '260px' }}>
              <div>
                <h3 style={{ marginBottom: '8px', color: '#fff', fontSize: '1.3rem' }}>EFA Nivel II</h3>
                <p style={{ marginBottom: '20px' }}>Simulador del examen Nivel II. 40 preguntas tipo test y 1 caso práctico.</p>
                <div style={{ display: 'flex', gap: '16px', color: 'var(--text-secondary)', fontSize: '0.9rem', marginBottom: '20px' }}>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}><Clock size={16} /> 2h 30m</span>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}><BookIcon size={16} /> 40 Test + 1 Caso</span>
                </div>
              </div>
              <button className="btn btn-primary" onClick={() => handleStartExam('EFA Nivel II')} disabled={isSubmitting}>
                <Play size={18} /> Iniciar Nivel II
              </button>
            </div>
          </div>

          <h2 style={{ marginBottom: '24px', fontSize: '1.5rem', borderLeft: '4px solid var(--secondary)', paddingLeft: '12px' }}>
            Tus Intentos Recientes
          </h2>
          <div className="card" style={{ padding: '0px', overflow: 'hidden' }}>
            <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
              <thead>
                <tr style={{ borderBottom: '1px solid var(--border-color)', background: 'rgba(255,255,255,0.02)' }}>
                  <th style={{ padding: '16px' }}>Examen</th>
                  <th style={{ padding: '16px' }}>Fecha</th>
                  <th style={{ padding: '16px' }}>Nota Promedio</th>
                  <th style={{ padding: '16px' }}>Estado</th>
                </tr>
              </thead>
              <tbody>
                {currentHistorial.length === 0 ? (
                  <tr>
                    <td colSpan={4} style={{ padding: '24px', textAlign: 'center', color: 'var(--text-secondary)' }}>
                      No tienes intentos registrados aún. ¡Comienza a estudiar o realiza un examen!
                    </td>
                  </tr>
                ) : (
                  currentHistorial.map((h, i) => (
                    <tr key={i} style={{ borderBottom: '1px solid var(--border-color)' }}>
                      <td style={{ padding: '16px', fontWeight: 500, color: '#fff' }}>{h.tipo}</td>
                      <td style={{ padding: '16px', color: 'var(--text-secondary)' }}>{h.fecha}</td>
                      <td style={{ padding: '16px', fontWeight: 600, color: h.aprobado ? 'var(--success)' : 'var(--error)' }}>
                        {h.nota}%
                      </td>
                      <td style={{ padding: '16px' }}>
                        <span style={{ 
                          padding: '4px 10px', 
                          borderRadius: '20px', 
                          fontSize: '0.8rem', 
                          fontWeight: 600,
                          background: h.aprobado ? 'rgba(16, 185, 129, 0.15)' : 'rgba(239, 68, 68, 0.15)',
                          color: h.aprobado ? 'var(--success)' : 'var(--error)',
                          border: `1px solid ${h.aprobado ? 'var(--success)' : 'var(--error)'}`
                        }}>
                          {h.aprobado ? 'APROBADO' : 'SUSPENDIDO'}
                        </span>
                      </td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* PANTALLA: SANDBOX DE ESTUDIO */}
      {screen === 'STUDY' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
          
          {/* Sub-navegación dentro de estudio */}
          <div style={{ display: 'flex', gap: '12px', borderBottom: '1px solid var(--border-color)', paddingBottom: '12px' }}>
            <button 
              className={`btn ${studySubTab === 'SANDBOX' ? 'btn-primary' : 'btn-secondary'}`}
              onClick={() => setStudySubTab('SANDBOX')}
              style={{ padding: '8px 16px', fontSize: '0.95rem' }}
            >
              <Calculator size={16} /> Calculadora Sandbox
            </button>
            <button 
              className={`btn ${studySubTab === 'APUNTES' ? 'btn-primary' : 'btn-secondary'}`}
              onClick={() => setStudySubTab('APUNTES')}
              style={{ padding: '8px 16px', fontSize: '0.95rem' }}
            >
              <BookOpen size={16} /> Temarios y Apuntes Oficiales
            </button>
          </div>

          {studySubTab === 'SANDBOX' ? (
            /* CALCULADORA SANDBOX */
            <div className="card" style={{ display: 'flex', flexDirection: 'column', gap: '16px', maxWidth: '760px' }}>
              <h3 style={{ fontSize: '1.4rem', borderLeft: '4px solid var(--secondary)', paddingLeft: '12px' }}>
                Calculadora Sandbox de Fórmulas
              </h3>
              <div>
                <label style={{ display: 'block', marginBottom: '8px', color: 'var(--text-secondary)', fontWeight: 500 }}>
                  Selecciona la fórmula a estudiar
                </label>
                <select
                  value={selectedFormula}
                  onChange={(e) => setSelectedFormula(e.target.value)}
                  style={{ width: '100%', background: 'rgba(0,0,0,0.3)', border: '1px solid var(--border-color)', padding: '12px', borderRadius: '8px', color: '#fff', fontSize: '1rem', outline: 'none' }}
                >
                  {FORMULA_KEYS.map((k) => (
                    <option key={k} value={k}>{FORMULAS[k].label}</option>
                  ))}
                </select>
              </div>

              <FormulaSimulator key={selectedFormula} formula={selectedFormula} />

              <button className="btn btn-secondary" style={{ width: 'fit-content' }} onClick={() => setScreen('DASHBOARD')}>
                Volver al Dashboard
              </button>
            </div>
          ) : (
            /* APUNTES TEÓRICOS */
            <div style={{ display: 'grid', gridTemplateColumns: '300px 1fr', gap: '32px', alignItems: 'start' }}>
              {/* Selector de módulo con submenú de secciones */}
              <aside className="card" style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '6px', position: 'sticky', top: '24px', maxHeight: 'calc(100vh - 48px)', overflowY: 'auto' }}>
                <h4 style={{ marginBottom: '12px', fontSize: '0.9rem', textTransform: 'uppercase', color: 'var(--text-secondary)', letterSpacing: '0.05em' }}>Módulos del Temario</h4>
                {Array.from({ length: 10 }).map((_, idx) => {
                  const mId = `M${idx + 1}`;
                  const activo = selectedApunteModulo === mId;
                  return (
                    <div key={mId}>
                      <button
                        onClick={() => setSelectedApunteModulo(mId)}
                        style={{
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'space-between',
                          width: '100%',
                          padding: '12px 16px',
                          borderRadius: '8px',
                          border: activo ? '1px solid var(--secondary)' : '1px solid var(--border-color)',
                          background: activo ? 'rgba(0, 229, 255, 0.08)' : 'rgba(255,255,255,0.02)',
                          color: activo ? '#fff' : 'var(--text-secondary)',
                          cursor: 'pointer',
                          textAlign: 'left',
                          fontSize: '0.95rem',
                          fontWeight: activo ? 600 : 400,
                          transition: 'all 0.15s ease'
                        }}
                      >
                        <span>Tema {idx + 1} ({mId})</span>
                        <span style={{ fontSize: '0.8rem', opacity: activo ? 1 : 0.4 }}>{activo ? '▾' : '→'}</span>
                      </button>
                      {activo && seccionesApuntes.length > 0 && (
                        <ul className="seccion-nav">
                          {seccionesApuntes.map((sec) => (
                            <li key={sec.id}>
                              <button onClick={() => irASeccion(sec.id)}>{sec.title}</button>
                            </li>
                          ))}
                        </ul>
                      )}
                    </div>
                  );
                })}
              </aside>

              {/* Visualizador de apuntes: el panel crece con el contenido y la
                  página hace scroll de forma natural (la barra lateral es sticky).
                  card-static evita el efecto de desplazamiento al pasar el ratón. */}
              <main className="card card-static" style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
                <div style={{ color: 'var(--text-primary)', lineHeight: '1.7', fontSize: '1.05rem' }}>
                  {/* Introducción del módulo */}
                  {seccionesData.intro && (
                    <div dangerouslySetInnerHTML={{ __html: renderMarkdownToHtml(seccionesData.intro) }} />
                  )}
                  {/* Secciones: título con id (para el submenú), cuerpo con simuladores en línea y ejercicios */}
                  {seccionesData.secciones.map((sec, i) => (
                    <section key={i} style={{ marginTop: '8px' }}>
                      <h2 id={`sec-${i}`} style={{ marginTop: '24px', marginBottom: '12px', fontWeight: 600, color: '#fff', fontSize: '1.5rem', borderBottom: '1px solid var(--border-color)', paddingBottom: '6px', scrollMarginTop: '24px' }}>
                        {limpiarTitulo(sec.titulo)}
                      </h2>
                      <SeccionCuerpo cuerpo={sec.cuerpo} />
                      {sec.ejercicios && sec.ejercicios.length > 0 && (
                        <div style={{ marginTop: '16px' }}>
                          <h4 style={{ fontSize: '1.1rem', color: 'var(--secondary)', marginBottom: '8px' }}>✍️ Practica lo aprendido</h4>
                          {sec.ejercicios.map((ej, j) => (
                            <EjercicioWidget key={j} ej={ej} n={j + 1} />
                          ))}
                        </div>
                      )}
                    </section>
                  ))}
                </div>

                <button className="btn btn-secondary" style={{ width: 'fit-content' }} onClick={() => setScreen('DASHBOARD')}>
                  Volver al Dashboard
                </button>
              </main>
            </div>
          )}

        </div>
      )}

      {/* PANTALLA: SIMULADOR */}
      {screen === 'SIMULATOR' && activeExam && (
        <div style={{ display: 'grid', gridTemplateColumns: '300px 1fr', gap: '32px' }}>
          
          <aside className="card" style={{ padding: '20px', height: 'fit-content' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '24px', background: 'rgba(255,255,255,0.04)', padding: '10px 16px', borderRadius: '12px', width: '100%', justifyContent: 'center' }}>
              <Clock style={{ color: 'var(--secondary)' }} />
              <span style={{ fontSize: '1.4rem', fontFamily: 'monospace', fontWeight: 'bold', color: '#fff' }}>
                {formatTime(timer)}
              </span>
            </div>

            <h4 style={{ marginBottom: '16px', fontSize: '0.9rem', textTransform: 'uppercase', color: 'var(--text-secondary)' }}>Preguntas</h4>
            
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: '10px', marginBottom: '24px' }}>
              {activeExam.preguntas_test.map((q, index) => {
                const contestada = answersTest[q.id] !== undefined;
                const activa = index === selectedQuestionIndex;
                return (
                  <button
                    key={q.id}
                    onClick={() => setSelectedQuestionIndex(index)}
                    style={{
                      height: '40px',
                      borderRadius: '8px',
                      border: activa ? '2px solid var(--secondary)' : '1px solid var(--border-color)',
                      background: activa 
                        ? 'rgba(0, 229, 255, 0.1)' 
                        : contestada ? 'var(--primary)' : 'rgba(255,255,255,0.03)',
                      color: activa || contestada ? '#fff' : 'var(--text-secondary)',
                      cursor: 'pointer',
                      fontWeight: 'bold',
                      transition: 'all 0.15s ease'
                    }}
                  >
                    {index + 1}
                  </button>
                );
              })}
              
              {activeExam.pregunta_practica && (
                <button
                  onClick={() => setSelectedQuestionIndex(activeExam.preguntas_test.length)}
                  style={{
                    gridColumn: 'span 5',
                    height: '40px',
                    borderRadius: '8px',
                    border: selectedQuestionIndex === activeExam.preguntas_test.length ? '2px solid var(--secondary)' : '1px solid var(--border-color)',
                    background: selectedQuestionIndex === activeExam.preguntas_test.length
                      ? 'rgba(0, 229, 255, 0.1)'
                      : answersPrac[activeExam.pregunta_practica.id] ? 'var(--success)' : 'rgba(255,255,255,0.03)',
                    color: '#fff',
                    cursor: 'pointer',
                    fontWeight: 'bold',
                    textTransform: 'uppercase',
                    fontSize: '0.8rem'
                  }}
                >
                  Parte II: Caso Práctico
                </button>
              )}
            </div>

            <button className="btn btn-danger" style={{ width: '100%' }} onClick={() => handleFinalizarExamen(false)} disabled={isSubmitting}>
              <Send size={16} /> Entregar Examen
            </button>
          </aside>

          <main className="card" style={{ minHeight: '400px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
            {selectedQuestionIndex < activeExam.preguntas_test.length ? (
              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '16px' }}>
                  <span style={{ fontSize: '0.85rem', color: 'var(--secondary)', textTransform: 'uppercase', fontWeight: 600, letterSpacing: '0.05em' }}>
                    Pregunta {selectedQuestionIndex + 1} de {activeExam.preguntas_test.length}
                  </span>
                  <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>
                    Módulo {activeExam.preguntas_test[selectedQuestionIndex].modulo}
                  </span>
                </div>
                
                <h2 style={{ fontSize: '1.3rem', marginBottom: '24px', lineHeight: '1.6' }}>
                  {activeExam.preguntas_test[selectedQuestionIndex].enunciado}
                </h2>
                
                <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
                  {activeExam.preguntas_test[selectedQuestionIndex].opciones.map((opcion, opIndex) => {
                    const qid = activeExam.preguntas_test[selectedQuestionIndex].id;
                    const selected = answersTest[qid] === opIndex;
                    return (
                      <div 
                        key={opIndex}
                        onClick={() => setAnswersTest(prev => ({ ...prev, [qid]: opIndex }))}
                        style={{
                          display: 'flex',
                          alignItems: 'center',
                          padding: '16px',
                          borderRadius: '12px',
                          border: selected ? '2px solid var(--primary)' : '1px solid var(--border-color)',
                          background: selected ? 'rgba(138, 43, 226, 0.08)' : 'rgba(255,255,255,0.01)',
                          cursor: 'pointer',
                          transition: 'all 0.15s ease'
                        }}
                      >
                        <input
                          type="radio"
                          name={`q-${qid}`}
                          checked={selected}
                          readOnly
                          style={{ marginRight: '16px', accentColor: 'var(--primary)', width: '18px', height: '18px' }}
                        />
                        <span style={{ color: '#fff', fontSize: '1.05rem' }}>{opcion}</span>
                      </div>
                    );
                  })}
                </div>
              </div>
            ) : (
              activeExam.pregunta_practica && (
                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '16px' }}>
                    <span style={{ fontSize: '0.85rem', color: 'var(--success)', textTransform: 'uppercase', fontWeight: 600, letterSpacing: '0.05em' }}>
                      Parte II: Ejercicio Práctico de Desarrollo
                    </span>
                    <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>
                      Módulo {activeExam.pregunta_practica.modulo}
                    </span>
                  </div>

                  <h2 style={{ fontSize: '1.3rem', marginBottom: '24px', lineHeight: '1.6' }}>
                    {activeExam.pregunta_practica.enunciado}
                  </h2>

                  <div style={{ marginBottom: '16px' }}>
                    <label style={{ display: 'block', marginBottom: '8px', color: 'var(--text-secondary)', fontWeight: 500 }}>
                      Tu respuesta razonada:
                    </label>
                    <textarea
                      rows={12}
                      value={answersPrac[activeExam.pregunta_practica.id] || ''}
                      onChange={(e) => setAnswersPrac(prev => ({ ...prev, [activeExam.pregunta_practica!.id]: e.target.value }))}
                      placeholder="Redacta la explicación de variables y muestra las aserciones cuantitativas obtenidas..."
                      style={{
                        width: '100%',
                        background: 'rgba(0,0,0,0.2)',
                        border: '1px solid var(--border-color)',
                        borderRadius: '12px',
                        padding: '16px',
                        color: '#fff',
                        fontFamily: 'inherit',
                        fontSize: '1.05rem',
                        lineHeight: '1.5',
                        resize: 'vertical',
                        outline: 'none'
                      }}
                    />
                  </div>
                </div>
              )
            )}

            <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '32px', borderTop: '1px solid var(--border-color)', paddingTop: '20px' }}>
              <button
                className="btn btn-secondary"
                onClick={() => setSelectedQuestionIndex(prev => Math.max(0, prev - 1))}
                disabled={selectedQuestionIndex === 0}
              >
                <ArrowLeft size={18} /> Anterior
              </button>

              <button
                className="btn btn-primary"
                onClick={() => setSelectedQuestionIndex(prev => {
                  const maxIndex = activeExam.pregunta_practica 
                    ? activeExam.preguntas_test.length 
                    : activeExam.preguntas_test.length - 1;
                  return Math.min(maxIndex, prev + 1);
                })}
                disabled={
                  (activeExam.pregunta_practica && selectedQuestionIndex === activeExam.preguntas_test.length) ||
                  (!activeExam.pregunta_practica && selectedQuestionIndex === activeExam.preguntas_test.length - 1)
                }
              >
                Siguiente <ArrowRight size={18} />
              </button>
            </div>
          </main>
        </div>
      )}

      {/* PANTALLA: RESULTADOS */}
      {screen === 'RESULTS' && activeReport && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '32px' }}>
          
          <div className="card" style={{ 
            borderLeft: `8px solid ${activeReport.aprobado_general ? 'var(--success)' : 'var(--error)'}`,
            background: activeReport.aprobado_general ? 'rgba(16, 185, 129, 0.04)' : 'rgba(239, 68, 68, 0.04)'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '20px' }}>
              <div>
                <span style={{ 
                  fontSize: '0.85rem', 
                  fontWeight: 'bold', 
                  color: activeReport.aprobado_general ? 'var(--success)' : 'var(--error)', 
                  textTransform: 'uppercase',
                  border: `1px solid ${activeReport.aprobado_general ? 'var(--success)' : 'var(--error)'}`,
                  padding: '4px 12px',
                  borderRadius: '20px',
                  display: 'inline-block',
                  marginBottom: '12px'
                }}>
                  {activeReport.aprobado_general ? 'Aprobado General' : 'Suspendido General'}
                </span>
                <h2 style={{ fontSize: '2rem' }}>{activeReport.tipo_examen}</h2>
              </div>
              
              <div style={{ display: 'flex', gap: '32px' }}>
                <div style={{ textAlign: 'center' }}>
                  <h3 style={{ color: activeReport.aprobado_test ? 'var(--success)' : 'var(--error)' }}>
                    {activeReport.nota_test_pct}%
                  </h3>
                  <p style={{ fontSize: '0.9rem' }}>Nota Teórica ({activeReport.aciertos_test}/{activeReport.total_test})</p>
                </div>
                {activeReport.nota_practica_pct !== null && (
                  <div style={{ textAlign: 'center' }}>
                    <h3 style={{ color: activeReport.aprobado_practica ? 'var(--success)' : 'var(--error)' }}>
                      {activeReport.nota_practica_pct}%
                    </h3>
                    <p style={{ fontSize: '0.9rem' }}>Nota Práctica</p>
                  </div>
                )}
              </div>
            </div>
            
            {activeReport.tipo_examen !== 'EIP' && !activeReport.aprobado_general && activeReport.aprobado_test && (
              <div style={{ marginTop: '20px', background: 'rgba(239, 68, 68, 0.1)', border: '1px solid var(--error)', padding: '12px', borderRadius: '8px', color: '#ff8a8a', fontSize: '0.95rem' }}>
                <strong>Aviso:</strong> Aprobaste la parte teórica pero no lograste el aprobado en la parte práctica de desarrollo. Recuerda que el examen EFA real exige aprobar ambas partes de manera independiente.
              </div>
            )}
          </div>

          {activeReport.evaluacion_practica && (
            <div className="card">
              <h3 style={{ fontSize: '1.4rem', marginBottom: '16px', display: 'flex', alignItems: 'center', gap: '10px', color: '#fff' }}>
                <Award /> Evaluación Detallada del Caso Práctico
              </h3>
              
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '24px', marginBottom: '24px' }}>
                <div style={{ background: 'rgba(255,255,255,0.02)', padding: '16px', borderRadius: '12px', border: '1px solid var(--border-color)' }}>
                  <h4 style={{ color: 'var(--secondary)', marginBottom: '8px', fontSize: '0.95rem' }}>Cumplimiento de Rúbrica</h4>
                  <ul style={{ paddingLeft: '20px', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                    {activeReport.evaluacion_practica.puntos_cumplidos.map((p, idx) => (
                      <li key={idx} style={{ color: 'var(--success)', fontSize: '0.95rem' }}>✓ {p}</li>
                    ))}
                    {activeReport.evaluacion_practica.puntos_fallidos.map((p, idx) => (
                      <li key={idx} style={{ color: 'var(--error)', fontSize: '0.95rem' }}>✗ {p}</li>
                    ))}
                  </ul>
                </div>
                
                <div style={{ background: 'rgba(255,255,255,0.02)', padding: '16px', borderRadius: '12px', border: '1px solid var(--border-color)' }}>
                  <h4 style={{ color: 'var(--secondary)', marginBottom: '8px', fontSize: '0.95rem' }}>Dictamen del Tribunal</h4>
                  <p style={{ color: '#fff', lineHeight: '1.6', fontSize: '0.95rem' }}>
                    {activeReport.evaluacion_practica.comentario_cualitativo}
                  </p>
                </div>
              </div>
            </div>
          )}

          <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
            <h3 style={{ fontSize: '1.4rem', borderLeft: '4px solid var(--primary)', paddingLeft: '12px', color: '#fff' }}>
              Desglose de Preguntas Teóricas
            </h3>
            
            {activeReport.desglose_test.map((item, idx) => (
              <div key={item.id} className="card" style={{ borderLeft: `4px solid ${item.es_correcta ? 'var(--success)' : 'var(--error)'}` }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '12px', alignItems: 'center' }}>
                  <span style={{ fontWeight: 'bold', fontSize: '0.9rem', color: 'var(--text-secondary)' }}>
                    Pregunta {idx + 1}
                  </span>
                  <span style={{ 
                    padding: '2px 8px', 
                    borderRadius: '12px', 
                    fontSize: '0.8rem', 
                    background: item.es_correcta ? 'rgba(16, 185, 129, 0.1)' : 'rgba(239, 68, 68, 0.1)',
                    color: item.es_correcta ? 'var(--success)' : 'var(--error)',
                    fontWeight: 600
                  }}>
                    {item.es_correcta ? 'Correcta' : 'Incorrecta'}
                  </span>
                </div>
                
                <h4 style={{ fontSize: '1.15rem', color: '#fff', marginBottom: '16px', lineHeight: '1.5' }}>
                  {item.enunciado}
                </h4>
                
                <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginBottom: '16px' }}>
                  {item.opciones.map((op, opIdx) => {
                    const isCorrect = opIdx === item.respuesta_correcta;
                    const isSelected = opIdx === item.respuesta_alumno;
                    let borderCol = 'var(--border-color)';
                    let bgCol = 'transparent';
                    if (isCorrect) {
                      borderCol = 'var(--success)';
                      bgCol = 'rgba(16, 185, 129, 0.05)';
                    } else if (isSelected && !item.es_correcta) {
                      borderCol = 'var(--error)';
                      bgCol = 'rgba(239, 68, 68, 0.05)';
                    }
                    return (
                      <div key={opIdx} style={{ padding: '12px', borderRadius: '8px', border: `1px solid ${borderCol}`, background: bgCol, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                        <span style={{ color: isCorrect || isSelected ? '#fff' : 'var(--text-secondary)' }}>{op}</span>
                        {isCorrect && <CheckCircle size={18} style={{ color: 'var(--success)' }} />}
                        {isSelected && !item.es_correcta && <XCircle size={18} style={{ color: 'var(--error)' }} />}
                      </div>
                    );
                  })}
                </div>
                
                <div style={{ background: 'rgba(0,0,0,0.15)', padding: '16px', borderRadius: '12px', border: '1px solid var(--border-color)', marginTop: '16px' }}>
                  <h5 style={{ color: 'var(--secondary)', marginBottom: '6px', fontSize: '0.9rem' }}>Explicación:</h5>
                  <p style={{ color: 'var(--text-primary)', fontSize: '0.95rem', lineHeight: '1.6' }}>
                    {item.explicacion}
                  </p>
                </div>
              </div>
            ))}
          </div>

          <button className="btn btn-primary" style={{ width: 'fit-content', alignSelf: 'center', marginTop: '20px' }} onClick={() => setScreen('DASHBOARD')}>
            Volver al Dashboard
          </button>
        </div>
      )}
    </div>
  );
}
