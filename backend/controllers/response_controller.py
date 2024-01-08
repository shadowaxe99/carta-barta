from flask import Blueprint, request, jsonify
from backend.services.response_service import ResponseService
from backend.services.auth_utils import login_required
from backend.models.response_model import ResponseSchema

response_blueprint = Blueprint('response_blueprint', __name__)
response_service = ResponseService()
response_schema = ResponseSchema()

@response_blueprint.route('/responses', methods=['POST'])
@login_required
def submit_response():
    try:
        data = request.get_json()
        errors = response_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        response = response_service.create_response(data)
        return response_schema.jsonify(response), 201
    except Exception as e:
        return jsonify(str(e)), 500

@response_blueprint.route('/responses/<survey_id>', methods=['GET'])
@login_required
def get_responses(survey_id):
    try:
        responses = response_service.get_responses_by_survey(survey_id)
        return response_schema.jsonify(responses, many=True), 200
    except Exception as e:
        return jsonify(str(e)), 500

@response_blueprint.route('/responses/<response_id>', methods=['DELETE'])
@login_required
def delete_response(response_id):
    try:
        response_service.delete_response(response_id)
        return jsonify({'message': 'Response deleted successfully'}), 200
    except Exception as e:
        return jsonify(str(e)), 500

@response_blueprint.route('/responses/analyze/<survey_id>', methods=['GET'])
@login_required
def analyze_responses(survey_id):
    try:
        analysis = response_service.analyze_survey_responses(survey_id)
        return jsonify(analysis), 200
    except Exception as e:
        return jsonify(str(e)), 500

# Register the blueprint in the app factory or main application module
# app.register_blueprint(response_blueprint, url_prefix='/api')