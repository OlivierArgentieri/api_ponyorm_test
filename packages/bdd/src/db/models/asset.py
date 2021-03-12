from db.server.server import db
from pony.orm import Required, Set, Optional
from db.models.project import Project
from db.models.asset_category import AssetCategory
import datetime


class Asset(db.Entity):
    name = Required(str)
    lod = Optional(int)
    Task = Set("Task", cascade_delete=False)
    project = Required(Project)
    asset_category = Required(AssetCategory)

    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")

