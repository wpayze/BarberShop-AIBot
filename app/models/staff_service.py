import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


def utc_now():
    return datetime.now(timezone.utc)


class StaffService(Base):
    __tablename__ = "staff_services"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)

    staffId = Column(
        UUID(as_uuid=True),
        ForeignKey("staff.id", ondelete="CASCADE"),
        nullable=False
    )
    serviceId = Column(
        UUID(as_uuid=True),
        ForeignKey("services.id", ondelete="CASCADE"),
        nullable=False
    )

    createdAt = Column(DateTime(timezone=True), nullable=False, default=utc_now)

    __table_args__ = (
        UniqueConstraint("staffId", "serviceId", name="uq_staff_service"),
    )
