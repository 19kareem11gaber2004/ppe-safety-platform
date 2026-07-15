from app.repositories.user_repository import UserRepository
from app.db.session import SessionLocal
from app.models.user import User


def test_user_repository_create_and_read():

    db = SessionLocal()

    try:
        repository = UserRepository(db)

        user = User(
            email="test@example.com",
            password_hash="hashed_password",
            role="admin",
            is_active=True,
        )

        created_user = repository.create(user)

        assert created_user.id is not None

        found_user = repository.get_by_email(
            "test@example.com"
        )

        assert found_user.email == "test@example.com"

    finally:
        db.close()