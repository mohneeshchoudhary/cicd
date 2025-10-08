import pytest
from fastapi.testclient import TestClient
from main import app

# Create a test client
client = TestClient(app)

# def test_root_endpoint():
#     """Test the root endpoint returns HTML content with correct status"""
#     response = client.get("/")
#     assert response.status_code == 200
#     assert "text/html" in response.headers["content-type"]
#     assert "FastAPI CICD Learning" in response.text
#     assert "Mohneesh" in response.text

def test_health_endpoint():
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy", 
        "message": "CICD Learning App is running!"
    }

def test_health_endpoint_content_type():
    """Test that health endpoint returns JSON"""
    response = client.get("/health")
    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]

def test_root_endpoint_contains_key_elements():
    """Test that root endpoint contains key educational elements"""
    response = client.get("/")
    html_content = response.text
    
    # Check for key elements in the HTML
    assert "🚀 FastAPI CICD Learning" in html_content
    assert "demo to teach students" in html_content
    assert "Continuous Integration" in html_content
    assert "Continuous Deployment" in html_content

def test_app_title():
    """Test that the FastAPI app has correct title"""
    assert app.title == "CICD Learning App"
    assert "simple FastAPI app to learn CI/CD" in app.description
