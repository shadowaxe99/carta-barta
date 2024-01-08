```python
from flask import Flask, jsonify, request
from flask_cors import CORS
from database.db import initialize_db
from api.survey_routes import survey_blueprint
from api.user_routes import user_blueprint
from api.response_routes import response_blueprint
from utils.auth_utils import AuthError, requires_auth

app = Flask(__name__)
CORS(app)

# Load configuration from config.py
app.config.from_object('backend.config')

# Initialize database
initialize_db(app)

# Register blueprints
app.register_blueprint(survey_blueprint, url_prefix='/api/surveys')
app.register_blueprint(user_blueprint, url_prefix='/api/users')
app.register_blueprint(response_blueprint, url_prefix='/api/responses')

# Error handler for AuthError
@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

# Health check route
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run()
```