from datetime import datetime, UTC
from typing import Any, Generic, Optional, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):

    success: bool = True

    message: str

    data: Optional[T] = None

    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )


class ErrorResponse(BaseModel):

    success: bool = False

    message: str

    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )
