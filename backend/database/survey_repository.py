from sqlalchemy.orm import Session
from sqlalchemy import update
from .db import get_db
from backend.models.survey_model import Survey

class SurveyRepository:

    def __init__(self, db_session: Session = None):
        self.db = db_session or next(get_db())

    def create_survey(self, survey_data: dict) -> Survey:
        new_survey = Survey(**survey_data)
        self.db.add(new_survey)
        self.db.commit()
        self.db.refresh(new_survey)
        return new_survey

    def get_survey_by_id(self, survey_id: int) -> Survey:
        return self.db.query(Survey).filter(Survey.id == survey_id).first()

    def get_all_surveys(self) -> list:
        return self.db.query(Survey).all()

    def update_survey(self, survey_id: int, update_data: dict) -> Survey:
        self.db.execute(update(Survey).where(Survey.id == survey_id).values(**update_data))
        self.db.commit()
        return self.get_survey_by_id(survey_id)

    def delete_survey(self, survey_id: int) -> None:
        survey_to_delete = self.get_survey_by_id(survey_id)
        self.db.delete(survey_to_delete)
        self.db.commit()

    def get_surveys_by_user_id(self, user_id: int) -> list:
        return self.db.query(Survey).filter(Survey.user_id == user_id).all()