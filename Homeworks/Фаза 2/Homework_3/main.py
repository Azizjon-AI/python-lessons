from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class Students(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=50,
        description="Имя студент",
        example="Azizjon"
    )
    grade: int = Field(
        ge=0,
        le=100,
        description="Оценка от 0 до 100",
        example=90
    )

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
    raise HTTPException(status_code=404, detail="Студент не найден")

@app.post(
    "/students",
    status_code=201,
    tags=["Студенти"],
    summary="Добавить студент"
)
def create_student(student: Students):
    students.append({
        "id": len(students) + 1,
        "name": student.name,
        "grade": student.grade
    })
    return {"message": f"Студент {student.name} добавлень!"}

@app.put(
    "/students/{student_id}",
    tags=["Студенти"],
    summary="Обновить студента"
)
def update_student(student_id: int, update_student: Students):
    for student in students:
        if student["id"] == student_id:
            student["name"] = update_student.name
            student["grade"] = update_student.grade
            return {"message": f"Студент {student_id} обнавлена!"}
    raise HTTPException(status_code=404, detail="Студент не найден")

@app.delete(
    "/students/{student_id}",
    tags=["Студенти"],
    summary="Удалить студент"
)
def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {"message": f"Студенть {student_id} удалена"}
    raise HTTPException(status_code=404, detail="Студент не найден")

@app.patch(
    "/students/{student_id}",
    tags=["Студенти"],
    summary="Обнавить оценку студента на 100"
)
def update_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
                student["grade"] = 100
                return {"message": f"Оценка студент {student_id} обнавлена на 100!"}
    raise HTTPException(status_code=404, detail="Сткдент не найден")

    