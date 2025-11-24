from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.notification_log_repository import NotificationLogRepository
from app.schemas.notification_log import NotificationLogCreate


class NotificationLogService:

    @staticmethod
    def log_notification(db: Session, data: NotificationLogCreate):
        try:
            log = NotificationLogRepository.create(db, data)
            db.commit()
            db.refresh(log)
            return log
        except Exception as exc:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Could not log notification: {str(exc)}",
            )

    @staticmethod
    def list_by_business(db: Session, business_id):
        return NotificationLogRepository.list_by_business(db, business_id)

    @staticmethod
    def list_by_booking_for_business(db: Session, booking_id, business_id):
        return NotificationLogRepository.list_by_booking_for_business(db, booking_id, business_id)
