import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, Date, Time, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base
from app.models.enums import BookingStatus, BookingSource


def utc_now():
    return datetime.now(timezone.utc)


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)

    businessId = Column(
        UUID(as_uuid=True),
        ForeignKey("businesses.id", ondelete="CASCADE"),
        nullable=False
    )

    staffId = Column(
        UUID(as_uuid=True),
        ForeignKey("staff.id", ondelete="SET NULL"),
        nullable=True,
    )

    serviceId = Column(
        UUID(as_uuid=True),
        ForeignKey("services.id", ondelete="SET NULL"),
        nullable=True,
    )

    clientId = Column(
        UUID(as_uuid=True),
        ForeignKey("clients.id", ondelete="SET NULL"),
        nullable=True,
    )

    clientName = Column(String(150), nullable=False)
    clientPhone = Column(String(50), nullable=False)
    clientEmail = Column(String(150), nullable=False)

    date = Column(Date, nullable=False)
    startTime = Column(Time, nullable=False)
    endTime = Column(Time, nullable=False)

    status = Column(String(50), nullable=False, default=BookingStatus.PENDING.value)
    source = Column(String(50), nullable=False, default=BookingSource.ONLINE.value)
    notes = Column(String(1000), nullable=True)

    createdAt = Column(DateTime(timezone=True), nullable=False, default=utc_now)
    updatedAt = Column(DateTime(timezone=True), nullable=False, default=utc_now, onupdate=utc_now)
