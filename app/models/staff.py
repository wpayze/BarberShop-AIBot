import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Boolean, DateTime, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


def utc_now():
    return datetime.now(timezone.utc)


class Staff(Base):
    __tablename__ = "staff"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)

    businessId = Column(
        UUID(as_uuid=True),
        ForeignKey("businesses.id", ondelete="CASCADE"),
        nullable=False
    )

    displayName = Column(String(150), nullable=False)
    photoUrl = Column(String(255), nullable=True)
    bio = Column(String(500), nullable=True)
    isActive = Column(Boolean, default=True)
    sortOrder = Column(Integer, default=0)

    createdAt = Column(DateTime(timezone=True), nullable=False, default=utc_now)
    updatedAt = Column(DateTime(timezone=True), nullable=False, default=utc_now, onupdate=utc_now)
