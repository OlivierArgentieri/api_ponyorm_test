from pony import orm
from db.server.server import db
from db.models.project import Project
from db.models.shot import Shot
from db.models.asset_category import AssetCategory
from db.models.asset import Asset
from db.models.task import Task
from db.repositories.task_repository import TaskRepository
import unittest


class TestTask(unittest.TestCase):
    """TestTask UnitTest class."""

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

        # xor on asset and shot
        TaskRepository.set_trigger_constraint_on_insert(dbo)
        self.task = Task.create_task("test_task", 10, self.asset)

    def reset(self, dbo):
        """
        Execute: clear, generate_structure and fill_data
        :param dbObject dbo: dbo
        :return:
        """
        TestTask.clear_structure(dbo)
        TestTask.generate_structure(dbo)
        self.fill_datas(dbo)

    def assert_value(self, task_test):
        """
        Asserts with test value
        :param taskObject task_test: task_test
        :return:
        """
        self.assertTrue(task_test)

        self.assertEqual("test_task", task_test.name)
        self.assertEqual("test_asset", task_test.asset.name)
        self.assertEqual(10, task_test.progress)

    # Test CRUD
    def create_task(self, dbo):
        """
        Test create_task, CRUD method
        :param dbObject dbo: dbo
        :return:
        """
        self.reset(dbo)  # create default object in fill_datas function

        with orm.db_session:
            # 1. get object in db with ponyorm function (get will be tested lately)
            temp_task = Task[self.task.id]

            # 2. assert on default value and getted value
            self.assert_value(temp_task)
            
            # try:
            #     # 3. test xor on asset/shot
            #     project = Project(name="test_project", short_name="test", year_start=2020, year_end=2021)
            #     shot = Shot(duration=1, project=project)
            #     asset_category = AssetCategory(name="test_category")
            #     asset = Asset(name="test_asset", project=project, asset_category=asset_category, lod=10)
            #
            #     test = Task.create_task("test_task", 10, asset, shot)
            #
            # except pony.orm.core.UnexpectedError as e:
            #     self.assertEqual("InternalError: Shot NOR Asset is REQUIRED", e)
            # todo see : https://github.com/ponyorm/pony/issues/592

    def main(self):
        """
        Entry point
        :return:
        """
        self.create_task(db)
        # self.find_asset(db)
        # self.update_asset(db)
        # self.remove_asset(db)
