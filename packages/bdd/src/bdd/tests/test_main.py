import unittest

# ENTITIES #
from bdd.models.file import File
from bdd.models.tag_file import TagFile
from bdd.models.extension import Extension
from bdd.models.software import Software
from bdd.models.extension_software import ExtensionSoftware
from bdd.models.task import Task
from bdd.models.substask import Subtask
from bdd.models.variant import Variant
from bdd.models.asset import Asset
from bdd.models.shot import Shot
from bdd.models.project import Project
from bdd.models.user import User
from bdd.repositories.task_repository import TaskRepository
# END ENTITIES #

from bdd.server.server import db
from bdd.tests.user import TestUser
from bdd.tests.shot import TestShot


class TestMain(unittest.TestCase):

    @staticmethod
    def generate_structure():
        db.generate_mapping(create_tables=True)

    def test_main(self):
        # init ddb
        TestMain.generate_structure()

        test_user = TestUser()
        test_user.test_create_user()

        test_shot = TestShot()
        test_shot.main()