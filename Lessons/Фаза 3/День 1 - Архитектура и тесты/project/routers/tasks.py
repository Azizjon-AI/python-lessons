from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database import engine
from models import TaskModel, UserModel
from schemas import TaskSchema

router = APIRouter(prefix="/tasks", tags=["Задачи"])

@router.get("/", summary="Получить все задачи")
def get_tasks():
    with Session(engine) as session:
        return session.query(TaskModel).all()

@router.get("/{task_id}", summary="Получить задачу по id")
def get_task(task_id: int):
    with Session(engine) as session:
        task = session.get(TaskModel, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Задача не найден")
        return task

@router.post("/", summary="Добавить задачу")
def create_task(task: TaskSchema):
    with Session(engine) as session:
        new_task = TaskModel(
            title = task.title,
            description = task.description,
            user_id = task.user_id
        )
        session.add(new_task)
        session.commit()
        return {"msg": f"Задача {task.title} добавлен"}

@router.put("/{task_id}", summary="Обнавить задачу")
def update_tasks(task_id: int, data: TaskSchema):
    with Session(engine) as session:
        task = session.get(TaskModel, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Задача не найдена")

        user = session.get(UserModel, data.user_id)
        if not user:
            raise HTTPException(status_code=404, detail=f"Пользовател {data.user_id} не найден")
            
        task.title = data.title
        task.description = data.description
        task.user_id = data.user_id
        session.commit()
        return {"msg": f"Задача {task_id} обнавлён!"}

@router.patch("/{task_id}", summary="Обнавить сделани задачу")
def update_task(task_id: int):
    with Session(engine) as session:
        task = session.get(TaskModel, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Задача не найден")
        task.done =  True
        session.commit()
        return {"msg": f"Задача {task_id} сдедано"}

@router.delete("/{task_id}", summary="Удалить задачу")
def delete_task(task_id: int):
    with Session(engine) as session:
        task = session.get(TaskModel, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Задача не найдена")
        session.delete(task)
        session.commit()
        return {"msg": f"Задача {task_id} удалён"}

