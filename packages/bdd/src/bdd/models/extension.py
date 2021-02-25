from bdd.server.server import db
from pony.orm import Required, Set, Optional
from bdd.models.software import Software
import datetime


class Extension(db.Entity):
    name = Required(str)
    description = Required(str)
    softwares = Set("ExtensionSoftware")


