from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CameraConfigurationBase(BaseModel):

    fps: int = 30
    resolution: str = "640x640"
    stream_timeout: int = 10
    retry_count: int = 3
    detection_enabled: bool = True
    ai_model: str = "yolov8"


class CameraConfigurationCreate(
    CameraConfigurationBase
):
    pass


class CameraConfigurationUpdate(BaseModel):

    fps: int | None = None
    resolution: str | None = None
    stream_timeout: int | None = None
    retry_count: int | None = None
    detection_enabled: bool | None = None
    ai_model: str | None = None


class CameraConfigurationResponse(
    CameraConfigurationBase
):

    id: int
    camera_id: int
    created_at: datetime
    updated_at: datetime


    model_config = ConfigDict(
        from_attributes=True
    )
