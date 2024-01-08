"""Initialize test suite for the backend components of Olvy's Customer Survey Tool."""

import unittest

# Import test modules
from tests.backend.test_survey_model import SurveyModelTestCase
from tests.backend.test_user_model import UserModelTestCase
from tests.backend.test_response_model import ResponseModelTestCase
from tests.backend.test_survey_service import SurveyServiceTestCase
from tests.backend.test_response_service import ResponseServiceTestCase
from tests.backend.test_user_service import UserServiceTestCase
from tests.backend.test_email_service import EmailServiceTestCase
from tests.backend.test_analysis_service import AnalysisServiceTestCase
from tests.backend.test_survey_controller import SurveyControllerTestCase
from tests.backend.test_response_controller import ResponseControllerTestCase
from tests.backend.test_user_controller import UserControllerTestCase

# Initialize a test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Add tests to the test suite
suite.addTests(loader.loadTestsFromTestCase(SurveyModelTestCase))
suite.addTests(loader.loadTestsFromTestCase(UserModelTestCase))
suite.addTests(loader.loadTestsFromTestCase(ResponseModelTestCase))
suite.addTests(loader.loadTestsFromTestCase(SurveyServiceTestCase))
suite.addTests(loader.loadTestsFromTestCase(ResponseServiceTestCase))
suite.addTests(loader.loadTestsFromTestCase(UserServiceTestCase))
suite.addTests(loader.loadTestsFromTestCase(EmailServiceTestCase))
suite.addTests(loader.loadTestsFromTestCase(AnalysisServiceTestCase))
suite.addTests(loader.loadTestsFromTestCase(SurveyControllerTestCase))
suite.addTests(loader.loadTestsFromTestCase(ResponseControllerTestCase))
suite.addTests(loader.loadTestsFromTestCase(UserControllerTestCase))

# Run the test suite
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)