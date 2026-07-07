import { render, screen } from '@testing-library/react';
import { expect, test } from 'vitest';
import App from '../App';

test('renders dashboard with title and exam buttons', () => {
  render(<App />);
  
  // Verificar cabecera
  expect(screen.getByText('EFA Prep')).toBeInTheDocument();
  
  // Verificar botones de examen
  expect(screen.getByText('EIP Nivel I')).toBeInTheDocument();
  expect(screen.getAllByText('EFA Completo')[0]).toBeInTheDocument();
  expect(screen.getByText('EFA Nivel II')).toBeInTheDocument();
});
