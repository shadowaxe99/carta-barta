from flask import Blueprint
from .survey_routes import survey_blueprint
from .user_routes import user_blueprint
from .response_routes import response_blueprint

api_blueprint = Blueprint('api', __name__)

api_blueprint.register_blueprint(survey_blueprint, url_prefix='/surveys')
api_blueprint.register_blueprint(user_blueprint, url_prefix='/users')
api_blueprint.register_blueprint(response_blueprint, url_prefix='/responses')