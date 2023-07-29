from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (
    check_full_amount, check_if_already_invested_in_project,
    check_if_project_is_closed, check_name_duplicate,
    check_project_exists
)
from app.core import current_superuser, get_async_session
from app.crud import donation_crud, project_crud
from app.schemas import ProjectCreate, ProjectDB, ProjectUpdate
from app.services import investing


router = APIRouter()


@router.post(
    '/',
    response_model=ProjectDB,
    dependencies=[Depends(current_superuser)],
    response_model_exclude_none=True
)
async def create_new_project(
    project: ProjectCreate,
    session: AsyncSession = Depends(get_async_session),
) -> ProjectDB:
    """Только для суперюзеров."""
    await check_name_duplicate(project.name, session)
    new_project = await project_crud.create(
        project, session, enable_commit=False
    )
    session.add_all(
        investing(
            new_project, await donation_crud.get_not_closed_db_objs(session)
        )
    )
    await session.commit()
    await session.refresh(new_project)
    return new_project


@router.get(
    '/',
    response_model=list[ProjectDB],
    response_model_exclude_none=True,
)
async def get_all_meeting_rooms(
    session: AsyncSession = Depends(get_async_session),
) -> list[ProjectDB]:
    """Запрос всех проектов"""
    return await project_crud.get_multi(session)


@router.delete(
    '/{project_id}',
    response_model=ProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def remove_meeting_room(
    project_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> ProjectDB:
    """Только для суперюзеров."""
    project = await check_project_exists(
        project_id, session
    )
    await check_if_already_invested_in_project(project_id, session)
    await check_if_project_is_closed(project_id, session)
    return await project_crud.remove(project, session)


@router.patch(
    '/{project_id}',
    response_model=ProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def partially_update_project(
    project_id: int,
    obj_in: ProjectUpdate,
    session: AsyncSession = Depends(get_async_session),
) -> ProjectDB:
    """Только для суперюзеров."""
    project = await check_project_exists(
        project_id, session
    )
    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, session)
    await check_if_project_is_closed(project_id, session)
    if obj_in.full_amount is not None:
        await check_full_amount(
            project_id, obj_in, session
        )
    return await project_crud.update(project, obj_in, session)
