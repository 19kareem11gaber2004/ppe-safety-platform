from datetime import datetime

from pydantic import BaseModel, ConfigDict


class WorkerBase(BaseModel):
    identifier: str
    name: str | None = None


class WorkerCreate(WorkerBase):
    pass


class WorkerUpdate(BaseModel):
    identifier: str | None = None
    name: str | None = None


class WorkerResponse(WorkerBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )
