from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.staff_service_repository import StaffServiceRepository
from app.schemas.staff_service import StaffServiceCreate


class StaffServiceLinkService:

    @staticmethod
    def link_staff_service(db: Session, data: StaffServiceCreate):
        existing = StaffServiceRepository.get_by_staff_and_service(
            db, data.staffId, data.serviceId
        )
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Staff is already assigned to this service.",
            )

        try:
            staff_service = StaffServiceRepository.create(db, data)
            db.commit()
            db.refresh(staff_service)
            return staff_service
        except Exception as exc:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Could not link staff to service: {str(exc)}",
            )

    @staticmethod
    def list_by_staff(db: Session, staff_id):
        return StaffServiceRepository.list_by_staff(db, staff_id)
