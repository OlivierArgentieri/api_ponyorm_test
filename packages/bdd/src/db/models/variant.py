from db.server.server import db
from pony.orm import Required, Set, Optional
from db.models.task import Task
import datetime


class Variant(db.Entity):
    name = Required(str)
    data = datetime.datetime
    state = Optional(str)
    task = Required(Task)
