from datetime import datetime
from http import HTTPStatus
from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, Extra, Field, validator

from app.core import settings


class ProjectBase(BaseModel):
    name: str = Field(..., max_length=settings.MAX_LENGTH)
    description: str
    full_amount: int = Field(..., gt=settings.DEFAULT_VALUE_FULL_AMOUNT)

    class Config:
        extra = Extra.forbid
        min_anystr_length = settings.MIN_LENGTH


class ProjectCreate(ProjectBase):

    @validator('name', 'description')
    def check_name(cls, value):
        if not value:
            raise ValueError("Обязательное поле")
        return value


class ProjectDB(ProjectBase):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True


class ProjectUpdate(ProjectBase):
    name: Optional[str]
    description: Optional[str]
    full_amount: Optional[int]

    @validator('name', 'description', 'full_amount')
    def cannot_be_null(cls, value):
        if not value:
            raise HTTPException(
                status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                detail='Нельзя передать null'
            )
        return value
