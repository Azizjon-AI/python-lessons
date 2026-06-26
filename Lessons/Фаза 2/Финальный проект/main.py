from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Session, relationship

app = FastAPI(title="Task Manager API")

DATABASE_URL = "postgresql://postgres:1234@localhost:5432/taskmanager_db"
engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass

# Таблица пользователей
class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    tasks = relationship("TaskModel", back_populates="user")

# Таблица задач
class TaskModel(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(String(500))
    done = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("UserModel", back_populates="tasks")

Base.metadata.create_all(engine)

class UserSchema(BaseModel):
    username: str = Field(min_length=2, max_length=50)
    email: str = Field(min_length=5, max_length=100)

class TaskScheme(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    description: str = Field(min_length=0, max_length=500)
    user_id: int


@app.get(
    "/users",
    tags=["Пользователи"],
    summary="Получить все ползователи"
)
def get_users():
    with Session(engine) as session:
        users = session.query(UserModel).all()
        return users

@app.get(
    "/users/{user_id}",
    tags=["Пользователи"],
    summary="Получить пользовател по id"
)
def get_user(user_id: int):
    with Session(engine) as session:
        user = session.get(UserModel, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Ползовател не найден")
        return user

@app.post(
    "/users",
    status_code=201,
    tags=["Пользователи"],
    summary="Добавить пользовател"
)
def create_user(user: UserSchema):
    with Session(engine) as session:
        new_user = UserModel(
            username=user.username,
            email=user.email
        )
        session.add(new_user)
        session.commit()
        return {"message": f"Пользовател {user.username} добавлень"}

@app.put(
    "/users/{user_id}",
    tags=["Пользователи"],
    summary="Обновить ползователа"
)
def update_user(user_id: int, data: UserSchema):
    with Session(engine) as session:
        user = session.get(UserModel, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Ползовател не найден")
        # Проверяем что пользователь существует:
        user = session.get(UserModel, data.user_id)
        if not user:
            raise HTTPException(status_code=404, detail=f"Пользователь {data.user_id} не найден")
        user.username=data.username
        user.email=data.email
        session.commit()
        return {"message": f"Ползователь {user_id} обновлён!"}

@app.delete(
    "/users/{user_id}",
    tags=["Пользователи"],
    summary="Удалить пользователа"
)
def delete_user(user_id: int):
    with Session(engine) as session:
        user = session.get(UserModel, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Ползовател не найден")
        session.delete(user)
        session.commit()
        return {"message": f"Ползователь {user_id} удалён!"}

@app.get(
    "/tasks",
    tags=["Задачи"],
    summary="Получить все звдачи"
)
def get_tasks():
    with Session(engine) as session:
        tasks = session.query(TaskModel).all()
        return tasks

@app.get(
    "/tasks/{task_id}",
    tags=["Задачи"],
    summary="Получить задачу по id"
)
def get_task(task_id: int):
    with Session(engine) as session:
        task = session.get(TaskModel, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Задача не найден")
        return task

@app.post(
    "/tasks",
    status_code=201,    
    tags=["Задачи"],
    summary="Добавить задачу"
)
def create_task(task: TaskScheme):
    with Session(engine) as session:
        new_task = TaskModel(
            title = task.title,
            description = task.description,
            user_id = task.user_id
        )
        session.add(new_task)
        session.commit()
        return {"message": f"Здача {task.title} добавлен!"}

@app.put(
    "/tasks/{task_id}",
    tags=["Задачи"],
    summary="Обновить задачу"
)
def update_task(task_id: int, data: TaskScheme):
    with Session(engine) as session:
        task = session.get(TaskModel, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Задача не найден")
        task.title = data.title
        task.description = data.description
        task.user_id = data.user_id
        session.commit()
        return {"message": f"Задача {task_id} обналена"}

@app.delete(
    "/tasks/{task_id}",
    tags=["Задачи"],
    summary="Удалить задачу"
)
def delete_task(task_id: int):
    with Session(engine) as session:
        task = session.get(TaskModel, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Задача не найден")
        session.delete(task)
        session.commit()
        return {"message": f"Задача {task_id} удалена"}

@app.patch(
    "/tasks/{task_id}",
    tags=["Задачи"], 
    summary="Отметить выполненной"
)
def complete_task(task_id: int):
    with Session(engine) as session:
        task = session.get(TaskModel, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Задача не найден")
        task.done = True
        session.commit()
        return {"message": f"Задача {task_id} выполнена"}

