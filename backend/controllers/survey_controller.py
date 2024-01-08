from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest, NotFound
from backend.services.survey_service import SurveyService
from backend.utils.auth_utils import token_required

survey_controller = Blueprint('survey_controller', __name__)

@survey_controller.route('/surveys', methods=['POST'])
@token_required
def create_survey(current_user):
    try:
        data = request.get_json()
        survey = SurveyService.create_survey(data, current_user)
        return jsonify(survey), 201
    except BadRequest as e:
        return jsonify(error=str(e)), 400

@survey_controller.route('/surveys', methods=['GET'])
@token_required
def get_surveys(current_user):
    try:
        surveys = SurveyService.get_surveys_for_user(current_user)
        return jsonify(surveys), 200
    except NotFound as e:
        return jsonify(error=str(e)), 404

@survey_controller.route('/surveys/<survey_id>', methods=['GET'])
@token_required
def get_survey(current_user, survey_id):
    try:
        survey = SurveyService.get_survey_by_id(survey_id, current_user)
        return jsonify(survey), 200
    except NotFound as e:
        return jsonify(error=str(e)), 404

@survey_controller.route('/surveys/<survey_id>', methods=['PUT'])
@token_required
def update_survey(current_user, survey_id):
    try:
        data = request.get_json()
        survey = SurveyService.update_survey(survey_id, data, current_user)
        return jsonify(survey), 200
    except NotFound as e:
        return jsonify(error=str(e)), 404
    except BadRequest as e:
        return jsonify(error=str(e)), 400

@survey_controller.route('/surveys/<survey_id>', methods=['DELETE'])
@token_required
def delete_survey(current_user, survey_id):
    try:
        SurveyService.delete_survey(survey_id, current_user)
        return jsonify({'message': 'Survey deleted successfully'}), 200
    except NotFound as e:
        return jsonify(error=str(e)), 404

@survey_controller.route('/surveys/<survey_id>/responses', methods=['GET'])
@token_required
def get_survey_responses(current_user, survey_id):
    try:
        responses = SurveyService.get_responses_for_survey(survey_id, current_user)
        return jsonify(responses), 200
    except NotFound as e:
        return jsonify(error=str(e)), 404

@survey_controller.route('/surveys/<survey_id>/analyze', methods=['GET'])
@token_required
def analyze_survey_responses(current_user, survey_id):
    try:
        analysis = SurveyService.analyze_responses(survey_id, current_user)
        return jsonify(analysis), 200
    except NotFound as e:
        return jsonify(error=str(e)), 404
    except Exception as e:
        return jsonify(error=str(e)), 500

# Add more endpoints as needed for additional functionality.