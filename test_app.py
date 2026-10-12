import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'online'
    assert 'ACEest' in json_data['system']

def test_get_programs(client):
    response = client.get('/programs')
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'fat_loss' in json_data['data']
    assert 'muscle_gain' in json_data['data']

def test_calculate_calories_valid(client):
    payload = {"weight": 70.0, "program": "fat_loss"}
    response = client.post('/calculate-calories', json=payload)
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['estimated_daily_calories'] == 1540

def test_calculate_calories_invalid_weight(client):
    payload = {"weight": -5, "program": "muscle_gain"}
    response = client.post('/calculate-calories', json=payload)
    assert response.status_code == 400

def test_add_client(client):
    payload = {"name": "Rashi Verma", "program": "beginner", "weight": 60}
    response = client.post('/clients', json=payload)
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data['data']['name'] == "Rashi Verma"
    assert json_data['data']['target_calories'] == 1560
