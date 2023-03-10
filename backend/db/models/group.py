import datetime

from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from config.settings import Base


class Group(Base):
    __tablename__ = "group"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_by = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    created_dttm = Column(DateTime, default=datetime.datetime.utcnow)

    name = Column(String, nullable=False)


class GroupMember(Base):
    __tablename__ = "group_member"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    joined_dttm = Column(DateTime, default=datetime.datetime.utcnow)

    invited_by = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    group_id = Column(UUID(as_uuid=True), ForeignKey("group.id"))
    member_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
