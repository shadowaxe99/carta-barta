import unittest
from unittest.mock import patch
from integration.openai_integration import OpenAIIntegration

class TestOpenAIIntegration(unittest.TestCase):
    def setUp(self):
        self.openai_integration = OpenAIIntegration(api_key='OPENAI_API_KEY')

    @patch('integration.openai_integration.OpenAIIntegration.analyze_survey_response')
    def test_analyze_survey_response(self, mock_analyze):
        # Mock response from OpenAI API
        mock_response = {
            'choices': [{
                'text': 'Positive sentiment detected in the response.'
            }]
        }
        mock_analyze.return_value = mock_response

        # Test data
        survey_response = "I love using Olvy, it has streamlined our cap table management."

        # Call the method
        analysis_result = self.openai_integration.analyze_survey_response(survey_response)

        # Assert the expected outcome
        self.assertEqual(analysis_result, mock_response)
        mock_analyze.assert_called_once_with(survey_response)

    @patch('integration.openai_integration.OpenAIIntegration.extract_keywords')
    def test_extract_keywords(self, mock_extract):
        # Mock response from OpenAI API
        mock_response = {
            'keywords': ['Olvy', 'cap table management', 'streamlined']
        }
        mock_extract.return_value = mock_response

        # Test data
        survey_response = "I love using Olvy, it has streamlined our cap table management."

        # Call the method
        keywords_result = self.openai_integration.extract_keywords(survey_response)

        # Assert the expected outcome
        self.assertEqual(keywords_result, mock_response)
        mock_extract.assert_called_once_with(survey_response)

if __name__ == '__main__':
    unittest.main()