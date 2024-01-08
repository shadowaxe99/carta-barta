import axios from 'axios';
import { API_URL } from '../config';

const authService = {
  login: async function (email, password) {
    try {
      const response = await axios.post(`${API_URL}/auth/login`, { email, password });
      if (response.data.token) {
        localStorage.setItem('user', JSON.stringify(response.data));
      }
      return response.data;
    } catch (error) {
      throw error.response.data;
    }
  },

  logout: function () {
    localStorage.removeItem('user');
  },

  register: async function (userData) {
    try {
      const response = await axios.post(`${API_URL}/auth/register`, userData);
      return response.data;
    } catch (error) {
      throw error.response.data;
    }
  },

  getCurrentUser: function () {
    return JSON.parse(localStorage.getItem('user'));
  },

  updateProfile: async function (userData) {
    try {
      const user = this.getCurrentUser();
      const response = await axios.put(`${API_URL}/auth/profile`, userData, {
        headers: {
          Authorization: `Bearer ${user.token}`
        }
      });
      if (response.data.token) {
        localStorage.setItem('user', JSON.stringify(response.data));
      }
      return response.data;
    } catch (error) {
      throw error.response.data;
    }
  }
};

export default authService;