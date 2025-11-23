from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.auth import BusinessSignupRequest, BusinessSignupResponse
from app.services.auth_service import AuthService
from app.db.session import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/signup", response_model=BusinessSignupResponse)
def signup(data: BusinessSignupRequest, db: Session = Depends(get_db)):
    return AuthService.signup(db, data)
