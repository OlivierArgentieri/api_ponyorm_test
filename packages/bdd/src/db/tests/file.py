from pony import orm

from db.repositories.task_repository import TaskRepository
from db.server.server import db
from db.models.project import Project
from db.models.shot import Shot
from db.models.asset_category import AssetCategory
from db.models.asset import Asset
from db.models.task import Task
from db.models.subtask import Subtask
from db.models.software import Software
from db.models.extension import Extension
from db.models.tag_file import TagFile
from db.models.file import File
from db.models.extension_software import ExtensionSoftware
import unittest


class TestFile(unittest.TestCase):
    """TestFile unitTest class."""

    project = None
    shot = None
    asset_category = None
    asset = None
    task = None
    subtask = None
    extension_software = None
    extension = None
    software = None
    tag_file = None
    file = None

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
        dbo.drop_table("subtask", if_exists=True, with_all_data=True)
        dbo.drop_table("file", if_exists=True, with_all_data=True)

    @staticmethod
    def generate_structure(dbo):
        """Create each needed entities tables

        :param dbObject dbo: dbo
        """
        dbo.create_tables()

    @orm.db_session
    def fill_datas(self, dbo):
        """fill tables with test datas

        :param dbObject dbo: dbo
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

        self.software = Software(name="test_software")
        self.extension = Extension(name="test_software", description="test_description")

        self.extension_software = ExtensionSoftware(extension=self.extension,
                                                    software=self.software)

        self.tag_file = TagFile(name="test_tag", description="test_tag_desc")

        self.file = File.create_file("test_file", self.extension_software,
                                     1, self.tag_file, self.subtask)

    def reset(self, dbo):
        """Execute: clear, generate_structure and fill_data

        :param dbObject dbo: dbo
        """
        TestFile.clear_structure(dbo)
        TestFile.generate_structure(dbo)
        self.fill_datas(dbo)

    def assert_value(self, file_test):
        """Asserts with test value

        :param fileObject file_test: file_test
        """
        self.assertTrue(file_test)

        self.assertEqual("test_file", file_test.name)
        self.assertEqual(1, file_test.iteration)
        self.assertEqual(self.tag_file.id, file_test.tag.id)
        self.assertEqual(self.subtask.id, file_test.subtask.id)

    # Test CRUD
    def create_file(self, dbo):
        """Test create_file, CRUD method

        :param dbObject dbo: dbo
        """
        self.reset(dbo)  # create default object in fill_datas function

        with orm.db_session:
            # 1. get object in db with ponyorm function (get will be tested lately)
            temp_file = File[self.file.id]

            # 2. assert on default value and getted value
            self.assert_value(temp_file)

    def find_file(self, dbo):
        """test find file, CRUD method

        :param dbObject dbo: dbo
        """
        self.reset(dbo)

        # 1. find tag_file from db
        with orm.db_session:
            temp_file, _ = File.find_file_by_id(
                self.file.id)

            # 2. test value
            self.assert_value(temp_file)

            temp_file, err = File.find_file_by_id(-1)

            # 3. assert on error
            self.assertEqual(err, "File Not Found !")
            self.assertEqual(temp_file, None)

            # 4. find_all temp_file from db
            temp_files = File.find_all_files()

            # 5. test value
            self.assertEqual(len(temp_files), 1)
            self.assert_value(temp_files[0])

    def update_file(self, dbo):
        """Test update_file, CRUD method

        :param dbObject dbo: dbo
        """
        self.reset(dbo)
        with orm.db_session:
            # 1. find update_file from db
            temp_file, _ = File.find_file_by_id(self.file.id)

            temp_file.name = "test_file_updated"
            temp_file.iteration = 2

            temp_file, _ = File.update_file_by_id(temp_file.id, temp_file)

            # 2. assert
            self.assertEqual("test_file_updated", temp_file.name)
            self.assertEqual(2, temp_file.iteration)

    def remove_file(self, dbo):
        """Test remove_file, CRUD method

        :param dbObject dbo: dbo
        """
        self.reset(dbo)
        with orm.db_session:
            # 1. find file from db
            temp_file, _ = File.find_file_by_id(self.file.id)

            # 2. remove
            File.remove_file_by_id(temp_file.id)

            # 3. re-get
            temp_file, err = File.find_file_by_id(self.file.id)

            # 4. assert
            self.assertEqual(temp_file, None)
            self.assertEqual("File Not Found !", err)

    def main(self):
        """Entry point"""

        self.create_file(db)
        self.find_file(db)
        self.update_file(db)
        self.remove_file(db)
