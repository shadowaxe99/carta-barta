import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from backend.models.user_model import User
from backend.database.db import get_db_session

SECRET_KEY = 'YOUR_SECRET_KEY'  # Replace with your actual secret key

def encode_auth_token(user_id):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            SECRET_KEY,
            algorithm='HS256'
        )
    except Exception as e:
        return e

def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, SECRET_KEY, algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

def hash_password(password):
    """
    Hash a password for storing.
    """
    return generate_password_hash(password)

def check_password(hashed_password, password):
    """
    Check hashed password. Using werkzeug to check hashed password.
    """
    return check_password_hash(hashed_password, password)

def authenticate_user(email, password):
    """
    Authenticate the user using email and password.
    """
    session = get_db_session()
    user = session.query(User).filter_by(email=email).first()
    if user and check_password(user.password, password):
        auth_token = encode_auth_token(user.id)
        return auth_token, None
    else:
        return None, 'Invalid email or password'

def create_user(email, password):
    """
    Create a new user with the provided email and password.
    """
    session = get_db_session()
    user = User(email=email, password=hash_password(password))
    session.add(user)
    session.commit()
    return user

def get_user_by_id(user_id):
    """
    Get a user by their ID.
    """
    session = get_db_session()
    return session.query(User).filter_by(id=user_id).first()