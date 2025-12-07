from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.staff_repository import StaffRepository
from app.schemas.staff import StaffCreate, StaffUpdate


class StaffService:

    @staticmethod
    def create_staff(db: Session, data: StaffCreate):
        try:
            staff = StaffRepository.create(db, data)
            db.commit()
            db.refresh(staff)
            return staff
        except Exception as exc:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Could not create staff: {str(exc)}",
            )

    @staticmethod
    def get_by_id(db: Session, staff_id):
        return StaffRepository.get_by_id(db, staff_id)

    @staticmethod
    def list_by_business(db: Session, business_id):
        return StaffRepository.list_by_business(db, business_id)

    @staticmethod
    def update_staff(db: Session, staff_id, data: StaffUpdate):
        staff = StaffRepository.get_by_id(db, staff_id)
        if not staff:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Staff not found.",
            )

        try:
            staff = StaffRepository.update(db, staff, data)
            db.commit()
            db.refresh(staff)
            return staff
        except Exception as exc:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Could not update staff: {str(exc)}",
            )
