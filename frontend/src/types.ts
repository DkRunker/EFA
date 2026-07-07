export interface PreguntaTest {
  id: number;
  modulo: string;
  tipo: string;
  enunciado: string;
  opciones: string[];
}

export interface PreguntaPractica {
  id: number;
  modulo: string;
  tipo: string;
  enunciado: string;
}

export interface ExamenSession {
  session_id: string;
  tipo_examen: string;
  preguntas_test: PreguntaTest[];
  incluye_practica: boolean;
  pregunta_practica: PreguntaPractica | null;
}

export interface DesgloseTestItem {
  id: number;
  modulo: string;
  enunciado: string;
  opciones: string[];
  respuesta_alumno: number | null;
  respuesta_correcta: number;
  es_correcta: boolean;
  explicacion: string;
}

export interface EvaluacionReporte {
  score: number;
  aprobado: boolean;
  comentario_cualitativo: string;
  puntos_cumplidos: string[];
  puntos_fallidos: string[];
  es_evaluacion_ia: boolean;
}

export interface ExamenReport {
  tipo_examen: string;
  nota_test_pct: number;
  aciertos_test: number;
  total_test: number;
  aprobado_test: boolean;
  nota_practica_pct: number | null;
  aprobado_practica: boolean | null;
  aprobado_general: boolean;
  evaluacion_practica: EvaluacionReporte | null;
  desglose_test: DesgloseTestItem[];
}
