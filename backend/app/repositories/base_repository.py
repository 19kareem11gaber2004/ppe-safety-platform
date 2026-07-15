from typing import Generic, Type, TypeVar

from sqlalchemy.orm import Session

from app.db.base import Base


ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):

    def __init__(
        self,
        model: Type[ModelType],
        db: Session,
    ):
        self.model = model
        self.db = db


    def get_by_id(
        self,
        entity_id: int,
    ):
        return (
            self.db.query(self.model)
            .filter(self.model.id == entity_id)
            .first()
        )


    def get_all(self):
        return self.db.query(self.model).all()


    def create(
        self,
        obj: ModelType,
    ):
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)

        return obj


    def delete(
        self,
        obj: ModelType,
    ):
        self.db.delete(obj)
        self.db.commit()