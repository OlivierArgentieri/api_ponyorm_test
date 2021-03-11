from bdd.server.server import db
from pony.orm import Required, Set, Optional
from bdd.models.project import Project
import datetime

"""
.. module:: useful_1
   :platform: Unix, Windows
   :synopsis: A useful module indeed.

.. moduleauthor:: Andrew Carter <andrew@invalid.com>


"""


class Shot(db.Entity):
    """Shot entity class."""

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
    def create_shot(_duration, _project, _complexity=0, _value='', _render='', _task=''):
        """Register shot in bdd

        :param _duration: duration
        :type _duration: int

        :param _project: project
        :type _project: projectObject

        :param _complexity: complexity
        :type _complexity: int, (opt)

        :param _value: value
        :type _value: str, (opt)

        :param _render: render
        :type _render: str, (opt)

        :param _task: task
        :type _task: taskObject, (opt)

        :return: shot object created
        """

        return Shot(duration=_duration, complexity=_complexity, value=_value, render=_render, task=_task,
                    project=_project)

    @staticmethod
    def find_all_shots():
        """find all shot, without deleted entities

        :return: lists of shot
        """
        return Shot.select(lambda s: s.deletedAt is None)[:]

    @staticmethod
    def find_shot_by_id(_shot_id):
        """find shot by id, without deleted entities

        :param _shot_id: shotId
        :type _shot_id: int

        :return: (shot, string) shot object found and string for potential error
        """

        _shot = Shot.get(lambda s: s.id == _shot_id and s.deletedAt is None)
        if _shot is None:
            return _shot, "Shot Not Found !"

        return _shot, ""

    @staticmethod
    def update_shot_by_id(_shot_id, _shot_updated):
        """Update shot by id

        :param _shot_id: id of shot target
        :type _shot_id: int

        :param _shot_updated: new value
        :type _shot_updated: shotObject

        :return: (shot, string) shot object updated and string for potential error
        """

        # get shot
        _targetShot = Shot.get(lambda s: s.id == _shot_id and s.deletedAt is None)

        # shot exist?
        if _targetShot is None:
            return _targetShot, "Shot Not Found !"

        _targetShot.duration = _shot_updated.duration
        _targetShot.complexity = _shot_updated.complexity
        _targetShot.value = _shot_updated.value
        _targetShot.render = _shot_updated.render
        _targetShot.task = _shot_updated.task
        _targetShot.project = _shot_updated.project
        _targetShot.updatedAt = datetime.datetime.utcnow()

        return _targetShot, ""

    @staticmethod
    def remove_shot_by_id(_shot_id):
        """Delete a shot

        :param _shot_id: id of shot
        :type _shot_id: int

        :return: (id, string) id of shot deleted and string for potential error
        """

        # get shot
        _targetShot = Shot.get(lambda s: s.id == _shot_id and s.deletedAt is None)

        # shot exist?
        if _targetShot is None:
            return 0, "Shot Not Found !"

        _targetShot.deletedAt = datetime.datetime.utcnow()

        return _targetShot.id, ""
