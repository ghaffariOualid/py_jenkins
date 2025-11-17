import pytest
from src.web_app import create_app

@pytest.fixture
def app():
    app = create_app({"TESTING": True})
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

def test_create_user_valid(client):
    data = {"name": "Ali", "age": 25}
    response = client.post("/users", json=data)
    assert response.status_code == 201
    result = response.get_json()
    assert result["name"] == "Ali"
    assert result["age"] == 25
    assert "id" in result

def test_create_user_invalid_name(client):
    data = {"name": "", "age": 25}
    response = client.post("/users", json=data)
    assert response.status_code == 400
    assert "name is required" in response.get_json()["error"]

def test_create_user_invalid_age(client):
    data = {"name": "Alice", "age": -5}
    response = client.post("/users", json=data)
    assert response.status_code == 400
    assert "age must be a non-negative integer" in response.get_json()["error"]

def test_create_user_no_json(client):
    response = client.post("/users", data="not json")
    assert response.status_code == 400
    assert "JSON required" in response.get_json()["error"]

# def test_list_users_empty(client):
#     response = client.get("/users")
#     assert response.status_code == 200
#     assert response.get_json() == []

# def test_list_users_with_data(client):
#     # Create a user first
#     data = {"name": "Bob", "age": 30}
#     client.post("/users", json=data)

#     response = client.get("/users")
#     assert response.status_code == 200
#     users = response.get_json()
#     assert len(users) == 1
#     assert users[0]["name"] == "Bob"
#     assert users[0]["age"] == 30

# def test_get_user_existing(client):
#     # Create a user first
#     data = {"name": "Charlie", "age": 35}
#     create_response = client.post("/users", json=data)
#     user_id = create_response.get_json()["id"]

#     response = client.get(f"/users/{user_id}")
#     assert response.status_code == 200
#     user = response.get_json()
#     assert user["name"] == "Charlie"
#     assert user["age"] == 35
#     assert user["id"] == user_id

# def test_get_user_not_found(client):
#     response = client.get("/users/nonexistent")
#     assert response.status_code == 404
#     assert "not found" in response.get_json()["error"]

# def test_update_user_valid(client):
#     # Create a user first
#     data = {"name": "David", "age": 40}
#     create_response = client.post("/users", json=data)
#     user_id = create_response.get_json()["id"]

#     update_data = {"name": "David Updated", "age": 45}
#     response = client.put(f"/users/{user_id}", json=update_data)
#     assert response.status_code == 200
#     user = response.get_json()
#     assert user["name"] == "David Updated"
#     assert user["age"] == 45
#     assert user["id"] == user_id

# def test_update_user_partial(client):
#     # Create a user first
#     data = {"name": "Eve", "age": 50}
#     create_response = client.post("/users", json=data)
#     user_id = create_response.get_json()["id"]

#     update_data = {"age": 55}  # Only update age
#     response = client.put(f"/users/{user_id}", json=update_data)
#     assert response.status_code == 200
#     user = response.get_json()
#     assert user["name"] == "Eve"  # Name should remain the same
#     assert user["age"] == 55

# def test_update_user_invalid_name(client):
#     # Create a user first
#     data = {"name": "Frank", "age": 60}
#     create_response = client.post("/users", json=data)
#     user_id = create_response.get_json()["id"]

#     update_data = {"name": "", "age": 65}
#     response = client.put(f"/users/{user_id}", json=update_data)
#     assert response.status_code == 400
#     assert "invalid name" in response.get_json()["error"]

def test_update_user_not_found(client):
    update_data = {"name": "Ghost", "age": 70}
    response = client.put("/users/nonexistent", json=update_data)
    assert response.status_code == 404
    assert "not found" in response.get_json()["error"]

# def test_delete_user_existing(client):
#     # Create a user first
#     data = {"name": "Helen", "age": 75}
#     create_response = client.post("/users", json=data)
#     user_id = create_response.get_json()["id"]

#     response = client.delete(f"/users/{user_id}")
#     assert response.status_code == 204

#     # Verify user is deleted
#     get_response = client.get(f"/users/{user_id}")
#     assert get_response.status_code == 404

# def test_delete_user_not_found(client):
#     response = client.delete("/users/nonexistent")
#     assert response.status_code == 404
#     assert "not found" in response.get_json()["error"]