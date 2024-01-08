```python
from werkzeug.security import generate_password_hash, check_password_hash
from backend.models.user_model import User
from backend.database.db import get_db_session
from sqlalchemy.exc import SQLAlchemyError

class UserService:

    @staticmethod
    def create_user(username, email, password):
        session = get_db_session()
        try:
            hashed_password = generate_password_hash(password)
            user = User(username=username, email=email, password=hashed_password)
            session.add(user)
            session.commit()
            return user
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @staticmethod
    def authenticate_user(email, password):
        session = get_db_session()
        try:
            user = session.query(User).filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                return user
            else:
                return None
        except SQLAlchemyError as e:
            raise e
        finally:
            session.close()

    @staticmethod
    def get_user_by_id(user_id):
        session = get_db_session()
        try:
            user = session.query(User).get(user_id)
            return user
        except SQLAlchemyError as e:
            raise e
        finally:
            session.close()

    @staticmethod
    def update_user(user_id, **kwargs):
        session = get_db_session()
        try:
            user = session.query(User).get(user_id)
            if not user:
                return None
            for key, value in kwargs.items():
                setattr(user, key, value)
            session.commit()
            return user
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @staticmethod
    def delete_user(user_id):
        session = get_db_session()
        try:
            user = session.query(User).get(user_id)
            if not user:
                return None
            session.delete(user)
            session.commit()
            return user_id
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()
```