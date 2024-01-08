from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .db import Base

class Response(Base):
    __tablename__ = 'responses'

    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey('surveys.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    survey = relationship("Survey", back_populates="responses")
    user = relationship("User", back_populates="responses")

    def __init__(self, survey_id, user_id, content):
        self.survey_id = survey_id
        self.user_id = user_id
        self.content = content

    def __repr__(self):
        return f"<Response(id={self.id}, survey_id={self.survey_id}, user_id={self.user_id}, content={self.content})>"