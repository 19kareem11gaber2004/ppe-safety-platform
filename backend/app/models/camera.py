from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Camera(Base):

    __tablename__ = "cameras"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )


    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )


    location: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )


    source_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )


    connection_url: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )


    status: Mapped[str] = mapped_column(
        String(50),
        default="inactive",
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )


    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )


    configuration = relationship(
        "CameraConfiguration",
        back_populates="camera",
        uselist=False,
        cascade="all, delete",
    )


    violations = relationship(
        "Violation",
        back_populates="camera",
    )
