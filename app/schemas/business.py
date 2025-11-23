from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class BusinessBase(BaseModel):
    name: str
    slug: str
    timezone: str
    contactEmail: EmailStr | None = None
    contactPhone: str | None = None
    addressLine1: str | None = None
    addressLine2: str | None = None
    city: str | None = None
    postalCode: str | None = None
    country: str | None = None
    planType: str = "free"
    isActive: bool = True

class BusinessCreate(BusinessBase):
    pass

class BusinessOut(BusinessBase):
    id: UUID
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True
