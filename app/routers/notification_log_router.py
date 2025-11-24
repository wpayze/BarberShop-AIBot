from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.notification_log import NotificationLogCreate, NotificationLogOut
from app.services.notification_log_service import NotificationLogService
from app.utils.dependencies import get_current_user
from app.db.session import get_db

router = APIRouter(prefix="/notification-logs", tags=["Notification Logs"])


@router.post("/", response_model=NotificationLogOut)
def log_notification(
    data: NotificationLogCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if data.businessId != current_user.businessId:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot log notifications for another business.",
        )
    return NotificationLogService.log_notification(db, data)


@router.get("/business/{business_id}", response_model=list[NotificationLogOut])
def list_by_business(
    business_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if business_id != current_user.businessId:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied for this business.",
        )
    return NotificationLogService.list_by_business(db, business_id)


@router.get("/booking/{booking_id}", response_model=list[NotificationLogOut])
def list_by_booking(
    booking_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return NotificationLogService.list_by_booking_for_business(
        db, booking_id, current_user.businessId
    )
