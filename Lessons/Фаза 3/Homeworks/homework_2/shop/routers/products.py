from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database import engine
from models import ProductModel
from schemas import ProductSchema

router = APIRouter(prefix="/products", tags=["Продукти"])

@router.get("/", summary="Получиь все товари!")
def get_products():
    with Session(engine) as session:
        return session.query(ProductModel).all()

@router.get("/{product_id}", summary="Получить продукт по id")
def get_product(product_id: int):
    with Session(engine) as session:
        product = session.get(ProductModel, product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Продукт не найден")
        return product

@router.post("/", status_code=201, summary="Добавить продукт")
def create_product(product: ProductSchema):
    with Session(engine) as session:
        new_product = ProductModel(
            name=product.name,
            price=product.price,
            quantities=product.quantities
        )
        session.add(new_product)
        session.flush()
        session.commit()
        return {"msg": f"Продукт {product.name} добавлено!", "id": new_product.id}

@router.put("/{product_id}", summary="Обновить продукт")
def update_product(product_id: int, data: ProductSchema):
    with Session(engine) as session:
        product = session.get(ProductModel, product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Продукт не найден!")
        product.name=data.name
        product.price=data.price
        product.quantities=data.quantities
        session.commit()
        return {"msg": f"Продукт {product_id} обнавлён"}

@router.delete("/{product_id}", summary="Удалить продукт")
def delete_product(product_id: int):
    with Session(engine) as session:
        product = session.get(ProductModel, product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Продукт не найден")
        session.delete(product)
        session.commit()
        return {"msg": f"Продукт {product_id} удалён!"}


