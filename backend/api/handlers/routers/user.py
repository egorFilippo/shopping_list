import uuid
from typing import List, Optional

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas import UserRead, UserCreate, UserUpdate
from db.sessions import get_async_session
import api.handlers.controllers.user as user_controller

user_router = APIRouter()


@user_router.post("/", response_model=UserRead)
async def create_user(user: UserCreate, session: AsyncSession = Depends(get_async_session)):
    return await user_controller._create_user(user, session)


@user_router.get("/", response_model=List[UserRead])
async def get_users(session: AsyncSession = Depends(get_async_session)) -> List[UserRead]:
    users = await user_controller._get_users(session)

    return users


@user_router.get("/{user_id}", response_model=UserRead)
async def get_user_by_id(user_id: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
    user = await user_controller._get_user_by_id(user_id, session)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id={user_id} does not exist",
                            #code="object_not_found"
        )
    return user


@user_router.patch("/{user_id}", response_model=Optional[UserRead])
async def update_user(user_id: uuid.UUID, body: UserUpdate, session: AsyncSession = Depends(get_async_session)):
    if body.dict(exclude_none=True) == {}:
        raise HTTPException(status_code=404, detail="At least one field should be provided")
    user = await user_controller._update_user(user_id, body, session)
    return user
