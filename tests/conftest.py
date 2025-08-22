import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture
def client():
    """Fixture to create a test client for the FastAPI app."""
    return TestClient(app)
