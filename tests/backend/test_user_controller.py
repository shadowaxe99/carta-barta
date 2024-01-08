import unittest
from unittest.mock import patch
from backend.controllers.user_controller import UserController
from backend.models.user_model import User
from backend.database.db import db_session

class TestUserController(unittest.TestCase):
    def setUp(self):
        self.user_controller = UserController()
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'securepassword123'
        }
        self.user = User(username=self.user_data['username'], email=self.user_data['email'])
        self.user.set_password(self.user_data['password'])

    def tearDown(self):
        db_session.remove()

    @patch('backend.database.user_repository.UserRepository.create_user')
    def test_create_user(self, mock_create_user):
        mock_create_user.return_value = self.user
        created_user = self.user_controller.create_user(self.user_data)
        self.assertEqual(created_user.username, self.user_data['username'])
        self.assertEqual(created_user.email, self.user_data['email'])
        self.assertTrue(created_user.check_password(self.user_data['password']))

    @patch('backend.database.user_repository.UserRepository.get_user_by_email')
    def test_authenticate_user_success(self, mock_get_user_by_email):
        mock_get_user_by_email.return_value = self.user
        authenticated_user = self.user_controller.authenticate_user(self.user_data['email'], self.user_data['password'])
        self.assertIsNotNone(authenticated_user)

    @patch('backend.database.user_repository.UserRepository.get_user_by_email')
    def test_authenticate_user_failure(self, mock_get_user_by_email):
        mock_get_user_by_email.return_value = self.user
        authenticated_user = self.user_controller.authenticate_user(self.user_data['email'], 'wrongpassword')
        self.assertIsNone(authenticated_user)

if __name__ == '__main__':
    unittest.main()