from db.server.server import db
from db.models.tag_file import TagFile
from db.models.extension_software import ExtensionSoftware
from db.models.subtask import Subtask
from pony.orm import Required, Set, Optional
import datetime


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
        :param extensionSoftwareObject ext: file extension
        :param int iteration: iteration
        :param tagFileObject tag: tag
        :param subtaskObject subtask: subtask
        :param str state: state (opt)
        :param fileObject references: file references (opt)

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

        file = File.get(lambda s: s.id == file_id and s.deletedAt is None)
        if file is None:
            return file, "File Not Found !"

        return file, ""

    @staticmethod
    def update_file_by_id(file_id, file_updated):
        """Update file by id

        :param int file_id: file_id
        :param fileObject file_updated: new value

        :return: file object updated and string for potential error
        :rtype: (fileObject, str)
        """

        # get file
        target_file = File.get(lambda s: s.id == file_id and s.deletedAt is None)

        # file exist?
        if target_file is None:
            return target_file, "File Not Found !"

        target_file.name = file_updated.name
        target_file.ext = file_updated.ext
        target_file.state = file_updated.state
        target_file.iteration = file_updated.iteration
        target_file.tag = file_updated.tag
        target_file.subtask = file_updated.subtask
        target_file.references = file_updated.references
        target_file.updatedAt = datetime.datetime.utcnow()

        return target_file, ""

    @staticmethod
    def remove_file_by_id(file_id):
        """Delete a file

        :param int file_id: file_id
        :return: id of file deleted and string for potential error
        :rtype: (int, str)
        """

        # get file
        target_file = File.get(lambda s: s.id == file_id and s.deletedAt is None)

        # File exist?
        if target_file is None:
            return 0, "File Not Found !"

        target_file.deletedAt = datetime.datetime.utcnow()

        return target_file.id, ""
