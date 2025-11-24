from uuid import UUID
from datetime import date, time
from pydantic import BaseModel


class StaffScheduleOverrideBase(BaseModel):
    staffId: UUID
    date: date
    isDayOff: bool = False
    startTime: time | None = None
    endTime: time | None = None


class StaffScheduleOverrideCreate(StaffScheduleOverrideBase):
    pass


class StaffScheduleOverrideOut(StaffScheduleOverrideBase):
    id: UUID

    class Config:
        from_attributes = True
