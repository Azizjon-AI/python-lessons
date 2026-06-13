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
def get_tesks():
    return tasks

@app.get(
    "/tasks/{task_id}",
    tags=["Задачи"],
    summary="Задачи по id"
)
def get_tesks(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return {"error": "Задача не найдена"}

@app.post(
    "/tasks",
    tags=["Задачи"],
    summary="Создать задачу"
)
def create_task(task: Task):
    tasks.append({
        "id": len(tasks) + 1,
        "title": task.title,
        "done": task.done
    }) 
    return {"message": f"Задача {task.title} добавлена"}

@app.put(
    "/tasks/{task_id}",
    tags=["Задачи"],
    summary="Обнавить задачи"
)
def update_task(task_id: int, update_task: Task):
    for task in tasks:
        if task["id"] == task_id:
            task["title"]: update_task.title
            task["done"]:  update_task.done 
            return {"message": f"Задача {task_id} обнавлена"}
    return {"error": "Задача не найдена"}

@app.delete(
    "/tasks/{task_id}",
    tags=["Задачи"],
    summary="Удалить задачу"
)
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": f"Задача {task_id} удалено"}
    return {"error": "Задача не найдена"}

@app.patch(
    "/tasks/{task_id}/complete",
    tags=["Задачи"],
    summary="Выполнить задачу"
)
def complete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return {"message": f"Задача {task_id} выполнена"}
    return {"error":  "Задача не найдена"}
    
