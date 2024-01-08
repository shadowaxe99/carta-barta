import axios from 'axios';
import { API_URL, OPENAI_API_KEY } from '../config';

const analyzeSurveyResponses = async (surveyId) => {
  try {
    const response = await axios.post(`${API_URL}/analyze-responses`, {
      surveyId: surveyId,
      apiKey: OPENAI_API_KEY,
    });

    if (response.data.success) {
      return response.data.analysis;
    } else {
      throw new Error('Failed to analyze survey responses');
    }
  } catch (error) {
    console.error('Error analyzing survey responses:', error);
    throw error;
  }
};

export default {
  analyzeSurveyResponses,
};