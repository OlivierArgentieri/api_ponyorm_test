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
        db.drop_table("assetcategory", if_exists=True, with_all_data=True)

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

    def find_asset_category(self):
        """
        test find asset_category, CRUD method
        :return:
        """
        self.reset(db)

        # 1. find asset_category from db
        with orm.db_session:
            temp_asset_category, _ = AssetCategory.find_asset_category_by_id(self.asset_category.id)

            # 2. test value
            self.assert_value(temp_asset_category)

            temp_asset_category, err = AssetCategory.find_asset_category_by_id(-1)

            # 3. assert on error
            self.assertEqual(err, "AssetCategory Not Found !")
            self.assertEqual(temp_asset_category, None)

            # 4. find_all asset_category from db
            temp_asset_categories = AssetCategory.find_all_asset_categories()

            # 5. test value
            self.assertEqual(len(temp_asset_categories), 1)
            self.assert_value(temp_asset_categories[0])

    def update_asset_category(self):
        """
        Test update_asset_category, CRUD method
        :return:
        """
        self.reset(db)
        with orm.db_session:
            # 1. find update_asset_category from db
            temp_asset_category, _ = AssetCategory.find_asset_category_by_id(self.asset_category.id)

            temp_asset_category.name = "updated_name"

            temp_asset_category, _ = AssetCategory.update_asset_category_by_id(temp_asset_category.id, temp_asset_category)

            # 2. assert
            self.assertEqual("updated_name", temp_asset_category.name)

    def remove_asset_category(self):
        """
        Test remove_asset_category, CRUD method
        :return:
        """
        self.reset(db)
        with orm.db_session:
            # 1. find asset_category from db
            temp_asset_category, _ = AssetCategory.find_asset_category_by_id(self.asset_category.id)

            # 2. remove
            AssetCategory.remove_asset_category_by_id(temp_asset_category.id)

            # 3. re-get
            temp_asset_category, err = AssetCategory.find_asset_category_by_id(self.asset_category.id)

            # 4. assert
            self.assertEqual(temp_asset_category, None)
            self.assertEqual("AssetCategory Not Found !", err)

    def main(self):
        """
        Entry point
        :return:
        """
        self.create_asset_category()
        self.find_asset_category()
        self.update_asset_category()
        self.remove_asset_category()