from sqlalchemy.orm import Session

from app.repositories.violation_repository import ViolationRepository
from app.models.violation import Violation
from app.schemas.violation import (
    ViolationCreate,
    ViolationUpdate,
)

class ViolationService:

    def __init__(self, db: Session):
        self.repository = ViolationRepository(db)


    def create_violation(
        self,
        camera_id: int,
        worker_id: int,
        violation_type: str,
        confidence: float,
    ) -> Violation:

        violation = Violation(
            camera_id=camera_id,
            worker_id=worker_id,
            violation_type=violation_type,
            confidence=confidence,
            status="open",
        )

        return self.repository.create(violation)


    def get_camera_violations(
        self,
        camera_id: int,
    ):

        return self.repository.get_by_camera(camera_id)
    def list_violations(self):
     return self.repository.list()


def get_violation(
    self,
    violation_id: int,
):
    return self.repository.get_by_id(
        violation_id
    )


def update_violation(
    self,
    violation: Violation,
    data: ViolationUpdate,
):

    update_data = data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(
            violation,
            key,
            value,
        )

    return self.repository.update(
        violation
    )


def delete_violation(
    self,
    violation: Violation,
):

    self.repository.delete(
        violation
    )