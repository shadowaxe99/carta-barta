import axios from 'axios';
import { API_URL } from '../config';

const createSurvey = async (surveyData, token) => {
  try {
    const response = await axios.post(`${API_URL}/surveys`, surveyData, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const getSurveys = async (token) => {
  try {
    const response = await axios.get(`${API_URL}/surveys`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const getSurveyById = async (surveyId, token) => {
  try {
    const response = await axios.get(`${API_URL}/surveys/${surveyId}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const updateSurvey = async (surveyId, surveyData, token) => {
  try {
    const response = await axios.put(`${API_URL}/surveys/${surveyId}`, surveyData, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const deleteSurvey = async (surveyId, token) => {
  try {
    const response = await axios.delete(`${API_URL}/surveys/${surveyId}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const submitResponse = async (surveyId, responseData, token) => {
  try {
    const response = await axios.post(`${API_URL}/surveys/${surveyId}/responses`, responseData, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const getResponses = async (surveyId, token) => {
  try {
    const response = await axios.get(`${API_URL}/surveys/${surveyId}/responses`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export {
  createSurvey,
  getSurveys,
  getSurveyById,
  updateSurvey,
  deleteSurvey,
  submitResponse,
  getResponses,
};