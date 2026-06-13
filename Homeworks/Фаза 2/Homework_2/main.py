from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Students(BaseModel):
    name: str
    grade: int

students = []

@app.get(
    "/students",
    tags=["Студенти"],
    summary="Показать все студенти"
)
def get_students():
    return students

@app.get(
    "/students/{student_id}",
    tags=["Студенти"],
    summary="Найти студент по id"
)
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    return {"error": "Студент не найден"}

@app.post(
    "/students",
    tags=["Студенти"],
    summary="Добавить студент"
)
def create_student(student: Students):
    students.append({
        "id": len(students) + 1,
        "name": student.name,
        "grade": student.grade
    })
    return {"message": f"Студент {student.name} добавлен!"}

@app.put(
    "/students/{student_id}",
    tags=["Студенти"],
    summary="Обнавить студенти"
)
def update_student(student_id: int, update_student: Students):
    for student in students:
        if student["id"] == student_id:
            student["name"] = update_student.name
            student["grade"] = update_student.grade
            return {"message": f"Суденте {student_id} обнавлена"}
    return {"error": f"Студент не найден"}


@app.delete(
    "/students/{student_id}",
    tags=["Студенти"],
    summary="Удалить студент"
)
def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {"message": f"Студент {student_id} удалена!"}
    return {"error": "Студент не найден"}

@app.patch(
    "/students/{student_id}",
    tags=["Студенти"],
    summary="Обнавить оценку студента на 100"
)
def complete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            student["grade"] = 100
            return {"message": f"Оценка студент {student_id} обнавлена на 100!"}
    return {"error": "Студент не найден"}



