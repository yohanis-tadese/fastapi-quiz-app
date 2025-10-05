from sqlalchemy import Boolean, Column, ForeignKey, Integer, Text
from config.db import Base

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(Text, nullable=False)
