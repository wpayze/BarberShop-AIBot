from uuid import UUID
from datetime import datetime, date, time
from pydantic import BaseModel

from app.models.enums import BookingStatus, BookingSource


class BookingBase(BaseModel):
    businessId: UUID
    staffId: UUID
    serviceId: UUID
    clientId: UUID
    clientName: str
    clientPhone: str
    clientEmail: str
    date: date
    startTime: time
    endTime: time
    status: BookingStatus = BookingStatus.PENDING
    source: BookingSource = BookingSource.ONLINE
    notes: str | None = None


class BookingCreate(BookingBase):
    pass


class BookingOut(BookingBase):
    id: UUID
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True
