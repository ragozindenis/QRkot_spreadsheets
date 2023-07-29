from datetime import datetime

from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, Integer

from app.core import Base


class CharityFundAbstractModel(Base):
    __abstract__ = True
    __table_args__ = (
        CheckConstraint('full_amount > 0', 'invested_amount <= full_amount'),
    )
    full_amount = Column(Integer)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=0)
    create_date = Column(DateTime, default=datetime.now())
    close_date = Column(DateTime, nullable=True)

    def __repr__(self):
        return (
            f'Инвестированно: {self.invested_amount} из {self.full_amount}, '
            f'Статус: {self.fully_invested}, '
            f'Создан: {self.create_date}, '
            f'Закрыт: {self.close_date}.'
        )
