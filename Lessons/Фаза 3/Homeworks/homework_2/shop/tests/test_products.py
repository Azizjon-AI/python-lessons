from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
product_id = None  # глобальная переменная

def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200

def test_post_product():
    global product_id
    response = client.post("/products/", json={
        "name": "Телефон Poc",
        "price": 1000,
        "quantities": 5
    })
    assert response.status_code == 201
    product_id = response.json()["id"]

def test_get_product():
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200

def test_get_product_not_found():
    response = client.get("/products/99999")
    assert response.status_code == 404

def test_update_product():
    response = client.put(f"/products/{product_id}", json={
        "name": "Ноутбук",
        "price": 1500,
        "quantities": 3
    })
    assert response.status_code == 200

def test_delete_product():
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 200