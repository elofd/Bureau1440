"""
Модуль test_secrets.py, содержит тесты для роутов sercets.
"""
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuration.settings import pg_config
from models import db
from configuration.fastapi_app import app

SQLALCHEMY_DATABASE_URL = (
    f"postgresql:/"
    f"/{pg_config.user}:{pg_config.password}"
    f"@{pg_config.host}:{pg_config.port}"
    f"/test_db"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autoflush=False, bind=engine)

client = TestClient(app)


def override_get_session():
    db.Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        db.Base.metadata.drop_all(bind=engine)


def test_generate_secret():
    secret_data = {
        "secret": "This is a secret",
        "code": "1234"
    }
    response = client.post("/api/v1/generate", json=secret_data)
    assert response.status_code == 200
    assert 'secret_key' in response.json()


def test_get_secret():
    secret_data = {
        "secret": "Another secret",
        "code": "5678"
    }
    response = client.post("/api/v1/generate", json=secret_data)
    assert response.status_code == 200
    secret_key = response.json()['secret_key']

    response = client.get(f"/api/v1/secrets/{secret_key}?code=5678")
    assert response.status_code == 200
    assert response.json()['secret_key'] == secret_key


def test_get_secret_wrong_code():
    secret_data = {
        "secret": "Another secret",
        "code": "5678"
    }
    response = client.post("/api/v1/generate", json=secret_data)
    assert response.status_code == 200
    secret_key = response.json()['secret_key']

    response = client.get(f"/api/v1/secrets/{secret_key}?code=9999")
    assert response.status_code == 403
