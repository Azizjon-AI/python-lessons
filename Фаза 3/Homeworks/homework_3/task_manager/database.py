from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "postgresql://postgres:1234@localhost:5432/task_manager02_db"
engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass