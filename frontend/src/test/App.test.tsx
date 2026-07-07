import { render, screen } from '@testing-library/react';
import { expect, test } from 'vitest';
import App from '../App';

test('renders auth screen by default', () => {
  render(<App />);
  
  // Verificar cabecera de autenticación
  expect(screen.getByText('EFA Prep Platform')).toBeInTheDocument();
  expect(screen.getByText('Accede a tu simulador inteligente oficial')).toBeInTheDocument();
  
  // Verificar campos
  expect(screen.getByText('Usuario')).toBeInTheDocument();
  expect(screen.getByText('Contraseña')).toBeInTheDocument();
});
