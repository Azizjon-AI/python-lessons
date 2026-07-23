from fastapi import FastAPI
from database import Base, engine
from routers import users, tasks

Base.metadata.create_all(engine)

app = FastAPI(title="Task Manager API")

app.include_router(users.router)
app.include_router(tasks.router)