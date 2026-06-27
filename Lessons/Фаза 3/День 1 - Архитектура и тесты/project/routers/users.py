from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database import engine
from models import UserModel
from schemas import UserSchema

router = APIRouter(prefix="/users", tags=["Пользователи"])

@router.get("/", summary="Получить все пользователи")
def get_users():
    with Session(engine) as session:
        return session.query(UserModel).all()

@router.get("/{user_id}", summary="Получить позовател по id")
def get_user(user_id: int):
    with Session(engine) as session:
        user = session.get(UserModel, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Пользовател не найден")
        return user

@router.post("/", status_code=201, summary="Добавить позователь")
def create_user(user: UserSchema):
    with Session(engine) as session:
        new_user = UserModel(
            username=user.username,
            email=user.email
        )
        session.add(new_user)
        session.commit()
        return {"msg": f"Пользователь {user.username} создань!"} 

@router.delete("/{user_id}", summary="Удалить пользоател")
def delete_user(user_id: int):
    with Session(engine) as session:
        user = session.get(UserModel, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Пользователь не найден!")
        session.delete(user)
        session.commit()
        return {"msg": f"Полбзователь {user_id} удалён"}
        
