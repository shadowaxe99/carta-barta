import unittest
from unittest.mock import patch
from backend.services.user_service import UserService
from backend.models.user_model import User
from backend.database.db import db_session

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService()
        self.user_data = {
            'email': 'test@example.com',
            'password': 'securepassword123',
            'name': 'Test User'
        }
        self.user = User(**self.user_data)

    def tearDown(self):
        db_session.remove()

    @patch('backend.database.user_repository.UserRepository.create_user')
    def test_create_user(self, mock_create_user):
        mock_create_user.return_value = self.user
        created_user = self.user_service.create_user(self.user_data)
        self.assertEqual(created_user.email, self.user_data['email'])
        self.assertEqual(created_user.name, self.user_data['name'])

    @patch('backend.database.user_repository.UserRepository.get_user_by_email')
    def test_authenticate_user_success(self, mock_get_user_by_email):
        mock_get_user_by_email.return_value = self.user
        authenticated_user = self.user_service.authenticate_user(self.user_data['email'], self.user_data['password'])
        self.assertIsNotNone(authenticated_user)

    @patch('backend.database.user_repository.UserRepository.get_user_by_email')
    def test_authenticate_user_failure(self, mock_get_user_by_email):
        mock_get_user_by_email.return_value = None
        authenticated_user = self.user_service.authenticate_user(self.user_data['email'], 'wrongpassword')
        self.assertIsNone(authenticated_user)

    @patch('backend.database.user_repository.UserRepository.get_user_by_email')
    def test_get_user_by_email(self, mock_get_user_by_email):
        mock_get_user_by_email.return_value = self.user
        user = self.user_service.get_user_by_email(self.user_data['email'])
        self.assertEqual(user.email, self.user_data['email'])

    @patch('backend.database.user_repository.UserRepository.update_user')
    def test_update_user(self, mock_update_user):
        updated_data = {'name': 'Updated Test User'}
        mock_update_user.return_value = updated_data
        updated_user = self.user_service.update_user(self.user.id, updated_data)
        self.assertEqual(updated_user['name'], updated_data['name'])

    @patch('backend.database.user_repository.UserRepository.delete_user')
    def test_delete_user(self, mock_delete_user):
        mock_delete_user.return_value = True
        result = self.user_service.delete_user(self.user.id)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()