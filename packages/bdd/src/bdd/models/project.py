from bdd.server.server import db
from pony.orm import Required, Set, Optional
import datetime


class Project(db.Entity):
    name = Required(str)
    short_name = Required(str)
    year_start = Required(int)
    year_end = Required(int)
    assets = Set("Asset")
    shots = Set("Shot")

    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")
