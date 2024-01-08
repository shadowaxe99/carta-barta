from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from backend.database.db import Base

class Survey(Base):
    __tablename__ = 'surveys'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    creator_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    language = Column(String(50), nullable=False, default='en')
    expiration_date = Column(DateTime, nullable=True)
    max_responses = Column(Integer, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    creator = relationship("User", back_populates="surveys")
    questions = relationship("SurveyQuestion", cascade="all, delete-orphan")
    responses = relationship("Response", cascade="all, delete-orphan")

    def __init__(self, title, creator_id, language, expiration_date=None, max_responses=None, description=None):
        self.title = title
        self.creator_id = creator_id
        self.language = language
        self.expiration_date = expiration_date
        self.max_responses = max_responses
        self.description = description

class SurveyQuestion(Base):
    __tablename__ = 'survey_questions'

    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey('surveys.id'), nullable=False)
    question_text = Column(Text, nullable=False)
    question_type = Column(String(50), nullable=False)  # e.g., 'multiple_choice', 'open_ended'
    options = Column(Text, nullable=True)  # JSON string for multiple choice options

    survey = relationship("Survey", back_populates="questions")

    def __init__(self, survey_id, question_text, question_type, options=None):
        self.survey_id = survey_id
        self.question_text = question_text
        self.question_type = question_type
        self.options = options

User.surveys = relationship("Survey", order_by=Survey.id, back_populates="creator")