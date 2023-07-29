from datetime import datetime
from http import HTTPStatus
from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, Field, validator

from app.core import settings


class DonationBase(BaseModel):
    full_amount: Optional[int] = Field(
        ..., gt=settings.DEFAULT_VALUE_FULL_AMOUNT
    )
    comment: Optional[str]

    class Config:
        orm_mode = True


class DonationCreate(DonationBase):
    full_amount: int = Field(..., gt=settings.DEFAULT_VALUE_FULL_AMOUNT)

    @validator('full_amount')
    def full_amount_cannot_be_null(cls, value):
        if value is None:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Нельзя передать null'
            )
        return value


class DonationDB(DonationBase):
    id: int
    user_id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]
