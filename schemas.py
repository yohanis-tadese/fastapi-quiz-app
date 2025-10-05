from typing import List, Optional
from pydantic import BaseModel

class ChoiceCreate(BaseModel):
    choice_text: str
    is_correct: bool

class Choice(BaseModel):
    id: int
    choice_text: str
    is_correct: bool
    question_id: int

    class Config:
        from_attributes = True

class QuestionCreate(BaseModel):
    question_text: str
    category_id: int
    choices: List[ChoiceCreate]

class Question(BaseModel):
    id: int
    category_id: Optional[int] = None
    question_text: str
    choices: List[Choice]

    class Config:
        from_attributes = True

class CategoryCreate(BaseModel):
    name: str
    description: str

class Category(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True
