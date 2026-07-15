from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Snapshot(Base):

    __tablename__ = "snapshots"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


    violation_id: Mapped[int] = mapped_column(
        ForeignKey("violations.id"),
        nullable=False
    )


    storage_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


    violation = relationship(
        "Violation",
        back_populates="snapshots"
    )