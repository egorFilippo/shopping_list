import datetime
import uuid

from pydantic import BaseModel


class GroupCreate(BaseModel):
    name: str


class GroupRead(BaseModel):
    id: uuid.UUID
    created_by: uuid.UUID
    created_dttm: datetime.datetime


class GroupMemberCreate(BaseModel):
    group_id: uuid.UUID
    member_id: uuid.UUID


class GroupMemberRead(BaseModel):
    id: uuid.UUID
    joined_dttm: datetime.datetime
    invited_by: uuid.UUID
    group_id: uuid.UUID
    member_id: uuid.UUID
