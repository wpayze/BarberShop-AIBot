from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.business_opening_hours_repository import BusinessOpeningHoursRepository
from app.schemas.business_opening_hours import BusinessOpeningHoursCreate


class BusinessOpeningHoursService:

    @staticmethod
    def create_opening_hours(db: Session, data: BusinessOpeningHoursCreate):
        try:
            opening_hours = BusinessOpeningHoursRepository.create(db, data)
            db.commit()
            db.refresh(opening_hours)
            return opening_hours
        except Exception as exc:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Could not create opening hours: {str(exc)}",
            )

    @staticmethod
    def list_by_business(db: Session, business_id):
        return BusinessOpeningHoursRepository.list_by_business(db, business_id)
