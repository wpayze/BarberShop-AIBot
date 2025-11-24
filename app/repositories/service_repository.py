from sqlalchemy.orm import Session

from app.models.service import Service
from app.schemas.service import ServiceCreate


class ServiceRepository:

    @staticmethod
    def create(db: Session, data: ServiceCreate) -> Service:
        service = Service(**data.model_dump())
        db.add(service)
        db.flush()
        return service

    @staticmethod
    def get_by_id(db: Session, service_id):
        return db.query(Service).filter(Service.id == service_id).first()

    @staticmethod
    def list_by_business(db: Session, business_id):
        return db.query(Service).filter(Service.businessId == business_id).all()
