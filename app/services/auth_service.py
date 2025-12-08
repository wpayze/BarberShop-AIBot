from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.schemas.auth import (
    BusinessSignupRequest,
    BusinessSignupResponse,
    LoginRequest,
    LoginResponse,
    UserUpdate,
    PasswordUpdate,
)
from app.repositories.business_repository import BusinessRepository
from app.repositories.business_user_repository import BusinessUserRepository
from app.schemas.business import BusinessCreate
from app.utils.security import hash_password, verify_password
from app.utils.jwt import create_access_token


class AuthService:

    @staticmethod
    def signup(db: Session, data: BusinessSignupRequest):

        try:
            # 1. Validar email duplicado
            existing_user = BusinessUserRepository.get_by_email(db, data.adminEmail)
            if existing_user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already registered",
                )

            # 2. Validar slug duplicado
            existing_slug = BusinessRepository.get_by_slug(db, data.slug)
            if existing_slug:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Business slug already exists",
                )

            # 3. Crear negocio
            business = BusinessRepository.create(
                db,
                BusinessCreate(
                    name=data.businessName, slug=data.slug, timezone=data.timezone
                ),
            )

            # 4. Crear usuario admin
            user = BusinessUserRepository.create_admin(
                db,
                email=data.adminEmail,
                password_hash=hash_password(data.adminPassword),
                business_id=business.id,
            )

            # 5. Commit final
            db.commit()
            db.refresh(business)
            db.refresh(user)

            return BusinessSignupResponse(
                businessId=str(business.id), adminUserId=str(user.id)
            )

        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Signup failed: {str(e)}",
            )

    @staticmethod
    def login(db: Session, data: LoginRequest):
        user = BusinessUserRepository.get_by_email(db, data.email)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid email or password",
            )

        if not verify_password(data.password, user.passwordHash):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid email or password",
            )

        # Generate JWT
        token = create_access_token(
            {"sub": str(user.id), "businessId": str(user.businessId), "role": user.role}
        )

        return LoginResponse(accessToken=token, tokenType="bearer")

    @staticmethod
    def update_user(db: Session, user_id, data: UserUpdate, allowed_business_id=None):
        user = BusinessUserRepository.get_by_id(db, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )

        if allowed_business_id and str(user.businessId) != str(allowed_business_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )

        updates = data.model_dump(exclude_unset=True)

        if "email" in updates:
            existing = BusinessUserRepository.get_by_email(db, updates["email"])
            if existing and str(existing.id) != str(user_id):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already registered",
                )

        try:
            user = BusinessUserRepository.update(db, user, updates)
            db.commit()
            db.refresh(user)
            return user
        except Exception as exc:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Could not update user: {str(exc)}",
            )

    @staticmethod
    def list_users(db: Session, business_id):
        return BusinessUserRepository.list_by_business(db, business_id)

    @staticmethod
    def change_password(db: Session, user_id, data: PasswordUpdate):
        user = BusinessUserRepository.get_by_id(db, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )

        if not verify_password(data.currentPassword, user.passwordHash):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid current password",
            )

        try:
            new_hash = hash_password(data.newPassword)
            BusinessUserRepository.update(db, user, {"passwordHash": new_hash})
            db.commit()
            return {"message": "Password updated successfully"}
        except Exception as exc:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Could not update password: {str(exc)}",
            )
