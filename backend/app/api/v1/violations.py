from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.core.permissions import require_admin
from app.models.user import User
from app.schemas.violation import (
    ViolationCreate,
    ViolationResponse,
    ViolationUpdate,
)
from app.services.violation_service import ViolationService

router = APIRouter(
    prefix="/violations",
    tags=["Violations"],
)


@router.get(
    "/",
    response_model=list[ViolationResponse],
)
def list_violations(
    db: Session = Depends(get_db),
):
    service = ViolationService(db)
    return service.list_violations()


@router.get(
    "/camera/{camera_id}",
    response_model=list[ViolationResponse],
)
def get_camera_violations(
    camera_id: int,
    db: Session = Depends(get_db),
):
    service = ViolationService(db)
    return service.get_camera_violations(camera_id)


@router.get(
    "/{violation_id}",
    response_model=ViolationResponse,
)
def get_violation(
    violation_id: int,
    db: Session = Depends(get_db),
):
    service = ViolationService(db)

    violation = service.get_violation(violation_id)

    if violation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Violation not found",
        )

    return violation


@router.post(
    "/",
    response_model=ViolationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_violation(
    data: ViolationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    service = ViolationService(db)

    return service.create_violation(
        camera_id=data.camera_id,
        worker_id=data.worker_id,
        violation_type=data.violation_type,
        confidence=data.confidence,
    )


@router.put(
    "/{violation_id}",
    response_model=ViolationResponse,
)
def update_violation(
    violation_id: int,
    data: ViolationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    service = ViolationService(db)

    violation = service.get_violation(violation_id)

    if violation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Violation not found",
        )

    return service.update_violation(
        violation,
        data,
    )


@router.delete(
    "/{violation_id}",
)
def delete_violation(
    violation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    service = ViolationService(db)

    violation = service.get_violation(violation_id)

    if violation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Violation not found",
        )

    service.delete_violation(violation)

    return {
        "message": "Violation deleted successfully",
    }
