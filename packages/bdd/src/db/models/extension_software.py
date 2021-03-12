from db.server.server import db
from pony.orm import Required, PrimaryKey, Set
from db.models.extension import Extension
from db.models.software import Software


class ExtensionSoftware(db.Entity):
    _table_ = "extension_software"
    extension = Required(Extension)
    software = Required(Software)
    PrimaryKey(extension, software)
    file = Set("File", cascade_delete=True)

