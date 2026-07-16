from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, get_current_user
from app.core.permissions import require_admin
from app.models.user import User
from app.schemas.worker import (
    WorkerCreate,
    WorkerResponse,
    WorkerUpdate,
)
from app.services.worker_service import WorkerService


router = APIRouter(
    prefix="/workers",
    tags=["Workers"],
)


@router.get(
    "/",
    response_model=list[WorkerResponse],
)
def list_workers(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = WorkerService(db)

    return service.list_workers()


@router.get(
    "/{worker_id}",
    response_model=WorkerResponse,
)
def get_worker(
    worker_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = WorkerService(db)

    return service.get_worker(worker_id)


@router.post(
    "/",
    response_model=WorkerResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_worker(
    data: WorkerCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    service = WorkerService(db)

    return service.create_worker(data)


@router.put(
    "/{worker_id}",
    response_model=WorkerResponse,
)
def update_worker(
    worker_id: int,
    data: WorkerUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    service = WorkerService(db)

    return service.update_worker(
        worker_id,
        data,
    )


@router.delete(
    "/{worker_id}",
)
def delete_worker(
    worker_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    service = WorkerService(db)

    service.delete_worker(worker_id)

    return {
        "message": "Worker deleted successfully",
    }
