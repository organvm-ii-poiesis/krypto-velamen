from sqlmodel import SQLModel, create_engine, Session
import os

# Default to SQLite for local dev, PostgreSQL for production
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./identity.db")

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
