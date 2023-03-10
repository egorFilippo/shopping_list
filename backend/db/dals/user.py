import uuid

from sqlalchemy import select, and_, update
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import User


class UserDAL:
    """ Data Access Layer for operating User info"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, **kwargs):
        new_user = User(**kwargs, is_active=True)
        self.session.add(new_user)
        await self.session.flush()
        return new_user

    async def update_user(self, user_id, **kwargs):
        query = update(User).where(
                and_(
                User.id == user_id,
                User.is_active == True
            )
        ).values(kwargs).returning(User.id, User.first_name, User.last_name, User.email, User.is_active)
        result = await self.session.execute(query)
        update_user_row = result.fetchone()
        if update_user_row is not None:
            return update_user_row

    async def get_users(self):
        query = select(User)
        result = await self.session.execute(query)
        user_rows = result.fetchall()
        return user_rows

    async def get_user_by_id(self, user_id: uuid.UUID):
        query = select(User).where(and_(
            User.id == user_id,
            User.is_active == True
        ))
        result = await self.session.execute(query)
        user_row = result.fetchone()
        if user_row is not None:
            return user_row[0]

    async def delete_user(self, ):
        pass

