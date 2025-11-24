import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


def utc_now():
    return datetime.now(timezone.utc)


class NotificationLog(Base):
    __tablename__ = "notification_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)

    businessId = Column(
        UUID(as_uuid=True),
        ForeignKey("businesses.id", ondelete="CASCADE"),
        nullable=False
    )
    bookingId = Column(UUID(as_uuid=True), nullable=True)

    channel = Column(String(50), nullable=False)
    recipient = Column(String(150), nullable=False)
    templateKey = Column(String(100), nullable=False)
    payload = Column(JSON, nullable=True)
    status = Column(String(50), nullable=False)
    errorMessage = Column(String(500), nullable=True)

    createdAt = Column(DateTime(timezone=True), nullable=False, default=utc_now)
