from bdd.server.server import db
from pony.orm import Required, Set, Optional
import datetime


class User(db.Entity):
    name = Required(str)
    email = Required(str, unique=True)
    year_start = Required(int)
    year_end = Required(int)

    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")