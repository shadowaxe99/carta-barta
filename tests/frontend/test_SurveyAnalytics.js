import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import SurveyAnalytics from '../components/SurveyAnalytics';
import * as apiService from '../services/apiService';

jest.mock('../services/apiService');

describe('SurveyAnalytics Component', () => {
  const mockResponseData = {
    surveyId: '1',
    responses: [
      { responseId: 'r1', answer: 'Yes', sentiment: 'positive' },
      { responseId: 'r2', answer: 'No', sentiment: 'negative' },
    ],
    analytics: {
      sentimentScore: 0.5,
      keywordFrequencies: { 'customer service': 2, 'quality': 1 },
    },
  };

  beforeEach(() => {
    apiService.getSurveyAnalytics.mockResolvedValue(mockResponseData);
  });

  test('renders SurveyAnalytics component and displays analytics data', async () => {
    render(<SurveyAnalytics surveyId="1" />);

    await waitFor(() => {
      expect(apiService.getSurveyAnalytics).toHaveBeenCalledWith('1');
      expect(screen.getByText('Sentiment Score:')).toBeInTheDocument();
      expect(screen.getByText('0.5')).toBeInTheDocument();
      expect(screen.getByText('customer service')).toBeInTheDocument();
      expect(screen.getByText('2')).toBeInTheDocument();
      expect(screen.getByText('quality')).toBeInTheDocument();
      expect(screen.getByText('1')).toBeInTheDocument();
    });
  });

  test('handles API errors gracefully', async () => {
    apiService.getSurveyAnalytics.mockRejectedValue(new Error('API Error'));

    render(<SurveyAnalytics surveyId="1" />);

    await waitFor(() => {
      expect(apiService.getSurveyAnalytics).toHaveBeenCalledWith('1');
      expect(screen.getByText('Failed to load analytics data')).toBeInTheDocument();
    });
  });
});