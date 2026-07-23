from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database import engine
from models import UserModel, TaskModel
from schemas import UserSchemas, TaskSchemas

router = APIRouter(prefix="/users", tags=["Полбзователи"])

@router.get("/", summary="Получить все пользователи")
def get_users():
    with Session(engine) as session:
        return session.query(UserModel).all()

@router.post("/",status_code=201, summary="Добавить пользовател")
def create_user(user: UserSchemas):
    with Session(engine) as session:
        new_user = UserModel(
            name=user.name,
            email=user.email
        )
        session.add(new_user)
        session.flush()
        session.commit()
        return {"msg": f"Пользовател {user.name} добавлен!", "id": new_user.id}

@router.get("/{user_id}", summary="Получить пользовател по id")
def get_user(user_id: int):
    with Session(engine) as session:
        user = session.get(UserModel, user_id)
        if not user:
            raise HTTPException(status_code=400, detail=" Пользовател не найден")
        return user

@router.put("/{user_id}", summary="Обновить пользовател")
def update_user(user_id: int, data: UserSchemas):
    with Session(engine) as session:
        user = session.get(UserModel, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Подьзовател не найден!")
        user.name = data.name
        user.email = data.email
        session.commit()
        return {"msg": f"Пользовател {user_id} обнавлена"}

@router.delete("/{user_id}", summary="Удалить пользовател")
def delete_user(user_id: int):
    with Session(engine) as session:
        user = session.get(UserModel, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Пользовател не найден")
        session.delete(user)
        session.commit()
        return {"msg": f"Пользовател {user_id} удалён"}

