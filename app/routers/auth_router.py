from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.auth import (
    BusinessSignupRequest,
    BusinessSignupResponse,
    LoginRequest,
    LoginResponse,
    UserUpdate,
    UserOut,
    PasswordUpdate,
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
    user = AuthService.update_user(
        db, current_user.id, data, allowed_business_id=current_user.businessId
    )
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role,
        "businessId": user.businessId,
    }


@router.get("/users", response_model=list[UserOut])
def list_users(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    # Business scope comes from the authenticated user token
    return AuthService.list_users(db, current_user.businessId)


@router.patch("/user/{user_id}", response_model=UserOut)
def update_user(
    user_id: UUID,
    data: UserUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    # Only allow updates within the same business
    return AuthService.update_user(
        db, user_id, data, allowed_business_id=current_user.businessId
    )


@router.patch("/me/password")
def update_password(
    data: PasswordUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return AuthService.change_password(db, current_user.id, data)
