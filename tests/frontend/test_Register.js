import React from 'react';
import { render, fireEvent, waitFor, screen } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import Register from '../src/components/Register';
import authService from '../src/services/authService';

jest.mock('../src/services/authService');

describe('Register Component', () => {
  beforeEach(() => {
    authService.createUser.mockImplementation(() => Promise.resolve({ message: 'USER_CREATED' }));
  });

  test('renders Register form', () => {
    render(<Register />);
    expect(screen.getByTestId('registerForm')).toBeInTheDocument();
  });

  test('allows users to input data', () => {
    render(<Register />);
    fireEvent.change(screen.getByLabelText(/username/i), { target: { value: 'testuser' } });
    fireEvent.change(screen.getByLabelText(/email/i), { target: { value: 'test@example.com' } });
    fireEvent.change(screen.getByLabelText(/password/i), { target: { value: 'password123' } });

    expect(screen.getByLabelText(/username/i).value).toBe('testuser');
    expect(screen.getByLabelText(/email/i).value).toBe('test@example.com');
    expect(screen.getByLabelText(/password/i).value).toBe('password123');
  });

  test('submits the form and calls createUser', async () => {
    render(<Register />);

    fireEvent.change(screen.getByLabelText(/username/i), { target: { value: 'testuser' } });
    fireEvent.change(screen.getByLabelText(/email/i), { target: { value: 'test@example.com' } });
    fireEvent.change(screen.getByLabelText(/password/i), { target: { value: 'password123' } });
    fireEvent.click(screen.getByRole('button', { name: /register/i }));

    await waitFor(() => expect(authService.createUser).toHaveBeenCalledWith({
      username: 'testuser',
      email: 'test@example.com',
      password: 'password123'
    }));
  });

  test('displays a success message after successful registration', async () => {
    render(<Register />);

    fireEvent.change(screen.getByLabelText(/username/i), { target: { value: 'testuser' } });
    fireEvent.change(screen.getByLabelText(/email/i), { target: { value: 'test@example.com' } });
    fireEvent.change(screen.getByLabelText(/password/i), { target: { value: 'password123' } });
    fireEvent.click(screen.getByRole('button', { name: /register/i }));

    await waitFor(() => expect(screen.getByRole('alert')).toHaveTextContent('User successfully created'));
  });

  test('handles server errors when registration fails', async () => {
    authService.createUser.mockImplementationOnce(() => Promise.reject(new Error('User creation failed')));

    render(<Register />);

    fireEvent.change(screen.getByLabelText(/username/i), { target: { value: 'testuser' } });
    fireEvent.change(screen.getByLabelText(/email/i), { target: { value: 'test@example.com' } });
    fireEvent.change(screen.getByLabelText(/password/i), { target: { value: 'password123' } });
    fireEvent.click(screen.getByRole('button', { name: /register/i }));

    await waitFor(() => expect(screen.getByRole('alert')).toHaveTextContent('User creation failed'));
  });
});