from sqlalchemy.orm import Session

from app.models.camera import Camera
from app.repositories.base_repository import BaseRepository


class CameraRepository(BaseRepository[Camera]):

    def __init__(self, db: Session):
        super().__init__(
            Camera,
            db
        )


    def get_active_cameras(self):

        return (
            self.db.query(Camera)
            .filter(Camera.status == "active")
            .all()
        )
    def get_by_id(self, camera_id: int) -> Camera | None:
     return (
        self.db.query(Camera)
        .filter(Camera.id == camera_id)
        .first()
    )


def list(self) -> list[Camera]:
    return self.db.query(Camera).all()