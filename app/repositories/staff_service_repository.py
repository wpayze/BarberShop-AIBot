from sqlalchemy.orm import Session

from app.models.staff_service import StaffService
from app.schemas.staff_service import StaffServiceCreate


class StaffServiceRepository:

    @staticmethod
    def create(db: Session, data: StaffServiceCreate) -> StaffService:
        staff_service = StaffService(**data.model_dump())
        db.add(staff_service)
        db.flush()
        return staff_service

    @staticmethod
    def get_by_staff_and_service(db: Session, staff_id, service_id) -> StaffService | None:
        return (
            db.query(StaffService)
            .filter(StaffService.staffId == staff_id, StaffService.serviceId == service_id)
            .first()
        )

    @staticmethod
    def list_by_staff(db: Session, staff_id):
        return db.query(StaffService).filter(StaffService.staffId == staff_id).all()
