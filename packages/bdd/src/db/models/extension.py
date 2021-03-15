from db.server.server import db
from pony.orm import Required, Set, Optional
from db.models.software import Software
import datetime


class Extension(db.Entity):
    """Extension Entity class."""

    name = Required(str)
    description = Required(str)
    softwares = Set("ExtensionSoftware", cascade_delete=True)

    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")
