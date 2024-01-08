```python
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy with no settings
db = SQLAlchemy()

def init_db(app):
    """
    Initialize the database with the Flask app.
    :param app: Flask application instance
    """
    db.init_app(app)
    with app.app_context():
        # Create all tables in the database
        # This will be equivalent to "Create Table" statements in raw SQL.
        db.create_all()
```