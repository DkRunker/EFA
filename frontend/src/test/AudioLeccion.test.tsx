import { describe, expect, it } from 'vitest';
import { fireEvent, render, screen } from '@testing-library/react';
import { AudioLeccion } from '../AudioLeccion';
import audio from '../audio.json';

describe('AudioLeccion', () => {
  it('el manifiesto cubre los 10 módulos', () => {
    expect(Object.keys(audio)).toHaveLength(10);
  });

  it('no muestra botón si la lección no tiene audio', () => {
    const { container } = render(<AudioLeccion modulo="M1" pista={999} />);
    expect(container.firstChild).toBeNull();
  });

  it('el botón abre el reproductor con el MP3 de la lección', () => {
    const { container } = render(<AudioLeccion modulo="M10" pista={3} />);
    fireEvent.click(screen.getByRole('button', { name: /Escuchar esta lección/ }));
    expect(container.querySelector('audio')?.getAttribute('src')).toMatch(/\/v1\/m10-03\.mp3$/);
    expect(screen.getByRole('button', { name: '1,25×' })).toBeTruthy();
  });

  it('la pista 0 es la introducción', () => {
    render(<AudioLeccion modulo="M1" pista={0} />);
    expect(screen.getByRole('button', { name: /Escuchar la introducción/ })).toBeTruthy();
  });
});
