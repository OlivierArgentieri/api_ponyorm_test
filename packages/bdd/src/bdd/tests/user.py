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
        self.user = User(name="test", email="test@mail.com", createdAt=datetime.datetime.utcnow(), year_start=2020, year_end=2022, updatedAt=datetime.datetime.utcnow())

    def reset(self, db):
        TestUser.clear_structure(db)
        TestUser.generate_structure(db)
        self.fill_datas()

    def test_create_user(self):
        self.reset(db)

        self.assertEqual("test", self.user.name)
        self.assertEqual("test@mail.com", self.user.email)
        self.assertEqual(2020, self.user.year_start)
        self.assertEqual(2022, self.user.year_end)

