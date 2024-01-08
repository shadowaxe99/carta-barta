```python
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from backend.database.db import Base
from backend.models.user_model import User
from backend.models.survey_model import Survey
from backend.models.response_model import Response

# Database configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///olvy.db')

def setup_database():
    # Create an engine that stores data in the local directory's olvy.db file.
    engine = create_engine(DATABASE_URL)

    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = scoped_session(Session)

    # Add sample data to the database
    add_sample_data(session)

    # Commit the changes
    session.commit()

    print("Database setup completed successfully.")

def add_sample_data(session):
    # Add sample users
    user1 = User(username='founder', email='founder@example.com', hashed_password='hashed_password')
    user2 = User(username='hr_manager', email='hr_manager@example.com', hashed_password='hashed_password')
    user3 = User(username='investor_relations', email='investor_relations@example.com', hashed_password='hashed_password')

    session.add(user1)
    session.add(user2)
    session.add(user3)

    # Add sample surveys
    survey1 = Survey(title='Stakeholder Feedback', creator_id=user1.id)
    survey2 = Survey(title='Employee Satisfaction', creator_id=user2.id)
    survey3 = Survey(title='Investor Sentiment', creator_id=user3.id)

    session.add(survey1)
    session.add(survey2)
    session.add(survey3)

    # Add sample responses
    response1 = Response(survey_id=survey1.id, content='{"feedback": "Great product!"}')
    response2 = Response(survey_id=survey2.id, content='{"satisfaction": "Very satisfied"}')
    response3 = Response(survey_id=survey3.id, content='{"sentiment": "Optimistic about growth"}')

    session.add(response1)
    session.add(response2)
    session.add(response3)

if __name__ == '__main__':
    setup_database()
```