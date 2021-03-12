from db.server.server import db
from pony.orm import Required, Set, Optional
import datetime
from db.models.tag_file import TagFile
from db.models.extension_software import ExtensionSoftware
from db.models.substask import Subtask


class File(db.Entity):
    name = Required(str)
    ext = Required(ExtensionSoftware)
    state = Optional(str)
    iteration = Required(int)
    tag = Required(TagFile)
    subtask = Required(Subtask)
    references = Set("File", reverse="references", cascade_delete=False)
    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")

