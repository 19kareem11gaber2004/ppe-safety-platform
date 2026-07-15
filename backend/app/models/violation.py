from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Violation(Base):

    __tablename__ = "violations"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


    camera_id: Mapped[int] = mapped_column(
        ForeignKey("cameras.id"),
        nullable=False
    )


    worker_id: Mapped[int] = mapped_column(
        ForeignKey("workers.id"),
        nullable=False
    )


    violation_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )


    confidence: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )


    status: Mapped[str] = mapped_column(
        String(50),
        default="open"
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


    camera = relationship(
        "Camera",
        back_populates="violations"
    )


    worker = relationship(
        "Worker",
        back_populates="violations"
    )


    snapshots = relationship(
        "Snapshot",
        back_populates="violation"
    )