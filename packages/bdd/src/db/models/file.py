from db.server.server import db
from pony.orm import Required, Set, Optional
import datetime
from db.models.tag_file import TagFile
from db.models.extension_software import ExtensionSoftware
from db.models.substask import Subtask


class File(db.Entity):
    """File Entity class."""

    name = Required(str)
    ext = Required(ExtensionSoftware)
    state = Optional(str)
    iteration = Required(int)
    tag = Required(TagFile)
    subtask = Required(Subtask)
    references = Set("File", reverse="references_by", cascade_delete=False)
    # property references_by is used to break reverse : [1,2; 2,1]
    references_by = Set("File", reverse="references", cascade_delete=False)

    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")

    @staticmethod
    def create_file(name, ext, iteration, tag, subtask, state="", references=None):
        """Register file in db

        :param str name: name
        :param int ext: file extension
        :param int iteration: iteration
        :param int tag: tag
        :param int subtask: subtask
        :param int state: state
        :param int references: file references

        :return: file object created
        :rtype: fileObject
        """
        if references:
            return File(name=name, ext=ext, iteration=iteration, tag=tag, subtask=subtask, state=state, references=references)
        return File(name=name, ext=ext, iteration=iteration, tag=tag, subtask=subtask, state=state)

    @staticmethod
    def find_all_files():
        """find all file, without deleted entities

        :return: list of file
        :rtype: fileObjects
        """
        return File.select(lambda s: s.deletedAt is None)[:]

    @staticmethod
    def find_file_by_id(file_id):
        """find file by id, without deleted entities

        :param int file_id: file_id

        :return: file object found and string for potential error
        :rtype: (fileObject, str)
        """

        _file = File.get(lambda s: s.id == file_id and s.deletedAt is None)
        if _file is None:
            return _file, "File Not Found !"

        return _file, ""

    @staticmethod
    def update_file_by_id(file_id, file_updated):
        """Update file by id

        :param int file_id: file_id
        :param fileObject file_updated: new value

        :return: file object updated and string for potential error
        :rtype: (fileObject, str)
        """

        # get file
        _targetFile = File.get(lambda s: s.id == file_id and s.deletedAt is None)

        # file exist?
        if _targetFile is None:
            return _targetFile, "File Not Found !"

        _targetFile.name = file_updated.name
        _targetFile.ext = file_updated.ext
        _targetFile.state = file_updated.state
        _targetFile.iteration = file_updated.iteration
        _targetFile.tag = file_updated.tag
        _targetFile.subtask = file_updated.subtask
        _targetFile.references = file_updated.references
        _targetFile.updatedAt = datetime.datetime.utcnow()

        return _targetFile, ""

    @staticmethod
    def remove_file_by_id(file_id):
        """Delete a file

        :param int file_id: file_id
        :return: id of file deleted and string for potential error
        :rtype: (int, str)
        """

        # get file
        _targetFile = File.get(lambda s: s.id == file_id and s.deletedAt is None)

        # File exist?
        if _targetFile is None:
            return 0, "File Not Found !"

        _targetFile.deletedAt = datetime.datetime.utcnow()

        return _targetFile.id, ""