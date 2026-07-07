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
  AlertTriangle 
} from 'lucide-react';
import type { ExamenSession, ExamenReport } from './types';

export default function App() {
  const [screen, setScreen] = useState<'DASHBOARD' | 'SIMULATOR' | 'RESULTS'>('DASHBOARD');
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
  
  // Historial e intentos almacenados localmente
  const [historial, setHistorial] = useState<Array<{ tipo: string; nota: number; aprobado: boolean; fecha: string }>>(() => {
    const saved = localStorage.getItem('efa_historial');
    return saved ? JSON.parse(saved) : [
      { tipo: "EIP", nota: 78.5, aprobado: true, fecha: "2026-07-01" },
      { tipo: "EFA Completo", nota: 68.0, aprobado: false, fecha: "2026-07-04" }
    ];
  });

  // Efecto para renderizar KaTeX dinámicamente cada vez que cambia el estado relevante
  useEffect(() => {
    if (typeof (window as any).renderMathInElement === 'function') {
      // Damos un breve timeout para asegurar que el DOM se haya renderizado
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
  }, [screen, selectedQuestionIndex, activeReport]);

  // Manejo del temporizador
  useEffect(() => {
    if (screen === 'SIMULATOR' && timer > 0) {
      timerIntervalRef.current = setInterval(() => {
        setTimer((prev) => {
          if (prev <= 1) {
            clearInterval(timerIntervalRef.current!);
            handleFinalizarExamen(true); // Auto-entrega
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

  // Función para comenzar un examen
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
        throw new Error('No se pudo iniciar el examen. Asegúrate de que el backend de FastAPI esté corriendo en el puerto 8000.');
      }
      
      const data: ExamenSession = await response.json();
      setActiveExam(data);
      setAnswersTest({});
      setAnswersPrac({});
      setSelectedQuestionIndex(0);
      setTimer(1.5 * 60 * 60); // 1 hora y 30 minutos (5400 segundos)
      setScreen('SIMULATOR');
    } catch (err: any) {
      setErrorMsg(err.message || 'Error de conexión');
    } finally {
      setIsSubmitting(false);
    }
  };

  // Función para entregar el examen
  const handleFinalizarExamen = async (autoSubmit = false) => {
    if (!activeExam) return;
    if (!autoSubmit && !window.confirm('¿Estás seguro de que deseas finalizar y calificar el examen?')) return;
    
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
        throw new Error('Error al enviar las respuestas al servidor.');
      }
      
      const report: ExamenReport = await response.json();
      setActiveReport(report);
      
      // Guardar en el historial local
      const nota_final = report.nota_practica_pct !== null 
        ? (report.nota_test_pct + report.nota_practica_pct) / 2 
        : report.nota_test_pct;
        
      const nuevoIntento = {
        tipo: report.tipo_examen,
        nota: Math.round(nota_final * 10) / 10,
        aprobado: report.aprobado_general,
        fecha: new Date().toISOString().split('T')[0]
      };
      
      const nuevoHistorial = [nuevoIntento, ...historial];
      setHistorial(nuevoHistorial);
      localStorage.setItem('efa_historial', JSON.stringify(nuevoHistorial));
      
      setScreen('RESULTS');
    } catch (err: any) {
      setErrorMsg(err.message || 'Error al calificar');
    } finally {
      setIsSubmitting(false);
    }
  };

  // Formato del cronómetro (MM:SS)
  const formatTime = (seconds: number) => {
    const hrs = Math.floor(seconds / 3600);
    const mins = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    
    const displayMins = mins < 10 ? `0${mins}` : mins;
    const displaySecs = secs < 10 ? `0${secs}` : secs;
    
    if (hrs > 0) {
      return `${hrs}:${displayMins}:${displaySecs}`;
    }
    return `${displayMins}:${displaySecs}`;
  };

  // Porcentaje de aciertos históricos en Dashboard
  const calculateGlobalAverage = () => {
    if (historial.length === 0) return 0;
    const total = historial.reduce((acc, curr) => acc + curr.nota, 0);
    return Math.round(total / historial.length);
  };

  // Renderizador principal por pantallas
  return (
    <div className="container fade-in">
      <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '40px', borderBottom: '1px solid var(--border-color)', paddingBottom: '20px' }}>
        <div>
          <h1 style={{ fontSize: '2.2rem', display: 'flex', alignItems: 'center', gap: '12px' }}>
            <span style={{ background: 'linear-gradient(135deg, var(--secondary) 0%, var(--primary) 100%)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>EFA Prep</span>
            <span style={{ fontSize: '1rem', padding: '4px 8px', background: 'rgba(255,255,255,0.06)', borderRadius: '6px', color: 'var(--text-secondary)', fontWeight: 400 }}>Pro 2026</span>
          </h1>
        </div>
        {screen !== 'DASHBOARD' && (
          <button className="btn btn-secondary" onClick={() => setScreen('DASHBOARD')}>
            Volver al Panel
          </button>
        )}
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
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '24px', marginBottom: '40px' }}>
            <div className="card" style={{ display: 'flex', alignItems: 'center', gap: '20px' }}>
              <div style={{ background: 'rgba(138, 43, 226, 0.15)', padding: '16px', borderRadius: '12px' }}>
                <TrendingUp style={{ color: 'var(--primary)', width: '32px', height: '32px' }} />
              </div>
              <div>
                <h3 style={{ fontSize: '1.8rem' }}>{calculateGlobalAverage()}%</h3>
                <p>Media de Preparación</p>
              </div>
            </div>
            
            <div className="card" style={{ display: 'flex', alignItems: 'center', gap: '20px' }}>
              <div style={{ background: 'rgba(0, 229, 255, 0.15)', padding: '16px', borderRadius: '12px' }}>
                <Award style={{ color: 'var(--secondary)', width: '32px', height: '32px' }} />
              </div>
              <div>
                <h3 style={{ fontSize: '1.8rem' }}>{historial.filter(h => h.aprobado).length}</h3>
                <p>Simulaciones Aprobadas</p>
              </div>
            </div>

            <div className="card" style={{ display: 'flex', alignItems: 'center', gap: '20px' }}>
              <div style={{ background: 'rgba(255, 255, 255, 0.05)', padding: '16px', borderRadius: '12px' }}>
                <BookOpen style={{ color: '#fff', width: '32px', height: '32px' }} />
              </div>
              <div>
                <h3 style={{ fontSize: '1.8rem' }}>{historial.length}</h3>
                <p>Exámenes Realizados</p>
              </div>
            </div>
          </div>

          <h2 style={{ marginBottom: '24px', fontSize: '1.5rem', borderLeft: '4px solid var(--primary)', paddingLeft: '12px' }}>
            Iniciar Nueva Simulación Oficial (MiFID II Compliant)
          </h2>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '24px', marginBottom: '40px' }}>
            <div className="card" style={{ display: 'flex', flexDirection: 'column', justifyContent: 'space-between', minHeight: '260px' }}>
              <div>
                <h3 style={{ marginBottom: '8px', color: '#fff', fontSize: '1.3rem' }}>EIP Nivel I</h3>
                <p style={{ marginBottom: '20px' }}>Simulador del examen parcial oficial de acceso nivel I. 40 preguntas tipo test.</p>
                <div style={{ display: 'flex', gap: '16px', color: 'var(--text-secondary)', fontSize: '0.9rem', marginBottom: '20px' }}>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}><Clock size={16} /> 1h 30m</span>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}><BookOpen size={16} /> 40 Preguntas</span>
                </div>
              </div>
              <button className="btn btn-primary" onClick={() => handleStartExam('EIP')} disabled={isSubmitting}>
                <Play size={18} /> Iniciar Simulación
              </button>
            </div>

            <div className="card" style={{ display: 'flex', flexDirection: 'column', justifyContent: 'space-between', minHeight: '260px', border: '1px solid rgba(138, 43, 226, 0.2)' }}>
              <div>
                <h3 style={{ marginBottom: '8px', color: '#fff', fontSize: '1.3rem', display: 'flex', justifyContent: 'space-between' }}>
                  EFA Completo
                  <span style={{ fontSize: '0.75rem', padding: '2px 8px', background: 'var(--primary)', borderRadius: '12px', color: '#fff' }}>Recomendado</span>
                </h3>
                <p style={{ marginBottom: '20px' }}>Examen completo directo EFA. 50 preguntas tipo test más 1 caso de desarrollo financiero práctico.</p>
                <div style={{ display: 'flex', gap: '16px', color: 'var(--text-secondary)', fontSize: '0.9rem', marginBottom: '20px' }}>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}><Clock size={16} /> 2h 30m</span>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}><BookOpen size={16} /> 50 Test + 1 Caso</span>
                </div>
              </div>
              <button className="btn btn-accent" onClick={() => handleStartExam('EFA Completo')} disabled={isSubmitting}>
                <Play size={18} /> Iniciar Simulación
              </button>
            </div>

            <div className="card" style={{ display: 'flex', flexDirection: 'column', justifyContent: 'space-between', minHeight: '260px' }}>
              <div>
                <h3 style={{ marginBottom: '8px', color: '#fff', fontSize: '1.3rem' }}>EFA Nivel II</h3>
                <p style={{ marginBottom: '20px' }}>Examen de Nivel II para candidatos con el nivel I superado. 40 preguntas tipo test más 1 caso práctico.</p>
                <div style={{ display: 'flex', gap: '16px', color: 'var(--text-secondary)', fontSize: '0.9rem', marginBottom: '20px' }}>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}><Clock size={16} /> 2h 30m</span>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}><BookOpen size={16} /> 40 Test + 1 Caso</span>
                </div>
              </div>
              <button className="btn btn-primary" onClick={() => handleStartExam('EFA Nivel II')} disabled={isSubmitting}>
                <Play size={18} /> Iniciar Simulación
              </button>
            </div>
          </div>

          <h2 style={{ marginBottom: '24px', fontSize: '1.5rem', borderLeft: '4px solid var(--secondary)', paddingLeft: '12px' }}>
            Historial de Intentos Recientes
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
                {historial.map((h, i) => (
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
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* PANTALLA: SIMULADOR */}
      {screen === 'SIMULATOR' && activeExam && (
        <div style={{ display: 'grid', gridTemplateColumns: '300px 1fr', gap: '32px' }}>
          
          {/* Navegador lateral */}
          <aside className="card" style={{ padding: '20px', height: 'fit-content' }}>
            <div style={{ display: 'flex', justifySelf: 'center', alignItems: 'center', gap: '8px', marginBottom: '24px', background: 'rgba(255,255,255,0.04)', padding: '10px 16px', borderRadius: '12px', width: '100%', justifyContent: 'center' }}>
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

          {/* Área de Pregunta */}
          <main className="card" style={{ minHeight: '400px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
            {selectedQuestionIndex < activeExam.preguntas_test.length ? (
              // Pregunta de Test
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
              // Pregunta Práctica
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
                      Tu respuesta (Redacta las fórmulas, el desglose de cálculo paso a paso y la argumentación cualitativa):
                    </label>
                    <textarea
                      rows={12}
                      value={answersPrac[activeExam.pregunta_practica.id] || ''}
                      onChange={(e) => setAnswersPrac(prev => ({ ...prev, [activeExam.pregunta_practica!.id]: e.target.value }))}
                      placeholder="Escribe aquí tu desglose aritmético y justificación cualitativa..."
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

            {/* Controles de Navegación */}
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
          
          {/* Ficha Resumen */}
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

          {/* Detalle Práctica */}
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

          {/* Detalle de Preguntas de Test */}
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
