from pony import orm
from db.server.server import db
from db.models.variant import Variant
from db.models.tag_file import TagFile
import unittest


class TestTagFile(unittest.TestCase):
    """TestTagFile UnitTest class."""

    tagfile = None

    @staticmethod
    def clear_structure(dbo):
        """
        Drop each needed entities tables
        :param dbObject dbo: dbo
        :return:
        """

        dbo.drop_table("tagfile", if_exists=True, with_all_data=True)

    @staticmethod
    def generate_structure(dbo):
        """
        Create each needed entities tables
        :param dbObject dbo: dbo
        :return:
        """
        dbo.create_tables()

    @orm.db_session
    def fill_datas(self):
        """
        Fill tables with test data
        :param dbObject dbo: dbo
        :return:
        """
        self.tagfile = TagFile.create_tag_file("tag_file_test", "tag_name_desc")

    def reset(self, dbo):
        """
        Execute: clear, generate_structure and fill_data
        :param dbObject dbo: dbo
        :return:
        """
        TestTagFile.clear_structure(dbo)
        TestTagFile.generate_structure(dbo)
        self.fill_datas()

    def assert_value(self, tag_file_test):
        """
        Asserts with test value
        :param tagFileObject tag_file_test: task_test
        :return:
        """
        self.assertTrue(tag_file_test)

        self.assertEqual("tag_file_test", tag_file_test.name)
        self.assertEqual("tag_name_desc", tag_file_test.description)

        # Test CRUD
    def create_tag_file(self, dbo):
        """
        Test create_tag_file, CRUD method
        :param dbObject dbo: dbo
        :return:
        """
        self.reset(dbo)  # create default object in fill_datas function

        with orm.db_session:
            # 1. get object in db with ponyorm function (get will be tested lately)
            temp_tag_file = TagFile[self.tagfile.id]

            # 2. assert on default value and getted value
            self.assert_value(temp_tag_file)

    def main(self):
        """
        Entry point
        :return:
        """
        self.create_tag_file(db)
        # self.find_tag_file(db)
        # self.find_tag_file(db)
        # self.find_tag_file(db)
