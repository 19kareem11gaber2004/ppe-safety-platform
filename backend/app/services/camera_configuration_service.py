from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.camera_configuration import CameraConfiguration
from app.repositories.camera_configuration_repository import (
    CameraConfigurationRepository,
)
from app.repositories.camera_repository import CameraRepository
from app.schemas.camera_configuration import (
    CameraConfigurationCreate,
    CameraConfigurationUpdate,
)


class CameraConfigurationService:

    def __init__(self, db: Session):
        self.camera_repository = CameraRepository(db)
        self.repository = CameraConfigurationRepository(db)

    def get_configuration(
        self,
        camera_id: int,
    ) -> CameraConfiguration:

        camera = self.camera_repository.get_by_id(camera_id)

        if camera is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Camera not found",
            )

        configuration = self.repository.get_by_camera_id(camera_id)

        if configuration is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Camera configuration not found",
            )

        return configuration

    def create_configuration(
        self,
        camera_id: int,
        data: CameraConfigurationCreate,
    ) -> CameraConfiguration:

        camera = self.camera_repository.get_by_id(camera_id)

        if camera is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Camera not found",
            )

        existing = self.repository.get_by_camera_id(camera_id)

        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Camera configuration already exists",
            )

        configuration = CameraConfiguration(
            camera_id=camera_id,
            fps=data.fps,
            resolution=data.resolution,
            stream_timeout=data.stream_timeout,
            retry_count=data.retry_count,
            detection_enabled=data.detection_enabled,
            ai_model=data.ai_model,
        )

        return self.repository.create(configuration)

    def update_configuration(
        self,
        camera_id: int,
        data: CameraConfigurationUpdate,
    ) -> CameraConfiguration:

        configuration = self.get_configuration(camera_id)

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(configuration, key, value)

        return self.repository.update(configuration)

    def delete_configuration(
        self,
        camera_id: int,
    ) -> None:

        configuration = self.get_configuration(camera_id)

        self.repository.delete(configuration)