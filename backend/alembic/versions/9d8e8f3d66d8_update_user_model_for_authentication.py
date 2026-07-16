"""update user model for authentication

Revision ID: 9d8e8f3d66d8
Revises: f77a34bc873e
Create Date: 2026-07-16 01:06:28.913597
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = "9d8e8f3d66d8"
down_revision: Union[str, Sequence[str], None] = "f77a34bc873e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    user_role = postgresql.ENUM(
        "ADMIN",
        "SAFETY_OFFICER",
        "VIEWER",
        name="user_role",
    )

    user_role.create(op.get_bind(), checkfirst=True)

    op.add_column(
        "users",
        sa.Column(
            "is_superuser",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text("false"),
        ),
    )

    op.add_column(
        "users",
        sa.Column(
            "last_login_at",
            sa.DateTime(),
            nullable=True,
        ),
    )

    op.alter_column(
        "users",
        "role",
        existing_type=sa.VARCHAR(length=50),
        type_=user_role,
        existing_nullable=False,
        postgresql_using="role::user_role",
    )

    op.drop_constraint(
        op.f("users_email_key"),
        "users",
        type_="unique",
    )

    op.create_index(
        op.f("ix_users_email"),
        "users",
        ["email"],
        unique=True,
    )


def downgrade() -> None:
    """Downgrade schema."""

    user_role = postgresql.ENUM(
        "ADMIN",
        "SAFETY_OFFICER",
        "VIEWER",
        name="user_role",
    )

    op.drop_index(
        op.f("ix_users_email"),
        table_name="users",
    )

    op.create_unique_constraint(
        op.f("users_email_key"),
        "users",
        ["email"],
    )

    op.alter_column(
        "users",
        "role",
        existing_type=user_role,
        type_=sa.VARCHAR(length=50),
        existing_nullable=False,
    )

    op.drop_column("users", "last_login_at")
    op.drop_column("users", "is_superuser")

    user_role.drop(op.get_bind(), checkfirst=True)