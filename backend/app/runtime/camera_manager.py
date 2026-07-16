from sqlalchemy.orm import Session

from app.runtime.registry import camera_registry
from app.runtime.camera_worker import CameraWorker

from app.repositories.camera_repository import CameraRepository
from app.repositories.camera_configuration_repository import (
    CameraConfigurationRepository,
)


class CameraManager:

    def __init__(
        self,
        db: Session,
    ):
        self.camera_repository = CameraRepository(db)
        self.configuration_repository = (
            CameraConfigurationRepository(db)
        )

    def start_camera(
        self,
        camera_id: int,
    ) -> CameraWorker:

        worker = camera_registry.get(camera_id)

        if worker:
            return worker

        camera = self.camera_repository.get_by_id(camera_id)

        if camera is None:
            raise ValueError(
                "Camera not found"
            )

        configuration = (
            self.configuration_repository.get_by_camera_id(
                camera_id
            )
        )

        if configuration is None:
            raise ValueError(
                "Camera configuration not found"
            )

        worker = CameraWorker(
            camera,
            configuration,
        )

        worker.start()

        camera_registry.add(
            camera_id,
            worker,
        )

        return worker

    def stop_camera(
        self,
        camera_id: int,
    ) -> None:

        worker = camera_registry.get(camera_id)

        if worker is None:
            return

        worker.stop()

        camera_registry.remove(
            camera_id
        )

    def restart_camera(
        self,
        camera_id: int,
    ) -> CameraWorker:

        self.stop_camera(
            camera_id
        )

        return self.start_camera(
            camera_id
        )

    def get_worker(
        self,
        camera_id: int,
    ) -> CameraWorker | None:

        return camera_registry.get(
            camera_id
        )

    def running_cameras(self):

        return camera_registry.all()

    def running_count(self) -> int:

        return camera_registry.count()

    def stop_all(self):

        for worker in list(
            camera_registry.all().values()
        ):
            worker.stop()

        camera_registry.clear()