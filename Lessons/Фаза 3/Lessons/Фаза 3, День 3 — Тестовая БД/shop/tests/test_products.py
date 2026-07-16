from fastapi.testclient import TestClient
from main import app

product_id = None

def test_get_products(client):
    response = client.get("/products/")
    assert response.status_code == 200

def test_post_product(client):
    global product_id
    response = client.post("/products/", json={
        "name": "Телефон",
        "price": "1000",
        "quantities": 5
    })
    assert response.status_code == 201
    product_id = response.json()["id"]

def test_get_product(client):
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200 

def test_get_product_not_found(client):
    response = client.get("/products/99999")
    assert response.status_code == 404

def test_update_product(client):
    response = client.put(f"/products/{product_id}", json={
        "name": "Ноутбук",
        "price": 1500,
        "quantities": 3
    })
    assert response.status_code == 200

def test_delete_product(client):
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 200