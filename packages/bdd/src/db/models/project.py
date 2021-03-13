from db.server.server import db
from pony.orm import Required, Set, Optional
from db.models.user import User
import datetime


class Project(db.Entity):
    name = Required(str)
    short_name = Required(str)
    year_start = Required(int)
    year_end = Required(int)
    assets = Set("Asset")
    shots = Set("Shot")
    users = Set(User)

    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")

    @staticmethod
    def create_project(_name, _short_name, _year_start, _year_end):
        """Register project in db

        :param str _name: name
        :param str _short_name: short_name
        :param int _year_start: year_start
        :param int _year_end: year_end

        :return: project object created
        :rtype: projectObject
        """

        return Project(name=_name, short_name=_short_name, year_start=_year_start, year_end=_year_end)

    @staticmethod
    def find_all_projects():
        """find all project, without deleted entities

        :return: list of project
        :rtype: projectObjects
        """
        return Project.select(lambda s: s.deletedAt is None)[:]

    @staticmethod
    def find_project_by_id(_project_id):
        """find project by id, without deleted entities

        :param int _project_id: project_id

        :return: project object found and string for potential error
        :rtype: (projectObject, str)
        """

        _project = Project.get(lambda s: s.id == _project_id and s.deletedAt is None)
        if _project is None:
            return _project, "Project Not Found !"

        return _project, ""

    @staticmethod
    def update_project_by_id(_project_id, _projectUpdated):
        """Update project by id

        :param int _project_id: project_id
        :param projectObject _projectUpdated: new value

        :return: project object updated and string for potential error
        :rtype: (projectObject, str)
        """

        # get project
        _targetProject = Project.get(lambda s: s.id == _project_id and s.deletedAt is None)

        # project exist?
        if _targetProject is None:
            return _targetProject, "Project Not Found !"

        _targetProject.name = _projectUpdated.name
        _targetProject.email = _projectUpdated.email
        _targetProject.year_start = _projectUpdated.year_start
        _targetProject.year_end = _projectUpdated.year_end
        _targetProject.updatedAt = datetime.datetime.utcnow()

        return _targetProject, ""

    @staticmethod
    def remove_project_by_id(_project_id):
        """Delete a project

        :param int _project_id: project_id
        :return: id of project deleted and string for potential error
        :rtype: (int, str)
        """

        # get project
        _targetProject = Project.get(lambda s: s.id == _project_id and s.deletedAt is None)

        # Project exist?
        if _targetProject is None:
            return 0, "Project Not Found !"

        _targetProject.deletedAt = datetime.datetime.utcnow()

        return _targetProject.id, ""
