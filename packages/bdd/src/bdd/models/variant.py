from bdd.server.server import db
from pony.orm import Required, Set, Optional
from bdd.models.task import Task
import datetime


class Variant(db.Entity):
    name = Required(str)
    data = datetime.datetime
    state = Optional(str)
    task = Required(Task)
