import uuid
from typing import List, Optional

from api.schemas.user import UserCreate, UserRead, UserUpdate
from db.dals import UserDAL


async def _create_user(user: UserCreate, db):
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            new_user = await user_dal.create_user(**user.dict())

            return UserRead(
                id=new_user.id,
                first_name=new_user.first_name,
                last_name=new_user.last_name,
                email=new_user.email,
                is_active=new_user.is_active,
            )


async def _get_users(db) -> List[UserRead]:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            users = await user_dal.get_users()
            if users is not None:
                return [UserRead(
                    id=user[0].id,
                    first_name=user[0].first_name,
                    last_name=user[0].last_name,
                    email=user[0].email,
                    is_active=user[0].is_active,
                ) for user in users]


async def _get_user_by_id(user_id: uuid.UUID, db) -> Optional[UserRead]:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.get_user_by_id(user_id)
            if user is not None:
                return UserRead(
                    id=user.id,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    email=user.email,
                    is_active=user.is_active,
                )


async def _update_user(user_id: uuid.UUID, body: UserUpdate, db) -> Optional[UserRead]:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.update_user(user_id, **body.dict(exclude_none=True))
            if user is not None:
                return UserRead(
                    id=user.id,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    email=user.email,
                    is_active=user.is_active,
                )