from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ConfigurationBase(BaseModel):
    key: str
    value: str
    category: str
    data_type: str
    description: str | None = None
    is_editable: bool = True


class ConfigurationCreate(
    ConfigurationBase
):
    pass


class ConfigurationUpdate(BaseModel):
    value: str


class ConfigurationResponse(
    ConfigurationBase
):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )
