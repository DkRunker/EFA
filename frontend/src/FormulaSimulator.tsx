import { useState } from 'react';

// Configuración declarativa de cada fórmula del simulador.
// Se usa tanto en la pestaña Sandbox como incrustado en la teoría ([[sim:clave]]).

export interface ParamSpec {
  key: string;
  label: string;
  step?: number;
  integer?: boolean;
}

export interface FormulaSpec {
  label: string;
  params: ParamSpec[];
  defaults: Record<string, number>;
  // Devuelve las líneas de resultado a mostrar a partir de la respuesta de la API.
  format: (res: any) => { label: string; value: string }[];
}

const pct = (v: number, d = 4) => `${(v * 100).toFixed(d)} %`;
const eur = (v: number, d = 2) => `${v.toFixed(d)} €`;
const num = (v: number, d = 4) => v.toFixed(d);

export const FORMULAS: Record<string, FormulaSpec> = {
  gordon_shapiro: {
    label: 'Gordon-Shapiro (Precio Teórico de una Acción)',
    params: [
      { key: 'd1', label: 'D₁ — Dividendo esperado (€)', step: 0.01 },
      { key: 'ke', label: 'ke — Rentabilidad exigida (tanto por uno)', step: 0.001 },
      { key: 'g', label: 'g — Tasa de crecimiento (tanto por uno)', step: 0.001 },
    ],
    defaults: { d1: 4.0, ke: 0.12, g: 0.08 },
    format: (r) => [
      { label: 'Denominador (ke − g)', value: pct(r.denominador, 2) },
      { label: 'Precio teórico (P₀)', value: eur(r.precio_teorico) },
    ],
  },
  sharpe: {
    label: 'Ratio de Sharpe (Rentabilidad / Volatilidad)',
    params: [
      { key: 'rp', label: 'Rp — Rentabilidad de la cartera (tanto por uno)', step: 0.001 },
      { key: 'rf', label: 'Rf — Tasa libre de riesgo (tanto por uno)', step: 0.001 },
      { key: 'sigma_p', label: 'σp — Desviación típica / volatilidad (tanto por uno)', step: 0.001 },
    ],
    defaults: { rp: 0.15, rf: 0.03, sigma_p: 0.08 },
    format: (r) => [{ label: 'Ratio de Sharpe', value: num(r.result) }],
  },
  treynor: {
    label: 'Ratio de Treynor (Rentabilidad / Beta)',
    params: [
      { key: 'rp', label: 'Rp — Rentabilidad de la cartera (tanto por uno)', step: 0.001 },
      { key: 'rf', label: 'Rf — Tasa libre de riesgo (tanto por uno)', step: 0.001 },
      { key: 'beta_p', label: 'β — Beta de la cartera', step: 0.01 },
    ],
    defaults: { rp: 0.15, rf: 0.03, beta_p: 1.2 },
    format: (r) => [{ label: 'Ratio de Treynor', value: num(r.result) }],
  },
  jensen: {
    label: 'Alfa de Jensen (frente al CAPM)',
    params: [
      { key: 'rp', label: 'Rp — Rentabilidad de la cartera (tanto por uno)', step: 0.001 },
      { key: 'rf', label: 'Rf — Tasa libre de riesgo (tanto por uno)', step: 0.001 },
      { key: 'beta_p', label: 'β — Beta de la cartera', step: 0.01 },
      { key: 'rm', label: 'Rm — Rentabilidad del mercado (tanto por uno)', step: 0.001 },
    ],
    defaults: { rp: 0.15, rf: 0.03, beta_p: 1.2, rm: 0.10 },
    format: (r) => [{ label: 'Alfa de Jensen', value: pct(r.result) }],
  },
  tae: {
    label: 'Conversión de TIN a TAE (interés compuesto)',
    params: [
      { key: 'tin', label: 'TIN — Tipo de interés nominal (tanto por uno)', step: 0.001 },
      { key: 'm', label: 'm — Nº de liquidaciones al año', step: 1, integer: true },
    ],
    defaults: { tin: 0.06, m: 12 },
    format: (r) => [{ label: 'TAE equivalente', value: pct(r.result) }],
  },
  precio_bono: {
    label: 'Precio de un Bono de Renta Fija',
    params: [
      { key: 'nominal', label: 'Nominal — Valor de reembolso (€)', step: 1 },
      { key: 'cupon_anual_pct', label: 'Cupón anual (tanto por uno, p.ej. 0,05 = 5 %)', step: 0.001 },
      { key: 'n_anos', label: 'n — Años hasta el vencimiento', step: 1, integer: true },
      { key: 'tir', label: 'TIR — Rentabilidad exigida (tanto por uno)', step: 0.001 },
    ],
    defaults: { nominal: 1000.0, cupon_anual_pct: 0.05, n_anos: 3, tir: 0.04 },
    format: (r) => [{ label: 'Precio del bono', value: eur(r.result) }],
  },
  irpf_ahorro: {
    label: 'Escala del Ahorro del IRPF (España)',
    params: [{ key: 'base_liquidable', label: 'Base liquidable del ahorro (€)', step: 1 }],
    defaults: { base_liquidable: 70000.0 },
    format: (r) => [
      { label: 'Cuota total', value: eur(r.cuota_total) },
      ...r.desglose
        .filter((t: any) => t.base_tramo > 0)
        .map((t: any) => ({
          label: `Tramo ${t.tramo} (${(t.tipo * 100).toFixed(0)} %)`,
          value: eur(t.cuota_tramo),
        })),
    ],
  },
  duracion_bono: {
    label: 'Duración de Macaulay y Convexidad de un Bono',
    params: [
      { key: 'nominal', label: 'Nominal (€)', step: 1 },
      { key: 'cupon_anual_pct', label: 'Cupón anual (tanto por uno)', step: 0.001 },
      { key: 'n_anos', label: 'n — Años hasta el vencimiento', step: 1, integer: true },
      { key: 'tir', label: 'TIR (tanto por uno)', step: 0.001 },
      { key: 'frecuencia', label: 'Frecuencia de cupones al año', step: 1, integer: true },
    ],
    defaults: { nominal: 1000.0, cupon_anual_pct: 0.05, n_anos: 3, tir: 0.04, frecuencia: 1 },
    format: (r) => [
      { label: 'Precio del bono', value: eur(r.precio) },
      { label: 'Duración de Macaulay', value: `${num(r.macaulay)} años` },
      { label: 'Duración modificada', value: pct(r.modificada) },
      { label: 'Convexidad', value: num(r.convexidad) },
    ],
  },
  tipo_forward: {
    label: 'Tipo de Interés Forward Implícito',
    params: [
      { key: 's1', label: 's₁ — Tipo spot a t₁ (tanto por uno)', step: 0.001 },
      { key: 's2', label: 's₂ — Tipo spot a t₂ (tanto por uno)', step: 0.001 },
      { key: 't1', label: 't₁ — Plazo inicial (años)', step: 1 },
      { key: 't2', label: 't₂ — Plazo final (años)', step: 1 },
    ],
    defaults: { s1: 0.03, s2: 0.04, t1: 1, t2: 2 },
    format: (r) => [{ label: 'Tipo forward f(t₁, t₂)', value: pct(r.result) }],
  },
  tipo_cambio_forward: {
    label: 'Tipo de Cambio Forward (Paridad de Tipos de Interés)',
    params: [
      { key: 'spot', label: 'Spot — Tipo de cambio de contado', step: 0.0001 },
      { key: 'r_dom', label: 'r_dom — Tipo de interés de la divisa cotizada (tanto por uno)', step: 0.001 },
      { key: 'r_for', label: 'r_for — Tipo de interés de la divisa base (tanto por uno)', step: 0.001 },
      { key: 'dias', label: 'Días hasta el vencimiento (base 360)', step: 1, integer: true },
    ],
    defaults: { spot: 1.10, r_dom: 0.035, r_for: 0.02, dias: 180 },
    format: (r) => [{ label: 'Tipo de cambio forward', value: num(r.result, 6) }],
  },
  ratio_informacion: {
    label: 'Ratio de Información (Gestión Activa)',
    params: [
      { key: 'rp', label: 'Rp — Rentabilidad de la cartera (tanto por uno)', step: 0.001 },
      { key: 'rb', label: 'Rb — Rentabilidad del índice/benchmark (tanto por uno)', step: 0.001 },
      { key: 'tracking_error', label: 'Tracking Error (tanto por uno)', step: 0.001 },
    ],
    defaults: { rp: 0.15, rb: 0.08, tracking_error: 0.04 },
    format: (r) => [{ label: 'Ratio de Información', value: num(r.result) }],
  },
  ratio_sortino: {
    label: 'Ratio de Sortino (Riesgo de Pérdidas)',
    params: [
      { key: 'rp', label: 'Rp — Rentabilidad de la cartera (tanto por uno)', step: 0.001 },
      { key: 'rf', label: 'Rf — Tasa libre de riesgo (tanto por uno)', step: 0.001 },
      { key: 'downside_deviation', label: 'Downside deviation — Desviación a la baja (tanto por uno)', step: 0.001 },
    ],
    defaults: { rp: 0.15, rf: 0.03, downside_deviation: 0.05 },
    format: (r) => [{ label: 'Ratio de Sortino', value: num(r.result) }],
  },
  cartera_dos_activos: {
    label: 'Cartera de Dos Activos (Rentabilidad y Volatilidad)',
    params: [
      { key: 'w1', label: 'w₁ — Peso del activo 1 (tanto por uno)', step: 0.01 },
      { key: 'w2', label: 'w₂ — Peso del activo 2 (tanto por uno)', step: 0.01 },
      { key: 'r1', label: 'r₁ — Rentabilidad activo 1 (tanto por uno)', step: 0.001 },
      { key: 'r2', label: 'r₂ — Rentabilidad activo 2 (tanto por uno)', step: 0.001 },
      { key: 'sigma1', label: 'σ₁ — Volatilidad activo 1 (tanto por uno)', step: 0.001 },
      { key: 'sigma2', label: 'σ₂ — Volatilidad activo 2 (tanto por uno)', step: 0.001 },
      { key: 'correlacion', label: 'ρ — Correlación entre activos (−1 a 1)', step: 0.01 },
    ],
    defaults: { w1: 0.6, w2: 0.4, r1: 0.10, r2: 0.15, sigma1: 0.08, sigma2: 0.12, correlacion: -0.5 },
    format: (r) => [
      { label: 'Rentabilidad esperada de la cartera', value: pct(r.retorno_cartera) },
      { label: 'Volatilidad de la cartera', value: pct(r.volatilidad_cartera) },
    ],
  },
  valoracion_inmobiliaria: {
    label: 'Valoración Inmobiliaria (Capitalización de Rentas)',
    params: [
      { key: 'renta_neta', label: 'Renta neta anual (€)', step: 100 },
      { key: 'cap_rate', label: 'Cap Rate — Tasa de capitalización (tanto por uno)', step: 0.001 },
    ],
    defaults: { renta_neta: 12000.0, cap_rate: 0.06 },
    format: (r) => [{ label: 'Valor estimado del inmueble', value: eur(r.result) }],
  },
  amortizacion_francesa: {
    label: 'Amortización de Préstamo (Sistema Francés)',
    params: [
      { key: 'nominal', label: 'Nominal — Importe del préstamo (€)', step: 1000 },
      { key: 'tin', label: 'TIN — Tipo de interés nominal anual (tanto por uno)', step: 0.001 },
      { key: 'n_anos', label: 'n — Plazo en años', step: 1, integer: true },
      { key: 'frecuencia', label: 'Nº de cuotas al año', step: 1, integer: true },
    ],
    defaults: { nominal: 150000.0, tin: 0.04, n_anos: 25, frecuencia: 12 },
    format: (r) => [
      { label: 'Cuota periódica', value: eur(r.cuota_periodica) },
      { label: 'Total intereses pagados', value: eur(r.total_intereses) },
      { label: 'Total pagado (principal + intereses)', value: eur(r.total_pagado) },
    ],
  },
};

export const FORMULA_KEYS = Object.keys(FORMULAS);

const API = 'http://localhost:8000';

interface Props {
  formula: string;
  /** Modo compacto para incrustar junto a una fórmula en la teoría. */
  compact?: boolean;
}

export default function FormulaSimulator({ formula, compact = false }: Props) {
  const spec = FORMULAS[formula];
  const [params, setParams] = useState<Record<string, number>>(() => ({ ...(spec?.defaults ?? {}) }));
  const [result, setResult] = useState<any>(null);
  const [error, setError] = useState<string>('');
  const [loading, setLoading] = useState(false);

  if (!spec) return null;

  const setParam = (key: string, value: string) => {
    const n = parseFloat(value);
    setParams((prev) => ({ ...prev, [key]: isNaN(n) ? 0 : n }));
  };

  const calcular = async () => {
    setError('');
    setResult(null);
    setLoading(true);
    const payload: Record<string, any> = {};
    for (const p of spec.params) {
      payload[p.key] = p.integer ? Math.round(params[p.key]) : params[p.key];
    }
    try {
      const resp = await fetch(`${API}/api/formulas/calculate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ formula, params: payload }),
      });
      const data = await resp.json();
      if (!resp.ok) throw new Error(data.detail || 'Error al calcular.');
      setResult(data);
    } catch (e: any) {
      setError(e.message || 'Error en los parámetros.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={`sim-box${compact ? ' sim-compact' : ''}`}>
      <div className="sim-title">🧮 Simulador — {spec.label}</div>
      <div className="sim-grid">
        {spec.params.map((p) => (
          <label key={p.key} className="sim-field">
            <span>{p.label}</span>
            <input
              type="number"
              step={p.step ?? 0.01}
              value={params[p.key]}
              onChange={(e) => setParam(p.key, e.target.value)}
            />
          </label>
        ))}
      </div>
      <button className="btn btn-secondary sim-btn" onClick={calcular} disabled={loading}>
        {loading ? 'Calculando…' : 'Calcular'}
      </button>
      {error && <div className="sim-error">{error}</div>}
      {result && (
        <div className="sim-result">
          {spec.format(result).map((line, i) => (
            <div key={i} className="sim-result-line">
              <span>{line.label}</span>
              <strong>{line.value}</strong>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
