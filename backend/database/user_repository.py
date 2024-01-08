```python
from sqlalchemy.exc import SQLAlchemyError
from backend.database.db import db_session
from backend.models.user_model import User

class UserRepository:

    @staticmethod
    def create_user(user_data):
        try:
            user = User(**user_data)
            db_session.add(user)
            db_session.commit()
            return user
        except SQLAlchemyError as e:
            db_session.rollback()
            raise e

    @staticmethod
    def get_user_by_id(user_id):
        try:
            return db_session.query(User).filter(User.id == user_id).one_or_none()
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def get_user_by_email(email):
        try:
            return db_session.query(User).filter(User.email == email).one_or_none()
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def update_user(user_id, update_data):
        try:
            user = db_session.query(User).filter(User.id == user_id).one_or_none()
            if user:
                for key, value in update_data.items():
                    setattr(user, key, value)
                db_session.commit()
                return user
            return None
        except SQLAlchemyError as e:
            db_session.rollback()
            raise e

    @staticmethod
    def delete_user(user_id):
        try:
            user = db_session.query(User).filter(User.id == user_id).one_or_none()
            if user:
                db_session.delete(user)
                db_session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            db_session.rollback()
            raise e

    @staticmethod
    def list_users():
        try:
            return db_session.query(User).all()
        except SQLAlchemyError as e:
            raise e
```