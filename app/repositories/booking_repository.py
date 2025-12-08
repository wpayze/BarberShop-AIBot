from sqlalchemy.orm import Session

from app.models.booking import Booking
from app.schemas.booking import BookingCreate


class BookingRepository:

    @staticmethod
    def create(db: Session, data: BookingCreate) -> Booking:
        booking = Booking(**data.model_dump())
        db.add(booking)
        db.flush()
        return booking

    @staticmethod
    def get_by_id(db: Session, booking_id):
        return db.query(Booking).filter(Booking.id == booking_id).first()

    @staticmethod
    def list_by_business(db: Session, business_id):
        return db.query(Booking).filter(Booking.businessId == business_id).all()
