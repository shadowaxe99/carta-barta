from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from backend.models.user_model import User
from backend.services.user_service import UserService
from backend.utils.auth_utils import generate_token, verify_token
from backend.database.db import db_session

user_routes = Blueprint('user_routes', __name__)
user_service = UserService()

@user_routes.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    hashed_password = generate_password_hash(password)
    
    if user_service.get_user_by_email(email):
        return jsonify({'message': 'Email already exists'}), 409
    
    new_user = User(email=email, password=hashed_password)
    db_session.add(new_user)
    db_session.commit()
    
    return jsonify({'message': 'User created successfully'}), 201

@user_routes.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    user = user_service.get_user_by_email(email)
    
    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    token = generate_token(user.id)
    
    return jsonify({'token': token}), 200

@user_routes.route('/user', methods=['GET'])
def get_user():
    token = request.headers.get('Authorization').split(" ")[1]
    user_id = verify_token(token)
    
    if not user_id:
        return jsonify({'message': 'Invalid or expired token'}), 401
    
    user = user_service.get_user_by_id(user_id)
    
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    user_data = {
        'id': user.id,
        'email': user.email
    }
    
    return jsonify(user_data), 200

@user_routes.route('/user', methods=['DELETE'])
def delete_user():
    token = request.headers.get('Authorization').split(" ")[1]
    user_id = verify_token(token)
    
    if not user_id:
        return jsonify({'message': 'Invalid or expired token'}), 401
    
    user_service.delete_user(user_id)
    
    return jsonify({'message': 'User deleted successfully'}), 200

# Add more user-related routes as needed

# Remember to close the database session if the app context ends
@user_routes.teardown_app_request
def shutdown_session(exception=None):
    db_session.remove()