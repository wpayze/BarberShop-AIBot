from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class StaffBase(BaseModel):
    businessId: UUID
    displayName: str
    photoUrl: str | None = None
    bio: str | None = None
    isActive: bool = True
    sortOrder: int = 0


class StaffCreate(StaffBase):
    pass


class StaffOut(StaffBase):
    id: UUID
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True


class StaffUpdate(BaseModel):
    displayName: str | None = None
    photoUrl: str | None = None
    bio: str | None = None
    isActive: bool | None = None
    sortOrder: int | None = None

    class Config:
        extra = "forbid"
