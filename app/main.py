from typing import Optional
from fastapi import Body, FastAPI, status ,Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, get_db

# Create the database tables if they don't exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class Post(BaseModel): # validation of input schema
    title: str
    id: int
    rating: Optional[int] = None

@app.get("/posts")
def read_root():
    return {"Hello": "World"}

@app.get("/posts/{id}")
def read_root():
    return {"Hello": "World"}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def createPost(data:Post):
    print(data.rating)
    return { "data": data}

@app.put("/posts/{id}")
def read_root():
    return {"Hello": "World"}

@app.patch("/posts/{id}")
def read_root():
    return {"Hello": "World"}

@app.delete("/posts/{id}")
def read_root():
    return {"Hello": "World"}

# Endpoint to create a new user
@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)

# Endpoint to get a user by email
@app.get("/users/{email}", response_model=schemas.UserResponse)
def get_user(email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
