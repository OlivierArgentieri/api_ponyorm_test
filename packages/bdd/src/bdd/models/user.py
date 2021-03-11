from bdd.server.server import db
from pony.orm import Required, Set, Optional
import datetime


class User(db.Entity):
    """User entity class."""

    name = Required(str)
    email = Required(str, unique=True)
    year_start = Required(int)
    year_end = Required(int)

    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")

    @staticmethod
    def create_user(_name, _email, _year_start, _year_end):
        """Register user in bdd

        :param str _name: name
        :param str _email: name
        :param int _year_start: year_start
        :param int _year_end: year_end

        :return: user object created
        :rtype: userObject
        """

        return User(name=_name, email=_email, year_start=_year_start, year_end=_year_end)

    @staticmethod
    def find_all_users():
        """find all user, without deleted entities

        :return: list of user
        :rtype: userObjects
        """
        return User.select(lambda s: s.deletedAt is None)[:]

    @staticmethod
    def find_user_by_id(_user_id):
        """find user by id, without deleted entities

        :param int _user_id: user_id

        :return: user object found and string for potential error
        :rtype: (userObject, str)
        """

        _user = User.get(lambda s: s.id == _user_id and s.deletedAt is None)
        if _user is None:
            return _user, "User Not Found !"

        return _user, ""

    @staticmethod
    def update_user_by_id(_user_id, _userUpdated):
        """Update user by id

        :param int _user_id: user_id
        :param userObject _userUpdated: new value

        :return: user object updated and string for potential error
        :rtype: (userObject, str)
        """

        # get user
        _targetUser = User.get(lambda s: s.id == _user_id and s.deletedAt is None)

        # user exist?
        if _targetUser is None:
            return _targetUser, "User Not Found !"

        _targetUser.name = _userUpdated.name
        _targetUser.email = _userUpdated.email
        _targetUser.year_start = _userUpdated.year_start
        _targetUser.year_end = _userUpdated.year_end
        _targetUser.updatedAt = datetime.datetime.utcnow()

        return _targetUser, ""

    @staticmethod
    def remove_user_by_id(_user_id):
        """Delete a user

        :param int _user_id: user_id
        :return: id of user deleted and string for potential error
        :rtype: (int, str)
        """

        # get user
        _targetUser = User.get(lambda s: s.id == _user_id and s.deletedAt is None)

        # user exist?
        if _targetUser is None:
            return 0, "User Not Found !"

        _targetUser.deletedAt = datetime.datetime.utcnow()

        return _targetUser.id, ""