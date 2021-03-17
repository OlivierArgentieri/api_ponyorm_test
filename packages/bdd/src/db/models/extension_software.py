from db.server.server import db
from db.models.extension import Extension
from db.models.software import Software
from pony.orm import Required, PrimaryKey, Set, Optional
import datetime


class ExtensionSoftware(db.Entity):
    """ExtensionSoftware Entity class."""

    _table_ = "extension_software"  # name of table

    extension = Required(Extension)
    software = Required(Software)

    PrimaryKey(extension, software)

    file = Set("File", cascade_delete=False)
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")

    @staticmethod
    def create_extension_software(extension, software):
        """Register extensionSoftware in db

        :param str extension: extension
        :param softwareObject software: software

        :return: extensionSoftware object created
        :rtype: extensionSoftwareObject
        """

        return ExtensionSoftware(extension=extension, software=software)

    @staticmethod
    def find_all_extension_softwares():
        """find all extensionSoftware, without deleted entities

        :return: list of extensionSoftware
        :rtype: extensionSoftwareObjects
        """
        return ExtensionSoftware.select(lambda s: s.deletedAt is None)[:]

    @staticmethod
    def find_extension_software_by_id(extension_software_id):
        """find extensionSoftware by id, without deleted entities

        :param int extension_software_id: extension_software_id

        :return: extensionSoftware object found and string for potential error
        :rtype: (extensionSoftwareObject, str)
        """

        extension_software = ExtensionSoftware.get(
            lambda s: s.id == extension_software_id and s.deletedAt is None)

        if extension_software is None:
            return extension_software, "ExtensionSoftware Not Found !"

        return extension_software, ""

    @staticmethod
    def update_extension_software_by_id(extension_software_id, extension_software_updated):
        """Update extensionSoftware by id

        :param int extension_software_id: extension_software_id
        :param extensionSoftwareObject extension_software_updated: new value

        :return: extensionSoftware object updated and string for potential error
        :rtype: (extensionSoftwareObject, str)
        """

        # get targetExtension
        target_extension_software = ExtensionSoftware.get(
            lambda s: s.id == extension_software_id and s.deletedAt is None)

        # targetExtension exist?
        if target_extension_software is None:
            return target_extension_software, "ExtensionSoftware Not Found !"

        target_extension_software.extension = extension_software_updated.extension
        target_extension_software.software = extension_software_updated.software

        return target_extension_software, ""

    @staticmethod
    def remove_extension_software_by_id(extension_software_id):
        """Delete a extensionSoftware

        :param int extension_software_id: extension_software_id
        :return: id of extension_software deleted and string for potential error
        :rtype: (int, str)
        """

        # get targetExtension
        target_extension_software = ExtensionSoftware.get(
            lambda s: s.id == extension_software_id and s.deletedAt is None)

        # targetExtension exist?
        if target_extension_software is None:
            return 0, "ExtensionSoftware Not Found !"

        target_extension_software.deletedAt = datetime.datetime.utcnow()

        return extension_software_id, ""
