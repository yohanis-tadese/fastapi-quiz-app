from typing import List
from pydantic import BaseModel

class ChoiceCreate(BaseModel):
    choice_text: str
    is_correct: bool
    question_id: int

class Choice(BaseModel):
    id: int
    choice_text: str
    is_correct: bool
    question_id: int

    class Config:
        from_attributes = True

class QuestionCreate(BaseModel):
    question_text: str
    choices: List[ChoiceCreate]

class Question(BaseModel):
    id: int
    question_text: str
    choices: List[Choice]

    class Config:
        from_attributes = True
