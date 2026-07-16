from sqlalchemy.orm import Session

from app.models.worker import Worker
from app.repositories.base_repository import BaseRepository


class WorkerRepository(BaseRepository[Worker]):

    def __init__(self, db: Session):
        super().__init__(
            Worker,
            db,
        )

    def get_by_identifier(
        self,
        identifier: str,
    ) -> Worker | None:

        return (
            self.db.query(Worker)
            .filter(
                Worker.identifier == identifier,
            )
            .first()
        )
