import unittest
from backend.models.response_model import Response
from backend.database.db import db_session

class TestResponseModel(unittest.TestCase):

    def setUp(self):
        # Assuming db_session is a context manager that provides a transactional scope around a series of operations
        self.db_session = db_session()

    def tearDown(self):
        self.db_session.rollback()
        self.db_session.close()

    def test_create_response(self):
        response = Response(
            survey_id=1,
            user_id=1,
            answers={"Q1": "Yes", "Q2": "No"}
        )
        self.db_session.add(response)
        self.db_session.commit()

        saved_response = self.db_session.query(Response).filter_by(survey_id=1, user_id=1).first()
        self.assertIsNotNone(saved_response)
        self.assertEqual(saved_response.answers, {"Q1": "Yes", "Q2": "No"})

    def test_response_repr(self):
        response = Response(
            survey_id=1,
            user_id=1,
            answers={"Q1": "Yes", "Q2": "No"}
        )
        self.assertEqual(repr(response), f"<Response(survey_id={response.survey_id}, user_id={response.user_id})>")

    def test_update_response(self):
        response = Response(
            survey_id=1,
            user_id=1,
            answers={"Q1": "Yes", "Q2": "No"}
        )
        self.db_session.add(response)
        self.db_session.commit()

        response.answers = {"Q1": "Maybe", "Q2": "No", "Q3": "Yes"}
        self.db_session.commit()

        updated_response = self.db_session.query(Response).filter_by(survey_id=1, user_id=1).first()
        self.assertEqual(updated_response.answers, {"Q1": "Maybe", "Q2": "No", "Q3": "Yes"})

    def test_delete_response(self):
        response = Response(
            survey_id=1,
            user_id=1,
            answers={"Q1": "Yes", "Q2": "No"}
        )
        self.db_session.add(response)
        self.db_session.commit()

        self.db_session.delete(response)
        self.db_session.commit()

        deleted_response = self.db_session.query(Response).filter_by(survey_id=1, user_id=1).first()
        self.assertIsNone(deleted_response)

if __name__ == '__main__':
    unittest.main()