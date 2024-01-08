import re
from datetime import datetime, timedelta
from backend.models.survey_model import Survey
from backend.database.db import get_db_session

def validate_survey_data(survey_data):
    """
    Validates the survey data before creating a new survey.
    """
    if not survey_data.get('title') or not isinstance(survey_data.get('title'), str):
        raise ValueError("Survey title is required and must be a string.")
    
    if not survey_data.get('questions') or not isinstance(survey_data.get('questions'), list):
        raise ValueError("Survey questions are required and must be a list.")
    
    for question in survey_data.get('questions'):
        if not question.get('text') or not isinstance(question.get('text'), str):
            raise ValueError("Each question must have text and it must be a string.")
        if question.get('type') not in ['multiple_choice', 'open_ended']:
            raise ValueError("Invalid question type. Must be 'multiple_choice' or 'open_ended'.")
        if question.get('type') == 'multiple_choice' and not question.get('options'):
            raise ValueError("Multiple choice questions must have options.")
    
    if survey_data.get('expiration_date'):
        if not re.match(r'\d{4}-\d{2}-\d{2}', survey_data.get('expiration_date')):
            raise ValueError("Expiration date must be in YYYY-MM-DD format.")
        expiration_date = datetime.strptime(survey_data.get('expiration_date'), '%Y-%m-%d')
        if expiration_date < datetime.now():
            raise ValueError("Expiration date must be in the future.")
    
    return True

def create_survey(survey_data):
    """
    Creates a new survey with the provided data after validation.
    """
    validate_survey_data(survey_data)
    
    new_survey = Survey(
        title=survey_data.get('title'),
        description=survey_data.get('description'),
        questions=survey_data.get('questions'),
        expiration_date=datetime.strptime(survey_data.get('expiration_date'), '%Y-%m-%d') if survey_data.get('expiration_date') else None,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    
    session = get_db_session()
    session.add(new_survey)
    session.commit()
    
    return new_survey

def survey_expired(survey):
    """
    Checks if a survey has expired.
    """
    if survey.expiration_date and datetime.now() > survey.expiration_date:
        return True
    return False

def get_active_surveys():
    """
    Retrieves all active surveys that have not expired.
    """
    session = get_db_session()
    active_surveys = session.query(Survey).filter(Survey.expiration_date > datetime.now() or Survey.expiration_date == None).all()
    return active_surveys

def close_expired_surveys():
    """
    Closes surveys that have passed their expiration date.
    """
    session = get_db_session()
    expired_surveys = session.query(Survey).filter(Survey.expiration_date < datetime.now()).all()
    for survey in expired_surveys:
        survey.is_active = False
    session.commit()