from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Donation


class CRUDDonation(CRUDBase):

    async def get_donations_by_user_id(
            self,
            user: int,
            session: AsyncSession,
    ) -> Optional[int]:
        db_donations = await session.execute(
            select(Donation).where(
                Donation.user_id == user.id
            )
        )
        db_donations = db_donations.scalars().all()
        return db_donations


donation_crud = CRUDDonation(Donation)
