import uuid

from api.schemas import GroupCreate, GroupRead, GroupMemberCreate, GroupMemberRead
from db.dals import GroupDAL, GroupMemberDAL


async def _create_group(group: GroupCreate, created_by: uuid.UUID, db):
    async with db as session:
        async with session.begin():
            group_dal = GroupDAL(session)
            new_group = await group_dal.create_group(**group.dict(), created_by=created_by)

            # add creator in new group
            await GroupMemberDAL(session).create_group_member(
                **GroupMemberCreate(
                    group_id=new_group.id,
                    member_id=created_by
                ).dict(),
                invited_by=created_by
            )

            return GroupRead(
                id=new_group.id,
                created_by=new_group.created_by,
                created_dttm=new_group.created_dttm,
            )




async def _create_group_member(group_member: GroupMemberCreate, created_by_id: uuid.UUID, db) -> GroupMemberRead:
    async with db as session:
        async with session.begin():
            group_member_dal = GroupMemberDAL(session)
            new_group_member = await group_member_dal.create_group_member(
                **group_member.dict(),
                invited_by=created_by_id
            )

            return GroupMemberRead(
                id=new_group_member.id,
                joined_dttm=new_group_member.joined_dttm,
                invited_by=new_group_member.invited_by,
                group_id=new_group_member.group_id,
                member_id=new_group_member.member_id,
            )
