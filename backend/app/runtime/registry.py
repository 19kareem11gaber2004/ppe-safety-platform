from typing import Any


class CameraRegistry:
    def __init__(self):
        self._workers: dict[int, Any] = {}

    def add(
        self,
        camera_id: int,
        worker: Any,
    ) -> None:
        self._workers[camera_id] = worker

    def get(
        self,
        camera_id: int,
    ) -> Any | None:
        return self._workers.get(camera_id)

    def remove(
        self,
        camera_id: int,
    ) -> None:
        self._workers.pop(camera_id, None)

    def exists(
        self,
        camera_id: int,
    ) -> bool:
        return camera_id in self._workers

    def all(self) -> dict[int, Any]:
        return self._workers

    def count(self) -> int:
        return len(self._workers)

    def clear(self) -> None:
        self._workers.clear()


camera_registry = CameraRegistry()
