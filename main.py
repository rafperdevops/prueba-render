from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import crud, models, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

class ItemCreate(BaseModel):
    title: str
    description: str

@app.post("/items/", response_model=crud.ItemResponse)
def create_item(item: ItemCreate):
    return crud.create_item(item)

@app.get("/items/", response_model=List[crud.ItemResponse])
def read_items():
    return crud.get_items()
