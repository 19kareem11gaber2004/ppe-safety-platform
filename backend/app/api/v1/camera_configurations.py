from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.core.permissions import require_admin
from app.models.user import User
from app.schemas.camera_configuration import (
    CameraConfigurationCreate,
    CameraConfigurationResponse,
    CameraConfigurationUpdate,
)
from app.services.camera_configuration_service import (
    CameraConfigurationService,
)

router = APIRouter(
    prefix="/cameras/{camera_id}/configuration",
    tags=["Camera Configuration"],
)


@router.get(
    "",
    response_model=CameraConfigurationResponse,
)
def get_configuration(
    camera_id: int,
    db: Session = Depends(get_db),
):
    service = CameraConfigurationService(db)
    return service.get_configuration(camera_id)


@router.post(
    "",
    response_model=CameraConfigurationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_configuration(
    camera_id: int,
    data: CameraConfigurationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    service = CameraConfigurationService(db)
    return service.create_configuration(camera_id, data)


@router.put(
    "",
    response_model=CameraConfigurationResponse,
)
def update_configuration(
    camera_id: int,
    data: CameraConfigurationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    service = CameraConfigurationService(db)
    return service.update_configuration(camera_id, data)


@router.delete(
    "",
)
def delete_configuration(
    camera_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    service = CameraConfigurationService(db)
    service.delete_configuration(camera_id)

    return {
        "message": "Camera configuration deleted successfully"
    }
