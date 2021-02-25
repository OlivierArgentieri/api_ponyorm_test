from bdd.server.server import db
from pony.orm import Required, Set, Optional
import datetime

class Task(db.Entity):
    name = Required(str)
    progress = Optional(str)
    tasks = Set("Task", reverse="tasks")
    subtask = Set("Subtask")
    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")