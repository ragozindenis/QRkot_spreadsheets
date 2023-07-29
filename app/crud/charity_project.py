from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDProject(CRUDBase):

    async def get_project_id_by_name(
        self,
        project_name: str,
        session: AsyncSession,
    ) -> Optional[int]:
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        db_project_id = db_project_id.scalars().first()
        return db_project_id

    async def get_projects_by_completion_rate(
        self,
        session: AsyncSession,
    ):
        projects = await session.execute(
            select(self.model).where(self.model.fully_invested.is_(True))
        )
        projects = projects.scalars().all()
        projects.sort(
            key=lambda project: project.close_date - project.create_date
        )
        return projects


project_crud = CRUDProject(CharityProject)
