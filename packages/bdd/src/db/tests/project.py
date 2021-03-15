from pony import orm

from db.models.project import Project
from db.models.shot import Shot
from db.server.server import db
import unittest


class TestProject(unittest.TestCase):
    """TestProject unitTest class."""

    project = None
    shots = None

    @staticmethod
    def clear_structure(db):
        """
        Drop each needed entities tables
        :param db: db object
        :return:
        """
        db.drop_table("project", if_exists=True, with_all_data=True)
        db.drop_table("shot", if_exists=True, with_all_data=True)


    @staticmethod
    def generate_structure(db):
        """
        Create each needed entities tables
        :param db: db object
        :return:
        """
        db.create_tables()

    @orm.db_session
    def fill_datas(self):
        """
        fill tables with test data
        :return:
        """
        self.project = Project.create_project("test_project", "test", 2020, 2021)
        self.shots = [Shot(duration=10, project=self.project), Shot(duration=80, project=self.project)]

    def reset(self, db):
        """
        Execute: clear, generate_structure and fill_data
        :param db:
        :return:
        """
        TestProject.clear_structure(db)
        TestProject.generate_structure(db)
        self.fill_datas()

    def assert_value(self, project_test):
        """
        Assert with test value
        :param projectTestObject project_test:
        :return:
        """
        self.assertTrue(project_test)

        self.assertEqual("test_project", project_test.name)
        self.assertEqual("test", project_test.short_name)
        self.assertEqual(2020, project_test.year_start)
        self.assertEqual(2021, project_test.year_end)

        self.assertEqual(2, len(project_test.shots))
        self.assertEqual(10, self.shots[0].duration)
        self.assertEqual(80, self.shots[1].duration)

    # Test CRUD
    def create_project(self):
        """
        Test create_shot, CRUD method
        :return:
        """
        self.reset(db)

        # 1. get object in db with ponyorm function (get will be tested lately)
        with orm.db_session:
            temp_project = Project[self.project.id]

            # 2. assert on default value and getted value
            self.assert_value(temp_project)

    def find_project(self):
        """
        Test find_project, CRUD method
        :return:
        """
        self.reset(db)

        # 1. find project from db
        with orm.db_session:
            temp_project, _ = Project.find_project_by_id(self.project.id)

            # 2. test value
            self.assert_value(temp_project)

            temp_project, err = Project.find_project_by_id(-1)

            # 3. assert on error
            self.assertEqual(err, "Project Not Found !")
            self.assertEqual(temp_project, None)

            # 4. find_all project from db
            temp_projects = Project.find_all_projects()

            # 5. test value
            self.assertEqual(len(temp_projects), 1)
            self.assert_value(temp_projects[0])

    def main(self):
        """
        Entry point
        :return:
        """
        self.create_project()
        self.find_project()
        # self.update_project()
        # self.remove_project()