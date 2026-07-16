from sqlalchemy.orm import Session

from app.repositories.configuration_repository import (
    ConfigurationRepository,
)


class ConfigurationReader:

    def __init__(
        self,
        db: Session,
    ):
        self.repository = ConfigurationRepository(
            db
        )


    def get(
        self,
        key: str,
    ) -> str | None:

        config = (
            self.repository.get_by_key(
                key
            )
        )

        if not config:
            return None

        return config.value


    def get_float(
        self,
        key: str,
    ) -> float | None:

        value = self.get(key)

        if value is None:
            return None

        return float(value)


    def get_int(
        self,
        key: str,
    ) -> int | None:

        value = self.get(key)

        if value is None:
            return None

        return int(value)
