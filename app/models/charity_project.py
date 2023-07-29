from sqlalchemy import Column, String, Text

from .abstract_model import CharityFundAbstractModel
from app.core import settings


class CharityProject(CharityFundAbstractModel):
    name = Column(String(settings.MAX_LENGTH), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return (
            f'Имя проекта: {self.name}, {super().__repr__()}'
        )
