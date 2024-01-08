import unittest
from integration.crm_integration import CRMIntegration
from backend.models.user_model import User
from backend.database.db import db_session

class TestCRMIntegration(unittest.TestCase):
    def setUp(self):
        self.crm_integration = CRMIntegration()
        self.user = User(email="testuser@example.com", full_name="Test User")
        db_session.add(self.user)
        db_session.commit()

    def test_sync_user_data(self):
        # Test the synchronization of user data with the CRM
        result = self.crm_integration.sync_user_data(self.user)
        self.assertTrue(result)

    def test_fetch_crm_data(self):
        # Test fetching data from the CRM for a specific user
        crm_data = self.crm_integration.fetch_crm_data(self.user.email)
        self.assertIsNotNone(crm_data)
        self.assertEqual(crm_data.get('email'), self.user.email)

    def tearDown(self):
        # Clean up the database after tests
        db_session.delete(self.user)
        db_session.commit()

if __name__ == '__main__':
    unittest.main()