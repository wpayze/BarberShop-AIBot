from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.staff import StaffCreate, StaffOut
from app.services.staff_service import StaffService
from app.utils.dependencies import get_current_user
from app.db.session import get_db

router = APIRouter(prefix="/staff", tags=["Staff"])


@router.post("/", response_model=StaffOut)
def create_staff(
    data: StaffCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if data.businessId != current_user.businessId:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot create staff for another business.",
        )
    return StaffService.create_staff(db, data)


@router.get("/business/{business_id}", response_model=list[StaffOut])
def list_staff(
    business_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if business_id != current_user.businessId:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied for this business.",
        )
    return StaffService.list_by_business(db, business_id)


@router.get("/{staff_id}", response_model=StaffOut)
def get_staff(
    staff_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    staff = StaffService.get_by_id(db, staff_id)
    if not staff or staff.businessId != current_user.businessId:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff not found.",
        )
    return staff
