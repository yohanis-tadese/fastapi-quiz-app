from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.index import Category
import schemas

def get_all_categories(db: Session):
    categories = db.query(Category).all()
    if not categories:
        raise HTTPException(status_code=404, detail="No categories found")
    return categories

def create_category(category: schemas.CategoryCreate, db: Session):
    db_category = Category(name=category.name, description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_choice_by_id(category_id: int, db: Session):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


#export functions for easier imports elsewhere
__all__ = ["get_all_categories", "create_category", "get_choice_by_id"]
