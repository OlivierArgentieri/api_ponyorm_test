from db.server.server import db
from pony.orm import Required, Set, Optional
import datetime


class User(db.Entity):
    """User entity class."""

    name = Required(str)
    email = Required(str, unique=True)
    year_start = Required(int)
    year_end = Required(int)
    projects = Set("Project", cascade_delete=False)

    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")

    @staticmethod
    def create_user(name, email, year_start, year_end):
        """Register user in db

        :param str name: name
        :param str email: name
        :param int year_start: year_start
        :param int year_end: year_end

        :return: user object created
        :rtype: userObject
        """

        return User(name=name, email=email, year_start=year_start, year_end=year_end)

    @staticmethod
    def find_all_users():
        """find all user, without deleted entities

        :return: list of user
        :rtype: userObjects
        """
        return User.select(lambda s: s.deletedAt is None)[:]

    @staticmethod
    def find_user_by_id(user_id):
        """find user by id, without deleted entities

        :param int user_id: user_id

        :return: user object found and string for potential error
        :rtype: (userObject, str)
        """

        _user = User.get(lambda s: s.id == user_id and s.deletedAt is None)
        if _user is None:
            return _user, "User Not Found !"

        return _user, ""

    @staticmethod
    def update_user_by_id(user_id, userUpdated):
        """Update user by id

        :param int user_id: user_id
        :param userObject userUpdated: new value

        :return: user object updated and string for potential error
        :rtype: (userObject, str)
        """

        # get user
        target_user = User.get(lambda s: s.id == user_id and s.deletedAt is None)

        # user exist?
        if target_user is None:
            return target_user, "User Not Found !"

        target_user.name = userUpdated.name
        target_user.email = userUpdated.email
        target_user.year_start = userUpdated.year_start
        target_user.year_end = userUpdated.year_end
        target_user.updatedAt = datetime.datetime.utcnow()

        return target_user, ""

    @staticmethod
    def remove_user_by_id(user_id):
        """Delete a user

        :param int user_id: user_id
        :return: id of user deleted and string for potential error
        :rtype: (int, str)
        """

        # get user
        target_user = User.get(lambda s: s.id == user_id and s.deletedAt is None)

        # user exist?
        if target_user is None:
            return 0, "User Not Found !"

        target_user.deletedAt = datetime.datetime.utcnow()

        return target_user.id, ""
