import { useState, useContext, createContext } from 'react';
import apiService from '../services/apiService';

const authContext = createContext();

export function ProvideAuth({ children }) {
  const auth = useProvideAuth();
  return <authContext.Provider value={auth}>{children}</authContext.Provider>;
}

export const useAuth = () => {
  return useContext(authContext);
};

function useProvideAuth() {
  const [user, setUser] = useState(null);

  const signin = async (email, password) => {
    try {
      const response = await apiService.post('/auth/signin', { email, password });
      setUser(response.data.user);
      return response.data.user;
    } catch (error) {
      console.error('Sign in failed:', error);
      throw error;
    }
  };

  const signup = async (name, email, password) => {
    try {
      const response = await apiService.post('/auth/signup', { name, email, password });
      setUser(response.data.user);
      return response.data.user;
    } catch (error) {
      console.error('Sign up failed:', error);
      throw error;
    }
  };

  const signout = async () => {
    try {
      await apiService.post('/auth/signout');
      setUser(null);
    } catch (error) {
      console.error('Sign out failed:', error);
      throw error;
    }
  };

  const sendPasswordResetEmail = async (email) => {
    try {
      const response = await apiService.post('/auth/reset-password', { email });
      return response.data.message;
    } catch (error) {
      console.error('Password reset failed:', error);
      throw error;
    }
  };

  const confirmPasswordReset = async (token, newPassword) => {
    try {
      const response = await apiService.post('/auth/confirm-reset-password', { token, newPassword });
      return response.data.message;
    } catch (error) {
      console.error('Password reset confirmation failed:', error);
      throw error;
    }
  };

  return {
    user,
    signin,
    signup,
    signout,
    sendPasswordResetEmail,
    confirmPasswordReset
  };
}