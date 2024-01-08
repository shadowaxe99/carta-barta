import React, { useState, useEffect } from 'react';
import { getResponses } from '../services/surveyService';
import { ResponseSchema } from '../utils/validationUtils';

const ResponseList = ({ surveyId }) => {
  const [responses, setResponses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchResponses = async () => {
      try {
        setLoading(true);
        const data = await getResponses(surveyId);
        setResponses(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchResponses();
  }, [surveyId]);

  if (loading) return <div>Loading responses...</div>;
  if (error) return <div>Error fetching responses: {error}</div>;

  return (
    <div id="responseList">
      <h3>Responses</h3>
      {responses.length > 0 ? (
        <ul>
          {responses.map((response, index) => (
            <li key={index}>
              <ResponseSchema response={response} />
            </li>
          ))}
        </ul>
      ) : (
        <div>No responses yet.</div>
      )}
    </div>
  );
};

export default ResponseList;