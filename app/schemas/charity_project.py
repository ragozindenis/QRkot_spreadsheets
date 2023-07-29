from datetime import datetime
from fastapi import HTTPException
from typing import Optional

from pydantic import BaseModel, Extra, Field, validator


class ProjectBase(BaseModel):
    name: str = Field(..., max_length=100)
    description: str
    full_amount: int = Field(..., gt=0)

    class Config:
        extra = Extra.forbid
        min_anystr_length = 1


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
                status_code=422,
                detail='Нельзя передать null'
            )
        return value
