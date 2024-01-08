import axios from 'axios';
import { API_URL } from '../config';

const apiService = {
  get: async (endpoint, params = {}) => {
    try {
      const response = await axios.get(`${API_URL}/${endpoint}`, { params });
      return response.data;
    } catch (error) {
      throw error.response.data;
    }
  },

  post: async (endpoint, data) => {
    try {
      const response = await axios.post(`${API_URL}/${endpoint}`, data);
      return response.data;
    } catch (error) {
      throw error.response.data;
    }
  },

  put: async (endpoint, data) => {
    try {
      const response = await axios.put(`${API_URL}/${endpoint}`, data);
      return response.data;
    } catch (error) {
      throw error.response.data;
    }
  },

  delete: async (endpoint, params = {}) => {
    try {
      const response = await axios.delete(`${API_URL}/${endpoint}`, { params });
      return response.data;
    } catch (error) {
      throw error.response.data;
    }
  }
};

export default apiService;