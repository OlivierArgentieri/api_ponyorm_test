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
    def clear_structure(dbo):
        """Drop each needed entities tables

        :param dbObject dbo : db
        """
        dbo.drop_table("project", if_exists=True, with_all_data=True)
        dbo.drop_table("shot", if_exists=True, with_all_data=True)

    @staticmethod
    def generate_structure(dbo):
        """Create each needed entities tables

        :param dbObject dbo : db
        """
        dbo.create_tables()

    @orm.db_session
    def fill_datas(self):
        """fill tables with test data"""

        self.project = Project.create_project("test_project", "test", 2020, 2021)
        self.shots = [Shot(duration=10, project=self.project),
                      Shot(duration=80, project=self.project)]

    def reset(self, dbo):
        """Execute: clear, generate_structure and fill_data

        :param dbObject dbo: dbo
        """
        TestProject.clear_structure(dbo)
        TestProject.generate_structure(dbo)
        self.fill_datas()

    def assert_value(self, project_test):
        """Assert with test value

        :param projectTestObject project_test:
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
    def create_project(self, dbo):
        """Test create_project, CRUD method

        :param dbObject dbo: dbo
        """
        self.reset(dbo)

        # 1. get object in db with ponyorm function (get will be tested lately)
        with orm.db_session:
            temp_project = Project[self.project.id]

            # 2. assert on default value and getted value
            self.assert_value(temp_project)

    def find_project(self, dbo):
        """Test find_project, CRUD method

        :param dbObject dbo: dbo
        """
        self.reset(dbo)

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

    def update_project(self, dbo):
        """Test update_project, CRUD method

        :param dbObject dbo: dbo
        """
        self.reset(dbo)
        with orm.db_session:
            # 1. find project from db
            temp_project, _ = Project.find_project_by_id(self.project.id)

            # auto update to but not updatedAt datetime in this way
            temp_project.name = "updated_test_project"
            temp_project.short_name = "updated_test"
            temp_project.year_start += 1
            temp_project.year_end += 1
            temp_project, _ = Project.update_project_by_id(
                temp_project.id, temp_project)

            # 2. assert
            self.assertEqual("updated_test_project", temp_project.name)
            self.assertEqual("updated_test", temp_project.short_name)
            self.assertEqual(2021, temp_project.year_start)
            self.assertEqual(2022, temp_project.year_end)

    def remove_project(self, dbo):
        """Test remove_project, CRUD method

        :param dbObject dbo: dbo
        """
        self.reset(dbo)
        with orm.db_session:
            # 1. find project from db
            temp_project, _ = Project.find_project_by_id(self.project.id)

            # 2. remove
            Project.remove_project_by_id(temp_project.id)

            # 3. re-get
            temp_project, err = Project.find_project_by_id(self.project.id)

            # 4. assert
            self.assertEqual(temp_project, None)
            self.assertEqual("Project Not Found !", err)

    def main(self):
        """Entry point"""

        self.create_project(db)
        self.find_project(db)
        self.update_project(db)
        self.remove_project(db)
