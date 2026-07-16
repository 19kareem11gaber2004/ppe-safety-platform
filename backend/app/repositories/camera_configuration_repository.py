from sqlalchemy.orm import Session

from app.models.camera_configuration import CameraConfiguration
from app.repositories.base_repository import BaseRepository


class CameraConfigurationRepository(
    BaseRepository[CameraConfiguration]
):

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(
            CameraConfiguration,
            db,
        )


    def get_by_camera_id(
        self,
        camera_id: int,
    ) -> CameraConfiguration | None:

        return (
            self.db.query(CameraConfiguration)
            .filter(
                CameraConfiguration.camera_id == camera_id
            )
            .first()
        )


    def update(
        self,
        configuration: CameraConfiguration,
    ) -> CameraConfiguration:

        self.db.commit()
        self.db.refresh(configuration)

        return configuration


    def delete(
        self,
        configuration: CameraConfiguration,
    ) -> None:

        self.db.delete(configuration)
        self.db.commit()
