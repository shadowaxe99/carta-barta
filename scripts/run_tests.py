```python
import unittest
import os
import sys

# Add the backend directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

# Import test modules
from tests.backend.test_survey_model import TestSurveyModel
from tests.backend.test_user_model import TestUserModel
from tests.backend.test_response_model import TestResponseModel
from tests.backend.test_survey_service import TestSurveyService
from tests.backend.test_response_service import TestResponseService
from tests.backend.test_user_service import TestUserService
from tests.backend.test_email_service import TestEmailService
from tests.backend.test_analysis_service import TestAnalysisService
from tests.backend.test_survey_controller import TestSurveyController
from tests.backend.test_response_controller import TestResponseController
from tests.backend.test_user_controller import TestUserController
from tests.integration.test_carta_integration import TestCartaIntegration
from tests.integration.test_crm_integration import TestCRMIntegration
from tests.integration.test_openai_integration import TestOpenAIIntegration

# Frontend tests would be run with a JavaScript test runner like Jest

if __name__ == '__main__':
    # Initialize the test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add tests to the test suite
    suite.addTests(loader.loadTestsFromTestCase(TestSurveyModel))
    suite.addTests(loader.loadTestsFromTestCase(TestUserModel))
    suite.addTests(loader.loadTestsFromTestCase(TestResponseModel))
    suite.addTests(loader.loadTestsFromTestCase(TestSurveyService))
    suite.addTests(loader.loadTestsFromTestCase(TestResponseService))
    suite.addTests(loader.loadTestsFromTestCase(TestUserService))
    suite.addTests(loader.loadTestsFromTestCase(TestEmailService))
    suite.addTests(loader.loadTestsFromTestCase(TestAnalysisService))
    suite.addTests(loader.loadTestsFromTestCase(TestSurveyController))
    suite.addTests(loader.loadTestsFromTestCase(TestResponseController))
    suite.addTests(loader.loadTestsFromTestCase(TestUserController))
    suite.addTests(loader.loadTestsFromTestCase(TestCartaIntegration))
    suite.addTests(loader.loadTestsFromTestCase(TestCRMIntegration))
    suite.addTests(loader.loadTestsFromTestCase(TestOpenAIIntegration))

    # Run the test suite
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Exit with a non-zero exit code if there were any test failures
    sys.exit(not result.wasSuccessful())
```