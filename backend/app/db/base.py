from sqlalchemy.orm import DeclarativeBase
from app.db.base import Base
from app import models

class Base(DeclarativeBase):
    pass