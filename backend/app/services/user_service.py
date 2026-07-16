from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import hash_password

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_user(self, user_id: int) -> User | None:
        return self.repository.get_by_id(user_id)

    def get_user_by_email(self, email: str) -> User | None:
        return self.repository.get_by_email(email)

    def list_users(self) -> list[User]:
        return self.repository.list()

    def create_user(self, user_data: UserCreate) -> User:
        user = User(
            email=user_data.email,
            password_hash=hash_password(user_data.password),
            role=user_data.role,
        )

        return self.repository.create(user)

    def update_user(self, user: User, user_data: UserUpdate) -> User:
        if user_data.email is not None:
            user.email = user_data.email

        if user_data.role is not None:
            user.role = user_data.role

        if user_data.is_active is not None:
            user.is_active = user_data.is_active

        return self.repository.update(user)

    def delete_user(self, user: User) -> None:
        self.repository.delete(user)