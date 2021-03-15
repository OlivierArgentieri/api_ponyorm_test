from db.server.server import db
from pony.orm import Required, PrimaryKey, Set, Optional
from db.models.extension import Extension
from db.models.software import Software
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
        """Register extension_software in db

        :param str extension: extension
        :param int software: software

        :return: extensionSoftware object created
        :rtype: extensionSoftwareObject
        """

        return ExtensionSoftware(extension=extension, software=software)

    @staticmethod
    def find_all_extension_softwares():
        """find all extension_software, without deleted entities

        :return: list of extensionSoftware
        :rtype: extensionSoftwareObjects
        """
        return ExtensionSoftware.select(lambda s: s.deletedAt is None)[:]

    @staticmethod
    def find_extension_software_by_id(extension_software_id):
        """find extension_software by id, without deleted entities

        :param int extension_software_id: extension_software_id

        :return: extensionSoftware object found and string for potential error
        :rtype: (extensionSoftwareObject, str)
        """

        _extensionSoftware = ExtensionSoftware.get(lambda s: s.id == extension_software_id and s.deletedAt is None)
        if _extensionSoftware is None:
            return _extensionSoftware, "ExtensionSoftware Not Found !"

        return _extensionSoftware, ""

    @staticmethod
    def update_extension_software_by_id(extension_software_id, extension_software_updated):
        """Update extension_software by id

        :param int extension_software_id: extension_software_id
        :param extension_software_updated: new value

        :return: extensionSoftware object updated and string for potential error
        :rtype: (extensionSoftwareObject, str)
        """

        # get targetExtension
        _targetExtensionSoftware = ExtensionSoftware.get(lambda s: s.id == extension_software_id and s.deletedAt is None)

        # targetExtension exist?
        if _targetExtensionSoftware is None:
            return _targetExtensionSoftware, "ExtensionSoftware Not Found !"

        _targetExtensionSoftware.extension = extension_software_updated.extension
        _targetExtensionSoftware.software = extension_software_updated.software

        return _targetExtensionSoftware, ""

    @staticmethod
    def remove_extension_software_by_id(extension_software_id):
        """Delete a extension_software

        :param int extension_software_id: extension_software_id
        :return: id of extension_software deleted and string for potential error
        :rtype: (int, str)
        """

        # get targetExtension
        _targetExtensionSoftware = ExtensionSoftware.get(lambda s: s.id == extension_software_id and s.deletedAt is None)

        # targetExtension exist?
        if _targetExtensionSoftware is None:
            return 0, "ExtensionSoftware Not Found !"

        _targetExtensionSoftware.deletedAt = datetime.datetime.utcnow()

        return extension_software_id, ""