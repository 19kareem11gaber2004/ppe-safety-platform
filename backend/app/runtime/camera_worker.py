from app.models.camera import Camera
from app.models.camera_configuration import CameraConfiguration


class CameraWorker:
    def __init__(
        self,
        camera: Camera,
        configuration: CameraConfiguration,
    ):
        self.camera = camera
        self.configuration = configuration
        self.running = False

    def start(self) -> None:
        if self.running:
            return

        self.running = True

        print(
            f"Camera {self.camera.id} started"
        )

    def stop(self) -> None:
        if not self.running:
            return

        self.running = False

        print(
            f"Camera {self.camera.id} stopped"
        )

    def restart(self) -> None:
        self.stop()
        self.start()

    def is_running(self) -> bool:
        return self.running

    def update_configuration(
        self,
        configuration: CameraConfiguration,
    ) -> None:
        self.configuration = configuration