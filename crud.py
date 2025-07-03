from sqlalchemy.orm import Session
from database import SessionLocal
import models
from pydantic import BaseModel

class ItemResponse(BaseModel):
    id: int
    title: str
    description: str
    class Config:
        orm_mode = True

def get_items():
    db = SessionLocal()
    items = db.query(models.Item).all()
    db.close()
    return items

def create_item(item):
    db = SessionLocal()
    db_item = models.Item(title=item.title, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db.close()
    return db_item
