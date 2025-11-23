import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base
from app.models.enums import UserRole

def utc_now():
    return datetime.now(timezone.utc)

class BusinessUser(Base):
    __tablename__ = "business_users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)

    businessId = Column(
        UUID(as_uuid=True),
        ForeignKey("businesses.id", ondelete="CASCADE"),
        nullable=False
    )

    email = Column(String(150), nullable=False, unique=True)
    passwordHash = Column(String(255), nullable=False)

    role = Column(String(50), nullable=False, default=UserRole.STAFF.value)

    isActive = Column(Boolean, default=True)

    createdAt = Column(DateTime(timezone=True), nullable=False, default=utc_now)
    updatedAt = Column(DateTime(timezone=True), nullable=False, default=utc_now, onupdate=utc_now)
