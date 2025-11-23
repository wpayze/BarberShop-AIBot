from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.auth import (
    BusinessSignupRequest,
    BusinessSignupResponse,
    LoginRequest,
    LoginResponse,
)
from app.services.auth_service import AuthService
from app.utils.dependencies import get_current_user
from app.db.session import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/signup", response_model=BusinessSignupResponse)
def signup(data: BusinessSignupRequest, db: Session = Depends(get_db)):
    return AuthService.signup(db, data)

@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    return AuthService.login(db, data)

@router.get("/me")
def get_profile(current_user=Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "role": current_user.role,
    }
