from sqlalchemy.orm import Session

from app.models.camera import Camera
from app.repositories.camera_repository import CameraRepository
from app.schemas.camera import CameraUpdate


class CameraService:

    def __init__(
        self,
        db: Session,
    ):
        self.repository = CameraRepository(db)


    def create_camera(
        self,
        name: str,
        location: str | None,
        source_type: str,
        connection_url: str,
    ) -> Camera:

        camera = Camera(
            name=name,
            location=location,
            source_type=source_type,
            connection_url=connection_url,
            status="active",
        )

        return self.repository.create(
            camera
        )


    def list_cameras(
        self,
    ) -> list[Camera]:

        return self.repository.list()


    def get_active_cameras(
        self,
    ) -> list[Camera]:

        return self.repository.get_active_cameras()


    def get_camera(
        self,
        camera_id: int,
    ) -> Camera | None:

        return self.repository.get_by_id(
            camera_id
        )


    def update_camera(
        self,
        camera: Camera,
        data: CameraUpdate,
    ) -> Camera:

        update_data = data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                camera,
                key,
                value,
            )

        return self.repository.update(
            camera
        )


    def delete_camera(
        self,
        camera: Camera,
    ):

        self.repository.delete(
            camera
        )
