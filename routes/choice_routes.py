from typing import List
from fastapi import APIRouter, Depends
import controllers.choice_controller as controller
from sqlalchemy.orm import Session
import schemas
from db import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.Choice])
async def get_choices(db: Session = Depends(get_db)):
    return controller.get_all_choices(db)

@router.post("/", response_model=schemas.Choice)
async def create_choice(choice: schemas.ChoiceCreate, db: Session = Depends(get_db)):
    return controller.create_choice(choice, db)

@router.get("/{choice_id}", response_model=schemas.Choice)
async def get_choice(choice_id: int, db: Session = Depends(get_db)):
    return controller.get_choice_by_id(choice_id, db)
