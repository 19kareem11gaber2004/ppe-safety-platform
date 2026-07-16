from app.db.session import SessionLocal
from app.models.enums import UserRole
from app.models.user import User
from app.core.security import hash_password


ADMIN_EMAIL = "admin@ppe.com"
ADMIN_PASSWORD = "Admin@123"


def create_admin() -> None:
    db = SessionLocal()

    try:
        existing_admin = (
            db.query(User)
            .filter(User.email == ADMIN_EMAIL)
            .first()
        )

        if existing_admin:
            print("Admin user already exists.")
            return

        admin = User(
            email=ADMIN_EMAIL,
            password_hash=hash_password(ADMIN_PASSWORD),
            role=UserRole.ADMIN,
            is_active=True,
            is_superuser=True,
        )

        db.add(admin)
        db.commit()

        print("Admin user created successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    create_admin()