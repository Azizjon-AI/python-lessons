from fastapi.testclient import TestClient
from main import app

task_id = None

def test_get_tasks(client):
    response = client.get("/tasks/")
    assert response.status_code == 200

def test_create_task(client):
    global task_id
    user = client.post("/users/", json={
        "name": "TaskUser",
        "email": "taskuser@gmail.com"
    })
    user_id = user.json()["id"]
    response = client.post("/tasks/", json={
        "title": "Учить Python",
        "description": "hhhhfffff dddsss",
        "user_id": user_id
    })
    assert response.status_code == 201
    task_id = response.json()["id"]

def test_get_task(client):
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200

def test_get_tesk_not_found(client):
    response = client.get("/tasks/99999")
    assert response.status_code == 404

def test_update_task(client):
    response = client.put(f"/tasks/{task_id}", json={
        "title": "TitleTask",
        "description": "Descrition task",
        "user_id": 1
    })
    assert response.status_code == 200

def test_delete_task(client):
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200