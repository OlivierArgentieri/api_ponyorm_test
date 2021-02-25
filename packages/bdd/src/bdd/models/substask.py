from bdd.server.server import db
from pony.orm import Required, Set, Optional
from bdd.models.task import Task
import datetime


class Subtask(db.Entity):
    name = Required(str)
    file = Set("File")
    task = Required(Task)
    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")