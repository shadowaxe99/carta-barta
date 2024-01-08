from flask import Blueprint, request, jsonify
from backend.services.response_service import ResponseService
from backend.services.auth_utils import token_required
from backend.models.response_model import ResponseSchema

response_routes = Blueprint('response_routes', __name__, url_prefix='/api/responses')

@response_routes.route('/', methods=['POST'])
@token_required
def submit_response(current_user):
    data = request.get_json()
    response_service = ResponseService()
    response_schema = ResponseSchema()
    
    errors = response_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    
    try:
        response = response_service.create_response(data, current_user)
        return response_schema.jsonify(response), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@response_routes.route('/<int:survey_id>', methods=['GET'])
@token_required
def get_responses(current_user, survey_id):
    response_service = ResponseService()
    response_schema = ResponseSchema(many=True)
    
    try:
        responses = response_service.get_responses_for_survey(survey_id, current_user)
        return response_schema.jsonify(responses), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@response_routes.route('/<int:response_id>', methods=['GET'])
@token_required
def get_response(current_user, response_id):
    response_service = ResponseService()
    response_schema = ResponseSchema()
    
    try:
        response = response_service.get_response_by_id(response_id, current_user)
        return response_schema.jsonify(response), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 404

@response_routes.route('/<int:response_id>', methods=['DELETE'])
@token_required
def delete_response(current_user, response_id):
    response_service = ResponseService()
    
    try:
        response_service.delete_response(response_id, current_user)
        return jsonify({"message": "Response deleted successfully"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 404

# Additional routes can be added here for other response-related operations

# Register the blueprint in the app initialization file (app.py)
# app.register_blueprint(response_routes)