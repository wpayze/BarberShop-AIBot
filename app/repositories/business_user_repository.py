from sqlalchemy.orm import Session
from app.models.business_user import BusinessUser
from app.models.enums import UserRole

class BusinessUserRepository:
    @staticmethod
    def create_admin(db: Session, email: str, password_hash: str, business_id):
        user = BusinessUser(
            businessId=business_id,
            email=email,
            passwordHash=password_hash,
            role=UserRole.OWNER.value
        )
        db.add(user)
        db.flush()
        return user
    
    @staticmethod
    def get_by_email(db: Session, email: str) -> BusinessUser | None:
        return db.query(BusinessUser).filter(BusinessUser.email == email).first()
    
    @staticmethod
    def get_by_id(db: Session, user_id: str) -> BusinessUser | None:
        return db.query(BusinessUser).filter(BusinessUser.id == user_id).first()