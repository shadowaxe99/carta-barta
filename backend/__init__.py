```python
from flask import Flask
from backend.config import Config
from backend.database.db import initialize_db
from backend.api.survey_routes import survey_blueprint
from backend.api.user_routes import user_blueprint
from backend.api.response_routes import response_blueprint

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    initialize_db(app)

    app.register_blueprint(survey_blueprint, url_prefix='/api/surveys')
    app.register_blueprint(user_blueprint, url_prefix='/api/users')
    app.register_blueprint(response_blueprint, url_prefix='/api/responses')

    return app
```