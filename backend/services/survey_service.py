from datetime import datetime
from typing import List, Optional
from backend.database.survey_repository import SurveyRepository
from backend.models.survey_model import Survey, Question
from backend.services.email_service import EmailService
from backend.utils.auth_utils import AuthUtils

class SurveyService:
    def __init__(self):
        self.survey_repository = SurveyRepository()
        self.email_service = EmailService()

    def create_survey(self, user_id: str, title: str, description: str, questions: List[Question], language: str, expiration_date: Optional[datetime], max_responses: Optional[int]) -> Survey:
        survey = Survey(
            user_id=user_id,
            title=title,
            description=description,
            questions=questions,
            language=language,
            expiration_date=expiration_date,
            max_responses=max_responses,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        return self.survey_repository.add_survey(survey)

    def update_survey(self, survey_id: str, title: Optional[str], description: Optional[str], questions: Optional[List[Question]], language: Optional[str], expiration_date: Optional[datetime], max_responses: Optional[int]) -> Survey:
        survey = self.survey_repository.get_survey_by_id(survey_id)
        if survey:
            if title:
                survey.title = title
            if description:
                survey.description = description
            if questions:
                survey.questions = questions
            if language:
                survey.language = language
            if expiration_date:
                survey.expiration_date = expiration_date
            if max_responses:
                survey.max_responses = max_responses
            survey.updated_at = datetime.utcnow()
            return self.survey_repository.update_survey(survey)
        else:
            raise ValueError("Survey not found")

    def delete_survey(self, survey_id: str) -> bool:
        return self.survey_repository.delete_survey(survey_id)

    def get_survey_by_id(self, survey_id: str) -> Survey:
        return self.survey_repository.get_survey_by_id(survey_id)

    def get_all_surveys(self, user_id: str) -> List[Survey]:
        return self.survey_repository.get_surveys_by_user_id(user_id)

    def distribute_survey(self, survey_id: str, emails: List[str]) -> bool:
        survey = self.survey_repository.get_survey_by_id(survey_id)
        if survey:
            for email in emails:
                personalized_link = self.generate_survey_link(survey_id, email)
                self.email_service.send_email_invitation(email, survey.title, personalized_link)
            return True
        else:
            raise ValueError("Survey not found")

    def generate_survey_link(self, survey_id: str, email: str) -> str:
        token = AuthUtils.generate_token({'survey_id': survey_id, 'email': email})
        return f"{API_URL}/survey/{survey_id}/respond?token={token}"

    def close_survey(self, survey_id: str) -> bool:
        survey = self.survey_repository.get_survey_by_id(survey_id)
        if survey:
            survey.is_active = False
            survey.updated_at = datetime.utcnow()
            self.survey_repository.update_survey(survey)
            return True
        else:
            raise ValueError("Survey not found")