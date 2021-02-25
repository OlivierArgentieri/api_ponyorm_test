from bdd.server.server import db
from pony.orm import Required, PrimaryKey, Set
from bdd.models.extension import Extension
from bdd.models.software import Software


class ExtensionSoftware(db.Entity):
    _table_ = "extension_software"
    extension = Required(Extension)
    software = Required(Software)
    PrimaryKey(extension, software)
    file = Set("File")

