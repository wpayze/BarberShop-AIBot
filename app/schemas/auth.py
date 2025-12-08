from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr

from app.models.enums import UserRole


class BusinessSignupRequest(BaseModel):
    businessName: str
    slug: str
    timezone: str
    adminEmail: EmailStr
    adminPassword: str

class BusinessSignupResponse(BaseModel):
    businessId: str
    adminUserId: str

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    accessToken: str
    tokenType: str = "bearer"


class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    role: UserRole | None = None
    isActive: bool | None = None

    class Config:
        extra = "forbid"


class UserOut(BaseModel):
    id: UUID
    businessId: UUID
    name: str
    email: EmailStr
    role: str
    isActive: bool
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True


class PasswordUpdate(BaseModel):
    currentPassword: str
    newPassword: str

    class Config:
        extra = "forbid"
