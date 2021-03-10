from pony import orm

import unittest
from bdd.server.server import db


from bdd.models.project import Project
from bdd.models.shot import Shot


class TestShot(unittest.TestCase):

    shot = None
    project = None

    @staticmethod
    def clear_structure(db):
        print("Clear structure")
        db.drop_table("project", if_exists=True, with_all_data=True)
        db.drop_table("shot", if_exists=True, with_all_data=True)

    @staticmethod
    def generate_structure(db):
        print("Create structure")
        db.create_tables()

    @orm.db_session
    def fill_datas(self, db):
        print("Fill data")
        self.project = Project(name="test_project", short_name="test", year_start=2020, year_end=2021)
        self.shot, _ = Shot.create_shot(10, self.project)

    def reset(self, db):
        TestShot.clear_structure(db)
        TestShot.generate_structure(db)
        self.fill_datas(db)

    # Test CRUD
    def test_create_shot(self):
        self.reset(db)  # create default object in fill_datas function

        # 1. get object in bdd with ponyorm function (get will be tested lately)
        with orm.db_session:
            temp_shot = Shot[self.shot.id]

            # 2. assert on default value and getted value
            self.assertTrue(temp_shot)

            self.assertEqual("test_project", temp_shot.project.name)
            self.assertEqual("test",  temp_shot.project.short_name)
            self.assertEqual(2020,  temp_shot.project.year_start)
            self.assertEqual(2021,  temp_shot.project.year_end)

            self.assertEqual(10,  temp_shot.duration)
            self.assertEqual(self.project.id,  temp_shot.project.id)



    def test_main(self):
        self.reset(db)

        self.test_create_shot()
