from bdd.server.server import db
from pony.orm import Required, Set, Optional
from bdd.models.software import Software
import datetime


class Extension(db.Entity):
    name = Required(str)
    description = Required(str)
    file = Set("File")
    softwares = Set(Software)

    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")