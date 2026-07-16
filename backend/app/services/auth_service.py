from datetime import datetime, UTC

from app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    verify_password,
    TokenType,
)
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import LoginRequest, TokenResponse


class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def authenticate(self, credentials: LoginRequest) -> TokenResponse:
        user = self.repository.get_by_email(credentials.email)

        if user is None:
            raise ValueError("Invalid email or password")

        if not verify_password(
            credentials.password,
            user.password_hash,
        ):
            raise ValueError("Invalid email or password")

        if not user.is_active:
            raise ValueError("User account is disabled")

        user.last_login_at = datetime.now(UTC)
        self.repository.update(user)

        access_token = create_access_token(
            subject=str(user.id),
        )

        refresh_token = create_refresh_token(
            subject=str(user.id),
        )

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
        )

    def refresh_access_token(
        self,
        refresh_token: str,
    ) -> TokenResponse:
        try:
            payload = decode_token(refresh_token)
        except Exception:
            raise ValueError("Invalid refresh token")

        if payload.get("type") != TokenType.REFRESH.value:
            raise ValueError("Invalid refresh token")

        user_id = payload.get("sub")

        if user_id is None:
            raise ValueError("Invalid refresh token")

        user = self.repository.get_by_id(int(user_id))

        if user is None:
            raise ValueError("User not found")

        if not user.is_active:
            raise ValueError("User account is disabled")

        access_token = create_access_token(
            subject=str(user.id),
        )

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
        )

    def get_user_by_email(self, email: str) -> User | None:
        return self.repository.get_by_email(email)