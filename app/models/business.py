import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base

def utc_now():
    return datetime.now(timezone.utc)

class Business(Base):
    __tablename__ = "businesses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)

    name = Column(String(150), nullable=False)
    slug = Column(String(150), unique=True, nullable=False)

    timezone = Column(String(50), nullable=False)

    contactEmail = Column(String(150), nullable=True)
    contactPhone = Column(String(50), nullable=True)

    addressLine1 = Column(String(150), nullable=True)
    addressLine2 = Column(String(150), nullable=True)
    city = Column(String(100), nullable=True)
    postalCode = Column(String(20), nullable=True)
    country = Column(String(100), nullable=True)

    planType = Column(String(50), nullable=False, default="free")

    isActive = Column(Boolean, default=True)

    createdAt = Column(DateTime(timezone=True), nullable=False, default=utc_now)
    updatedAt = Column(DateTime(timezone=True), nullable=False, default=utc_now, onupdate=utc_now)
