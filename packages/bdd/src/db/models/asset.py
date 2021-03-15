from db.server.server import db
from pony.orm import Required, Set, Optional
from db.models.project import Project
from db.models.asset_category import AssetCategory
import datetime


class Asset(db.Entity):
    """Asset Entity class."""

    name = Required(str)
    lod = Optional(int)
    Task = Set("Task", cascade_delete=False)
    project = Required(Project)
    asset_category = Required(AssetCategory)

    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")

    @staticmethod
    def create_asset(name, project, asset_category, lod=0):
        """Register asset in db

        :param str name: name
        :param str project: project
        :param int asset_category: asset_category
        :param int lod: lod

        :return: asset object created
        :rtype: assetObject
        """

        return Asset(name=name, project=project, asset_category=asset_category, lod=lod)

    @staticmethod
    def find_all_assets():
        """find all asset, without deleted entities

        :return: list of asset
        :rtype: assetObjects
        """
        return Asset.select(lambda s: s.deletedAt is None)[:]

    @staticmethod
    def find_asset_by_id(asset_id):
        """find asset by id, without deleted entities

        :param int asset_id: asset_id

        :return: asset object found and string for potential error
        :rtype: (assetObject, str)
        """

        asset = Asset.get(lambda s: s.id == asset_id and s.deletedAt is None)
        if asset is None:
            return asset, "Asset Not Found !"

        return asset, ""

    @staticmethod
    def update_asset_by_id(asset_id, asset_updated):
        """Update asset by id

        :param int asset_id: asset_id
        :param assetObject asset_updated: new value

        :return: asset object updated and string for potential error
        :rtype: (assetObject, str)
        """

        # get asset
        target_asset = Asset.get(lambda s: s.id == asset_id and s.deletedAt is None)

        # asset exist?
        if target_asset is None:
            return target_asset, "Asset Not Found !"

        target_asset.name = asset_updated.name
        target_asset.lod = asset_updated.lod
        target_asset.project = asset_updated.project
        target_asset.asset_category = asset_updated.asset_category
        target_asset.updatedAt = datetime.datetime.utcnow()

        return target_asset, ""

    @staticmethod
    def remove_asset_by_id(asset_id):
        """Delete a asset

        :param int asset_id: asset_id
        :return: id of asset deleted and string for potential error
        :rtype: (int, str)
        """

        # get asset
        target_asset = Asset.get(lambda s: s.id == asset_id and s.deletedAt is None)

        # Asset exist?
        if target_asset is None:
            return 0, "Asset Not Found !"

        target_asset.deletedAt = datetime.datetime.utcnow()

        return target_asset.id, ""
