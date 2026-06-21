from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session

app = FastAPI()

# Подключение к базе данных
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/students_db"
engine = create_engine(DATABASE_URL)

# Базовый класс для моделей
class Base(DeclarativeBase):
    pass

# Таблица студентов
class StudentModel(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    grade = Column(Integer)

# Создаём таблицу в БД
Base.metadata.create_all(engine)

# Pydantic модель
class StudentSchema(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    grade: int = Field(ge=0, le=100)

# Endpoints
@app.get(
    "/students",
    tags=["Студенты"],
    summary="Все студенты"
)
def get_students():
    with Session(engine) as session:
        students = session.query(StudentModel).all()
        return students

@app.post(
    "/students",
    status_code=201,
    tags=["Студенты"],
    summary="Добавить судент"
)
def create_student(student: StudentSchema):
    with Session(engine) as session:
        new_student = StudentModel(
            name=student.name,
            grade=student.grade
        )
        session.add(new_student)
        session.commit()
        return {"message": f"Студент {student.name} добавлен!"}

@app.get(
    "/students/{student_id}",
    tags=["Студенты"],
    summary="Получить студента по id"
)
def get_student(student_id: int):
    with Session(engine) as session:
        student = session.get(StudentModel, student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Студент не найден")
        return student

@app.put(
    "/students/{student_id}",
    tags=["Студенты"],
    summary="Обнавить студента"
)
def update_students(student_id: int, data: StudentSchema):
    with Session(engine) as session:
        student = session.get(StudentModel, student_id)
        if not student: 
            raise HTTPException(status_code=404, detail="Студент не найден")
        student.name = data.name,
        student.grade = data.grade
        session.commit()
        return {"message": f"Студент {student_id} обнавлён"}

@app.patch(
    "/students/{student_id}", 
    tags=["Студенты"],
    summary="Обнавить балл студента на 100"
)
def update_student(student_id: int):
    with Session(engine) as session:
        student = session.get(StudentModel, student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Стутудент не найден")
        student.grade = 100
        session.commit()
        return {"message": f"Балл {student_id} изменился на 100"}
@app.delete(
    "/students/{student_id}",
    tags=["Студенты"],
    summary="Удалить студента"
)
def delete_student(student_id: int):
    with Session(engine) as session:
        student = session.get(StudentModel, student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Студент не найден")
        session.delete(student)
        session.commit()
        return {"message": f"Студент {student_id} удалён!"}
