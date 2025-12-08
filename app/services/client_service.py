from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.client_repository import ClientRepository
from app.schemas.client import ClientCreate


class ClientService:

    @staticmethod
    def create_client(db: Session, data: ClientCreate):
        try:
            client = ClientRepository.create(db, data)
            db.commit()
            db.refresh(client)
            return client
        except Exception as exc:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Could not create client: {str(exc)}",
            )

    @staticmethod
    def get_by_id(db: Session, client_id):
        return ClientRepository.get_by_id(db, client_id)

    @staticmethod
    def list_by_business(db: Session, business_id):
        return ClientRepository.list_by_business(db, business_id)
