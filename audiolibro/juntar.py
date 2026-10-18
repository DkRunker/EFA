"""Junta los MP3 de sección de cada módulo en un audiolibro .m4b con capítulos.

Entrada:  audiolibro_generado/mp3/mN/NN-slug.mp3 (los genera sintetizar.py, por bloques)
Salida:   audiolibro_generado/audiolibro/EFA-Modulo-N-<nombre>.m4b  (AAC 64 kb/s, mono, capítulos)

El .m4b es el formato estándar de audiolibro: los reproductores (Apple Libros, Smart AudioBook
Player, VLC, BookPlayer…) recuerdan por dónde vas y muestran los capítulos. Los MP3 por sección se
conservan tal cual por si prefieres escucharlos sueltos.

Uso:  python audiolibro/juntar.py [m1 … m10 | todos] [--parcial]
      Sin --parcial, solo se juntan los módulos que tienen TODAS sus secciones generadas.
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BASE = REPO / 'audiolibro_generado'
sys.path.insert(0, str(REPO / 'backend'))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from guion import limpiar_titulo  # noqa: E402


def duracion(mp3: Path) -> float:
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0',
                        str(mp3)], capture_output=True, text=True, check=True)
    return float(r.stdout.strip())


def titulo_de(mp3: Path, mod) -> str:
    """'00-…' -> 'Introducción'; 'NN-…' -> 'NN. <título de la sección>' (como en el índice del libro)."""
    k = int(mp3.stem[:2])
    if k == 0:
        return 'Introducción'
    return f'{k}. {limpiar_titulo(mod.SECCIONES[k - 1]["titulo"])}'


def nombre_fichero(n: int, nombre: str) -> str:
    """Mismo nombre que el libro: 'EFA-Modulo-1-Instrumentos-y-Mercados-Financieros'."""
    t = unicodedata.normalize('NFD', nombre)
    t = re.sub(r'[̀-ͯ]', '', t)
    t = re.sub(r'[^A-Za-z0-9]+', '-', t).strip('-')
    return f'EFA-Modulo-{n}-{t}'


def _esc(t: str) -> str:
    """Escapa el texto para el formato FFMETADATA."""
    for c in ('\\', '=', ';', '#', '\n'):
        t = t.replace(c, '\\' + c)
    return t


def juntar_modulo(clave: str, parcial: bool) -> Path | None:
    import importlib
    mod = importlib.import_module(f'content.{clave}')
    n = int(clave[1:])
    guiones = sorted((BASE / 'guion' / clave).glob('*.txt'))
    mp3s = [BASE / 'mp3' / clave / (g.stem + '.mp3') for g in guiones]
    faltan = [m for m in mp3s if not m.exists()]
    if faltan and not parcial:
        print(f'{clave}: faltan {len(faltan)}/{len(mp3s)} secciones; no se junta (usa --parcial para forzar)')
        return None
    mp3s = [m for m in mp3s if m.exists()]
    if not mp3s:
        print(f'{clave}: no hay ninguna sección generada')
        return None

    salida = BASE / 'audiolibro' / f'{nombre_fichero(n, mod.NOMBRE)}.m4b'
    salida.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        lista = tmp / 'lista.txt'
        lista.write_text(''.join(f"file '{m.as_posix()}'\n" for m in mp3s), encoding='utf-8')
        meta = [';FFMETADATA1', f'title={_esc(f"Módulo {n}. {mod.NOMBRE}")}',
                f'album={_esc(f"Preparación EFA · Módulo {n}")}', 'artist=Preparación EFA',
                'genre=Audiobook', 'language=spa']
        t = 0.0
        for m in mp3s:
            d = duracion(m)
            meta += ['[CHAPTER]', 'TIMEBASE=1/1000', f'START={int(t * 1000)}',
                     f'END={int((t + d) * 1000)}', f'title={_esc(titulo_de(m, mod))}']
            t += d
        (tmp / 'meta.txt').write_text('\n'.join(meta) + '\n', encoding='utf-8')
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', str(lista),
                        '-i', str(tmp / 'meta.txt'), '-map_metadata', '1', '-map_chapters', '1',
                        '-map', '0:a', '-c:a', 'aac', '-b:a', '64k', '-ac', '1',
                        '-movflags', '+faststart', '-f', 'mp4', str(tmp / 'salida.m4b')], check=True)
        shutil.move(tmp / 'salida.m4b', salida)
    aviso = f' (PARCIAL: faltan {len(faltan)} secciones)' if faltan else ''
    print(f'{clave}: {salida.relative_to(REPO)}  {len(mp3s)} capítulos, {t / 3600:.1f} h, '
          f'{salida.stat().st_size / 2**20:.0f} MB{aviso}')
    return salida


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('modulos', nargs='*')
    ap.add_argument('--parcial', action='store_true', help='juntar aunque falten secciones')
    a = ap.parse_args()
    if not shutil.which('ffmpeg'):
        sys.exit('Falta ffmpeg en el PATH.')
    claves = [f'm{i}' for i in range(1, 11)] if (not a.modulos or 'todos' in a.modulos) else a.modulos
    for c in claves:
        juntar_modulo(c, a.parcial)


if __name__ == '__main__':
    main()
