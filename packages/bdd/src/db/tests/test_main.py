import unittest

# ENTITIES #
from db.models.user import User
from db.models.project import Project
from db.models.asset import Asset
from db.models.shot import Shot
from db.models.task import Task
from db.models.variant import Variant
from db.models.subtask import Subtask
from db.models.file import File
from db.models.extension import Extension
from db.models.software import Software
from db.models.extension_software import ExtensionSoftware
from db.models.tag_file import TagFile
from db.repositories.task_repository import TaskRepository
# END ENTITIES #

from db.server.server import db
from db.tests.asset_category import TestAssetCategory
from db.tests.project import TestProject
from db.tests.user import TestUser
from db.tests.shot import TestShot
from db.tests.asset import TestAsset
from db.tests.task import TestTask
from db.tests.subtask import TestSubtask
from db.tests.variant import TestVariant
from db.tests.tagfile import TestTagFile


class TestMain(unittest.TestCase):

    @staticmethod
    def clear_structure():
        db.drop_table("tagfile", if_exists=True, with_all_data=True)
        db.drop_table("file_references", if_exists=True, with_all_data=True)
        db.drop_table("extension_software", if_exists=True, with_all_data=True)
        db.drop_table("extension", if_exists=True, with_all_data=True)
        db.drop_table("software", if_exists=True, with_all_data=True)
        db.drop_table("subtask", if_exists=True, with_all_data=True)
        db.drop_table("file", if_exists=True, with_all_data=True)

        db.drop_table("task_need", if_exists=True, with_all_data=True)
        db.drop_table("variant", if_exists=True, with_all_data=True)
        db.drop_table("project_user", if_exists=True, with_all_data=True)
        db.drop_table("user", if_exists=True, with_all_data=True)
        db.drop_table("project", if_exists=True, with_all_data=True)

        db.drop_table("assetcategory", if_exists=True, with_all_data=True)
        db.drop_table("asset", if_exists=True, with_all_data=True)
        db.drop_table("shot", if_exists=True, with_all_data=True)
        db.drop_table("task_task", if_exists=True, with_all_data=True)
        db.drop_table("task", if_exists=True, with_all_data=True)

    @staticmethod
    def generate_structure():
        db.generate_mapping(create_tables=True)

    @staticmethod
    def test_main():
        # init ddb
        TestMain.clear_structure()
        TestMain.generate_structure()

        TestUser().main()
        TestShot().main()
        TestProject().main()
        TestAssetCategory().main()
        TestAsset().main()
        TestTask().main()
        TestSubtask().main()
        TestVariant().main()
        TestTagFile().main()
