from bdd.server.server import db
from pony.orm import Required, Set, Optional

import datetime


class Shot(db.Entity):
    duration = Required(int)
    complexity = Optional(int)
    value = Optional(str)
    render = Optional(str)
    task = Set("Task")

    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")

