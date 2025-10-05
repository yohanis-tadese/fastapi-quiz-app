from sqlalchemy.orm import relationship
from models.choice_models import Choice
from models.question_models import Question
from models.category_models import Category
from config.db import Base

# Define relationship between Question and Choice
Question.choices = relationship("Choice", back_populates="question", cascade="all, delete-orphan")
Choice.question = relationship("Question", back_populates="choices")

# Define relationship between Category and Question
Category.questions = relationship(
    "Question", back_populates="category", cascade="all, delete-orphan")
Question.category = relationship("Category", back_populates="questions")

#re-export models for easier imports elsewhere
__all__ = ["Question", "Choice", "Category", "Base"]
