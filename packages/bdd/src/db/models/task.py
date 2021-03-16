from db.server.server import db
from db.models.asset import Asset
from db.models.shot import Shot
from pony.orm import Required, Set, Optional
import datetime


class Task(db.Entity):
    """Task Entity class."""

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
    def create_task(name, progress=0, asset=None, shot=None, need=None):
        """Register task in db

        :param str name: name
        :param str progress: progress (opt)
        :param assetObject asset: asset (opt)
        :param shotObject shot: shot (opt)
        :param taskObject need: need (opt)

        :return: task  object created
        :rtype: taskObject
        """

        if need:
            return Task(name=name, progress=progress, asset=asset, shot=shot, need=need)
        return Task(name=name, progress=progress, asset=asset, shot=shot)

    @staticmethod
    def find_all_tasks():
        """find all task, without deleted entities

        :return: list of task
        :rtype: taskObjects
        """
        return Task.select(lambda s: s.deletedAt is None)[:]

    @staticmethod
    def find_task_by_id(task_id):
        """find task by id, without deleted entities

        :param int task_id: task_id

        :return: task object found and string for potential error
        :rtype: (taskObject, str)
        """

        task = Task.get(lambda s: s.id == task_id and s.deletedAt is None)
        if task is None:
            return task, "Task Not Found !"

        return task, ""

    @staticmethod
    def update_task_by_id(task_id, task_updated):
        """Update task by id

        :param int task_id: task_id
        :param taskObject task_updated: new value

        :return: task object updated and string for potential error
        :rtype: (taskObject, str)
        """

        # get task
        target_ask = Task.get(lambda s: s.id == task_id and s.deletedAt is None)

        # task exist?
        if target_ask is None:
            return target_ask, "Task Not Found !"

        target_ask.name = task_updated.name
        target_ask.progress = task_updated.progress
        target_ask.shot = task_updated.shot
        target_ask.asset = task_updated.asset
        target_ask.need = task_updated.need
        target_ask.updatedAt = datetime.datetime.utcnow()

        return target_ask, ""

    @staticmethod
    def remove_task_by_id(task_id):
        """Delete a task

        :param int task_id: task_id
        :return: id of task deleted and string for potential error
        :rtype: (int, str)
        """

        # get task
        target_ask = Task.get(lambda s: s.id == task_id and s.deletedAt is None)

        # Task exist?
        if target_ask is None:
            return 0, "Task Not Found !"

        target_ask.deletedAt = datetime.datetime.utcnow()

        return target_ask.id, ""
