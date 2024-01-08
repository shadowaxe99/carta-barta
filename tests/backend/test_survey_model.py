import unittest
from backend.models.survey_model import Survey
from backend.database.db import db_session

class TestSurveyModel(unittest.TestCase):
    def setUp(self):
        # Setup a test database (could be an in-memory database)
        self.db = db_session

    def tearDown(self):
        # Clean up and remove the test database
        self.db.remove()

    def test_create_survey(self):
        # Test survey creation
        survey = Survey(title="Customer Feedback", description="Survey for customer feedback on our services.")
        self.db.add(survey)
        self.db.commit()
        self.assertIsNotNone(survey.id)
        self.assertEqual(survey.title, "Customer Feedback")
        self.assertEqual(survey.description, "Survey for customer feedback on our services.")

    def test_update_survey(self):
        # Test survey update
        survey = Survey(title="Employee Feedback", description="Survey for employee feedback on workplace environment.")
        self.db.add(survey)
        self.db.commit()
        survey.title = "Updated Employee Feedback"
        self.db.commit()
        updated_survey = self.db.query(Survey).filter(Survey.id == survey.id).first()
        self.assertEqual(updated_survey.title, "Updated Employee Feedback")

    def test_delete_survey(self):
        # Test survey deletion
        survey = Survey(title="Investor Feedback", description="Survey for investor feedback on company performance.")
        self.db.add(survey)
        self.db.commit()
        self.db.delete(survey)
        self.db.commit()
        deleted_survey = self.db.query(Survey).filter(Survey.id == survey.id).first()
        self.assertIsNone(deleted_survey)

    def test_survey_to_dict(self):
        # Test conversion of survey data to a dictionary
        survey = Survey(title="Market Research", description="Survey for market research on product demand.")
        self.db.add(survey)
        self.db.commit()
        survey_dict = survey.to_dict()
        self.assertIsInstance(survey_dict, dict)
        self.assertEqual(survey_dict['title'], "Market Research")
        self.assertEqual(survey_dict['description'], "Survey for market research on product demand.")

if __name__ == '__main__':
    unittest.main()