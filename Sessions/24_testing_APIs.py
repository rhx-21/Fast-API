# iss file ka naam test_{name} format m dena necessary hai. e.g - test_main.py
# Pip install pytest  or  pip install httpx2
# run cmd - pytest

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

# Test Home API

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message":"Testing Page"}

# Test Add API

def test_add():
    response = client.get("/add?a=6&b=5")
    assert response.status_code == 200
    assert response.json() == {"sum": 11}
