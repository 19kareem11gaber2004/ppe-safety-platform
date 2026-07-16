from sqlalchemy.orm import Session

from app.models.configuration import SystemConfiguration
from app.repositories.base_repository import BaseRepository


class ConfigurationRepository(
    BaseRepository[SystemConfiguration]
):

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(
            SystemConfiguration,
            db,
        )


    def get_by_key(
        self,
        key: str,
    ) -> SystemConfiguration | None:

        return (
            self.db.query(SystemConfiguration)
            .filter(
                SystemConfiguration.key == key
            )
            .first()
        )


    def get_by_category(
        self,
        category: str,
    ) -> list[SystemConfiguration]:

        return (
            self.db.query(SystemConfiguration)
            .filter(
                SystemConfiguration.category == category
            )
            .all()
        )


    def get_all(
        self,
    ) -> list[SystemConfiguration]:

        return (
            self.db.query(SystemConfiguration)
            .all()
        )


    def update_value(
        self,
        configuration: SystemConfiguration,
        value: str,
    ) -> SystemConfiguration:

        configuration.value = value

        self.db.commit()
        self.db.refresh(
            configuration
        )

        return configuration


    def delete(
        self,
        configuration: SystemConfiguration,
    ) -> None:

        self.db.delete(
            configuration
        )

        self.db.commit()
