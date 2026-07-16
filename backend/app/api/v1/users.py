from fastapi import APIRouter, Depends

from app.core.dependencies import get_current_user
from app.models.user import User
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.core.permissions import require_admin
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/me")
def get_profile(
    current_user: User = Depends(get_current_user),
):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "role": current_user.role,
        "is_active": current_user.is_active,
        "is_superuser": current_user.is_superuser,
    }
    
@router.get(
    "",
    response_model=list[UserResponse],
)
def list_users(
    _: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    service = UserService(UserRepository(db))
    return service.list_users()


@router.get(
    "/{user_id}",
    response_model=UserResponse,
)
def get_user(
    user_id: int,
    _: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    service = UserService(UserRepository(db))

    user = service.get_user(user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user_data: UserCreate,
    _: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    service = UserService(UserRepository(db))

    if service.get_user_by_email(user_data.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists",
        )

    return service.create_user(user_data)


@router.put(
    "/{user_id}",
    response_model=UserResponse,
)
def update_user(
    user_id: int,
    user_data: UserUpdate,
    _: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    service = UserService(UserRepository(db))

    user = service.get_user(user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return service.update_user(user, user_data)


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user(
    user_id: int,
    _: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    service = UserService(UserRepository(db))

    user = service.get_user(user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    service.delete_user(user)