from sqlalchemy import Column, String, Text

from .abstract_model import CharityFundAbstractModel


class CharityProject(CharityFundAbstractModel):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return (
            f'Имя проекта: {self.name}, {super().__repr__()}'
        )
