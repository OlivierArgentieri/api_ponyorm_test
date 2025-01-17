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
        """Drop each needed entities tables

        :param dbObject dbo: dbo
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
        """Create each needed entities tables

        :param dbObject dbo: dbo
        """
        dbo.create_tables()

    @orm.db_session
    def fill_datas(self):
        """fill tables with test datas"""

        self.task = Task(name="test_task")
        self.variant = Variant.create_variant("test_variant", self.task, "test_state")

    def reset(self, dbo):
        """Execute: clear, generate_structure and fill_data

        :param dbObject dbo: dbo
        """
        TestVariant.clear_structure(dbo)
        TestVariant.generate_structure(dbo)
        self.fill_datas()

    def assert_value(self, variant_test):
        """Assert with test value

        :param variantTestObject variant_test:
        """
        self.assertTrue(variant_test)

        self.assertEqual("test_variant", variant_test.name)
        self.assertEqual(self.task.id, variant_test.task.id)
        self.assertEqual("test_state", variant_test.state)

    # Test CRUD
    def create_variant(self, dbo):
        """Test create_variant, CRUD method

        :param dbObject dbo: dbo
        """
        self.reset(dbo)

        # 1. get object in db with ponyorm function (get will be tested lately)
        with orm.db_session:
            temp_variant = Variant[self.task.id]

            # 2. assert on default value and getted value
            self.assert_value(temp_variant)

    def find_variant(self, dbo):
        """Test find_variant, CRUD method

        :param dbObject dbo: dbo
        """
        self.reset(dbo)

        # 1. find temp_variant from db
        with orm.db_session:
            temp_variant, _ = Variant.find_variant_by_id(self.variant.id)

            # 2. test value
            self.assert_value(temp_variant)

            temp_variant, err = Variant.find_variant_by_id(-1)

            # 3. assert on error
            self.assertEqual(err, "Variant Not Found !")
            self.assertEqual(temp_variant, None)

            # 4. find_all variant from db
            temp_variants = Variant.find_all_variants()

            # 5. test value
            self.assertEqual(len(temp_variants), 1)
            self.assert_value(temp_variants[0])

    def update_variant(self, dbo):
        """Test update_variant, CRUD method

        :param dbObject dbo: dbo
        """
        self.reset(dbo)
        with orm.db_session:
            # 1. find update_variant from db
            temp_variant, _ = Variant.find_variant_by_id(self.variant.id)

            temp_variant.name = "test_variant_updated"
            temp_variant.state = "test_state_updated"

            temp_variant, _ = Variant.update_variant_by_id(
                temp_variant.id, temp_variant)

            # 2. assert
            self.assertEqual("test_variant_updated", temp_variant.name)
            self.assertEqual("test_state_updated", temp_variant.state)

    def remove_variant(self, dbo):
        """Test remove_variant, CRUD method

        :param dbObject dbo: dbo
        """
        self.reset(dbo)
        with orm.db_session:
            # 1. find variant from db
            temp_variant, _ = Variant.find_variant_by_id(self.variant.id)

            # 2. remove
            Variant.remove_variant_by_id(temp_variant.id)

            # 3. re-get
            temp_variant, err = Variant.find_variant_by_id(self.variant.id)

            # 4. assert
            self.assertEqual(temp_variant, None)
            self.assertEqual("Variant Not Found !", err)

    def main(self):
        """Entry point"""

        self.create_variant(db)
        self.find_variant(db)
        self.update_variant(db)
        self.remove_variant(db)
