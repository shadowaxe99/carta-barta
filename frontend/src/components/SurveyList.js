import React, { useState, useEffect } from 'react';
import { getSurveys } from '../services/surveyService';
import SurveyItem from './SurveyItem';

const SurveyList = () => {
  const [surveys, setSurveys] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchSurveys = async () => {
      try {
        const data = await getSurveys();
        setSurveys(data);
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    fetchSurveys();
  }, []);

  if (loading) {
    return <div>Loading surveys...</div>;
  }

  if (error) {
    return <div>Error fetching surveys: {error}</div>;
  }

  return (
    <div id="surveyList">
      {surveys.length > 0 ? (
        <ul>
          {surveys.map((survey) => (
            <SurveyItem key={survey.id} survey={survey} />
          ))}
        </ul>
      ) : (
        <div>No surveys available.</div>
      )}
    </div>
  );
};

export default SurveyList;