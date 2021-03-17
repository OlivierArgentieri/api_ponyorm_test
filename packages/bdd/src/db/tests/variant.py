from pony import orm
from db.server.server import db
from db.models.variant import Variant
from db.models.task import Task
import unittest


class TestVariant(unittest.TestCase):
    """TestVariant unitTest class."""

    variant = None
    task = None

    @staticmethod
    def clear_structure(dbo):
        """
        Drop each needed entities tables
        :param dbObject dbo: dbo
        :return:
        """
        dbo.drop_table("variant", if_exists=True, with_all_data=True)
        dbo.drop_table("asset", if_exists=True, with_all_data=True)
        dbo.drop_table("shot", if_exists=True, with_all_data=True)
        dbo.drop_table("task", if_exists=True, with_all_data=True)
        dbo.drop_table("project", if_exists=True, with_all_data=True)

        dbo.drop_table("subtask", if_exists=True, with_all_data=True)
        dbo.drop_table("task", if_exists=True, with_all_data=True)
        dbo.drop_table("variant", if_exists=True, with_all_data=True)

    @staticmethod
    def generate_structure(dbo):
        """
        Create each needed entities tables
        :param dbObject dbo: dbo
        :return:
        """
        dbo.create_tables()

    @orm.db_session
    def fill_datas(self):
        """
        fill tables with test datas
        :return:
        """
        self.task = Task(name="test_task")
        self.variant = Variant.create_variant("test_variant", self.task, "test_state")

    def reset(self, dbo):
        """
        Execute: clear, generate_structure and fill_data
        :param dbObject dbo: dbo
        :return:
        """
        TestVariant.clear_structure(dbo)
        TestVariant.generate_structure(dbo)
        self.fill_datas()

    def assert_value(self, variant_test):
        """
        Assert with test value
        :param variantTestObject variant_test:
        :return:
        """
        self.assertTrue(variant_test)

        self.assertEqual("test_variant", variant_test.name)
        self.assertEqual(self.task.id, variant_test.task.id)
        self.assertEqual("test_state", variant_test.state)

    # Test CRUD
    def create_variant(self, dbo):
        """
        Test create_variant, CRUD method
        :param dbObject dbo: dbo
        :return:
        """
        self.reset(dbo)

        # 1. get object in db with ponyorm function (get will be tested lately)
        with orm.db_session:
            temp_variant = Variant[self.task.id]

            # 2. assert on default value and getted value
            self.assert_value(temp_variant)

    def main(self):
        """
        Entry point
        :return:
        """
        self.create_variant(db)
        # self.find_asset(db)
        # self.update_asset(db)
        # self.remove_asset(db)