from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.staff_schedule_override_repository import StaffScheduleOverrideRepository
from app.schemas.staff_schedule_override import StaffScheduleOverrideCreate


class StaffScheduleOverrideService:

    @staticmethod
    def create_override(db: Session, data: StaffScheduleOverrideCreate):
        try:
            override = StaffScheduleOverrideRepository.create(db, data)
            db.commit()
            db.refresh(override)
            return override
        except Exception as exc:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Could not create schedule override: {str(exc)}",
            )

    @staticmethod
    def list_by_staff(db: Session, staff_id):
        return StaffScheduleOverrideRepository.list_by_staff(db, staff_id)
