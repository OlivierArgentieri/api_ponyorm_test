from pony import orm

import unittest
from bdd.server.server import db


from bdd.models.car import Car
from bdd.models.person import Person


class TestShot(unittest.TestCase):

    car = None

    def clear_structure(self, db):
        print("Clear structure")
        db.drop_table("car", if_exists=True, with_all_data=True)
        db.drop_table("person", if_exists=True, with_all_data=True)

    def generate_structure(self, db):
        print("Create structure")
        db.create_tables()

    @orm.db_session()
    def fill_datas(self, db):
        print("Fill data")
        self.person = Person(name="test", age=10)
        self.car = Car(make="test", model="test_model", owner=self.person)

    def reset(self, db):
        self.clear_structure(db)
        self.generate_structure(db)
        self.fill_datas(db)
        pass

    def test_create_shot(self):
        self.reset(db)

        self.assertEqual("test", self.car.make)
        self.assertEqual("test_model", self.car.model)
