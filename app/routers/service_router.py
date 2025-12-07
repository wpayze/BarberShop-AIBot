from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.service import ServiceCreate, ServiceOut, ServiceUpdate
from app.services.service_service import ServiceService
from app.utils.dependencies import get_current_user
from app.db.session import get_db

router = APIRouter(prefix="/services", tags=["Services"])


@router.post("/", response_model=ServiceOut)
def create_service(
    data: ServiceCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if data.businessId != current_user.businessId:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot create services for another business.",
        )
    return ServiceService.create_service(db, data)


@router.get("/business/{business_id}", response_model=list[ServiceOut])
def list_services(
    business_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if business_id != current_user.businessId:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied for this business.",
        )
    return ServiceService.list_by_business(db, business_id)


@router.get("/{service_id}", response_model=ServiceOut)
def get_service(
    service_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    service = ServiceService.get_by_id(db, service_id)
    if not service or service.businessId != current_user.businessId:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found.",
        )
    return service


@router.patch("/{service_id}", response_model=ServiceOut)
def update_service(
    service_id: UUID,
    data: ServiceUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    service = ServiceService.get_by_id(db, service_id)
    if not service or service.businessId != current_user.businessId:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found.",
        )
    return ServiceService.update_service(db, service_id, data)
