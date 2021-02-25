from bdd.server.server import db
from pony.orm import Required, Set


class TagFile(db.Entity):
    name = Required(str)
    description = Required(str)
    file = Set("File")
