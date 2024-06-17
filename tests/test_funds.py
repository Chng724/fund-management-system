import pytest
from app import create_app
from models import db, Fund
from config import TestConfig  # Import TestConfig


@pytest.fixture
def app():
    
    app = create_app(config_class=TestConfig)
    with app.app_context():
        db.create_all()  
        yield app  
        db.session.remove()  
        db.drop_all()  


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_all_funds_empty(client):
    response = client.get('/api/funds/')
    assert response.status_code == 200  # Check if the status code is 200
    assert response.get_json() == []  # Check if the response is an empty list

# Test to create a new fund
def test_create_fund(client):
    response = client.post('/api/funds/', json={
        "name": "Test Fund",
        "manager_name": "Jane Doe",
        "description": "A test fund",
        "nav": 1000000.0,
        "performance": 10.0
    })
    assert response.status_code == 201  # Check if the status code is 201
    data = response.get_json()
    assert data['name'] == "Test Fund"  # Verify the name of the fund
    assert data['manager_name'] == "Jane Doe"  # Verify the manager name

# Test to get a specific fund by ID
def test_get_fund(client):
    response = client.post('/api/funds/', json={
        "name": "Test Fund",
        "manager_name": "Jane Doe",
        "description": "A test fund",
        "nav": 1000000.0,
        "performance": 10.0
    })
    fund_id = response.get_json()['id']
    response = client.get(f'/api/funds/{fund_id}')
    assert response.status_code == 200  # Check if the status code is 200
    data = response.get_json()
    assert data['name'] == "Test Fund"  # Verify the name of the fund
    assert data['manager_name'] == "Jane Doe"  # Verify the manager name

# Test to update the performance of a specific fund by ID
def test_update_fund_performance(client):
    response = client.post('/api/funds/', json={
        "name": "Test Fund",
        "manager_name": "Jane Doe",
        "description": "A test fund",
        "nav": 1000000.0,
        "performance": 10.0
    })
    fund_id = response.get_json()['id']
    response = client.put(f'/api/funds/{fund_id}', json={"performance": 15.0})
    assert response.status_code == 200  # Check if the status code is 200
    data = response.get_json()
    assert data['performance'] == 15.0  # Verify the updated performance

# Test to delete a specific fund by ID
def test_delete_fund(client):
    response = client.post('/api/funds/', json={
        "name": "Test Fund",
        "manager_name": "Jane Doe",
        "description": "A test fund",
        "nav": 1000000.0,
        "performance": 10.0
    })
    fund_id = response.get_json()['id']
    response = client.delete(f'/api/funds/{fund_id}')
    assert response.status_code == 200  # Check if the status code is 200
    response = client.get(f'/api/funds/{fund_id}')
    assert response.status_code == 404  # if fund is not found after deletion
