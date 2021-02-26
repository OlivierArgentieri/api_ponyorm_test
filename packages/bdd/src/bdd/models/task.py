from bdd.server.server import db
from pony.orm import Required, Set, Optional
import datetime

from bdd.models.asset import Asset
from bdd.models.shot import Shot


class Task(db.Entity):
    name = Required(str)
    progress = Optional(str)
    tasks = Set("Task", reverse="tasks")
    subtask = Set("Subtask")
    variant = Set("Variant")
    asset = Optional(Asset)
    shot = Optional(Shot)

    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")

    def before_insert(self):
        #raise NameError("eeee")
        pass