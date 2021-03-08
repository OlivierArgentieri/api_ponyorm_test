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
    def CreateShot(_duration, _project, _complexity=0, _value='', _render='', _task=''):
        """
        Register shot in bdd
        :param _duration:
        :param _project:
        :param _complexity:
        :param _value:
        :param _render:
        :param _task:
        :return: (shot, string) shot object created and string for potential error
        """

        return Shot(duration=_duration, complexity=_complexity, value=_value, render=_render, task=_task,
                    project=_project), ""

    @staticmethod
    def FindAllShot():
        """
        find all shot, without deleted entities
        :return: lists of shot
        """
        return Shot.select(lambda s: s.deletedAt is None)

    @staticmethod
    def FindShotByID(_shotId):
        """
        find shot by id, without deleted entities
        :return: (shot, string) shot object found and string for potential error
        """

        _shot = Shot.get(lambda s: s.id == _shotId and s.deletedAt is None)
        if _shot is None:
            return _shot, "Shot Not Found !"

        return _shot, ""


    @staticmethod
    def UpdateShotById(_shotId, _shotUpdated):
        """
        Update shot by id
        :param _shotId: id of shot target
        :param _shotUpdated: new value
        :return: (shot, string) shot object updated and string for potential error
        """

        # get shot
        _targetShot = Shot.get(lambda s: s.id == _shotId and s.deletedAt is None)

        # shot exist?
        if _targetShot is None:
            return _targetShot, "Shot Not Found !"

        _targetShot.duration = _shotUpdated.duration
        _targetShot.complexity = _shotUpdated.complexity
        _targetShot.value = _shotUpdated.value
        _targetShot.render = _shotUpdated.render
        _targetShot.task = _shotUpdated.task
        _targetShot.project = _shotUpdated.project
        _targetShot.updatedAt = datetime.datetime.utcnow()

        return _targetShot, ""


    @staticmethod
    def DeleteShotById(_shotId):
        """
        Delete a shot
        :param _shotId: id of shot
        :return: (id, string) id of shot deleted and string for potential error
        """
        # get shot
        _targetShot = Shot.get(lambda s: s.id == _shotId and s.deletedAt is None)

        # shot exist?
        if _targetShot is None:
            return 0, "Shot Not Found !"

        _targetShot.deletedAt = datetime.datetime.utcnow()

        return _targetShot.id, ""
