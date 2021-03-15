from pony import orm

from db.models.asset_category import AssetCategory
from db.server.server import db
import unittest


class TestAssetCategory(unittest.TestCase):
    """TestAssetCategory unitTest class."""

    asset_category = None

    @staticmethod
    def clear_structure(db):
        """
        Drop each needed entities tables
        :param db: db object
        :return:
        """
        db.drop_table("asset_category", if_exists=True, with_all_data=True)

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
        fill tables with test datas
        :return:
        """
        self.asset_category = AssetCategory.create_asset_category("test_asset_category")

    def reset(self, db):
        """
        Execute: clear, generate_structure and fill_data
        :param db:
        :return:
        """
        TestAssetCategory.clear_structure(db)
        TestAssetCategory.generate_structure(db)
        self.fill_datas()

    def assert_value(self, asset_category_test):
        """
        Assert with test value
        :param assetCategoryTestObject asset_category_test:
        :return:
        """
        self.assertTrue(asset_category_test)

        self.assertEqual("test_asset_category", asset_category_test.name)

    # Test CRUD
    def create_asset_category(self):
        """
        Test create_asset_category, CRUD method
        :return:
        """
        self.reset(db)

        # 1. get object in db with ponyorm function (get will be tested lately)
        with orm.db_session:
            temp_asset_category = AssetCategory[self.asset_category.id]

            # 2. assert on default value and getted value
            self.assert_value(temp_asset_category)

    def main(self):
        """
        Entry point
        :return:
        """
        self.create_asset_category()
        # self.find_asset_category()
        # self.update_asset_category()
        # self.remove_asset_category()
