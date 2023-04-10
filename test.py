from flask.testing import FlaskClient
from app import app

print('Test code!')

def test_index():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200

def test_append():
    with app.test_client() as client:
        response = client.get('/rooms')
        assert response.status_code == 200

def test_battles():
    with app.test_client() as client:
        response = client.get('/booking')
        assert response.status_code == 200