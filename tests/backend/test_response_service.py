import unittest
from unittest.mock import patch
from backend.services.response_service import ResponseService
from backend.models.response_model import Response
from backend.database.response_repository import ResponseRepository

class TestResponseService(unittest.TestCase):
    def setUp(self):
        self.response_service = ResponseService()
        self.mock_response_data = {
            'survey_id': '123',
            'user_id': '456',
            'answers': {
                'question_1': 'Answer 1',
                'question_2': 'Answer 2'
            }
        }
        self.mock_response = Response(**self.mock_response_data)

    @patch.object(ResponseRepository, 'save_response')
    def test_submit_response(self, mock_save_response):
        mock_save_response.return_value = self.mock_response
        response = self.response_service.submit_response(self.mock_response_data)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.survey_id, self.mock_response_data['survey_id'])
        self.assertEqual(response.user_id, self.mock_response_data['user_id'])
        self.assertEqual(response.answers, self.mock_response_data['answers'])
        mock_save_response.assert_called_once_with(self.mock_response)

    @patch.object(ResponseRepository, 'get_responses_by_survey_id')
    def test_get_responses_by_survey_id(self, mock_get_responses_by_survey_id):
        mock_get_responses_by_survey_id.return_value = [self.mock_response]
        responses = self.response_service.get_responses_by_survey_id(self.mock_response_data['survey_id'])
        self.assertIsInstance(responses, list)
        self.assertEqual(len(responses), 1)
        self.assertIsInstance(responses[0], Response)
        mock_get_responses_by_survey_id.assert_called_once_with(self.mock_response_data['survey_id'])

    @patch.object(ResponseRepository, 'get_response_by_id')
    def test_get_response_by_id(self, mock_get_response_by_id):
        mock_get_response_by_id.return_value = self.mock_response
        response = self.response_service.get_response_by_id('789')
        self.assertIsInstance(response, Response)
        self.assertEqual(response.survey_id, self.mock_response_data['survey_id'])
        self.assertEqual(response.user_id, self.mock_response_data['user_id'])
        self.assertEqual(response.answers, self.mock_response_data['answers'])
        mock_get_response_by_id.assert_called_once_with('789')

if __name__ == '__main__':
    unittest.main()