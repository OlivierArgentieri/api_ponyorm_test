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
        """Drop each needed entities tables

        :param dbObject dbo: dbo
        """
        dbo.drop_table("variant", if_exists=True, with_all_data=True)
        dbo.drop_table("asset", if_exists=True, with_all_data=True)
        dbo.drop_table("shot", if_exists=True, with_all_data=True)
        dbo.drop_table("task", if_exists=True, with_all_data=True)
        dbo.drop_table("project", if_exists=True, with_all_data=True)

    @staticmethod
    def generate_structure(dbo):
        """Create each needed entities tables

        :param dbObject dbo: dbo
        """
        dbo.create_tables()

    @orm.db_session
    def fill_datas(self, dbo):
        """Fill tables with test data

        :param dbObject dbo: dbo
        """
        self.project = Project(name="test_project", short_name="test",
                               year_start=2020, year_end=2021)

        self.shot = Shot(duration=1, project=self.project)
        self.asset_category = AssetCategory(name="test_category")

        self.asset = Asset(name="test_asset", project=self.project,
                           asset_category=self.asset_category, lod=10)

        # xor on asset and shot
        TaskRepository.set_trigger_constraint_on_insert(dbo)
        self.task = Task.create_task("test_task", 10, self.asset)

    def reset(self, dbo):
        """Execute: clear, generate_structure and fill_data

        :param dbObject dbo: dbo
        """
        TestTask.clear_structure(dbo)
        TestTask.generate_structure(dbo)
        self.fill_datas(dbo)

    def assert_value(self, task_test):
        """Asserts with test value
        :param taskObject task_test: task_test
        """
        self.assertTrue(task_test)

        self.assertEqual("test_task", task_test.name)
        self.assertEqual("test_asset", task_test.asset.name)
        self.assertEqual(10, task_test.progress)

    # Test CRUD
    def create_task(self, dbo):
        """Test create_task, CRUD method

        :param dbObject dbo: dbo
        """
        self.reset(dbo)  # create default object in fill_datas function

        with orm.db_session:
            # 1. get object in db with ponyorm function (get will be tested lately)
            temp_task = Task[self.task.id]

            # 2. assert on default value and getted value
            self.assert_value(temp_task)

            # try:
            #     # 3. test xor on asset/shot
            #     project = Project(name="test_project", short_name="test",
            #                       year_start=2020, year_end=2021)

            #     shot = Shot(duration=1, project=project)
            #     asset_category = AssetCategory(name="test_category")
            
            #     asset = Asset(name="test_asset", project=project,
            #                   asset_category=asset_category, lod=10)
            #
            #     test = Task.create_task("test_task", 10, asset, shot)
            #
            # except pony.orm.core.UnexpectedError as e:
            #     self.assertEqual("InternalError: Shot NOR Asset is REQUIRED", e)
            # todo see : https://github.com/ponyorm/pony/issues/592

    def find_task(self, dbo):
        """test find_task, CRUD method

        :param dbObject dbo: dbo
        """
        self.reset(dbo)

        # 1. find task from db
        with orm.db_session:
            temp_task, _ = Task.find_task_by_id(self.task.id)

            # 2. test value
            self.assert_value(temp_task)

            temp_task, err = Task.find_task_by_id(-1)

            # 3. assert on error
            self.assertEqual(err, "Task Not Found !")
            self.assertEqual(temp_task, None)

            # 4. find_all task from db
            temp_task = Task.find_all_tasks()

            # 5. test value
            self.assertEqual(len(temp_task), 1)
            self.assert_value(temp_task[0])

    def update_task(self, dbo):
        """Test update_task, CRUD method

        :param dbObject dbo: dbo
        """
        self.reset(dbo)
        with orm.db_session:
            # 1. find task from db
            temp_task, _ = Task.find_task_by_id(self.task.id)

            # auto update to but not updatedAt datetime in this way
            temp_task.name = "updated_test_task"
            temp_task.progress = 100
            temp_task, _ = Task.update_task_by_id(temp_task.id, temp_task)

            # 2. assert
            self.assertEqual("updated_test_task", temp_task.name)
            self.assertEqual(100, temp_task.progress)

    def remove_task(self, dbo):
        """Test remove_task, CRUD method

        :param dbObject dbo: dbo
        """
        self.reset(dbo)
        with orm.db_session:
            # 1. find task from db
            temp_task, _ = Task.find_task_by_id(self.task.id)

            # 2. remove
            Task.remove_task_by_id(temp_task.id)

            # 3. re-get
            temp_task, err = Task.find_task_by_id(self.task.id)

            # 4. assert
            self.assertEqual(temp_task, None)
            self.assertEqual("Task Not Found !", err)

    def main(self):
        """Entry point"""
        
        self.create_task(db)
        self.find_task(db)
        self.update_task(db)
        self.remove_task(db)
