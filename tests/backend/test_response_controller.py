import unittest
from unittest.mock import patch
from backend.controllers.response_controller import ResponseController
from backend.models.response_model import Response
from backend.database.db import db_session
from backend.database.response_repository import ResponseRepository

class TestResponseController(unittest.TestCase):

    def setUp(self):
        self.controller = ResponseController()
        self.mock_response_data = {
            'survey_id': 1,
            'user_id': 1,
            'answers': {
                'question_1': 'Answer 1',
                'question_2': 'Answer 2'
            }
        }
        self.mock_response = Response(
            survey_id=self.mock_response_data['survey_id'],
            user_id=self.mock_response_data['user_id'],
            answers=self.mock_response_data['answers']
        )

    @patch.object(ResponseRepository, 'add_response')
    def test_submit_response(self, mock_add_response):
        mock_add_response.return_value = self.mock_response
        response = self.controller.submit_response(self.mock_response_data)
        self.assertIsInstance(response, Response)
        self.assertEqual(response.survey_id, self.mock_response_data['survey_id'])
        self.assertEqual(response.user_id, self.mock_response_data['user_id'])
        self.assertEqual(response.answers, self.mock_response_data['answers'])

    @patch.object(ResponseRepository, 'get_responses_by_survey')
    def test_get_responses(self, mock_get_responses_by_survey):
        mock_get_responses_by_survey.return_value = [self.mock_response]
        responses = self.controller.get_responses(1)
        self.assertIsInstance(responses, list)
        self.assertEqual(len(responses), 1)
        self.assertIsInstance(responses[0], Response)

    @patch.object(db_session, 'commit')
    def test_response_commit(self, mock_db_commit):
        self.controller.submit_response(self.mock_response_data)
        mock_db_commit.assert_called_once()

    @patch.object(db_session, 'rollback')
    @patch.object(ResponseRepository, 'add_response', side_effect=Exception('Test exception'))
    def test_response_rollback_on_exception(self, mock_add_response, mock_db_rollback):
        with self.assertRaises(Exception):
            self.controller.submit_response(self.mock_response_data)
        mock_db_rollback.assert_called_once()

if __name__ == '__main__':
    unittest.main()