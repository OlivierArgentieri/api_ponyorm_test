from db.server.server import db
from pony.orm import Required, Set, Optional
import datetime


class Extension(db.Entity):
    """Extension Entity class."""

    name = Required(str)
    description = Required(str)
    softwares = Set("ExtensionSoftware", cascade_delete=False)

    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")

    @staticmethod
    def create_extension(name, description):
        """Register extension in db

        :param str name: name
        :param str description: description

        :return: extension object created
        :rtype: extensionObject
        """

        return Extension(name=name, description=description)

    @staticmethod
    def find_all_extensions():
        """find all extension, without deleted entities

        :return: list of extension
        :rtype: extensionObjects
        """
        return Extension.select(lambda s: s.deletedAt is None)[:]

    @staticmethod
    def find_extension_by_id(extension_id):
        """find extension by id, without deleted entities

        :param int extension_id: extension_id

        :return: extension object found and string for potential error
        :rtype: (extensionObject, str)
        """

        extension = Extension.get(
            lambda s: s.id == extension_id and s.deletedAt is None)
        if extension is None:
            return extension, "Extension Not Found !"

        return extension, ""

    @staticmethod
    def update_extension_by_id(extension_id, extension_updated):
        """Update extension by id

        :param int extension_id: extension_id
        :param extensionObject extension_updated: new value

        :return: extension object updated and string for potential error
        :rtype: (extensionObject, str)
        """

        # get targetExtension
        target_extension = Extension.get(
            lambda s: s.id == extension_id and s.deletedAt is None)

        # targetExtension exist?
        if target_extension is None:
            return target_extension, "Extension Not Found !"

        target_extension.name = extension_updated.name
        target_extension.description = extension_updated.description

        return target_extension, ""

    @staticmethod
    def remove_extension_by_id(extension_id):
        """Delete a extension

        :param int extension_id: extension_id
        :return: id of extension deleted and string for potential error
        :rtype: (int, str)
        """

        # get targetExtension
        target_extension = Extension.get(lambda s: s.id == extension_id and s.deletedAt is None)

        # targetExtension exist?
        if target_extension is None:
            return 0, "Extension Not Found !"

        target_extension.deletedAt = datetime.datetime.utcnow()

        return target_extension, ""
