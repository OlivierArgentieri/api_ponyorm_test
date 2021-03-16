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
        self.project = Project(name="test_project", short_name="test",
                               year_start=2020, year_end=2021)

        self.shot = Shot(duration=1, project=self.project)
        self.asset_category = AssetCategory(name="test_category")

        self.asset = Asset(name="test_asset", project=self.project,
                           asset_category=self.asset_category, lod=10)

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

    def find_subtask(self, dbo):
        """
        test find_subtask, CRUD method
        :param dbObject dbo: dbo
        :return:
        """
        self.reset(dbo)

        # 1. find subtask from db
        with orm.db_session:
            temp_subtask, _ = Subtask.find_subtask_by_id(self.subtask.id)

            # 2. test value
            self.assert_value(temp_subtask)

            temp_subtask, err = Subtask.find_subtask_by_id(-1)

            # 3. assert on error
            self.assertEqual(err, "Subtask Not Found !")
            self.assertEqual(temp_subtask, None)

            # 4. find_all subtask from db
            temp_subtasks = Subtask.find_all_subtasks()

            # 5. test value
            self.assertEqual(len(temp_subtasks), 1)
            self.assert_value(temp_subtasks[0])

    def update_subtask(self, dbo):
        """
        Test update_subtask, CRUD method
        :param dbObject dbo: dbo
        :return:
        """
        self.reset(dbo)
        with orm.db_session:
            # 1. find subtask from db
            temp_subtask, _ = Subtask.find_subtask_by_id(self.task.id)

            # auto update to but not updatedAt datetime in this way
            temp_subtask.name = "updated_test_subtask"
            temp_subtask.progress = 100
            temp_task, _ = Subtask.update_subtask_by_id(temp_subtask.id, temp_subtask)

            # 2. assert
            self.assertEqual("updated_test_subtask", temp_task.name)
            self.assertEqual(100, temp_task.progress)

    def remove_subtask(self, dbo):
        """
        Test remove_subtask, CRUD method
        :param dbObject dbo: dbo
        :return:
        """
        self.reset(dbo)
        with orm.db_session:
            # 1. find subtask from db
            temp_subtask, _ = Subtask.find_subtask_by_id(self.task.id)

            # 2. remove
            Subtask.remove_subtask_by_id(temp_subtask.id)

            # 3. re-get
            temp_subtask, err = Subtask.find_subtask_by_id(self.task.id)

            # 4. assert
            self.assertEqual(temp_subtask, None)
            self.assertEqual("Subtask Not Found !", err)

    def main(self):
        """
        Entry point
        :return:
        """
        self.create_subtask(db)
        self.find_subtask(db)
        self.update_subtask(db)
        self.remove_subtask(db)
