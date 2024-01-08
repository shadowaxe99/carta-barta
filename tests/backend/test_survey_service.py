import unittest
from unittest.mock import patch
from backend.services.survey_service import SurveyService
from backend.models.survey_model import Survey
from backend.database.db import db_session

class TestSurveyService(unittest.TestCase):
    def setUp(self):
        self.survey_service = SurveyService()
        self.survey_data = {
            'title': 'Employee Satisfaction',
            'description': 'A survey to gauge employee satisfaction levels.',
            'questions': [
                {
                    'text': 'How satisfied are you with your job?',
                    'response_type': 'multiple_choice',
                    'options': ['Very satisfied', 'Satisfied', 'Neutral', 'Unsatisfied', 'Very unsatisfied']
                },
                {
                    'text': 'What can we do to improve your satisfaction?',
                    'response_type': 'open_ended',
                    'options': []
                }
            ],
            'language': 'en',
            'expires_at': None,
            'max_responses': None
        }

    def test_create_survey(self):
        with patch.object(db_session, 'add', return_value=None) as mock_db_add, \
             patch.object(db_session, 'commit', return_value=None) as mock_db_commit:
            survey = self.survey_service.create_survey(**self.survey_data)
            self.assertIsInstance(survey, Survey)
            self.assertEqual(survey.title, self.survey_data['title'])
            self.assertEqual(survey.description, self.survey_data['description'])
            self.assertEqual(survey.language, self.survey_data['language'])
            mock_db_add.assert_called_once()
            mock_db_commit.assert_called_once()

    def test_get_survey_by_id(self):
        with patch.object(self.survey_service, 'get_survey_by_id', return_value=Survey(**self.survey_data)) as mock_get_survey:
            survey_id = 1
            survey = self.survey_service.get_survey_by_id(survey_id)
            self.assertIsInstance(survey, Survey)
            self.assertEqual(survey.title, self.survey_data['title'])
            mock_get_survey.assert_called_once_with(survey_id)

    def test_update_survey(self):
        with patch.object(self.survey_service, 'get_survey_by_id', return_value=Survey(**self.survey_data)) as mock_get_survey, \
             patch.object(db_session, 'commit', return_value=None) as mock_db_commit:
            survey_id = 1
            update_data = {'title': 'Updated Employee Satisfaction'}
            survey = self.survey_service.update_survey(survey_id, **update_data)
            self.assertIsInstance(survey, Survey)
            self.assertEqual(survey.title, update_data['title'])
            mock_get_survey.assert_called_once_with(survey_id)
            mock_db_commit.assert_called_once()

    def test_delete_survey(self):
        with patch.object(self.survey_service, 'get_survey_by_id', return_value=Survey(**self.survey_data)) as mock_get_survey, \
             patch.object(db_session, 'delete', return_value=None) as mock_db_delete, \
             patch.object(db_session, 'commit', return_value=None) as mock_db_commit:
            survey_id = 1
            result = self.survey_service.delete_survey(survey_id)
            self.assertIsNone(result)
            mock_get_survey.assert_called_once_with(survey_id)
            mock_db_delete.assert_called_once()
            mock_db_commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()