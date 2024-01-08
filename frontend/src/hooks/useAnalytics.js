import { useState, useEffect } from 'react';
import apiService from '../services/apiService';
import { OPENAI_API_KEY } from '../config';

const useAnalytics = (surveyId) => {
  const [analyticsData, setAnalyticsData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchAnalyticsData = async () => {
      setLoading(true);
      try {
        const response = await apiService.get(`/surveys/${surveyId}/responses`);
        const responses = response.data;

        // Assuming OpenAI's API provides a method `analyzeSurveyResponses`
        // that takes an array of survey responses and returns analytics data
        const analyticsResponse = await apiService.post('/openai/analyzeSurveyResponses', {
          responses,
          apiKey: OPENAI_API_KEY,
        });

        setAnalyticsData(analyticsResponse.data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    if (surveyId) {
      fetchAnalyticsData();
    }
  }, [surveyId]);

  return { analyticsData, loading, error };
};

export default useAnalytics;