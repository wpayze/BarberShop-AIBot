from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.business_opening_hours import (
    BusinessOpeningHoursCreate,
    BusinessOpeningHoursOut,
)
from app.services.business_opening_hours_service import BusinessOpeningHoursService
from app.utils.dependencies import get_current_user
from app.db.session import get_db

router = APIRouter(prefix="/business-opening-hours", tags=["Business Opening Hours"])


@router.post("/", response_model=BusinessOpeningHoursOut)
def create_opening_hours(
    data: BusinessOpeningHoursCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if data.businessId != current_user.businessId:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot create opening hours for another business.",
        )
    return BusinessOpeningHoursService.create_opening_hours(db, data)


@router.get("/business/{business_id}", response_model=list[BusinessOpeningHoursOut])
def list_opening_hours(
    business_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if business_id != current_user.businessId:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied for this business.",
        )
    return BusinessOpeningHoursService.list_by_business(db, business_id)
