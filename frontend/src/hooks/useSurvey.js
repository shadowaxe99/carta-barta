import { useState, useEffect, useCallback } from 'react';
import surveyService from '../services/surveyService';

const useSurvey = () => {
  const [surveys, setSurveys] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchSurveys = useCallback(async () => {
    setLoading(true);
    try {
      const response = await surveyService.getSurveys();
      setSurveys(response.data);
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, []);

  const createSurvey = useCallback(async (surveyData) => {
    setLoading(true);
    try {
      const response = await surveyService.createSurvey(surveyData);
      setSurveys(prevSurveys => [...prevSurveys, response.data]);
      setError(null);
      return response.data;
    } catch (err) {
      setError(err.message);
      return null;
    } finally {
      setLoading(false);
    }
  }, []);

  const deleteSurvey = useCallback(async (surveyId) => {
    setLoading(true);
    try {
      await surveyService.deleteSurvey(surveyId);
      setSurveys(prevSurveys => prevSurveys.filter(survey => survey.id !== surveyId));
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchSurveys();
  }, [fetchSurveys]);

  return {
    surveys,
    loading,
    error,
    createSurvey,
    deleteSurvey,
    fetchSurveys
  };
};

export default useSurvey;