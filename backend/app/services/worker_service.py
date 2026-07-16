from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.worker import Worker
from app.repositories.worker_repository import WorkerRepository
from app.schemas.worker import WorkerCreate, WorkerUpdate


class WorkerService:

    def __init__(self, db: Session):
        self.repository = WorkerRepository(db)

    def create_worker(
        self,
        data: WorkerCreate,
    ) -> Worker:

        existing_worker = self.repository.get_by_identifier(
            data.identifier
        )

        if existing_worker:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Worker identifier already exists",
            )

        worker = Worker(
            identifier=data.identifier,
            name=data.name,
        )

        return self.repository.create(worker)


    def get_worker(
        self,
        worker_id: int,
    ) -> Worker:

        worker = self.repository.get_by_id(worker_id)

        if not worker:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Worker not found",
            )

        return worker


    def list_workers(self) -> list[Worker]:

        return self.repository.get_all()


    def update_worker(
        self,
        worker_id: int,
        data: WorkerUpdate,
    ) -> Worker:

        worker = self.get_worker(worker_id)

        if data.identifier:

            existing_worker = self.repository.get_by_identifier(
                data.identifier
            )

            if existing_worker and existing_worker.id != worker.id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Worker identifier already exists",
                )

        update_data = data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(worker, key, value)

        self.repository.db.commit()
        self.repository.db.refresh(worker)

        return worker


    def delete_worker(
        self,
        worker_id: int,
    ) -> None:

        worker = self.get_worker(worker_id)

        self.repository.delete(worker)

        self.repository.db.commit()