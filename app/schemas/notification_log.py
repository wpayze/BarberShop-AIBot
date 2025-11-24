from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class NotificationLogBase(BaseModel):
    businessId: UUID
    bookingId: UUID | None = None
    channel: str
    recipient: str
    templateKey: str
    payload: dict | None = None
    status: str
    errorMessage: str | None = None


class NotificationLogCreate(NotificationLogBase):
    pass


class NotificationLogOut(NotificationLogBase):
    id: UUID
    createdAt: datetime

    class Config:
        from_attributes = True
