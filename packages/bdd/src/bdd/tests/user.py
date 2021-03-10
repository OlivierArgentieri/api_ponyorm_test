from pony import orm

import unittest
import datetime
from bdd.server.server import db
from bdd.models.user import User


class TestUser(unittest.TestCase):

    user = None

    def clearStructure(self, db):
        print("Clear user structure")
        db.drop_table("user", if_exists=True, with_all_data=True)

    def generateStructure(self, db):
        print("Create user structure")
        db.create_tables()

    @orm.db_session()
    def fillDatas(self, db):
        print("Fill user data")
        self.user = User(name="test", email="test@mail.com", createdAt=datetime.datetime.utcnow(), year_start=2020, year_end=2022, updatedAt=datetime.datetime.utcnow())

    def reset(self, db):
        self.clearStructure(db)
        self.generateStructure(db)
        self.fillDatas(db)

    def testCreateUser(self):
        self.reset(db)

        self.assertEqual("test", self.user.name)
        self.assertEqual("test@mail.com", self.user.email)
        self.assertEqual(2020, self.user.year_start)
        self.assertEqual(2022, self.user.year_end)

        # tests create
        # temp_shot = Shot(duration=100, complexity=0, value='', render='', task='', project=TestShot.project)
        #
        # self.assertEqual(temp_shot.duration, TestShot.shot.duration)
        # self.assertEqual(temp_shot.complexity, TestShot.shot.complexity)
        # self.assertEqual(temp_shot.project, TestShot.shot.project)
