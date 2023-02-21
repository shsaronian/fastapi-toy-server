import pytest

from fastapi.testclient import TestClient
from app.main.app import create_app, init_config, init_logger


@pytest.fixture
def client():
    init_config()
    init_logger()
    app = create_app()
    return TestClient(app)
