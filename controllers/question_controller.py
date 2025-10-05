from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.index import Question, Choice
import schemas

def get_all_questions(db: Session):
    questions = db.query(Question).all()
    if not questions:
        raise HTTPException(status_code=404, detail="No questions found")
    return questions

def create_question(question: schemas.QuestionCreate, db: Session):
    db_question = Question(
        question_text=question.question_text,
        category_id=question.category_id
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    for choice in question.choices:
        db_choice = Choice(
            choice_text=choice.choice_text,
            is_correct=choice.is_correct,
            question_id=db_question.id,
        )
        db.add(db_choice)

    db.commit()
    db.refresh(db_question)
    return db_question

def get_question_by_id(question_id: int, db: Session):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

def delete_question(question_id: int, db: Session):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    db.delete(question)
    db.commit()
    return {"message": "Question deleted successfully"}

def update_question(question_id: int, updated_question: schemas.Question, db: Session):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    question.question_text = updated_question.question_text
    db.commit()

    db.query(Choice).filter(Choice.question_id == question_id).delete()
    for choice in updated_question.choices:
        db_choice = Choice(
            choice_text=choice.choice_text,
            is_correct=choice.is_correct,
            question_id=question.id
        )
        db.add(db_choice)

    db.commit()
    db.refresh(question)
    return question


# export controller for easier imports elsewhere
__all__ = ["get_all_questions", "create_question", "get_question_by_id"]
