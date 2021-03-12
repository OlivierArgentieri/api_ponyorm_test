from db.server.server import db
from pony.orm import Required, Set, Optional
import datetime

from db.models.asset import Asset
from db.models.shot import Shot


class Task(db.Entity):
    name = Required(str)
    progress = Optional(str)
    need = Set("Task", reverse="need")
    subtask = Set("Subtask", cascade_delete=False)
    variant = Set("Variant", cascade_delete=False)
    asset = Optional(Asset)
    shot = Optional(Shot)

    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")
