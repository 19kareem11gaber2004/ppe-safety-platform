from sqlalchemy.orm import Session

from fastapi import HTTPException, status

from app.models.configuration import SystemConfiguration
from app.repositories.configuration_repository import (
    ConfigurationRepository,
)
from app.schemas.configuration import (
    ConfigurationCreate,
    ConfigurationUpdate,
)


class ConfigurationService:

    def __init__(
        self,
        db: Session,
    ):
        self.repository = ConfigurationRepository(db)


    # ==========================
    # CRUD
    # ==========================

    def get_all(
        self,
    ) -> list[SystemConfiguration]:

        return self.repository.get_all()


    def get_by_category(
        self,
        category: str,
    ) -> list[SystemConfiguration]:

        return self.repository.get_by_category(
            category
        )


    def get_by_key(
        self,
        key: str,
    ) -> SystemConfiguration:

        configuration = (
            self.repository.get_by_key(key)
        )

        if not configuration:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Configuration not found",
            )

        return configuration


    def create(
        self,
        data: ConfigurationCreate,
    ) -> SystemConfiguration:

        existing = (
            self.repository.get_by_key(data.key)
        )

        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Configuration key already exists",
            )

        configuration = SystemConfiguration(
            key=data.key,
            value=data.value,
            category=data.category,
            data_type=data.data_type,
            description=data.description,
            is_editable=data.is_editable,
        )

        return self.repository.create(configuration)


    def update(
        self,
        key: str,
        data: ConfigurationUpdate,
    ) -> SystemConfiguration:

        configuration = self.get_by_key(key)

        if not configuration.is_editable:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Configuration cannot be edited",
            )

        self.validate_value(
            data.value,
            configuration.data_type,
        )

        return self.repository.update_value(
            configuration,
            data.value,
        )


    def delete(
        self,
        key: str,
    ) -> None:

        configuration = self.get_by_key(key)

        if not configuration.is_editable:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Configuration cannot be deleted",
            )

        self.repository.delete(configuration)


    # ==========================
    # Runtime Configuration
    # ==========================

    def get_value(
        self,
        key: str,
    ):

        configuration = self.get_by_key(key)

        value = configuration.value
        data_type = configuration.data_type


        if data_type == "integer":
            return int(value)


        if data_type == "float":
            return float(value)


        if data_type == "boolean":
            return value.lower() in (
                "true",
                "1",
                "yes",
            )


        return value



    def get_string(
        self,
        key: str,
    ) -> str:

        return str(
            self.get_value(key)
        )


    def get_int(
        self,
        key: str,
    ) -> int:

        return int(
            self.get_value(key)
        )


    def get_float(
        self,
        key: str,
    ) -> float:

        return float(
            self.get_value(key)
        )


    def get_bool(
        self,
        key: str,
    ) -> bool:

        return bool(
            self.get_value(key)
        )


    # ==========================
    # Validation
    # ==========================

    def validate_value(
        self,
        value: str,
        data_type: str,
    ) -> None:


        try:

            if data_type == "integer":
                int(value)


            elif data_type == "float":
                float(value)


            elif data_type == "boolean":

                if value.lower() not in (
                    "true",
                    "false",
                    "1",
                    "0",
                    "yes",
                    "no",
                ):
                    raise ValueError


        except ValueError:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid value for type {data_type}",
            )
