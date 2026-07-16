from sqlalchemy.orm import Session

from app.models.violation import Violation
from app.repositories.base_repository import BaseRepository


class ViolationRepository(BaseRepository[Violation]):

    def __init__(self, db: Session):
        super().__init__(
            Violation,
            db
        )


    def get_by_camera(
        self,
        camera_id: int,
    ):

        return (
            self.db.query(Violation)
            .filter(
                Violation.camera_id == camera_id
            )
            .all()
        )
def get_by_id(
    self,
    violation_id: int,
) -> Violation | None:

    return (
        self.db.query(Violation)
        .filter(
            Violation.id == violation_id
        )
        .first()
    )


def list(self):

    return (
        self.db.query(Violation)
        .order_by(
            Violation.created_at.desc()
        )
        .all()
    )