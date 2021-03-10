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

    def assert_value(self, shot_test):
        self.assertTrue(shot_test)

        self.assertEqual("test_project", shot_test.project.name)
        self.assertEqual("test", shot_test.project.short_name)
        self.assertEqual(2020, shot_test.project.year_start)
        self.assertEqual(2021, shot_test.project.year_end)

        self.assertEqual(10, shot_test.duration)
        self.assertEqual(self.project.id, shot_test.project.id)

    # Test CRUD
    def create_shot(self):
        self.reset(db)  # create default object in fill_datas function

        # 1. get object in bdd with ponyorm function (get will be tested lately)
        with orm.db_session:
            temp_shot = Shot[self.shot.id]

            # 2. assert on default value and getted value
            self.assert_value(temp_shot)

    def find_shot(self):
        self.reset(db)

        # 1. find shot from db
        with orm.db_session:
            temp_shot, _ = Shot.find_shot_by_id(self.shot.id)

            # 2. test value
            self.assert_value(temp_shot)

            # 3. find_all shot from db
            temp_shots = Shot.find_all_shot()

            # 4. test value
            self.assertEqual(len(temp_shots), 1)
            self.assert_value(temp_shots[0])

    def update_shot(self):
        self.reset(db)
        with orm.db_session:
            # 1. find shot from db
            temp_shot, _ = Shot.find_shot_by_id(self.shot.id)

            temp_shot.duration += 20  # auto update to but not updatedAt datetime in this way
            temp_shot, _ = Shot.update_shot_by_id(temp_shot.id, temp_shot)

            # 2. assert
            self.assertEqual("test_project", temp_shot.project.name)
            self.assertEqual("test", temp_shot.project.short_name)
            self.assertEqual(2020, temp_shot.project.year_start)
            self.assertEqual(2021, temp_shot.project.year_end)

            self.assertEqual(30, temp_shot.duration)
            self.assertEqual(self.project.id, temp_shot.project.id)

    def remove_shot(self):
        self.reset(db)
        with orm.db_session:
            # 1. find shot from db
            temp_shot, _ = Shot.find_shot_by_id(self.shot.id)

            # 2. remove
            Shot.remove_shot_by_id(temp_shot.id)

            # 3. re-get
            temp_shot, err = Shot.find_shot_by_id(self.shot.id)

            # 4. assert
            self.assertEqual(temp_shot, None)
            self.assertEqual("Shot Not Found !", err)

    def main(self):
        self.create_shot()
        self.find_shot()
        self.update_shot()
        self.remove_shot()
