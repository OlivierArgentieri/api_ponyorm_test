from db.server.server import db
from db.models.project import Project
from pony.orm import Required, Set, Optional
import datetime


class Shot(db.Entity):
    """Shot entity class."""

    duration = Required(int)
    complexity = Optional(int)
    value = Optional(str)
    render = Optional(str)
    task = Set("Task", cascade_delete=False)
    project = Required(Project)

    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")

    @staticmethod
    def create_shot(duration, project, complexity=0, value='', render='', task=''):
        """Register shot in db

        :param int duration: duration
        :param projectObject project: project
        :param int complexity: complexity (opt)
        :param str value: value (opt)
        :param str render: render (opt)
        :param taskObject task: task (opt)

        :return: shot object created
        """

        return Shot(duration=duration, complexity=complexity,
                    value=value, render=render, task=task,
                    project=project)

    @staticmethod
    def find_all_shots():
        """find all shot, without deleted entities

        :return: lists of shot
        """
        return Shot.select(lambda s: s.deletedAt is None)[:]

    @staticmethod
    def find_shot_by_id(shot_id):
        """find shot by id, without deleted entities

        :param int shot_id: shotId

        :return: (shot, string) shot object found and string for potential error
        """

        shot = Shot.get(lambda s: s.id == shot_id and s.deletedAt is None)
        if shot is None:
            return shot, "Shot Not Found !"

        return shot, ""

    @staticmethod
    def update_shot_by_id(shot_id, shot_updated):
        """Update shot by id

        :param int shot_id: id of shot target
        :param shotObject shot_updated: new value

        :return: (shot, string) shot object updated and string for potential error
        """

        # get shot
        target_shot = Shot.get(lambda s: s.id == shot_id and s.deletedAt is None)

        # shot exist?
        if target_shot is None:
            return target_shot, "Shot Not Found !"

        target_shot.duration = shot_updated.duration
        target_shot.complexity = shot_updated.complexity
        target_shot.value = shot_updated.value
        target_shot.render = shot_updated.render
        target_shot.task = shot_updated.task
        target_shot.project = shot_updated.project
        target_shot.updatedAt = datetime.datetime.utcnow()

        return target_shot, ""

    @staticmethod
    def remove_shot_by_id(shot_id):
        """Delete a shot

        :param int shot_id: id of shot

        :return: (id, string) id of shot deleted and string for potential error
        """

        # get shot
        target_shot = Shot.get(lambda s: s.id == shot_id and s.deletedAt is None)

        # shot exist?
        if target_shot is None:
            return 0, "Shot Not Found !"

        target_shot.deletedAt = datetime.datetime.utcnow()

        return target_shot.id, ""
