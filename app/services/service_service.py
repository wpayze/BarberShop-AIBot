from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.service_repository import ServiceRepository
from app.schemas.service import ServiceCreate


class ServiceService:

    @staticmethod
    def create_service(db: Session, data: ServiceCreate):
        try:
            service = ServiceRepository.create(db, data)
            db.commit()
            db.refresh(service)
            return service
        except Exception as exc:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Could not create service: {str(exc)}",
            )

    @staticmethod
    def get_by_id(db: Session, service_id):
        return ServiceRepository.get_by_id(db, service_id)

    @staticmethod
    def list_by_business(db: Session, business_id):
        return ServiceRepository.list_by_business(db, business_id)
