from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import current_superuser, current_user, get_async_session
from app.crud import donation_crud, project_crud
from app.models import User
from app.schemas import DonationCreate, DonationDB
from app.services import investing


router = APIRouter()


@router.post(
    '/',
    response_model=DonationDB,
    response_model_exclude={
        'invested_amount', 'fully_invested', 'user_id', 'close_date'
    },
    response_model_exclude_none=True
)
async def create_new_donation(
    donation: DonationCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
) -> DonationDB:
    """Создание пожертвования, только для зарегистрированных пользователей."""
    new_donation = await donation_crud.create(
        donation, session, user, enable_commit=False)
    session.add_all(
        investing(
            new_donation, await project_crud.get_not_closed_db_objs(session)
        )
    )
    await session.commit()
    await session.refresh(new_donation)
    return new_donation


@router.get(
    '/',
    response_model=list[DonationDB],
    dependencies=[Depends(current_superuser)],
    response_model_exclude_none=True,
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session),
) -> list[DonationDB]:
    """Только для суперюзеров."""
    all_donations = await donation_crud.get_multi(session)
    return all_donations


@router.get(
    '/my',
    response_model=list[DonationDB],
    response_model_exclude={
        'invested_amount', 'fully_invested', 'user_id', 'close_date'
    },
    response_model_exclude_none=True,
)
async def get_my_donations(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session),
) -> list[DonationDB]:
    """Получает список всех пожертвований для текущего пользователя."""
    donations = await donation_crud.get_donations_by_user_id(user, session)
    return donations
