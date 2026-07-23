/**
 * Acceso a la API: dirección base configurable y sesión.
 *
 * Antes la URL `http://localhost:8000` estaba incrustada en cada `fetch`, lo
 * que impedía desplegar la aplicación en cualquier otro sitio. Ahora se toma de
 * `VITE_API_URL` y, si no está definida, se usa el mismo origen que sirve la
 * página (que es como funciona el modo portable y el despliegue normal).
 */

export const API_URL: string =
  (import.meta.env.VITE_API_URL as string | undefined)?.replace(/\/$/, '') ?? '';

const CLAVE_TOKEN = 'efa_token';
const CLAVE_USUARIO = 'efa_usuario';

export function guardarSesion(usuario: string, token: string): void {
  localStorage.setItem(CLAVE_USUARIO, usuario);
  localStorage.setItem(CLAVE_TOKEN, token);
}

export function borrarSesion(): void {
  localStorage.removeItem(CLAVE_USUARIO);
  localStorage.removeItem(CLAVE_TOKEN);
}

export function usuarioGuardado(): string | null {
  return localStorage.getItem(CLAVE_USUARIO);
}

export function tokenGuardado(): string | null {
  return localStorage.getItem(CLAVE_TOKEN);
}

/**
 * `fetch` con la dirección base y el token de sesión ya puestos.
 * Si el servidor responde 401 o 403, la sesión se descarta para que la
 * aplicación vuelva a pedir el acceso en lugar de quedarse en un estado roto.
 */
export async function apiFetch(ruta: string, opciones: RequestInit = {}): Promise<Response> {
  const token = tokenGuardado();
  const cabeceras = new Headers(opciones.headers ?? {});
  if (!cabeceras.has('Content-Type') && opciones.body) {
    cabeceras.set('Content-Type', 'application/json');
  }
  if (token) {
    cabeceras.set('Authorization', `Bearer ${token}`);
  }

  const respuesta = await fetch(`${API_URL}${ruta}`, { ...opciones, headers: cabeceras });

  if (respuesta.status === 401 || respuesta.status === 403) {
    borrarSesion();
  }
  return respuesta;
}

/** Lee el token que devuelve el proveedor externo en la URL de vuelta. */
export function recogerSesionDeLaUrl(): { usuario: string; token: string } | null {
  const parametros = new URLSearchParams(window.location.search);
  const token = parametros.get('token');
  const usuario = parametros.get('usuario');
  if (token && usuario) {
    // Limpiamos la barra de direcciones para no dejar el token a la vista
    // ni en el historial del navegador.
    window.history.replaceState({}, '', window.location.pathname);
    return { usuario, token };
  }
  return null;
}

/** Lee el motivo de error que puede devolver el proveedor externo. */
export function recogerErrorDeLaUrl(): string | null {
  const parametros = new URLSearchParams(window.location.search);
  const error = parametros.get('error_auth');
  if (error) {
    window.history.replaceState({}, '', window.location.pathname);
  }
  return error;
}

export interface ProveedorAcceso {
  id: string;
  nombre: string;
}

export async function proveedoresDisponibles(): Promise<ProveedorAcceso[]> {
  try {
    const r = await fetch(`${API_URL}/api/auth/oauth/proveedores`);
    if (!r.ok) return [];
    const d = await r.json();
    return d.proveedores ?? [];
  } catch {
    return [];
  }
}

export function urlAccesoProveedor(id: string): string {
  return `${API_URL}/api/auth/oauth/${id}`;
}
