import React from 'react';
import { render, fireEvent, waitFor, screen } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import Login from '../src/components/Login';
import authService from '../src/services/authService';

jest.mock('../src/services/authService');

describe('Login Component', () => {
  beforeEach(() => {
    authService.authenticateUser.mockImplementation(() => Promise.resolve({ message: 'USER_AUTH_SUCCESS' }));
  });

  test('renders login form', () => {
    render(<Login />);
    expect(screen.getByTestId('loginForm')).toBeInTheDocument();
  });

  test('allows the user to login successfully', async () => {
    const { getByLabelText, getByText } = render(<Login />);
    const emailInput = getByLabelText(/email/i);
    const passwordInput = getByLabelText(/password/i);
    const loginButton = getByText(/login/i);

    fireEvent.change(emailInput, { target: { value: 'test@example.com' } });
    fireEvent.change(passwordInput, { target: { value: 'password123' } });
    fireEvent.click(loginButton);

    await waitFor(() => expect(authService.authenticateUser).toHaveBeenCalledWith('test@example.com', 'password123'));
    await waitFor(() => expect(screen.getByText('USER_AUTH_SUCCESS')).toBeInTheDocument());
  });

  test('displays error message on login failure', async () => {
    authService.authenticateUser.mockImplementation(() => Promise.reject(new Error('Login failed')));
    const { getByLabelText, getByText } = render(<Login />);
    const emailInput = getByLabelText(/email/i);
    const passwordInput = getByLabelText(/password/i);
    const loginButton = getByText(/login/i);

    fireEvent.change(emailInput, { target: { value: 'wrong@example.com' } });
    fireEvent.change(passwordInput, { target: { value: 'wrongpassword' } });
    fireEvent.click(loginButton);

    await waitFor(() => expect(authService.authenticateUser).toHaveBeenCalledWith('wrong@example.com', 'wrongpassword'));
    await waitFor(() => expect(screen.getByText(/login failed/i)).toBeInTheDocument());
  });
});