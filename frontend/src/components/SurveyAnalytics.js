import React, { useState, useEffect } from 'react';
import { Chart } from 'react-chartjs-2';
import { chartDataPreparation } from '../utils/chartUtils';
import { analyzeResponses } from '../services/analysisService';
import { API_URL } from '../config';

const SurveyAnalytics = ({ surveyId }) => {
  const [chartData, setChartData] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchAnalyticsData = async () => {
      try {
        setLoading(true);
        const response = await fetch(`${API_URL}/api/surveys/${surveyId}/responses/analyze`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            // Include other headers such as authorization if needed
          },
        });

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const data = await response.json();
        const preparedData = chartDataPreparation(data);
        setChartData(preparedData);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchAnalyticsData();
  }, [surveyId]);

  if (loading) {
    return <div>Loading analytics...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h2>Survey Analytics</h2>
      <div>
        <Chart
          type="bar"
          data={chartData}
          options={{
            responsive: true,
            title: {
              display: true,
              text: 'Survey Response Analysis',
            },
            scales: {
              yAxes: [{
                ticks: {
                  beginAtZero: true,
                },
              }],
            },
          }}
        />
      </div>
    </div>
  );
};

export default SurveyAnalytics;