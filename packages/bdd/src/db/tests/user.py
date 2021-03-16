from pony import orm
from db.server.server import db
from db.models.user import User
import unittest


class TestUser(unittest.TestCase):
    """Test shot class"""

    user = None

    @staticmethod
    def clear_structure(dbo):
        """
        Drop each needed entities tables
        :param dbObject dbo: dbo
        :return:
        """
        dbo.drop_table("user", if_exists=True, with_all_data=True)

    @staticmethod
    def generate_structure(dbo):
        """
        Create each needed entities tables
        :param dbObject dbo: dbo
        :return:
        """
        dbo.create_tables()

    @orm.db_session()
    def fill_datas(self):
        """
        Fill tables with test data
        :return:
        """
        self.user = User.create_user("test", "test@mail.com", 2020, 2021)

    def reset(self, dbo):
        """
        Execute: clear, generate_structure and fill_data
       :param dbObject dbo: dbo
        :return:
        """
        TestUser.clear_structure(dbo)
        TestUser.generate_structure(dbo)
        self.fill_datas()

    def assert_value(self, user_test):
        """
        Asserts with test value
        :param user_test: user object
        :return:
        """
        self.assertTrue(user_test)

        self.assertEqual("test", user_test.name)
        self.assertEqual("test@mail.com", user_test.email)
        self.assertEqual(2020, user_test.year_start)
        self.assertEqual(2021, user_test.year_end)

    # Test CRUD
    def create_user(self, dbo):
        """
        Test create_user, CRUD method
        :param dbObject dbo: dbo
        :return:
        """
        self.reset(dbo)  # create default object in fill_datas function

        # 1. get object in db with ponyorm function (get will be tested lately)
        with orm.db_session:
            temp_shot = User[self.user.id]

            # 2. assert on default value and getted value
            self.assert_value(temp_shot)

    def main(self):
        print("aaa")
        self.create_user(db)
