from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    handle: str = Field(index=True, unique=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str
    
    # "The Mask" Settings
    is_public: bool = False
    surveillance_pressure: int = Field(default=1, description="1-5 scale of privacy calibration")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class UserCreate(SQLModel):
    handle: str
    email: str
    password: str # allow-secret

class UserPublic(SQLModel):
    id: int
    handle: str
    is_public: bool
    surveillance_pressure: int
