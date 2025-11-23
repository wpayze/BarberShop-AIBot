import uuid
from sqlalchemy import Column, Boolean, Date, Time, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class StaffScheduleOverride(Base):
    __tablename__ = "staff_schedule_overrides"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)

    staffId = Column(
        UUID(as_uuid=True),
        ForeignKey("staff.id", ondelete="CASCADE"),
        nullable=False
    )

    date = Column(Date, nullable=False)
    isDayOff = Column(Boolean, default=False)
    startTime = Column(Time, nullable=True)
    endTime = Column(Time, nullable=True)
