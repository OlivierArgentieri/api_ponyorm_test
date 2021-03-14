from db.server.server import db
from pony.orm import Required, Set, Optional, PrimaryKey
import datetime

from db.models.asset import Asset
from db.models.shot import Shot


class Task(db.Entity):
    """Task Entity"""

    name = Required(str)
    progress = Optional(float)
    need = Set("Task", reverse="need_by")
    need_by = Set("Task", reverse="need")  # property is used to break reverse : [1,2; 2,1]
    subtask = Set("Subtask", cascade_delete=False)
    variant = Set("Variant", cascade_delete=False)
    asset = Optional(Asset)
    shot = Optional(Shot)

    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")

    @staticmethod
    def create_task(_name, _progress=0, _asset=None, _shot=None, _need=None):
        """Register task in db

        :param str _name: name
        :param str _progress: progress
        :param int _asset: asset
        :param int _shot: shot
        :param taskObject _need: need

        :return: task  object created
        :rtype: taskObject
        """

        if _need:
            return Task(name=_name, progress=_progress, asset=_asset, shot=_shot, need=_need)
        return Task(name=_name, progress=_progress, asset=_asset, shot=_shot)

    @staticmethod
    def find_all_tasks():
        """find all task, without deleted entities

        :return: list of task
        :rtype: taskObjects
        """
        return Task.select(lambda s: s.deletedAt is None)[:]

    @staticmethod
    def find_task_by_id(_task_id):
        """find task by id, without deleted entities

        :param int _task_id: task_id

        :return: task object found and string for potential error
        :rtype: (taskObject, str)
        """

        _task = Task.get(lambda s: s.id == _task_id and s.deletedAt is None)
        if _task is None:
            return _task, "Task Not Found !"

        return _task, ""

    @staticmethod
    def update_task_by_id(_task_id, _task_updated):
        """Update task by id

        :param int _task_id: task_id
        :param taskObject _task_updated: new value

        :return: task object updated and string for potential error
        :rtype: (taskObject, str)
        """

        # get task
        _targetTask = Task.get(lambda s: s.id == _task_id and s.deletedAt is None)

        # task exist?
        if _targetTask is None:
            return _targetTask, "Task Not Found !"

        _targetTask.name = _task_updated.name
        _targetTask.progress = _task_updated.short_name
        _targetTask.shot = _task_updated.year_start
        _targetTask.asset = _task_updated.year_end
        _targetTask.need = _task_updated.need
        _targetTask.updatedAt = datetime.datetime.utcnow()

        return _targetTask, ""

    @staticmethod
    def remove_task_by_id(_task_id):
        """Delete a task

        :param int _task_id: task_id
        :return: id of task deleted and string for potential error
        :rtype: (int, str)
        """

        # get task
        _targetTask = Task.get(lambda s: s.id == _task_id and s.deletedAt is None)

        # Task exist?
        if _targetTask is None:
            return 0, "Task Not Found !"

        _targetTask.deletedAt = datetime.datetime.utcnow()

        return _targetTask.id, ""
