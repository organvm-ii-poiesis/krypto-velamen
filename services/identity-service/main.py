from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from database import create_db_and_tables, get_session
from models import User, UserCreate, UserPublic

app = FastAPI(title="KRYPTO-VELAMEN Identity Service")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def root():
    return {"status": "online", "service": "identity-service", "version": "1.0.0"}

@app.post("/users/", response_model=UserPublic)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    db_user = User.from_orm(user)
    # Mock password hashing for MVP
    db_user.hashed_password = f"hashed_{user.password}"
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@app.get("/users/", response_model=List[UserPublic])
def read_users(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users

@app.get("/profile/{handle}", response_model=UserPublic)
def get_profile(handle: str, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.handle == handle)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
