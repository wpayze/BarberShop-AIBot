from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.auth import (
    BusinessSignupRequest,
    BusinessSignupResponse,
    LoginRequest,
    LoginResponse,
    UserUpdate,
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
        "name": current_user.name,
        "email": current_user.email,
        "role": current_user.role,
        "businessId": current_user.businessId,
    }


@router.patch("/me")
def update_profile(
    data: UserUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    user = AuthService.update_user(db, current_user.id, data)
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role,
        "businessId": user.businessId,
    }
