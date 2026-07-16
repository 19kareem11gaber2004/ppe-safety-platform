from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.core.permissions import require_admin
from app.models.user import User
from app.schemas.camera import (
    CameraCreate,
    CameraResponse,
    CameraUpdate,
)
from app.services.camera_service import CameraService

router = APIRouter(
    prefix="/cameras",
    tags=["Cameras"],
)


@router.get(
    "/",
    response_model=list[CameraResponse],
)
def list_cameras(
    db: Session = Depends(get_db),
):
    service = CameraService(db)
    return service.list_cameras()


@router.get(
    "/active",
    response_model=list[CameraResponse],
)
def list_active_cameras(
    db: Session = Depends(get_db),
):
    service = CameraService(db)
    return service.get_active_cameras()


@router.get(
    "/{camera_id}",
    response_model=CameraResponse,
)
def get_camera(
    camera_id: int,
    db: Session = Depends(get_db),
):
    service = CameraService(db)

    camera = service.get_camera(camera_id)

    if camera is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Camera not found",
        )

    return camera


@router.post(
    "/",
    response_model=CameraResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_camera(
    data: CameraCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    service = CameraService(db)

    return service.create_camera(
        name=data.name,
        location=data.location,
        source_type=data.source_type,
        connection_url=data.connection_url,
    )


@router.put(
    "/{camera_id}",
    response_model=CameraResponse,
)
def update_camera(
    camera_id: int,
    data: CameraUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    service = CameraService(db)

    camera = service.get_camera(camera_id)

    if camera is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Camera not found",
        )

    return service.update_camera(
        camera,
        data,
    )


@router.delete(
    "/{camera_id}",
)
def delete_camera(
    camera_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    service = CameraService(db)

    camera = service.get_camera(camera_id)

    if camera is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Camera not found",
        )

    service.delete_camera(camera)

    return {
        "message": "Camera deleted successfully",
    }
