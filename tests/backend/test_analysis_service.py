import unittest
from unittest.mock import patch
from backend.services.analysis_service import AnalysisService
from backend.models.response_model import Response

class TestAnalysisService(unittest.TestCase):

    def setUp(self):
        self.analysis_service = AnalysisService()
        self.sample_responses = [
            Response(response_data="I love the product!", sentiment_score=0.95),
            Response(response_data="The product is okay, but could be better.", sentiment_score=0.1),
            Response(response_data="I really dislike the product.", sentiment_score=-0.85)
        ]

    @patch('backend.services.analysis_service.OpenAIIntegration')
    def test_analyze_sentiment(self, mock_openai_integration):
        mock_openai_integration.analyze_sentiment.return_value = {
            "sentiments": [0.95, 0.1, -0.85]
        }

        sentiments = self.analysis_service.analyze_sentiment([r.response_data for r in self.sample_responses])
        self.assertEqual(sentiments, [0.95, 0.1, -0.85])

    @patch('backend.services.analysis_service.OpenAIIntegration')
    def test_extract_keywords(self, mock_openai_integration):
        mock_openai_integration.extract_keywords.return_value = {
            "keywords": [["product"], ["product", "better"], ["dislike", "product"]]
        }

        keywords = self.analysis_service.extract_keywords([r.response_data for r in self.sample_responses])
        self.assertEqual(keywords, [["product"], ["product", "better"], ["dislike", "product"]])

    def test_calculate_average_sentiment(self):
        average_sentiment = self.analysis_service.calculate_average_sentiment([r.sentiment_score for r in self.sample_responses])
        self.assertAlmostEqual(average_sentiment, 0.06666666666, places=2)

    def test_generate_insights(self):
        insights = self.analysis_service.generate_insights(self.sample_responses)
        self.assertIsInstance(insights, dict)
        self.assertIn('average_sentiment', insights)
        self.assertIn('sentiment_distribution', insights)
        self.assertIn('keyword_frequencies', insights)

if __name__ == '__main__':
    unittest.main()