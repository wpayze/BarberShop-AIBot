from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr


class ClientBase(BaseModel):
    businessId: UUID
    fullName: str
    phone: str
    email: EmailStr
    notes: str | None = None


class ClientCreate(ClientBase):
    pass


class ClientOut(ClientBase):
    id: UUID
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True
