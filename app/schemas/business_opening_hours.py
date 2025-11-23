from uuid import UUID
from datetime import time
from pydantic import BaseModel


class BusinessOpeningHoursBase(BaseModel):
    businessId: UUID
    dayOfWeek: int
    openTime: time | None = None
    closeTime: time | None = None
    isClosed: bool = False


class BusinessOpeningHoursCreate(BusinessOpeningHoursBase):
    pass


class BusinessOpeningHoursOut(BusinessOpeningHoursBase):
    id: UUID

    class Config:
        from_attributes = True
