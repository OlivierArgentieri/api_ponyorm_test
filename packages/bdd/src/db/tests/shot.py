from pony import orm
from db.server.server import db
from db.models.project import Project
from db.models.shot import Shot
import unittest


class TestShot(unittest.TestCase):
    """TestShot UnitTest class."""

    shot = None
    project = None

    @staticmethod
    def clear_structure(_db):
        """
        Drop each needed entities tables
        :param _db: db object
        :return:
        """
        _db.drop_table("project", if_exists=True, with_all_data=True)
        _db.drop_table("shot", if_exists=True, with_all_data=True)

    @staticmethod
    def generate_structure(_db):
        """
        Create each needed entities tables
        :param _db: db object
        :return:
        """
        _db.create_tables()

    @orm.db_session
    def fill_datas(self):
        """
        Fill tables with test data
        :return:
        """
        self.project = Project(name="test_project", short_name="test", year_start=2020, year_end=2021)
        self.shot = Shot.create_shot(10, self.project)

    def reset(self, _db):
        """
        Execute: clear, generate_structure and fill_data
        :param _db: db object
        :return:
        """
        TestShot.clear_structure(_db)
        TestShot.generate_structure(_db)
        self.fill_datas()

    def assert_value(self, shot_test):
        """
        Asserts with test value
        :param shot_test: shot object
        :return:
        """
        self.assertTrue(shot_test)

        self.assertEqual("test_project", shot_test.project.name)
        self.assertEqual("test", shot_test.project.short_name)
        self.assertEqual(2020, shot_test.project.year_start)
        self.assertEqual(2021, shot_test.project.year_end)

        self.assertEqual(10, shot_test.duration)
        self.assertEqual(self.project.id, shot_test.project.id)

    # Test CRUD
    def create_shot(self):
        """
        Test create_shot, CRUD method
        :return:
        """
        self.reset(db)  # create default object in fill_datas function

        # 1. get object in db with ponyorm function (get will be tested lately)
        with orm.db_session:
            temp_shot = Shot[self.shot.id]

            # 2. assert on default value and getted value
            self.assert_value(temp_shot)

    def find_shot(self):
        """
        Test find_shot, CRUD method
        :return:
        """
        self.reset(db)

        # 1. find shot from db
        with orm.db_session:
            temp_shot, _ = Shot.find_shot_by_id(self.shot.id)

            # 2. test value
            self.assert_value(temp_shot)

            temp_shot, err = Shot.find_shot_by_id(-1)

            # 3. assert on error
            self.assertEqual(err, "Shot Not Found !")
            self.assertEqual(temp_shot, None)

            # 4. find_all shot from db
            temp_shots = Shot.find_all_shots()

            # 5. test value
            self.assertEqual(len(temp_shots), 1)
            self.assert_value(temp_shots[0])

    def update_shot(self):
        """
        Test update_shot, CRUD method
        :return:
        """
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

            # 3. assert on error
            temp_shot, err = Shot.update_shot_by_id(-1, temp_shot)
            self.assertEqual(err, "Shot Not Found !")
            self.assertEqual(temp_shot, None)

    def remove_shot(self):
        """
        Test remove_shot, CRUD method
        :return:
        """
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
        """
        Entry point
        :return:
        """
        self.create_shot()
        self.find_shot()
        self.update_shot()
        self.remove_shot()
