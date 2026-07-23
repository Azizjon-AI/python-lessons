from fastapi.testclient import TestClient
from main import app

user_id = None

def test_get_users(client):
    response = client.get("/users/")
    assert response.status_code == 200

def test_post_user(client):
    global user_id
    response = client.post("/users/", json={
        "name": "Azizjon",
        "email": "azizjon@gamil.com"
    })
    assert response.status_code == 201
    user_id = response.json()["id"]

def test_get_user(client):
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200

def test_get_user_not_found(client):
    response = client.get("/users/9999")
    assert response.status_code == 400

def test_update_user(client):
    response = client.put(f"/users/{user_id}", json={
        "name": "Ayzik",
        "email": "ayzik@gmail.com"
    })
    assert response.status_code == 200

def test_delete_user(client):
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200