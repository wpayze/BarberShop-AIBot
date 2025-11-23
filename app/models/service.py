import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Boolean, DateTime, Integer, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


def utc_now():
    return datetime.now(timezone.utc)


class Service(Base):
    __tablename__ = "services"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)

    businessId = Column(
        UUID(as_uuid=True),
        ForeignKey("businesses.id", ondelete="CASCADE"),
        nullable=False
    )

    name = Column(String(150), nullable=False)
    description = Column(String(1000), nullable=True)
    durationMinutes = Column(Integer, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    category = Column(String(150), nullable=True)
    isActive = Column(Boolean, default=True)

    createdAt = Column(DateTime(timezone=True), nullable=False, default=utc_now)
    updatedAt = Column(DateTime(timezone=True), nullable=False, default=utc_now, onupdate=utc_now)
