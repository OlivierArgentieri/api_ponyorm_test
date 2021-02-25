from bdd.server.server import db
from pony.orm import Required, Set
import datetime
from bdd.models.tag_file import TagFile


class File(db.Entity):
    name = Required(str)
    ext = Required(str)
    createdAt = Required(datetime.datetime)
    state = Required(str)
    iteration = Required(int)
    tag = Required(TagFile)
    references = Set("File", reverse="references")


