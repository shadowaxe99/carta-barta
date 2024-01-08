```python
import requests
from backend.config import API_URL

class CRMIntegration:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        self.crm_base_url = "https://api.crmplatform.com"

    def sync_survey_data(self, survey_id):
        """
        Sync survey data with the CRM platform.
        """
        survey_data = self.get_survey_data(survey_id)
        if survey_data:
            response = requests.post(
                f"{self.crm_base_url}/surveys",
                headers=self.headers,
                json=survey_data
            )
            return response.json()
        else:
            return None

    def get_survey_data(self, survey_id):
        """
        Retrieve survey data from Olvy's backend.
        """
        response = requests.get(
            f"{API_URL}/surveys/{survey_id}",
            headers=self.headers
        )
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def sync_respondent_data(self, respondent_id):
        """
        Sync respondent data with the CRM platform.
        """
        respondent_data = self.get_respondent_data(respondent_id)
        if respondent_data:
            response = requests.post(
                f"{self.crm_base_url}/respondents",
                headers=self.headers,
                json=respondent_data
            )
            return response.json()
        else:
            return None

    def get_respondent_data(self, respondent_id):
        """
        Retrieve respondent data from Olvy's backend.
        """
        response = requests.get(
            f"{API_URL}/respondents/{respondent_id}",
            headers=self.headers
        )
        if response.status_code == 200:
            return response.json()
        else:
            return None

# Example usage:
# crm_integration = CRMIntegration(api_key='your_crm_api_key')
# survey_sync_result = crm_integration.sync_survey_data(survey_id='12345')
# respondent_sync_result = crm_integration.sync_respondent_data(respondent_id='67890')
```