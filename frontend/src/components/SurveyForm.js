import React, { useState } from 'react';
import { useForm } from '../hooks/useForm';
import { surveyService } from '../services/surveyService';
import { API_URL } from '../config';

const SurveyForm = () => {
  const [formValues, handleInputChange, resetForm] = useForm({
    title: '',
    description: '',
    questions: [],
    language: 'en',
    expirationDate: '',
    maxResponses: null,
    accessRestriction: false,
  });

  const [currentQuestion, setCurrentQuestion] = useState('');
  const [questionType, setQuestionType] = useState('text');

  const addQuestion = () => {
    if (currentQuestion.trim() !== '') {
      const newQuestion = {
        content: currentQuestion,
        type: questionType,
        options: questionType === 'multiple' ? [] : undefined,
      };
      handleInputChange({
        target: {
          name: 'questions',
          value: [...formValues.questions, newQuestion],
        },
      });
      setCurrentQuestion('');
      setQuestionType('text');
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await surveyService.createSurvey(API_URL, formValues);
      if (response.status === 201) {
        alert('Survey created successfully');
        resetForm();
      } else {
        alert('Failed to create survey');
      }
    } catch (error) {
      console.error('Error creating survey:', error);
      alert('Error creating survey');
    }
  };

  return (
    <div className="survey-form-container">
      <form id="surveyForm" onSubmit={handleSubmit}>
        <h2>Create Survey</h2>
        <div className="form-group">
          <label htmlFor="title">Title</label>
          <input
            type="text"
            name="title"
            value={formValues.title}
            onChange={handleInputChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="description">Description</label>
          <textarea
            name="description"
            value={formValues.description}
            onChange={handleInputChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="language">Language</label>
          <select
            name="language"
            value={formValues.language}
            onChange={handleInputChange}
            required
          >
            <option value="en">English</option>
            <option value="es">Spanish</option>
            <option value="fr">French</option>
            {/* Add more languages as needed */}
          </select>
        </div>
        <div className="form-group">
          <label htmlFor="expirationDate">Expiration Date</label>
          <input
            type="date"
            name="expirationDate"
            value={formValues.expirationDate}
            onChange={handleInputChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="maxResponses">Max Responses</label>
          <input
            type="number"
            name="maxResponses"
            value={formValues.maxResponses}
            onChange={handleInputChange}
            min="1"
          />
        </div>
        <div className="form-group">
          <label htmlFor="accessRestriction">Restrict Access</label>
          <input
            type="checkbox"
            name="accessRestriction"
            checked={formValues.accessRestriction}
            onChange={handleInputChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="currentQuestion">Question</label>
          <input
            type="text"
            name="currentQuestion"
            value={currentQuestion}
            onChange={(e) => setCurrentQuestion(e.target.value)}
          />
          <select
            name="questionType"
            value={questionType}
            onChange={(e) => setQuestionType(e.target.value)}
          >
            <option value="text">Text</option>
            <option value="multiple">Multiple Choice</option>
            {/* Add more question types as needed */}
          </select>
          <button type="button" onClick={addQuestion}>
            Add Question
          </button>
        </div>
        <div className="form-group">
          <button type="submit">Create Survey</button>
        </div>
      </form>
      <div className="questions-preview">
        <h3>Questions Preview</h3>
        <ul>
          {formValues.questions.map((question, index) => (
            <li key={index}>{question.content}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default SurveyForm;