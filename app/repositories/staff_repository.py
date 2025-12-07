from sqlalchemy.orm import Session

from app.models.staff import Staff
from app.schemas.staff import StaffCreate, StaffUpdate


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

    @staticmethod
    def update(db: Session, staff: Staff, data: StaffUpdate) -> Staff:
        updates = data.model_dump(exclude_unset=True)
        for key, value in updates.items():
            setattr(staff, key, value)
        db.flush()
        return staff
