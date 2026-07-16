from sqlalchemy.orm import Session

from app.repositories.configuration_repository import (
    ConfigurationRepository,
)


class ConfigurationService:

    def __init__(
        self,
        db: Session,
    ):
        self.repository = ConfigurationRepository(db)


    def get_value(
        self,
        key: str,
    ):

        config = self.repository.get_by_key(key)

        if not config:
            return None

        return config.value