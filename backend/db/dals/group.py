from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Group, GroupMember


class GroupDAL:
    """ Data Access Layer for operating Group info"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_group(self, **kwargs):
        new_group = Group(**kwargs)
        self.session.add(new_group)
        await self.session.flush()
        return new_group


class GroupMemberDAL:
    """ Data Access Layer for operating GroupMember info"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_group_member(self, **kwargs):
        new_group_member = GroupMember(**kwargs)
        self.session.add(new_group_member)
        await self.session.flush()
        return new_group_member
