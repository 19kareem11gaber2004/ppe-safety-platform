from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Worker(Base):

    __tablename__ = "workers"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    identifier: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    name: Mapped[str | None] = mapped_column(
        String(100)
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


    violations = relationship(
        "Violation",
        back_populates="worker"
    )