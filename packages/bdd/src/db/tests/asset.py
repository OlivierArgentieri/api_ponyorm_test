from pony import orm
from db.models.asset import Asset
from db.models.asset_category import AssetCategory
from db.models.project import Project
from db.server.server import db
import unittest


class TestAsset(unittest.TestCase):
    """TestAsset unitTest class."""

    asset = None
    asset_category = None
    project = None

    @staticmethod
    def clear_structure(dbo):
        """
        Drop each needed entities tables
        :param dbObject dbo: dbo
        :return:
        """
        dbo.drop_table("assetcategory", if_exists=True, with_all_data=True)
        dbo.drop_table("project", if_exists=True, with_all_data=True)
        dbo.drop_table("asset", if_exists=True, with_all_data=True)

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
        self.asset_category = AssetCategory.create_asset_category("test_asset")
        self.project = Project.create_project("test_project", "test", 2020, 2021)

        self.asset = Asset.create_asset("test_asset", self.project, self.asset_category, 10)

    def reset(self, dbo):
        """
        Execute: clear, generate_structure and fill_data
        :param dbObject dbo: dbo
        :return:
        """
        TestAsset.clear_structure(dbo)
        TestAsset.generate_structure(dbo)
        self.fill_datas()

    def assert_value(self, asset_test):
        """
        Assert with test value
        :param assetTestObject asset_test:
        :return:
        """
        self.assertTrue(asset_test)

        self.assertEqual("test_asset", asset_test.name)
        self.assertEqual(self.project.id, asset_test.project.id)
        self.assertEqual(self.asset_category.id, asset_test.asset_category.id)
        self.assertEqual(10, asset_test.lod)

    # Test CRUD
    def create_asset(self, dbo):
        """
        Test create_asset, CRUD method
        :param dbObject dbo: dbo
        :return:
        """
        self.reset(dbo)

        # 1. get object in db with ponyorm function (get will be tested lately)
        with orm.db_session:
            temp_asset = Asset[self.asset.id]

            # 2. assert on default value and getted value
            self.assert_value(temp_asset)

    def main(self):
        """
        Entry point
        :return:
        """
        print("bbb")

        self.create_asset(db)
        # self.find_project(db)
        # self.update_project(db)
        # self.remove_project(db)
