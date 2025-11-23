from sqlalchemy.orm import Session

from app.models.staff import Staff
from app.schemas.staff import StaffCreate


class StaffRepository:

    @staticmethod
    def create(db: Session, data: StaffCreate) -> Staff:
        staff = Staff(**data.model_dump())
        db.add(staff)
        db.flush()
        return staff

    @staticmethod
    def get_by_id(db: Session, staff_id):
        return db.query(Staff).filter(Staff.id == staff_id).first()

    @staticmethod
    def list_by_business(db: Session, business_id):
        return db.query(Staff).filter(Staff.businessId == business_id).all()
