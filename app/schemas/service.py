from uuid import UUID
from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel


class ServiceBase(BaseModel):
    businessId: UUID
    name: str
    description: str | None = None
    durationMinutes: int
    price: Decimal
    category: str | None = None
    isActive: bool = True


class ServiceCreate(ServiceBase):
    pass


class ServiceOut(ServiceBase):
    id: UUID
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True


class ServiceUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    durationMinutes: int | None = None
    price: Decimal | None = None
    category: str | None = None
    isActive: bool | None = None

    class Config:
        extra = "forbid"
