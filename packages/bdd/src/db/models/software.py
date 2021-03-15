from db.server.server import db
from pony.orm import Required, Set, Optional
import datetime


class Software(db.Entity):
    """Software Entity class."""

    name = Required(str)
    extensions = Set("ExtensionSoftware", cascade_delete=False)

    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")

    @staticmethod
    def create_software(name):
        """Register software in db

        :param str name: name

        :return: software object created
        :rtype: softwareObject
        """

        return Software(name=name)

    @staticmethod
    def find_all_softwares():
        """find all software, without deleted entities

        :return: list of software
        :rtype: softwareObjects
        """
        return Software.select(lambda s: s.deletedAt is None)[:]

    @staticmethod
    def find_software_by_id(software_id):
        """find software by id, without deleted entities

        :param int software_id: software_id

        :return: software object found and string for potential error
        :rtype: (softwareObject, str)
        """

        software = Software.get(lambda s: s.id == software_id and s.deletedAt is None)
        if software is None:
            return software, "Software Not Found !"

        return software, ""

    @staticmethod
    def update_software_by_id(software_id, software_updated):
        """Update software by id

        :param int software_id: software_id
        :param softwareObject software_updated: new value

        :return: software object updated and string for potential error
        :rtype: (softwareObject, str)
        """

        # get software
        target_software = Software.get(lambda s: s.id == software_id and s.deletedAt is None)

        # Software exist?
        if target_software is None:
            return target_software, "Software Not Found !"

        target_software.name = software_updated.name

        return target_software, ""

    @staticmethod
    def remove_software_by_id(software_id):
        """Delete a software

        :param int software_id: software_id
        :return: id of software deleted and string for potential error
        :rtype: (int, str)
        """

        # get software
        target_software = Software.get(lambda s: s.id == software_id and s.deletedAt is None)

        # Software exist?
        if target_software is None:
            return 0, "Software Not Found !"

        target_software.deletedAt = datetime.datetime.utcnow()

        return target_software, ""
