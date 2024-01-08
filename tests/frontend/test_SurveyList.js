import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import SurveyList from '../../src/components/SurveyList';
import surveyService from '../../src/services/surveyService';

jest.mock('../../src/services/surveyService');

describe('SurveyList Component', () => {
  const mockSurveys = [
    {
      id: '1',
      title: 'Customer Satisfaction',
      description: 'Survey about customer service satisfaction.',
      createdAt: '2021-01-01T00:00:00.000Z',
      responses: 150,
    },
    {
      id: '2',
      title: 'Product Feedback',
      description: 'Survey for feedback on our new product.',
      createdAt: '2021-02-01T00:00:00.000Z',
      responses: 89,
    },
  ];

  beforeEach(() => {
    surveyService.getSurveys.mockResolvedValue(mockSurveys);
  });

  test('renders survey list with surveys', async () => {
    render(<SurveyList />);

    await waitFor(() => {
      expect(screen.getByText('Customer Satisfaction')).toBeInTheDocument();
      expect(screen.getByText('Survey about customer service satisfaction.')).toBeInTheDocument();
      expect(screen.getByText('Product Feedback')).toBeInTheDocument();
      expect(screen.getByText('Survey for feedback on our new product.')).toBeInTheDocument();
    });
  });

  test('displays the number of responses for each survey', async () => {
    render(<SurveyList />);

    await waitFor(() => {
      expect(screen.getByText('150 responses')).toBeInTheDocument();
      expect(screen.getByText('89 responses')).toBeInTheDocument();
    });
  });

  test('calls getSurveys on component mount', async () => {
    render(<SurveyList />);

    await waitFor(() => {
      expect(surveyService.getSurveys).toHaveBeenCalledTimes(1);
    });
  });

  test('displays message when no surveys are available', async () => {
    surveyService.getSurveys.mockResolvedValueOnce([]);
    render(<SurveyList />);

    await waitFor(() => {
      expect(screen.getByText('No surveys available.')).toBeInTheDocument();
    });
  });

  test('displays error message when surveys cannot be fetched', async () => {
    const errorMessage = 'Unable to fetch surveys.';
    surveyService.getSurveys.mockRejectedValueOnce(new Error(errorMessage));
    render(<SurveyList />);

    await waitFor(() => {
      expect(screen.getByText(errorMessage)).toBeInTheDocument();
    });
  });
});