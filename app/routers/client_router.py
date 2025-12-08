from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.client import ClientCreate, ClientOut
from app.services.client_service import ClientService
from app.utils.dependencies import get_current_user
from app.db.session import get_db

router = APIRouter(prefix="/clients", tags=["Clients"])


@router.post("/", response_model=ClientOut)
def create_client(
    data: ClientCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if data.businessId != current_user.businessId:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot create client for another business.",
        )
    return ClientService.create_client(db, data)


@router.get("/business/{business_id}", response_model=list[ClientOut])
def list_clients(
    business_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if business_id != current_user.businessId:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied for this business.",
        )
    return ClientService.list_by_business(db, business_id)


@router.get("/{client_id}", response_model=ClientOut)
def get_client(
    client_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    client = ClientService.get_by_id(db, client_id)
    if not client or client.businessId != current_user.businessId:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Client not found.",
        )
    return client
