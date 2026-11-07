import { useRef, useState } from 'react';
import { Headphones } from 'lucide-react';
import audio from './audio.json';

// Los MP3 viven en una release de un repo público aparte: pesan ~2,7 GB y no caben en Render.
const BASE_AUDIO = 'https://github.com/DkRunker/EFA-audio/releases/download/v1';
const VELOCIDADES = [1, 1.25, 1.5];
const MANIFIESTO = audio as Record<string, Record<string, number>>;

// localStorage puede fallar (ventana privada, datos bloqueados): el reproductor funciona igual sin él.
function leer(clave: string): number {
  try {
    return Number(localStorage.getItem(clave)) || 0;
  } catch {
    return 0;
  }
}

function guardar(clave: string, valor: number) {
  try {
    localStorage.setItem(clave, String(valor));
  } catch {
    // sin almacenamiento simplemente no se recuerda
  }
}

// `pista` es el número del MP3: 0 la introducción del módulo y N la sección N-1 de la lista.
export function AudioLeccion({ modulo, pista }: { modulo: string; pista: number }) {
  const segundos = MANIFIESTO[modulo]?.[String(pista)];
  const [abierto, setAbierto] = useState(false);
  const [velocidad, setVelocidad] = useState(() => leer('efa-audio-velocidad') || 1);
  const ref = useRef<HTMLAudioElement>(null);
  if (!segundos) return null;

  const clave = `efa-audio-${modulo}-${pista}`;
  const minutos = Math.max(1, Math.round(segundos / 60));
  const nombre = pista === 0 ? 'la introducción' : 'esta lección';
  const src = `${BASE_AUDIO}/${modulo.toLowerCase()}-${String(pista).padStart(2, '0')}.mp3`;

  const cambiarVelocidad = (v: number) => {
    setVelocidad(v);
    guardar('efa-audio-velocidad', v);
    if (ref.current) ref.current.playbackRate = v;
  };

  if (!abierto) {
    return (
      <button className="audio-boton" onClick={() => setAbierto(true)}>
        <Headphones size={16} /> Escuchar {nombre} ({minutos} min)
      </button>
    );
  }

  return (
    <div className="audio-leccion">
      <audio
        ref={ref}
        src={src}
        controls
        autoPlay
        preload="metadata"
        aria-label={`Audio de ${nombre}`}
        onLoadedMetadata={(e) => {
          e.currentTarget.playbackRate = velocidad;
          const pos = leer(clave);
          if (pos > 0 && pos < e.currentTarget.duration - 5) e.currentTarget.currentTime = pos;
        }}
        onTimeUpdate={(e) => guardar(clave, Math.floor(e.currentTarget.currentTime))}
        onEnded={() => guardar(clave, 0)}
        onPlay={(e) => {
          // una sola lección sonando a la vez
          document.querySelectorAll('audio').forEach((a) => {
            if (a !== e.currentTarget) a.pause();
          });
        }}
      />
      <div className="audio-velocidades" role="group" aria-label="Velocidad de reproducción">
        {VELOCIDADES.map((v) => (
          <button
            key={v}
            className={v === velocidad ? 'activa' : ''}
            aria-pressed={v === velocidad}
            onClick={() => cambiarVelocidad(v)}
          >
            {String(v).replace('.', ',')}×
          </button>
        ))}
      </div>
    </div>
  );
}
