from sqlalchemy.orm import Session
from app.models.business import Business
from app.schemas.business import BusinessCreate

class BusinessRepository:

    @staticmethod
    def create(db: Session, data: BusinessCreate) -> Business:
        business = Business(**data.model_dump())
        db.add(business)
        db.flush()
        return business

    @staticmethod
    def get_by_slug(db: Session, slug: str) -> Business | None:
        return db.query(Business).filter(Business.slug == slug).first()

    @staticmethod
    def get_by_id(db: Session, business_id):
        return db.query(Business).filter(Business.id == business_id).first()