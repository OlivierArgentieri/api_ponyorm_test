from db.server.server import db
from pony.orm import Required, Set, Optional
import datetime


class AssetCategory(db.Entity):
    """AssetCategory Entity"""

    name = Required(str)
    asset = Set("Asset", cascade_delete=False)

    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")

    @staticmethod
    def create_asset_category(_name):
        """Register assetCategory in db

        :param str _name: name

        :return: assetCategory object created
        :rtype: assetCategoryObject
        """

        return AssetCategory(name=_name)

    @staticmethod
    def find_all_asset_categories():
        """find all assetCategory, without deleted entities

        :return: list of assetCategory
        :rtype: assetCategoryObjects
        """
        return AssetCategory.select(lambda s: s.deletedAt is None)[:]

    @staticmethod
    def find_asset_category_by_id(_asset_category_id):
        """find assetCategory by id, without deleted entities

        :param int _asset_category_id: asset_category_id

        :return: assetCategory object found and string for potential error
        :rtype: (assetCategoryObject, str)
        """

        _assetCategory = AssetCategory.get(lambda s: s.id == _asset_category_id and s.deletedAt is None)
        if _assetCategory is None:
            return _assetCategory, "AssetCategory Not Found !"

        return _assetCategory, ""

    @staticmethod
    def update_asset_category_by_id(_asset_category_id, _asset_category_updated):
        """Update assetCategory by id

        :param int _asset_category_id: asset_category_id
        :param assetCategoryObject _asset_category_updated: new value

        :return: assetCategory object updated and string for potential error
        :rtype: (assetCategoryObject, str)
        """

        # get assetCategory
        _targetAssetCategory = AssetCategory.get(lambda s: s.id == _asset_category_id and s.deletedAt is None)

        # assetCategory exist?
        if _targetAssetCategory is None:
            return _targetAssetCategory, "AssetCategory Not Found !"

        _targetAssetCategory.name = _asset_category_updated.name

        return _targetAssetCategory, ""

    @staticmethod
    def remove_asset_category_by_id(_asset_category_id):
        """Delete a assetCategory

        :param int _asset_category_id: asset_category_id
        :return: id of assetCategory deleted and string for potential error
        :rtype: (int, str)
        """

        # get assetCategory
        _targetAssetCategory = AssetCategory.get(lambda s: s.id == _asset_category_id and s.deletedAt is None)

        # assetCategory exist?
        if _targetAssetCategory is None:
            return 0, "AssetCategory Not Found !"

        _targetAssetCategory.deletedAt = datetime.datetime.utcnow()

        return _targetAssetCategory.id, ""