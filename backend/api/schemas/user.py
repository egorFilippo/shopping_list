import uuid
from typing import Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: str


class UserRead(BaseModel):
    id: uuid.UUID
    first_name: Optional[str]
    last_name: Optional[str]
    email: str
    is_active: bool


class UserUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
