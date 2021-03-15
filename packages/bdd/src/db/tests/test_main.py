import unittest

# ENTITIES #
from db.models.file import File
from db.models.tag_file import TagFile
from db.models.extension import Extension
from db.models.software import Software
from db.models.extension_software import ExtensionSoftware
from db.models.task import Task
from db.models.subtask import Subtask
from db.models.variant import Variant
from db.models.asset import Asset
from db.models.shot import Shot
from db.models.project import Project
from db.models.user import User
from db.repositories.task_repository import TaskRepository
# END ENTITIES #

from db.server.server import db
from db.tests.user import TestUser
from db.tests.shot import TestShot


class TestMain(unittest.TestCase):

    @staticmethod
    def generate_structure():
        db.generate_mapping(create_tables=True)

    @staticmethod
    def test_main():
        # init ddb
        TestMain.generate_structure()

        test_user = TestUser()
        test_user.main()

        test_shot = TestShot()
        test_shot.main()