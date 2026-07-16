import pytest

from app.db.session import SessionLocal
from app.models.user import User
from app.models.camera import Camera


@pytest.fixture(autouse=True)
def clean_database():

    db = SessionLocal()

    try:
        db.query(Camera).delete()
        db.query(User).delete()

        db.commit()

        yield

    finally:
        db.close()