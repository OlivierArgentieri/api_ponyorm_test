from bdd.server.server import db
from pony.orm import Required, Set, Optional
import datetime
from bdd.models.tag_file import TagFile


class File(db.Entity):
    name = Required(str)
    ext = Required(str)
    state = Optional(str)
    iteration = Required(int)
    tag = Required(TagFile)
    references = Set("File", reverse="references")
    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")

