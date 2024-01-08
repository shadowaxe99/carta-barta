import unittest
from unittest.mock import patch
from backend.controllers.survey_controller import SurveyController
from backend.models.survey_model import Survey
from backend.database.db import initialize_db
from backend.database.survey_repository import SurveyRepository
from backend.services.survey_service import SurveyService

class TestSurveyController(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize the database and create tables
        initialize_db()

    def setUp(self):
        self.survey_controller = SurveyController()
        self.survey_data = {
            'title': 'Employee Satisfaction',
            'questions': [
                {
                    'text': 'How satisfied are you with your job?',
                    'response_type': 'multiple_choice',
                    'options': ['Very satisfied', 'Satisfied', 'Neutral', 'Unsatisfied', 'Very unsatisfied']
                },
                {
                    'text': 'What can we do to improve your work experience?',
                    'response_type': 'open_ended'
                }
            ],
            'language': 'en',
            'expires_at': None,
            'max_responses': None
        }

    def test_create_survey(self):
        with patch.object(SurveyService, 'create_survey', return_value=Survey(**self.survey_data)) as mock_create_survey:
            response = self.survey_controller.create_survey(self.survey_data)
            self.assertIsInstance(response, Survey)
            self.assertEqual(response.title, self.survey_data['title'])
            mock_create_survey.assert_called_once_with(self.survey_data)

    def test_get_survey(self):
        with patch.object(SurveyRepository, 'get_survey_by_id', return_value=Survey(**self.survey_data)) as mock_get_survey:
            survey_id = 1
            response = self.survey_controller.get_survey(survey_id)
            self.assertIsInstance(response, Survey)
            self.assertEqual(response.title, self.survey_data['title'])
            mock_get_survey.assert_called_once_with(survey_id)

    def test_get_all_surveys(self):
        with patch.object(SurveyRepository, 'get_all_surveys', return_value=[Survey(**self.survey_data)]) as mock_get_all_surveys:
            response = self.survey_controller.get_all_surveys()
            self.assertIsInstance(response, list)
            self.assertGreater(len(response), 0)
            self.assertIsInstance(response[0], Survey)
            mock_get_all_surveys.assert_called_once()

    def test_update_survey(self):
        updated_data = {'title': 'Updated Employee Satisfaction'}
        with patch.object(SurveyService, 'update_survey', return_value=Survey(**{**self.survey_data, **updated_data})) as mock_update_survey:
            survey_id = 1
            response = self.survey_controller.update_survey(survey_id, updated_data)
            self.assertIsInstance(response, Survey)
            self.assertEqual(response.title, updated_data['title'])
            mock_update_survey.assert_called_once_with(survey_id, updated_data)

    def test_delete_survey(self):
        with patch.object(SurveyService, 'delete_survey', return_value=True) as mock_delete_survey:
            survey_id = 1
            response = self.survey_controller.delete_survey(survey_id)
            self.assertTrue(response)
            mock_delete_survey.assert_called_once_with(survey_id)

    @classmethod
    def tearDownClass(cls):
        # Drop the database tables and clean up
        pass

if __name__ == '__main__':
    unittest.main()