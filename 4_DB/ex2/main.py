from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, crud, schemas

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try :
        yield db
    finally :
        db.close()

@app.post("/users", response_model = schemas.UserResponse)
def create_user(user: schemas.UserCreate, db : Session = Depends(get_db)):
    return crud.create_user(db, user.name)

@app.get("/users", response_model=list[schemas.UserResponse])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)
