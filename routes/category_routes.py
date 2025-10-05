from typing import List
from fastapi import APIRouter, Depends
from controllers import category_controller as controller
from sqlalchemy.orm import Session
import schemas
from config.db import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.Category])
async def get_choices(db: Session = Depends(get_db)):
    return controller.get_all_categories(db)

@router.post("/", response_model=schemas.Category)
async def create_choice(choice: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return controller.create_category(choice, db)

@router.get("/{choice_id}", response_model=schemas.Category)
async def get_choice(choice_id: int, db: Session = Depends(get_db)):
    return controller.get_choice_by_id(choice_id, db)
