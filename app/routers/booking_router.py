from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.booking import BookingCreate, BookingOut
from app.services.booking_service import BookingService
from app.utils.dependencies import get_current_user
from app.db.session import get_db

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.post("/", response_model=BookingOut)
def create_booking(
    data: BookingCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if data.businessId != current_user.businessId:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot create booking for another business.",
        )
    return BookingService.create_booking(db, data)


@router.get("/business/{business_id}", response_model=list[BookingOut])
def list_bookings(
    business_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if business_id != current_user.businessId:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied for this business.",
        )
    return BookingService.list_by_business(db, business_id)


@router.get("/{booking_id}", response_model=BookingOut)
def get_booking(
    booking_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    booking = BookingService.get_by_id(db, booking_id)
    if not booking or booking.businessId != current_user.businessId:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found.",
        )
    return booking
