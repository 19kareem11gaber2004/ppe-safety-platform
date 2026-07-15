from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class AuditLog(Base):

    __tablename__ = "audit_logs"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )


    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )


    action: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )


    entity: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


    user = relationship(
        "User",
        back_populates="audit_logs"
    )