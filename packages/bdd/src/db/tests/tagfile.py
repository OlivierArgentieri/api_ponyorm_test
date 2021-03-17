from pony import orm
from db.server.server import db
from db.models.tag_file import TagFile
import unittest


class TestTagFile(unittest.TestCase):
    """TestTagFile UnitTest class."""

    tag_file = None

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
        self.tag_file = TagFile.create_tag_file("tag_file_test", "tag_name_desc")

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
            temp_tag_file = TagFile[self.tag_file.id]

            # 2. assert on default value and getted value
            self.assert_value(temp_tag_file)

    def find_tag_file(self, dbo):
        """
        test find tag_file, CRUD method
        :param dbObject dbo: dbo
        :return:
        """
        self.reset(dbo)

        # 1. find tag_file from db
        with orm.db_session:
            temp_tag_file, _ = TagFile.find_tag_file_by_id(
                self.tag_file.id)

            # 2. test value
            self.assert_value(temp_tag_file)

            temp_tag_file, err = TagFile.find_tag_file_by_id(-1)

            # 3. assert on error
            self.assertEqual(err, "TagFile Not Found !")
            self.assertEqual(temp_tag_file, None)

            # 4. find_all tag_file from db
            temp_tag_files = TagFile.find_all_tag_files()

            # 5. test value
            self.assertEqual(len(temp_tag_files), 1)
            self.assert_value(temp_tag_files[0])

    def update_tag_file(self, dbo):
        """
        Test update_tag_file, CRUD method
        :param dbObject dbo: dbo
        :return:
        """
        self.reset(dbo)
        with orm.db_session:
            # 1. find update_tag_file from db
            temp_tag_file, _ = TagFile.find_tag_file_by_id(self.tag_file.id)

            temp_tag_file.name = "test_tag_file_updated"
            temp_tag_file.description = "tag_file_updated"

            temp_tag_file, _ = TagFile.update_tag_file_by_id(temp_tag_file.id, temp_tag_file)

            # 2. assert
            self.assertEqual("test_tag_file_updated", temp_tag_file.name)
            self.assertEqual("tag_file_updated", temp_tag_file.description)

    def remove_tag_file(self, dbo):
        """
        Test remove_tag_file, CRUD method
        :param dbObject dbo: dbo
        :return:
        """
        self.reset(dbo)
        with orm.db_session:
            # 1. find tag_file from db
            temp_tag_file, _ = TagFile.find_tag_file_by_id(self.tag_file.id)

            # 2. remove
            TagFile.remove_tag_file_by_id(temp_tag_file.id)

            # 3. re-get
            temp_tag_file, err = TagFile.find_tag_file_by_id(self.tag_file.id)

            # 4. assert
            self.assertEqual(temp_tag_file, None)
            self.assertEqual("TagFile Not Found !", err)

    def main(self):
        """
        Entry point
        :return:
        """
        self.create_tag_file(db)
        self.find_tag_file(db)
        self.update_tag_file(db)
        self.remove_tag_file(db)
