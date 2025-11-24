from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.staff_service import StaffServiceCreate, StaffServiceOut
from app.services.staff_service import StaffService as StaffEntityService
from app.services.service_service import ServiceService
from app.services.staff_service_service import StaffServiceLinkService
from app.utils.dependencies import get_current_user
from app.db.session import get_db

router = APIRouter(prefix="/staff-services", tags=["Staff Services"])


@router.post("/", response_model=StaffServiceOut)
def link_staff_service(
    data: StaffServiceCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    staff = StaffEntityService.get_by_id(db, data.staffId)
    if not staff or staff.businessId != current_user.businessId:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff not found for this business.",
        )

    service = ServiceService.get_by_id(db, data.serviceId)
    if not service or service.businessId != current_user.businessId:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found for this business.",
        )

    return StaffServiceLinkService.link_staff_service(db, data)


@router.get("/staff/{staff_id}", response_model=list[StaffServiceOut])
def list_staff_services(
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

    return StaffServiceLinkService.list_by_staff(db, staff_id)
