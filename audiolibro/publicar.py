"""Prepara los MP3 de sección para publicarlos y genera el manifiesto que usa la web.

Entrada:  audiolibro_generado/mp3/mN/NN-slug.mp3 + .json (los genera sintetizar.py)
Salida:   audiolibro_generado/web/mN-NN.mp3     (enlaces duros, nombres estables para la release)
          frontend/src/audio.json               ({"M1": {"0": segundos, "1": segundos, …}, …})

El índice del manifiesto es el número del MP3: 0 es la introducción y N es SECCIONES[N-1].
Los ficheros se suben a mano a la release de DkRunker/EFA-audio con `gh release upload`.

Uso:  python audiolibro/publicar.py
"""
from __future__ import annotations

import importlib
import json
import os
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BASE = REPO / 'audiolibro_generado'
SALIDA = BASE / 'web'
MANIFIESTO = REPO / 'frontend' / 'src' / 'audio.json'
sys.path.insert(0, str(REPO / 'backend'))


def duracion(mp3: Path) -> float:
    # la del fichero real: el .json de sintetizar.py no cuenta las pausas
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0',
                        str(mp3)], capture_output=True, text=True, check=True)
    return float(r.stdout.strip())


def main() -> None:
    SALIDA.mkdir(parents=True, exist_ok=True)
    manifiesto: dict[str, dict[str, int]] = {}
    for n in range(1, 11):
        mod = importlib.import_module(f'content.m{n}')
        mp3s = sorted((BASE / 'mp3' / f'm{n}').glob('*.mp3'))
        if len(mp3s) != len(mod.SECCIONES) + 1:
            sys.exit(f'm{n}: hay {len(mp3s)} MP3 y {len(mod.SECCIONES) + 1} lecciones; '
                     'regenera el audio antes de publicar')
        pistas: dict[str, int] = {}
        for mp3 in mp3s:
            k = int(mp3.stem[:2])
            pistas[str(k)] = round(duracion(mp3))
            destino = SALIDA / f'm{n}-{k:02d}.mp3'
            destino.unlink(missing_ok=True)
            os.link(mp3, destino)
        manifiesto[f'M{n}'] = pistas
    MANIFIESTO.write_text(json.dumps(manifiesto, separators=(',', ':')) + '\n', 'utf-8')
    total = sum(s for p in manifiesto.values() for s in p.values())
    print(f'{sum(len(p) for p in manifiesto.values())} pistas, {total / 3600:.1f} h -> {SALIDA}')


if __name__ == '__main__':
    main()
