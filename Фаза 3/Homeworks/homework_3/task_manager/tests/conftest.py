import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database import Base
from main import app

#Тестовая БД
TEST_DATABASE_URL = "postgresql://postgres:1234@localhost:5432/taskmanager02_test_db"
test_engine = create_engine(TEST_DATABASE_URL)

# Создаём таблицы перед тестами
@pytest.fixture(scope="session", autouse=True)
def setup_database():
    Base.metadata.create_all(test_engine)
    yield
    Base.metadata.drop_all(test_engine)

@pytest.fixture(autouse=True)
def override_engine(monkeypatch):
    import routers.users as users_router
    import routers.tasks as tasks_router
    monkeypatch.setattr(users_router, "engine", test_engine)
    monkeypatch.setattr(tasks_router, "engine", test_engine)

@pytest.fixture
def client():
    return TestClient(app)


