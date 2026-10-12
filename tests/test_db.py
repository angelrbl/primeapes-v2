from sqlalchemy import text
from core.db import get_session

def test_sesion_funciona(db):
    with get_session() as session:
        assert session.execute(text("select 1")).scalar() == 1