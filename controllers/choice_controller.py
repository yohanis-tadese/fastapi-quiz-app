from fastapi import HTTPException
from sqlalchemy.orm import Session
import models.index as index
import schemas

def get_all_choices(db: Session):
    choices = db.query(index.Choice).all()
    if not choices:
        raise HTTPException(status_code=404, detail="No choices found")
    return choices

def create_choice(choice: schemas.ChoiceCreate, db: Session):
    db_choice = index.Choice(
        choice_text=choice.choice_text,
        is_correct=choice.is_correct,
        question_id=choice.question_id
    )
    db.add(db_choice)
    db.commit()
    db.refresh(db_choice)
    return db_choice

def get_choice_by_id(choice_id: int, db: Session):
    choice = db.query(index.Choice).filter(index.Choice.id == choice_id).first()
    if not choice:
        raise HTTPException(status_code=404, detail="Choice not found")
    return choice


# export controller for easier imports elsewhere
__all__ = ["get_all_choices", "create_choice", "get_choice_by_id"]
