from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.schemas import GroupRead, GroupCreate, GroupMemberRead, GroupMemberCreate
import api.handlers.controllers.group as group_controller
from db.sessions import get_async_session
import uuid


group_router = APIRouter()
group_member_router = APIRouter()


@group_router.post("/", response_model=GroupRead)
async def create_group(group: GroupCreate, requested_by_user_id: uuid.UUID = "6d2ee442-77d9-45f5-aa58-3c87961567b2",
                       session: AsyncSession = Depends(get_async_session)):
    return await group_controller._create_group(group, requested_by_user_id, session)


@group_member_router.post("/", response_model=GroupMemberRead)
async def create_group_member(group_member: GroupMemberCreate,
                              requested_by_user_id: uuid.UUID = "6d2ee442-77d9-45f5-aa58-3c87961567b2",
                              session: AsyncSession = Depends(get_async_session),
                              ):
    return await group_controller._create_group_member(group_member, requested_by_user_id, session)
