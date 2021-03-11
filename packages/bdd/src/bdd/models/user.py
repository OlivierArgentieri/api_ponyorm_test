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

        :param _name: name
        :type _name: str

        :param _email: name
        :type _email: str

        :param _year_start: year_start
        :type _year_start: int

        :param _year_end: year_end
        :type _year_end: int

        :return: user user object created
        """

        return User(name=_name, email=_email, year_start=_year_start, year_end=_year_end)

    @staticmethod
    def find_all_users():
        """find all user, without deleted entities

        :return: lists of user
        """
        return User.select(lambda s: s.deletedAt is None)[:]

    @staticmethod
    def find_user_by_id(_user_id):
        """find user by id, without deleted entities

        :param _user_id: user_id
        :type _user_id: int

        :return: (user, string) user object found and string for potential error
        """

        _user = User.get(lambda s: s.id == _user_id and s.deletedAt is None)
        if _user is None:
            return _user, "User Not Found !"

        return _user, ""

    @staticmethod
    def update_user_by_id(_user_id, _userUpdated):
        """Update user by id

        :param _user_id: user_id
        :type _user_id: int

        :param _userUpdated: new value
        :type _userUpdated: userObject

        :return: (user, string) user object updated and string for potential error
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

        :param _user_id: user_id
        :type _user_id: int

        :return: (id, string) id of user deleted and string for potential error
        """

        # get user
        _targetUser = User.get(lambda s: s.id == _user_id and s.deletedAt is None)

        # user exist?
        if _targetUser is None:
            return 0, "User Not Found !"

        _targetUser.deletedAt = datetime.datetime.utcnow()

        return _targetUser.id, ""