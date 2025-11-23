from sqlalchemy.orm import Session

from app.models.business_opening_hours import BusinessOpeningHours
from app.schemas.business_opening_hours import BusinessOpeningHoursCreate


class BusinessOpeningHoursRepository:

    @staticmethod
    def create(db: Session, data: BusinessOpeningHoursCreate) -> BusinessOpeningHours:
        opening_hours = BusinessOpeningHours(**data.model_dump())
        db.add(opening_hours)
        db.flush()
        return opening_hours

    @staticmethod
    def list_by_business(db: Session, business_id):
        return (
            db.query(BusinessOpeningHours)
            .filter(BusinessOpeningHours.businessId == business_id)
            .order_by(BusinessOpeningHours.dayOfWeek)
            .all()
        )
