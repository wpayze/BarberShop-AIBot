from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.booking_repository import BookingRepository
from app.schemas.booking import BookingCreate


class BookingService:

    @staticmethod
    def create_booking(db: Session, data: BookingCreate):
        try:
            booking = BookingRepository.create(db, data)
            db.commit()
            db.refresh(booking)
            return booking
        except Exception as exc:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Could not create booking: {str(exc)}",
            )

    @staticmethod
    def get_by_id(db: Session, booking_id):
        return BookingRepository.get_by_id(db, booking_id)

    @staticmethod
    def list_by_business(db: Session, business_id):
        return BookingRepository.list_by_business(db, business_id)
