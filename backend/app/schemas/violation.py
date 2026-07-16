from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ViolationBase(BaseModel):
    camera_id: int
    worker_id: int
    violation_type: str
    confidence: float


class ViolationCreate(ViolationBase):
    pass


class ViolationUpdate(BaseModel):
    status: str | None = None


class ViolationResponse(ViolationBase):
    id: int
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
