import unittest
from backend.models.user_model import User
from backend.database.db import db_session

class TestUserModel(unittest.TestCase):
    def setUp(self):
        # Assuming db_session is a context manager that provides a transactional scope
        self.db_session = db_session()

    def tearDown(self):
        self.db_session.rollback()
        self.db_session.close()

    def test_create_user(self):
        new_user = User(username='testuser', email='testuser@example.com', password='TestPassword123')
        self.db_session.add(new_user)
        self.db_session.commit()

        user = self.db_session.query(User).filter_by(username='testuser').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.check_password('TestPassword123'))

    def test_user_representation(self):
        user = User(username='testuser', email='testuser@example.com', password='TestPassword123')
        self.assertEqual(user.__repr__(), '<User testuser>')

    def test_password_hashing(self):
        user = User(username='testuser', email='testuser@example.com', password='TestPassword123')
        self.assertFalse(user.password == 'TestPassword123')
        self.assertTrue(user.check_password('TestPassword123'))

    def test_duplicate_username(self):
        user1 = User(username='testuser', email='user1@example.com', password='TestPassword123')
        user2 = User(username='testuser', email='user2@example.com', password='TestPassword123')
        self.db_session.add(user1)
        self.db_session.commit()

        with self.assertRaises(Exception):
            self.db_session.add(user2)
            self.db_session.commit()

    def test_duplicate_email(self):
        user1 = User(username='user1', email='testuser@example.com', password='TestPassword123')
        user2 = User(username='user2', email='testuser@example.com', password='TestPassword123')
        self.db_session.add(user1)
        self.db_session.commit()

        with self.assertRaises(Exception):
            self.db_session.add(user2)
            self.db_session.commit()

if __name__ == '__main__':
    unittest.main()