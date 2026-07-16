from datetime import datetime

from sqlalchemy import (
    Boolean,
    DateTime,
    Integer,
    String,
    ForeignKey,
)

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class CameraConfiguration(Base):

    __tablename__ = "camera_configurations"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )


    camera_id: Mapped[int] = mapped_column(
        ForeignKey("cameras.id"),
        nullable=False,
        unique=True,
    )


    fps: Mapped[int] = mapped_column(
        Integer,
        default=30,
    )


    resolution: Mapped[str] = mapped_column(
        String(50),
        default="640x640",
    )


    stream_timeout: Mapped[int] = mapped_column(
        Integer,
        default=10,
    )


    retry_count: Mapped[int] = mapped_column(
        Integer,
        default=3,
    )


    detection_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )


    ai_model: Mapped[str] = mapped_column(
        String(100),
        default="yolov8",
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


    camera = relationship(
        "Camera",
        back_populates="configuration",
    )
