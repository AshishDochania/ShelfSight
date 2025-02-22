from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to ShelfSight AI API"}

def test_get_shelf_status():
    response = client.get("/shelf_status")
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    
    if len(data) > 0:
        assert "shelf_id" in data[0]
        assert "product_id" in data[0]
        assert "stock_level" in data[0]

def test_get_shelf_status_by_id():
    response = client.get("/shelf_status/1")
    
    if response.status_code == 200:
        data = response.json()
        assert "shelf_id" in data
        assert "product_id" in data
        assert "stock_level" in data
        assert data["shelf_id"] == 1

def test_get_tasks():
    response = client.get("/tasks")
    
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    
    if len(data) > 0:
        assert "task_id" in data[0]
        assert "description" in data[0]
        assert "priority" in data[0]

def test_get_task_by_id():
    response = client.get("/tasks/1")
    
    if response.status_code == 200:
        data = response.json()
        assert "task_id" in data
        assert "description" in data
        assert "priority" in data
        assert data["task_id"] == 1