import pytest

from core.db import init_db, reset_engine


@pytest.fixture
def db(monkeypatch):
    monkeypatch.setenv("PRIMEAPES_DATABASE_URL", "sqlite://")
    reset_engine()
    init_db()
    yield
    reset_engine()  