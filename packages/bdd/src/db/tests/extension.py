from pony import orm
from db.server.server import db
from db.models.extension import Extension
import unittest


class TestExtension(unittest.TestCase):
    """TestExtension unitTest class."""

    extension = None

    @staticmethod
    def clear_structure(dbo):
        """Drop each needed entities tables

        :param dbObject dbo: dbo
        """

        db.drop_table("file", if_exists=True, with_all_data=True)
        dbo.drop_table("extension_software", if_exists=True, with_all_data=True)
        dbo.drop_table("extension", if_exists=True, with_all_data=True)
        dbo.drop_table("software", if_exists=True, with_all_data=True)

    @staticmethod
    def generate_structure(dbo):
        """Create each needed entities tables

        :param dbObject dbo: dbo
        """
        dbo.create_tables()

    @orm.db_session
    def fill_datas(self):
        """fill tables with test datas"""

        # xor on asset and shot
        self.extension = Extension(name="test_ext", description="test_desc")

    def reset(self, dbo):
        """Execute: clear, generate_structure and fill_data

        :param dbObject dbo: dbo
        """
        TestExtension.clear_structure(dbo)
        TestExtension.generate_structure(dbo)
        self.fill_datas()

    def assert_value(self, extension_test):
        """Asserts with test value

        :param extensionObject extension_test: extension_test
        """
        self.assertTrue(extension_test)

        self.assertEqual("test_ext", extension_test.name)
        self.assertEqual("test_desc", extension_test.description)

    # Test CRUD
    def create_extension(self, dbo):
        """Test create_extension, CRUD method

        :param dbObject dbo: dbo
        """
        self.reset(dbo)  # create default object in fill_datas function

        with orm.db_session:
            # 1. get object in db with ponyorm function (get will be tested lately)
            temp_extension = Extension[self.extension.id]

            # 2. assert on default value and getted value
            self.assert_value(temp_extension)

    def find_extension(self, dbo):
        """test find extension, CRUD method

        :param dbObject dbo: dbo
        """
        self.reset(dbo)

        # 1. find find_extension from db
        with orm.db_session:
            temp_extension, _ = Extension.find_extension_by_id(
                self.extension.id)

            # 2. test value
            self.assert_value(temp_extension)

            temp_extension, err = Extension.find_extension_by_id(-1)

            # 3. assert on error
            self.assertEqual(err, "Extension Not Found !")
            self.assertEqual(temp_extension, None)

            # 4. find_all temp_file from db
            temp_extension = Extension.find_all_extensions()

            # 5. test value
            self.assertEqual(len(temp_extension), 1)
            self.assert_value(temp_extension[0])

    def update_extension(self, dbo):
        """Test update_extension, CRUD method

        :param dbObject dbo: dbo
        """
        self.reset(dbo)
        with orm.db_session:
            # 1. find update_extension from db
            temp_extension, _ = Extension.find_extension_by_id(self.extension.id)

            temp_extension.name = "test_extension_updated"
            temp_extension.description = "test_desc_updated"

            temp_extension, _ = Extension.update_extension_by_id(
                temp_extension.id, temp_extension)

            # 2. assert
            self.assertEqual("test_extension_updated", temp_extension.name)
            self.assertEqual("test_desc_updated", temp_extension.description)

    def remove_extension(self, dbo):
        """Test remove_extension, CRUD method

        :param dbObject dbo: dbo
        """
        self.reset(dbo)
        with orm.db_session:
            # 1. find extension from db
            temp_extension, _ = Extension.find_extension_by_id(self.extension.id)

            # 2. remove
            Extension.remove_extension_by_id(temp_extension.id)

            # 3. re-get
            temp_extension, err = Extension.find_extension_by_id(self.extension.id)

            # 4. assert
            self.assertEqual(temp_extension, None)
            self.assertEqual("Extension Not Found !", err)

    def main(self):
        """Entry point"""

        self.create_extension(db)
        self.find_extension(db)
        self.update_extension(db)
        self.remove_extension(db)
