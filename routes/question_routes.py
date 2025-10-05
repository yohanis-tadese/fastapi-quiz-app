from fastapi import APIRouter, Depends
from typing import List
from controllers import question_controller as controller
from sqlalchemy.orm import Session
import schemas
from db import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.Question])
async def get_questions(db: Session = Depends(get_db)):
    return controller.get_all_questions(db)

@router.post("/", response_model=schemas.Question)
async def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    return controller.create_question(question, db)

@router.get("/{question_id}", response_model=schemas.Question)
async def get_question(question_id: int, db: Session = Depends(get_db)):
    return controller.get_question_by_id(question_id, db)

@router.delete("/{question_id}")
async def delete_question(question_id: int, db: Session = Depends(get_db)):
    return controller.delete_question(question_id, db)

@router.put("/{question_id}", response_model=schemas.Question)
async def update_question(question_id: int, updated_question: schemas.Question, db: Session = Depends(get_db)):
    return controller.update_question(question_id, updated_question, db)
