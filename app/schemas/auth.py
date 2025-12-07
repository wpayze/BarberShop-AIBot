from pydantic import BaseModel, EmailStr


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
    password: str | None = None

    class Config:
        extra = "forbid"
