from flask import Blueprint, request, jsonify
from backend.services.survey_service import SurveyService
from backend.services.auth_utils import token_required
from backend.models.survey_model import SurveySchema

survey_routes = Blueprint('survey_routes', __name__)
survey_service = SurveyService()
survey_schema = SurveySchema()

@survey_routes.route('/surveys', methods=['POST'])
@token_required
def create_survey(current_user):
    data = request.get_json()
    errors = survey_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    survey = survey_service.create_survey(data, current_user)
    return survey_schema.dump(survey), 201

@survey_routes.route('/surveys', methods=['GET'])
@token_required
def get_surveys(current_user):
    surveys = survey_service.get_surveys(current_user)
    return jsonify(survey_schema.dump(surveys, many=True)), 200

@survey_routes.route('/surveys/<int:survey_id>', methods=['GET'])
@token_required
def get_survey(current_user, survey_id):
    survey = survey_service.get_survey_by_id(survey_id, current_user)
    if survey is None:
        return jsonify({'message': 'Survey not found'}), 404
    return survey_schema.dump(survey), 200

@survey_routes.route('/surveys/<int:survey_id>', methods=['PUT'])
@token_required
def update_survey(current_user, survey_id):
    data = request.get_json()
    errors = survey_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    survey = survey_service.update_survey(survey_id, data, current_user)
    if survey is None:
        return jsonify({'message': 'Survey not found'}), 404
    return survey_schema.dump(survey), 200

@survey_routes.route('/surveys/<int:survey_id>', methods=['DELETE'])
@token_required
def delete_survey(current_user, survey_id):
    result = survey_service.delete_survey(survey_id, current_user)
    if result is None:
        return jsonify({'message': 'Survey not found'}), 404
    return jsonify({'message': 'Survey deleted'}), 200

@survey_routes.route('/surveys/<int:survey_id>/responses', methods=['GET'])
@token_required
def get_survey_responses(current_user, survey_id):
    responses = survey_service.get_survey_responses(survey_id, current_user)
    if responses is None:
        return jsonify({'message': 'Survey not found or you do not have access to its responses'}), 404
    return jsonify(responses), 200

@survey_routes.route('/surveys/<int:survey_id>/analyze', methods=['GET'])
@token_required
def analyze_survey_responses(current_user, survey_id):
    analysis = survey_service.analyze_survey_responses(survey_id, current_user)
    if analysis is None:
        return jsonify({'message': 'Survey not found or no responses to analyze'}), 404
    return jsonify(analysis), 200

# Add more routes as needed for additional functionality.