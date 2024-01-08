import unittest
from unittest.mock import patch
from integration.carta_integration import CartaIntegration

class TestCartaIntegration(unittest.TestCase):
    def setUp(self):
        self.carta_integration = CartaIntegration(api_url='https://api.carta.com', api_key='CARTA_API_KEY')

    @patch('integration.carta_integration.requests')
    def test_import_cap_table_data(self, mock_requests):
        mock_response = mock_requests.get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'success': True,
            'data': {
                'cap_table': [
                    {'shareholder': 'John Doe', 'shares': 1000},
                    {'shareholder': 'Jane Smith', 'shares': 500}
                ]
            }
        }

        result = self.carta_integration.import_cap_table_data()
        self.assertTrue(result['success'])
        self.assertEqual(len(result['data']['cap_table']), 2)

    @patch('integration.carta_integration.requests')
    def test_export_cap_table_data(self, mock_requests):
        mock_response = mock_requests.post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'success': True,
            'message': 'Cap table data exported successfully.'
        }

        cap_table_data = [
            {'shareholder': 'John Doe', 'shares': 1000},
            {'shareholder': 'Jane Smith', 'shares': 500}
        ]
        result = self.carta_integration.export_cap_table_data(cap_table_data)
        self.assertTrue(result['success'])
        self.assertEqual(result['message'], 'Cap table data exported successfully.')

    @patch('integration.carta_integration.requests')
    def test_integration_error_handling(self, mock_requests):
        mock_response = mock_requests.get.return_value
        mock_response.status_code = 500
        mock_response.json.return_value = {
            'success': False,
            'error': 'Internal server error'
        }

        with self.assertRaises(Exception) as context:
            self.carta_integration.import_cap_table_data()

        self.assertTrue('Internal server error' in str(context.exception))

if __name__ == '__main__':
    unittest.main()