```python
import openai
from config import OPENAI_API_KEY

class OpenAIIntegration:
    def __init__(self):
        self.openai_api_key = OPENAI_API_KEY
        openai.api_key = self.openai_api_key

    def analyze_survey_response(self, response_text):
        try:
            analysis = openai.Completion.create(
                engine="text-davinci-003",
                prompt=self.generate_prompt(response_text),
                max_tokens=1024
            )
            return analysis.choices[0].text.strip()
        except openai.error.OpenAIError as e:
            print(f"An error occurred: {e}")
            return None

    @staticmethod
    def generate_prompt(text):
        return f"Please analyze the following survey response for sentiment and key themes:\n\n'{text}'\n\nThe sentiment can be positive, neutral, or negative and the key themes are the main topics mentioned in the response."

# Example usage:
# openai_integration = OpenAIIntegration()
# analysis = openai_integration.analyze_survey_response("I love the new features, but I think the user interface could be improved.")
# print(analysis)
```