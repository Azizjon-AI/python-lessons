from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    title: str
    done: bool = False

tasks = []

@app.get(
    "/tasks",
    tags=["Задачи"],
    summary="Показать все задачи"
)
def get_tasks():
    return tasks 

@app.post(
    "/tasks",
    tags=["Задачи"],
    summary="Добавить новую Задачу")
def create_task(task: Task):
    tasks.append({
        "id": len(tasks) + 1, 
        "title": task.title, 
        "done": task.done
        })
    return {"message": f"Задача {task.title} добавлен"}

@app.get(
    "/tasks/{task_id}",
    tags=["Задачи"],
    summary="Получить задачу по id"
)
def get_tasks(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return {"error": "Задача не найден"}


    


