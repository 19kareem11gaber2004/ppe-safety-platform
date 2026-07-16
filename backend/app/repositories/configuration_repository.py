from sqlalchemy.orm import Session

from app.models.configuration import SystemConfiguration
from app.repositories.base_repository import BaseRepository


class ConfigurationRepository(
    BaseRepository[SystemConfiguration]
):

    def __init__(self, db: Session):
        super().__init__(
            SystemConfiguration,
            db
        )


    def get_by_key(
        self,
        key: str,
    ):

        return (
            self.db.query(SystemConfiguration)
            .filter(
                SystemConfiguration.key == key
            )
            .first()
        )