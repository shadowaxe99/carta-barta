import React from 'react';
import { render, fireEvent, waitFor, screen } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import SurveyForm from '../components/SurveyForm';

describe('SurveyForm Component', () => {
  test('renders SurveyForm component', () => {
    render(<SurveyForm />);
    expect(screen.getByTestId('surveyForm')).toBeInTheDocument();
  });

  test('allows the user to create a survey', async () => {
    const { getByLabelText, getByRole } = render(<SurveyForm />);
    
    fireEvent.change(getByLabelText(/survey title/i), { target: { value: 'Customer Feedback' } });
    fireEvent.change(getByLabelText(/survey description/i), { target: { value: 'Please provide your feedback' } });
    fireEvent.change(getByLabelText(/question 1/i), { target: { value: 'How do you rate our service?' } });
    fireEvent.click(getByRole('button', { name: /add question/i }));
    fireEvent.change(getByLabelText(/question 2/i), { target: { value: 'Any suggestions for improvement?' } });

    fireEvent.click(getByRole('button', { name: /submit survey/i }));

    await waitFor(() => {
      expect(screen.getByText(/survey created/i)).toBeInTheDocument();
    });
  });

  test('validates form fields before submission', async () => {
    const { getByRole, getByText } = render(<SurveyForm />);
    
    fireEvent.click(getByRole('button', { name: /submit survey/i }));

    await waitFor(() => {
      expect(getByText(/title is required/i)).toBeInTheDocument();
      expect(getByText(/at least one question is required/i)).toBeInTheDocument();
    });
  });
});