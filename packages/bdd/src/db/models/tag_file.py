from db.server.server import db
from pony.orm import Required, Set, Optional
import datetime


class TagFile(db.Entity):
    """TagFile Entity class."""

    name = Required(str)
    description = Required(str)
    file = Set("File")

    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")

    @staticmethod
    def create_tag_file(name, description):
        """Register tagFile in db

        :param str name: name
        :param str description: description

        :return: tagFile object created
        :rtype: tagFileObject
        """

        return TagFile(name=name, description=description)

    @staticmethod
    def find_all_tag_files():
        """find all tagFile, without deleted entities

        :return: list of tagFile
        :rtype: tagFileObjects
        """
        return TagFile.select(lambda s: s.deletedAt is None)[:]

    @staticmethod
    def find_tag_file_by_id(tag_file_id):
        """find tagFile by id, without deleted entities

        :param int tag_file_id: tag_file_id

        :return: tagFile object found and string for potential error
        :rtype: (tagFileObject, str)
        """

        tag_file = TagFile.get(lambda s: s.id == tag_file_id and s.deletedAt is None)
        if tag_file is None:
            return tag_file, "TagFile Not Found !"

        return tag_file, ""

    @staticmethod
    def update_tag_file_by_id(tag_file_id, tag_file_updated):
        """Update tagFile by id

        :param int tag_file_id: tag_file_id
        :param tagFile tag_file_updated: new value

        :return: tagFile object updated and string for potential error
        :rtype: (tagFileObject, str)
        """

        # get targetTagFile
        target_tag_file = TagFile.get(lambda s: s.id == tag_file_id and s.deletedAt is None)

        # targetTagFile exist?
        if target_tag_file is None:
            return target_tag_file, "TagFile Not Found !"

        target_tag_file.name = tag_file_updated.name
        target_tag_file.description = tag_file_updated.description

        return target_tag_file, ""

    @staticmethod
    def remove_tag_file_by_id(tag_file_id):
        """Delete a tagFile

        :param int tag_file_id: tag_file_id
        :return: id of tagFile deleted and string for potential error
        :rtype: (int, str)
        """

        # get targetTagFile
        target_tag_file = TagFile.get(
            lambda s: s.id == tag_file_id and s.deletedAt is None)

        # targetTagFile exist?
        if target_tag_file is None:
            return 0, "TagFile Not Found !"

        target_tag_file.deletedAt = datetime.datetime.utcnow()

        return target_tag_file, ""
