from pony import orm

import unittest
import datetime
from bdd.server.server import db
from bdd.models.user import User


class TestUser(unittest.TestCase):

    user = None

    @staticmethod
    def clear_structure(db):
        print("Clear user structure")
        db.drop_table("user", if_exists=True, with_all_data=True)

    @staticmethod
    def generate_structure(db):
        print("Create user structure")
        db.create_tables()

    @orm.db_session()
    def fill_datas(self):
        print("Fill user data")
        self.user = User(name="test", email="test@mail.com", createdAt=datetime.datetime.utcnow(), year_start=2020, year_end=2021, updatedAt=datetime.datetime.utcnow())

    def reset(self, db):
        TestUser.clear_structure(db)
        TestUser.generate_structure(db)
        self.fill_datas()

    def assert_value(self, user_test):
        self.assertTrue(user_test)

        self.assertEqual("test", user_test.name)
        self.assertEqual("test@mail.com", user_test.email)
        self.assertEqual(2020, user_test.year_start)
        self.assertEqual(2021, user_test.year_end)

    # Test CRUD
    def create_user(self):
        self.reset(db)  # create default object in fill_datas function

        # 1. get object in bdd with ponyorm function (get will be tested lately)
        with orm.db_session:
            temp_shot = User[self.user.id]

            # 2. assert on default value and getted value
            self.assert_value(temp_shot)

    def main(self):
        self.create_user()


