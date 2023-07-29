from sqlalchemy import Column, ForeignKey, Integer, Text

from .abstract_model import CharityFundAbstractModel


class Donation(CharityFundAbstractModel):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)

    def __repr__(self):
        return (
            f'Id пользователя: {self.user_id}, {super().__repr__()}'
        )
