from sqlalchemy.orm import Session

from app.models.staff_schedule_override import StaffScheduleOverride
from app.schemas.staff_schedule_override import StaffScheduleOverrideCreate


class StaffScheduleOverrideRepository:

    @staticmethod
    def create(db: Session, data: StaffScheduleOverrideCreate) -> StaffScheduleOverride:
        override = StaffScheduleOverride(**data.model_dump())
        db.add(override)
        db.flush()
        return override

    @staticmethod
    def list_by_staff(db: Session, staff_id):
        return (
            db.query(StaffScheduleOverride)
            .filter(StaffScheduleOverride.staffId == staff_id)
            .order_by(StaffScheduleOverride.date)
            .all()
        )
