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