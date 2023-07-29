from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import project_crud
from app.models import CharityProject
from app.schemas import ProjectUpdate


async def check_name_duplicate(
    project_name: str,
    session: AsyncSession,
) -> None:
    project_id = await project_crud.get_project_id_by_name(
        project_name, session
    )
    if project_id is not None:
        raise HTTPException(
            status_code=400,
            detail='Проект с таким именем уже существует!',
        )


async def check_project_exists(
    project_id: int,
    session: AsyncSession,
) -> CharityProject:
    project = await project_crud.get(project_id, session)
    if project is None:
        raise HTTPException(
            status_code=404,
            detail='Проект не найден!'
        )
    return project


async def check_if_already_invested_in_project(
    project_id: int,
    session: AsyncSession,
) -> None:
    project = await project_crud.get(project_id, session)
    if project.invested_amount > 0:
        raise HTTPException(
            status_code=400,
            detail='В проект были внесены средства, не подлежит удалению!'
        )


async def check_if_project_is_closed(
    project_id: int,
    session: AsyncSession,
) -> None:
    project = await project_crud.get(project_id, session)
    if project.fully_invested is True:
        raise HTTPException(
            status_code=400,
            detail='Закрытый проект нельзя редактировать!'
        )


async def check_full_amount(
    project_id: int,
    obj_in: ProjectUpdate,
    session: AsyncSession,
) -> None:
    project = await project_crud.get(project_id, session)
    if obj_in.full_amount < project.invested_amount:
        raise HTTPException(
            status_code=422,
            detail='Сумма не может быть меньше уже внесённой!'
        )
