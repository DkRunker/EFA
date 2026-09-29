"""Sintetiza los guiones de audio (audiolibro_generado/guion/mN/*.txt) a MP3 con VoiceStudio.

VoiceStudio (AGPL-3.0) se usa SOLO como herramienta externa: su API local OpenAI-compatible
(http://127.0.0.1:3900/v1/audio/speech). Nada de su código entra en este proyecto.

- Un MP3 por sección (capítulo del libro): audiolibro_generado/mp3/mN/NN-slug.mp3, con etiquetas ID3.
- Cada párrafo se pide por separado y se guarda en caché (audiolibro_generado/cache/…pcm), así que
  el proceso se puede cortar y reanudar sin repetir trabajo. Cambiar de voz invalida la caché.
- Pausas: 0,45 s entre párrafos y 1,2 s antes de cada apartado (párrafos marcados con '§ ').

Uso:
  python audiolibro/sintetizar.py m1 [m2 …|todos] [--voz ID|default] [--instruct "female, middle-aged"]
                                  [--seed 7] [--pasos 32] [--velocidad 1.0] [--solo 01] [--max-parrafos N]
  python audiolibro/sintetizar.py --probar "texto" --instruct "male, low pitch" --salida prueba.mp3
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BASE = REPO / 'audiolibro_generado'
GUION = BASE / 'guion'
CACHE = BASE / 'cache'
MP3 = BASE / 'mp3'
API = 'http://127.0.0.1:3900/v1/audio/speech'
SR = 24000                      # el formato 'pcm' de la API es 24 kHz, 16 bits, mono
MAX_CHARS = 700                 # párrafos más largos se parten por frases
PAUSA = 0.45
PAUSA_APARTADO = 1.2


def silencio(seg: float) -> bytes:
    return b'\x00\x00' * int(SR * seg)


def trocear(parrafo: str) -> list[str]:
    if len(parrafo) <= MAX_CHARS:
        return [parrafo]
    frases = re.split(r'(?<=[.;:?!])\s+', parrafo)
    trozos, actual = [], ''
    for f in frases:
        if actual and len(actual) + len(f) + 1 > MAX_CHARS:
            trozos.append(actual)
            actual = f
        else:
            actual = f'{actual} {f}'.strip()
    if actual:
        trozos.append(actual)
    # una "frase" aislada enorme (tabla larga…) se parte por comas
    final = []
    for t in trozos:
        while len(t) > MAX_CHARS * 1.5:
            corte = t.rfind(', ', 0, MAX_CHARS)
            corte = corte if corte > 100 else MAX_CHARS
            final.append(t[:corte + 1])
            t = t[corte + 1:].strip()
        final.append(t)
    return final


def pedir(texto: str, opciones: dict, reintentos: int = 3) -> bytes:
    cuerpo = {'model': 'omnivoice', 'input': texto, 'response_format': 'pcm', 'language': 'es',
              'voice': opciones['voz'], 'speed': opciones['velocidad'], 'num_step': opciones['pasos']}
    if opciones.get('instruct'):
        cuerpo['instruct'] = opciones['instruct']
    if opciones.get('seed') is not None:
        cuerpo['seed'] = opciones['seed']
    datos = json.dumps(cuerpo).encode('utf-8')
    for intento in range(reintentos):
        try:
            req = urllib.request.Request(API, data=datos, headers={'Content-Type': 'application/json'})
            with urllib.request.urlopen(req, timeout=600) as r:
                return r.read()
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            detalle = e.read().decode('utf-8', 'replace')[:300] if isinstance(e, urllib.error.HTTPError) else e
            print(f'      ! error ({detalle}); reintento {intento + 1}/{reintentos}', flush=True)
            time.sleep(5 * (intento + 1))
    raise RuntimeError('VoiceStudio no responde. ¿Está la app abierta y el modelo descargado?')


def clave_cache(texto: str, opciones: dict) -> str:
    firma = json.dumps([texto, opciones['voz'], opciones.get('instruct'), opciones.get('seed'),
                        opciones['pasos'], opciones['velocidad']], ensure_ascii=False)
    return hashlib.sha1(firma.encode('utf-8')).hexdigest()


def audio_de(texto: str, opciones: dict) -> tuple[bytes, bool]:
    ruta = CACHE / (clave_cache(texto, opciones) + '.pcm')
    if ruta.exists():
        return ruta.read_bytes(), True
    pcm = pedir(texto, opciones)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    tmp = ruta.with_suffix('.tmp')
    tmp.write_bytes(pcm)
    tmp.replace(ruta)
    return pcm, False


def a_mp3(pcm: bytes, destino: Path, etiquetas: dict) -> None:
    ffmpeg = shutil.which('ffmpeg')
    if not ffmpeg:
        raise RuntimeError('Falta ffmpeg en el PATH.')
    destino.parent.mkdir(parents=True, exist_ok=True)
    meta = []
    for k, v in etiquetas.items():
        meta += ['-metadata', f'{k}={v}']
    subprocess.run([ffmpeg, '-y', '-loglevel', 'error', '-f', 's16le', '-ar', str(SR), '-ac', '1',
                    '-i', 'pipe:0', '-af', 'loudnorm=I=-18:TP=-1.5:LRA=11',
                    '-ar', '24000', '-c:a', 'libmp3lame', '-b:a', '64k', *meta, str(destino)],
                   input=pcm, check=True)


def sintetizar_fichero(txt: Path, opciones: dict, n_mod: int, pista: int, total_pistas: int,
                       max_parrafos: int | None) -> None:
    parrafos = [p.strip() for p in txt.read_text(encoding='utf-8').split('\n\n') if p.strip()]
    if max_parrafos:
        parrafos = parrafos[:max_parrafos]
    trozos: list[tuple[str, float]] = []
    for p in parrafos:
        pausa = PAUSA
        if p.startswith('§ '):
            p, pausa = p[2:], PAUSA_APARTADO
        for k, t in enumerate(trocear(p)):
            trozos.append((t, pausa if k == 0 else 0.15))
    titulo = parrafos[0].rstrip('.')
    print(f'  [{txt.parent.name}/{txt.name}] {len(trozos)} fragmentos, '
          f'{sum(len(t) for t, _ in trozos):,} caracteres', flush=True)
    partes = [silencio(0.3)]
    t0, nuevos, audio_s = time.time(), 0, 0.0
    for i, (t, pausa) in enumerate(trozos, 1):
        if i > 1:
            partes.append(silencio(pausa))
        pcm, de_cache = audio_de(t, opciones)
        partes.append(pcm)
        audio_s += len(pcm) / 2 / SR
        if not de_cache:
            nuevos += 1
        if not de_cache and (i % 10 == 0 or i == len(trozos)):
            gen = time.time() - t0
            print(f'      {i}/{len(trozos)}  audio {audio_s / 60:.1f} min  '
                  f'(tiempo real ×{audio_s / max(gen, 1e-6):.1f})', flush=True)
    partes.append(silencio(1.0))
    destino = MP3 / txt.parent.name / (txt.stem + '.mp3')
    a_mp3(b''.join(partes), destino, {
        'title': titulo, 'album': f'Preparación EFA · Módulo {n_mod}', 'artist': 'Preparación EFA',
        'track': f'{pista}/{total_pistas}', 'genre': 'Audiobook', 'language': 'spa'})
    print(f'    -> {destino.relative_to(REPO)} ({audio_s / 60:.1f} min, {nuevos} fragmentos nuevos)',
          flush=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('modulos', nargs='*')
    ap.add_argument('--voz', default='default', help="ID de perfil de voz de VoiceStudio o 'default'")
    ap.add_argument('--instruct', default=None, help="diseño de voz OmniVoice, p. ej. 'female, middle-aged'")
    ap.add_argument('--seed', type=int, default=7)
    ap.add_argument('--pasos', type=int, default=32, help='num_step (16 rápido, 32 calidad)')
    ap.add_argument('--velocidad', type=float, default=1.0)
    ap.add_argument('--solo', default=None, help='prefijo de fichero, p. ej. 01')
    ap.add_argument('--max-parrafos', type=int, default=None)
    ap.add_argument('--probar', default=None, help='sintetiza solo este texto')
    ap.add_argument('--salida', default=None)
    a = ap.parse_args()
    opciones = {'voz': a.voz, 'instruct': a.instruct, 'seed': a.seed, 'pasos': a.pasos,
                'velocidad': a.velocidad}

    if a.probar is not None:
        if not a.probar.strip():
            sys.exit('--probar necesita un texto')
        pcm, _ = audio_de(a.probar, opciones)
        destino = Path(a.salida or (BASE / 'pruebas' / 'prueba.mp3'))
        a_mp3(pcm, destino, {'title': 'Prueba'})
        print(destino)
        return

    claves = [f'm{i}' for i in range(1, 11)] if (not a.modulos or 'todos' in a.modulos) else a.modulos
    for c in claves:
        ficheros = sorted((GUION / c).glob('*.txt'))
        if not ficheros:
            sys.exit(f'No hay guion para {c}: ejecuta antes  python audiolibro/guion.py {c}')
        print(f'== Módulo {c[1:]} ({len(ficheros)} pistas)', flush=True)
        for k, f in enumerate(ficheros, 1):
            if a.solo and not f.name.startswith(a.solo):
                continue
            sintetizar_fichero(f, opciones, int(c[1:]), k, len(ficheros), a.max_parrafos)


if __name__ == '__main__':
    main()
