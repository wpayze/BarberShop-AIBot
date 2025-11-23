from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class StaffServiceBase(BaseModel):
    staffId: UUID
    serviceId: UUID


class StaffServiceCreate(StaffServiceBase):
    pass


class StaffServiceOut(StaffServiceBase):
    id: UUID
    createdAt: datetime

    class Config:
        from_attributes = True
