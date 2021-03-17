from pony import orm
from db.server.server import db
from db.models.software import Software
import unittest


class TestSoftware(unittest.TestCase):
    """TestSoftware unitTest class."""

    software = None

    @staticmethod
    def clear_structure(dbo):
        """
        Drop each needed entities tables
        :param dbObject dbo: dbo
        :return:
        """

        db.drop_table("file", if_exists=True, with_all_data=True)
        dbo.drop_table("extension_software", if_exists=True, with_all_data=True)
        dbo.drop_table("extension", if_exists=True, with_all_data=True)
        dbo.drop_table("software", if_exists=True, with_all_data=True)

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
        fill tables with test datas
        :return:
        """
        # xor on asset and shot
        self.software = Software(name="test_software")

    def reset(self, dbo):
        """
        Execute: clear, generate_structure and fill_data
        :param dbObject dbo: dbo
        :return:
        """
        TestSoftware.clear_structure(dbo)
        TestSoftware.generate_structure(dbo)
        self.fill_datas()

    def assert_value(self, software_test):
        """
        Asserts with test value
        :param softwareObject software_test: software_test
        :return:
        """
        self.assertTrue(software_test)

        self.assertEqual("test_software", software_test.name)

    # Test CRUD
    def create_software(self, dbo):
        """
        Test create_software, CRUD method
        :param dbObject dbo: dbo
        :return:
        """
        self.reset(dbo)  # create default object in fill_datas function

        with orm.db_session:
            # 1. get object in db with ponyorm function (get will be tested lately)
            create_software = Software[self.software.id]

            # 2. assert on default value and getted value
            self.assert_value(create_software)

    def find_software(self, dbo):
        """
        test find software, CRUD method
        :param dbObject dbo: dbo
        :return:
        """
        self.reset(dbo)

        # 1. find find_software from db
        with orm.db_session:
            temp_software, _ = Software.find_software_by_id(
                self.software.id)

            # 2. test value
            self.assert_value(temp_software)

            temp_software, err = Software.find_software_by_id(-1)

            # 3. assert on error
            self.assertEqual(err, "Software Not Found !")
            self.assertEqual(temp_software, None)

            # 4. find_all temp_file from db
            temp_software = Software.find_all_softwares()

            # 5. test value
            self.assertEqual(len(temp_software), 1)
            self.assert_value(temp_software[0])

    def update_software(self, dbo):
        """
        Test update_software, CRUD method
        :param dbObject dbo: dbo
        :return:
        """
        self.reset(dbo)
        with orm.db_session:
            # 1. find update_software from db
            temp_software, _ = Software.find_software_by_id(self.software.id)

            temp_software.name = "test_software_updated"

            temp_software, _ = Software.update_software_by_id(
                temp_software.id, temp_software)

            # 2. assert
            self.assertEqual("test_software_updated", temp_software.name)

    def remove_software(self, dbo):
        """
        Test remove_software, CRUD method
        :param dbObject dbo: dbo
        :return:
        """
        self.reset(dbo)
        with orm.db_session:
            # 1. find software from db
            temp_software, _ = Software.find_software_by_id(self.software.id)

            # 2. remove
            Software.remove_software_by_id(temp_software.id)

            # 3. re-get
            temp_software, err = Software.find_software_by_id(self.software.id)

            # 4. assert
            self.assertEqual(temp_software, None)
            self.assertEqual("Software Not Found !", err)

    def main(self):
        """
        Entry point
        :return:
        """
        self.create_software(db)
        self.find_software(db)
        self.update_software(db)
        self.remove_software(db)
