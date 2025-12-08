from sqlalchemy.orm import Session

from app.models.client import Client
from app.schemas.client import ClientCreate


class ClientRepository:

    @staticmethod
    def create(db: Session, data: ClientCreate) -> Client:
        client = Client(**data.model_dump())
        db.add(client)
        db.flush()
        return client

    @staticmethod
    def get_by_id(db: Session, client_id):
        return db.query(Client).filter(Client.id == client_id).first()

    @staticmethod
    def list_by_business(db: Session, business_id):
        return db.query(Client).filter(Client.businessId == business_id).all()
