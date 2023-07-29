from datetime import datetime

from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, Integer

from app.core import Base, settings


class CharityFundAbstractModel(Base):
    __abstract__ = True
    __table_args__ = (
        CheckConstraint('full_amount > 0', 'invested_amount <= full_amount'),
    )
    full_amount = Column(Integer)
    invested_amount = Column(
        Integer, default=settings.DEFAULT_VALUE_INVESTED_AMOUNT
    )
    fully_invested = Column(
        Boolean, default=settings.DEFALUT_VALUE_FULLY_INVESTED
    )
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime, nullable=True)

    def __repr__(self):
        return (
            f'Инвестированно: {self.invested_amount} из {self.full_amount}, '
            f'Статус: {self.fully_invested}, '
            f'Создан: {self.create_date}, '
            f'Закрыт: {self.close_date}.'
        )
