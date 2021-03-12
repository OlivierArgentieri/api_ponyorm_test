from db.server.server import db
from pony.orm import Required, Set


class AssetCategory(db.Entity):
    name = Required(str)
    asset = Set("Asset", cascade_delete=False)
