from bdd.server.server import db
from pony.orm import Required, Set, Optional
from bdd.models.project import Project
import datetime


class Shot(db.Entity):
    duration = Required(int)
    complexity = Optional(int)
    value = Optional(str)
    render = Optional(str)
    task = Set("Task")
    project = Required(Project)

    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")

    @staticmethod
    def CreateShot(_duration,_project, _complexity=0, _value='', _render='', _task=''):
        return Shot(duration=_duration, complexity=_complexity, value=_value, render=_render, task=_task, project=_project)

