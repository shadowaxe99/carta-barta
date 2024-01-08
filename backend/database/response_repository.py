from sqlalchemy.orm import Session
from backend.models.response_model import Response
from typing import List, Optional
from backend.database.db import get_db


class ResponseRepository:

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_response(self, response_data: dict) -> Response:
        new_response = Response(**response_data)
        self.db_session.add(new_response)
        self.db_session.commit()
        self.db_session.refresh(new_response)
        return new_response

    def get_response_by_id(self, response_id: int) -> Optional[Response]:
        return self.db_session.query(Response).filter(Response.id == response_id).first()

    def get_all_responses(self) -> List[Response]:
        return self.db_session.query(Response).all()

    def get_responses_by_survey_id(self, survey_id: int) -> List[Response]:
        return self.db_session.query(Response).filter(Response.survey_id == survey_id).all()

    def update_response(self, response_id: int, update_data: dict) -> Optional[Response]:
        response = self.get_response_by_id(response_id)
        if response:
            for key, value in update_data.items():
                setattr(response, key, value)
            self.db_session.commit()
            self.db_session.refresh(response)
        return response

    def delete_response(self, response_id: int) -> bool:
        response = self.get_response_by_id(response_id)
        if response:
            self.db_session.delete(response)
            self.db_session.commit()
            return True
        return False


# Example usage:
# db = next(get_db())
# response_repo = ResponseRepository(db)
# response = response_repo.create_response({'survey_id': 1, 'user_id': 1, 'content': 'Sample response'})
# print(response.id)