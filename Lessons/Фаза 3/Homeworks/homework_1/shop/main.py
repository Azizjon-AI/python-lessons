from fastapi import FastAPI
from database import Base, engine
from routers import products

Base.metadata.create_all(engine)

app = FastAPI(title="Task Manager API")

app.include_router(products.router)