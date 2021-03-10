from pony import orm

import unittest
from bdd.server.server import db


from bdd.models.car import Car
from bdd.models.person import Person


class TestShot(unittest.TestCase):

    car = None

    def clearStructure(self, db):
        print("Clear structure")
        db.drop_table("car", if_exists=True, with_all_data=True)
        db.drop_table("person", if_exists=True, with_all_data=True)

    def generateStructure(self, db):
        print("Create structure")
        db.create_tables()

    @orm.db_session()
    def fillDatas(self, db):
        print("Fill data")
        self.person = Person(name="test", age=10)
        self.car = Car(make="test", model="test_model", owner=self.person)


    def reset(self, db):
        self.clearStructure(db)
        self.generateStructure(db)
        self.fillDatas(db)
        pass

    def testCreateShot(self):
        self.reset(db)

        self.assertEqual("test", self.car.make)
        self.assertEqual("test_model", self.car.model)


        # tests create
        # temp_shot = Shot(duration=100, complexity=0, value='', render='', task='', project=TestShot.project)
        #
        # self.assertEqual(temp_shot.duration, TestShot.shot.duration)
        # self.assertEqual(temp_shot.complexity, TestShot.shot.complexity)
        # self.assertEqual(temp_shot.project, TestShot.shot.project)
