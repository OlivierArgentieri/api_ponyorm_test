from db.server.server import db
from db.models.task import Task
from pony.orm import Required, Set, Optional
import datetime


class Subtask(db.Entity):
    """Entity Subtask class."""

    name = Required(str)
    file = Set("File")
    task = Required(Task)
    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")

    @staticmethod
    def create_subtask(name, task):
        """Register subtask in db

        :param str name: name
        :param taskObject task: task

        :return: variant object created
        :rtype: variantObject
        """

        return Subtask(name=name, task=task)

    @staticmethod
    def find_all_subtasks():
        """find all subtask, without deleted entities

        :return: list of subtask
        :rtype: subtaskObjects
        """
        return Subtask.select(lambda s: s.deletedAt is None)[:]

    @staticmethod
    def find_subtask_by_id(subtask_id):
        """find subtask by id, without deleted entities

        :param int subtask_id: subtask_id

        :return: subtask object found and string for potential error
        :rtype: (subtaskObject, str)
        """

        subtask = Subtask.get(lambda s: s.id == subtask_id and s.deletedAt is None)
        if subtask is None:
            return subtask, "Subtask Not Found !"

        return subtask, ""

    @staticmethod
    def update_subtask_by_id(subtask_id, subtask_updated):
        """Update subtask by id

        :param int subtask_id: subtask_id
        :param subtaskObject subtask_updated: new value

        :return: subtask object updated and string for potential error
        :rtype: (subtaskObject, str)
        """

        # get subtask
        target_subtask = Subtask.get(lambda s: s.id == subtask_id and s.deletedAt is None)

        # subtask exist?
        if target_subtask is None:
            return target_subtask, "Subtask Not Found !"

        target_subtask.name = subtask_updated.name
        target_subtask.file = subtask_updated.file
        target_subtask.task = subtask_updated.task
        target_subtask.updatedAt = datetime.datetime.utcnow()

        return target_subtask, ""

    @staticmethod
    def remove_subtask_by_id(subtask_id):
        """Delete a subtask

        :param int subtask_id: subtask_id
        :return: id of subtask deleted and string for potential error
        :rtype: (int, str)
        """

        # get variant
        target_subtask = Subtask.get(lambda s: s.id == subtask_id and s.deletedAt is None)

        # Variant exist?
        if target_subtask is None:
            return 0, "Subtask Not Found !"

        target_subtask.deletedAt = datetime.datetime.utcnow()

        return target_subtask.id, ""
