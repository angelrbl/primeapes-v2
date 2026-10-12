import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DB_FILENAME = "primeapes.db"


def data_dir() -> Path:
    base = os.getenv("FLET_APP_STORAGE_DATA")
    folder = Path(base) if base else PROJECT_ROOT / "storage" / "data"
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def db_path() -> Path:
    return data_dir() / DB_FILENAME


def database_url() -> str:
    """URL de SQLAlchemy. Se puede sobrescribir, por ejemplo en los tests."""
    override = os.getenv("PRIMEAPES_DATABASE_URL")
    return override or f"sqlite:///{db_path().as_posix()}"