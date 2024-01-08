import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import ResponseList from '../../src/components/ResponseList';
import apiService from '../../src/services/apiService';

jest.mock('../../src/services/apiService');

describe('ResponseList Component', () => {
  const mockResponses = [
    { id: 1, surveyId: 1, content: 'Response 1', respondent: 'User1' },
    { id: 2, surveyId: 1, content: 'Response 2', respondent: 'User2' },
  ];

  beforeEach(() => {
    apiService.getResponses.mockResolvedValue(mockResponses);
  });

  test('should render without crashing', async () => {
    render(<ResponseList surveyId={1} />);
    await waitFor(() => expect(apiService.getResponses).toHaveBeenCalledWith(1));
  });

  test('should display a list of responses', async () => {
    render(<ResponseList surveyId={1} />);
    await waitFor(() => {
      expect(screen.getByText('Response 1')).toBeInTheDocument();
      expect(screen.getByText('Response 2')).toBeInTheDocument();
    });
  });

  test('should handle no responses', async () => {
    apiService.getResponses.mockResolvedValueOnce([]);
    render(<ResponseList surveyId={1} />);
    await waitFor(() => {
      expect(screen.getByText('No responses yet.')).toBeInTheDocument();
    });
  });

  test('should handle API errors gracefully', async () => {
    const errorMessage = 'Error fetching responses';
    apiService.getResponses.mockRejectedValueOnce(new Error(errorMessage));
    render(<ResponseList surveyId={1} />);
    await waitFor(() => {
      expect(screen.getByText('Failed to load responses.')).toBeInTheDocument();
    });
  });
});