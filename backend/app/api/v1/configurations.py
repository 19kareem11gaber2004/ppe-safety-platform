from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.permissions import require_admin
from app.core.dependencies import get_db
from app.models.user import User
from app.schemas.configuration import (
    ConfigurationCreate,
    ConfigurationResponse,
    ConfigurationUpdate,
)
from app.services.configuration_service import (
    ConfigurationService,
)


router = APIRouter(
    prefix="/configurations",
    tags=["Configurations"],
)


@router.get(
    "",
    response_model=list[ConfigurationResponse],
)
def get_configurations(
    db: Session = Depends(get_db),
):
    service = ConfigurationService(db)

    return service.get_all()


@router.get(
    "/category/{category}",
    response_model=list[ConfigurationResponse],
)
def get_configurations_by_category(
    category: str,
    db: Session = Depends(get_db),
):
    service = ConfigurationService(db)

    return service.get_by_category(
        category
    )


@router.get(
    "/{key}",
    response_model=ConfigurationResponse,
)
def get_configuration(
    key: str,
    db: Session = Depends(get_db),
):
    service = ConfigurationService(db)

    return service.get_by_key(
        key
    )


@router.post(
    "",
    response_model=ConfigurationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_configuration(
    data: ConfigurationCreate,
    db: Session = Depends(get_db),
    _: User = Depends(require_admin),
):
    service = ConfigurationService(db)

    return service.create(
        data
    )


@router.put(
    "/{key}",
    response_model=ConfigurationResponse,
)
def update_configuration(
    key: str,
    data: ConfigurationUpdate,
    db: Session = Depends(get_db),
    _: User = Depends(require_admin),
):
    service = ConfigurationService(db)

    return service.update(
        key,
        data,
    )


@router.delete(
    "/{key}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_configuration(
    key: str,
    db: Session = Depends(get_db),
    _: User = Depends(require_admin),
):
    service = ConfigurationService(db)

    service.delete(
        key
    )

    return None
