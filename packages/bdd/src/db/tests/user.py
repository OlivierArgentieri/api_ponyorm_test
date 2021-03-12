from pony import orm

import unittest
import datetime
from db.server.server import db
from db.models.user import User


class TestUser(unittest.TestCase):
    user = None

    @staticmethod
    def clear_structure(_db):
        """
        Drop each needed entities tables
        :param _db: db object
        :return:
        """
        db.drop_table("user", if_exists=True, with_all_data=True)

    @staticmethod
    def generate_structure(_db):
        """
        Create each needed entities tables
        :param _db: db object
        :return:
        """
        db.create_tables()

    @orm.db_session()
    def fill_datas(self):
        """
        Fill tables with test data
        :return:
        """
        self.user = User.create_user("test", "test@mail.com", 2020, 2021)

    def reset(self, _db):
        """
        Execute: clear, generate_structure and fill_data
        :param _db: db object
        :return:
        """
        TestUser.clear_structure(db)
        TestUser.generate_structure(db)
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
    def create_user(self):
        """
        Test create_user, CRUD method
        :return:
        """
        self.reset(db)  # create default object in fill_datas function

        # 1. get object in db with ponyorm function (get will be tested lately)
        with orm.db_session:
            temp_shot = User[self.user.id]

            # 2. assert on default value and getted value
            self.assert_value(temp_shot)

    def main(self):
        self.create_user()
