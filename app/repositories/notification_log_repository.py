from sqlalchemy.orm import Session

from app.models.notification_log import NotificationLog
from app.schemas.notification_log import NotificationLogCreate


class NotificationLogRepository:

    @staticmethod
    def create(db: Session, data: NotificationLogCreate) -> NotificationLog:
        log = NotificationLog(**data.model_dump())
        db.add(log)
        db.flush()
        return log

    @staticmethod
    def list_by_business(db: Session, business_id):
        return db.query(NotificationLog).filter(NotificationLog.businessId == business_id).all()

    @staticmethod
    def list_by_booking_for_business(db: Session, booking_id, business_id):
        return (
            db.query(NotificationLog)
            .filter(
                NotificationLog.bookingId == booking_id,
                NotificationLog.businessId == business_id,
            )
            .all()
        )
