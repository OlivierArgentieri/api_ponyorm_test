from pony import orm
from db.server.server import db
from db.models.project import Project
from db.models.shot import Shot
from db.models.asset_category import AssetCategory
from db.models.asset import Asset
from db.models.task import Task
from db.models.subtask import Subtask
from db.repositories.task_repository import TaskRepository
import unittest


class TestSubtask(unittest.TestCase):
    """TestSubTask unitTest class."""

    shot = None
    project = None
    asset_category = None
    asset = None
    variant = None
    task = None

    @staticmethod
    def clear_structure(dbo):
        """
        Drop each needed entities tables
        :param dbObject dbo: dbo
        :return:
        """
        dbo.drop_table("variant", if_exists=True, with_all_data=True)
        dbo.drop_table("asset", if_exists=True, with_all_data=True)
        dbo.drop_table("shot", if_exists=True, with_all_data=True)
        dbo.drop_table("task", if_exists=True, with_all_data=True)
        dbo.drop_table("project", if_exists=True, with_all_data=True)
        dbo.drop_table("subtask", if_exists=True, with_all_data=True)

    @staticmethod
    def generate_structure(dbo):
        """
        Create each needed entities tables
        :param dbObject dbo: dbo
        :return:
        """
        dbo.create_tables()

    @orm.db_session
    def fill_datas(self, dbo):
        """
        Fill tables with test data
        :param dbObject dbo: dbo
        :return:
        """
        self.project = Project(name="test_project", short_name="test", year_start=2020, year_end=2021)
        self.shot = Shot(duration=1, project=self.project)
        self.asset_category = AssetCategory(name="test_category")
        self.asset = Asset(name="test_asset", project=self.project, asset_category=self.asset_category, lod=10)
        self.task = Task.create_task("test_task", 10, self.asset)
        # xor on asset and shot
        TaskRepository.set_trigger_constraint_on_insert(dbo)

        self.subtask = Subtask.create_subtask("test_subtask", self.task)

    def reset(self, dbo):
        """
        Execute: clear, generate_structure and fill_data
        :param dbObject dbo: dbo
        :return:
        """
        TestSubtask.clear_structure(dbo)
        TestSubtask.generate_structure(dbo)
        self.fill_datas(dbo)

    def assert_value(self, subtask_test):
        """
        Asserts with test value
        :param subtaskObject subtask_test: subtask_test
        :return:
        """
        self.assertTrue(subtask_test)

        self.assertEqual("test_subtask", subtask_test.name)
        self.assertEqual("test_task", subtask_test.task.name)

    # Test CRUD
    def create_subtask(self, dbo):
        """
        Test create_subtask, CRUD method
        :param dbObject dbo: dbo
        :return:
        """
        self.reset(dbo)  # create default object in fill_datas function

        with orm.db_session:
            # 1. get object in db with ponyorm function (get will be tested lately)
            temp_subtask = Subtask[self.subtask.id]

            # 2. assert on default value and getted value
            self.assert_value(temp_subtask)

    def main(self):
        """
        Entry point
        :return:
        """
        self.create_subtask(db)
        # self.find_subtask(db)
        # self.update_subtask(db)
        # self.remove_subtask(db)
        # self.remove_subtask(db)
