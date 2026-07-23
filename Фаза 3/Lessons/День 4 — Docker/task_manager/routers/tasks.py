from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database import engine
from models import UserModel, TaskModel
from schemas import UserSchemas, TaskSchemas

router = APIRouter(prefix="/tasks", tags=["Задачи"])

@router.get("/", summary="Видить все задачи")
def get_tasks():
    with Session(engine) as session:
        return session.query(TaskModel).all()

@router.post("/", status_code=201, summary="Добавть задачу")
def create_task(task: TaskSchemas):
    with Session(engine) as session:
        new_task = TaskModel(
            title = task.title,
            description = task.description,
            user_id = task.user_id
        )
        session.add(new_task)
        session.flush()
        session.commit()
        return {"msg": f"Задача {task.title} добавлено!", "id": new_task.id}


@router.get("/{task_id}", summary="Получить задачу по id")
def get_task(task_id: int):
    with Session(engine) as session:
        task = session.get(TaskModel, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Задача не найдена!")
        return task

@router.put("/{task_id}", summary="Обновить задачу")
def update_task(task_id: int, data: TaskSchemas):
    with Session(engine) as session:
        task = session.get(TaskModel, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Задача не найдена")
        task.title = data.title
        task.description = data.description
        task.user_id = data.user_id
        session.commit()
        return {"msg": f"Задача {task_id} обнавлено"}

@router.delete("/{task_id}", summary="Удалить задачу")
def delete_task(task_id: int):
    with Session(engine) as session:
        task = session.get(TaskModel, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Задача не найден")
        session.delete(task)
        session.commit()
        return {"msg": f"Задача {task_id} удалён"}