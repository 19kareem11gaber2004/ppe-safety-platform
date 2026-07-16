from app.db.session import SessionLocal

from app.services.user_service import UserService
from app.services.camera_service import CameraService


def test_user_service_create():

    db = SessionLocal()

    try:
        service = UserService(db)

        user = service.create_user(
            email="service@test.com",
            password_hash="hashed_password",
            role="admin",
        )

        assert user.id is not None
        assert user.email == "service@test.com"

    finally:
        db.close()



def test_camera_service_create():

    db = SessionLocal()

    try:
        service = CameraService(db)

        camera = service.create_camera(
            name="Camera 01",
            location="Factory A",
            source_type="rtsp",
            connection_url="rtsp://camera01",
        )

        assert camera.id is not None
        assert camera.name == "Camera 01"

    finally:
        db.close()