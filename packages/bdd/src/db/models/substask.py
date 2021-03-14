from db.server.server import db
from pony.orm import Required, Set, Optional
from db.models.task import Task
import datetime


class Subtask(db.Entity):
    name = Required(str)
    file = Set("File")
    task = Required(Task)
    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")

    @staticmethod
    def create_subtask(_name, _task):
        """Register subtask in db

        :param str _name: name
        :param int _task: task

        :return: variant object created
        :rtype: variantObject
        """

        return Subtask(name=_name, task=_task)

    @staticmethod
    def find_all_subtasks():
        """find all subtask, without deleted entities

        :return: list of subtask
        :rtype: subtaskObjects
        """
        return Subtask.select(lambda s: s.deletedAt is None)[:]

    @staticmethod
    def find_subtask_by_id(_subtask_id):
        """find subtask by id, without deleted entities

        :param int _subtask_id: subtask_id

        :return: subtask object found and string for potential error
        :rtype: (subtaskObject, str)
        """

        _subtask = Subtask.get(lambda s: s.id == _subtask_id and s.deletedAt is None)
        if _subtask is None:
            return _subtask, "Subtask Not Found !"

        return _subtask, ""

    @staticmethod
    def update_subtask_by_id(_subtask_id, _subtask_updated):
        """Update subtask by id

        :param int _subtask_id: subtask_id
        :param subtaskObject _subtask_updated: new value

        :return: subtask object updated and string for potential error
        :rtype: (subtaskObject, str)
        """

        # get subtask
        _targetSubtask = Subtask.get(lambda s: s.id == _subtask_id and s.deletedAt is None)

        # subtask exist?
        if _targetSubtask is None:
            return _targetSubtask, "Subtask Not Found !"

        _targetSubtask.name = _subtask_updated.name
        _targetSubtask.file = _subtask_updated.file
        _targetSubtask.task = _subtask_updated.task
        _targetSubtask.updatedAt = datetime.datetime.utcnow()

        return _targetSubtask, ""

    @staticmethod
    def remove_subtask_by_id(_subtask_id):
        """Delete a subtask

        :param int _subtask_id: subtask_id
        :return: id of subtask deleted and string for potential error
        :rtype: (int, str)
        """

        # get variant
        _targetSubtask = Subtask.get(lambda s: s.id == _subtask_id and s.deletedAt is None)

        # Variant exist?
        if _targetSubtask is None:
            return 0, "Subtask Not Found !"

        _targetSubtask.deletedAt = datetime.datetime.utcnow()

        return _targetSubtask.id, ""
