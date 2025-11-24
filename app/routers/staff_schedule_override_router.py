from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.staff_schedule_override import (
    StaffScheduleOverrideCreate,
    StaffScheduleOverrideOut,
)
from app.services.staff_service import StaffService as StaffEntityService
from app.services.staff_schedule_override_service import StaffScheduleOverrideService
from app.utils.dependencies import get_current_user
from app.db.session import get_db

router = APIRouter(prefix="/staff-schedule-overrides", tags=["Staff Schedule Overrides"])


@router.post("/", response_model=StaffScheduleOverrideOut)
def create_override(
    data: StaffScheduleOverrideCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    staff = StaffEntityService.get_by_id(db, data.staffId)
    if not staff or staff.businessId != current_user.businessId:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff not found for this business.",
        )
    return StaffScheduleOverrideService.create_override(db, data)


@router.get("/staff/{staff_id}", response_model=list[StaffScheduleOverrideOut])
def list_overrides(
    staff_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    staff = StaffEntityService.get_by_id(db, staff_id)
    if not staff or staff.businessId != current_user.businessId:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff not found for this business.",
        )
    return StaffScheduleOverrideService.list_by_staff(db, staff_id)
