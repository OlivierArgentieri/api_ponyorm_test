from db.server.server import db
from pony.orm import Required, Set, Optional
import datetime


class AssetCategory(db.Entity):
    """AssetCategory Entity class."""

    name = Required(str)
    asset = Set("Asset", cascade_delete=False)

    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")

    @staticmethod
    def create_asset_category(name):
        """Register assetCategory in db

        :param str name: name

        :return: assetCategory object created
        :rtype: assetCategoryObject
        """

        return AssetCategory(name=name)

    @staticmethod
    def find_all_asset_categories():
        """find all assetCategory, without deleted entities

        :return: list of assetCategory
        :rtype: assetCategoryObjects
        """
        return AssetCategory.select(lambda s: s.deletedAt is None)[:]

    @staticmethod
    def find_asset_category_by_id(asset_category_id):
        """find assetCategory by id, without deleted entities

        :param int asset_category_id: asset_category_id

        :return: assetCategory object found and string for potential error
        :rtype: (assetCategoryObject, str)
        """

        asset_category = AssetCategory.get(
            lambda s: s.id == asset_category_id and s.deletedAt is None)

        if asset_category is None:
            return asset_category, "AssetCategory Not Found !"

        return asset_category, ""

    @staticmethod
    def update_asset_category_by_id(asset_category_id, asset_category_updated):
        """Update assetCategory by id

        :param int asset_category_id: asset_category_id
        :param assetCategoryObject asset_category_updated: new value

        :return: assetCategory object updated and string for potential error
        :rtype: (assetCategoryObject, str)
        """

        # get assetCategory
        target_asset_category = AssetCategory.get(
            lambda s: s.id == asset_category_id and s.deletedAt is None)

        # assetCategory exist?
        if target_asset_category is None:
            return target_asset_category, "AssetCategory Not Found !"

        target_asset_category.name = asset_category_updated.name

        return target_asset_category, ""

    @staticmethod
    def remove_asset_category_by_id(asset_category_id):
        """Delete a assetCategory

        :param int asset_category_id: asset_category_id
        :return: id of assetCategory deleted and string for potential error
        :rtype: (int, str)
        """

        # get assetCategory
        target_asset_category = AssetCategory.get(
            lambda s: s.id == asset_category_id and s.deletedAt is None)

        # assetCategory exist?
        if target_asset_category is None:
            return 0, "AssetCategory Not Found !"

        target_asset_category.deletedAt = datetime.datetime.utcnow()

        return target_asset_category.id, ""
