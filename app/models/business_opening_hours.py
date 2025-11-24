import uuid
from sqlalchemy import Column, Integer, Boolean, Time, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class BusinessOpeningHours(Base):
    __tablename__ = "business_opening_hours"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)

    businessId = Column(
        UUID(as_uuid=True),
        ForeignKey("businesses.id", ondelete="CASCADE"),
        nullable=False
    )

    dayOfWeek = Column(Integer, nullable=False)
    openTime = Column(Time, nullable=True)
    closeTime = Column(Time, nullable=True)
    isClosed = Column(Boolean, default=False)
