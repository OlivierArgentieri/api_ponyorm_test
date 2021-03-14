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
    def create_asset(_name, _project, _asset_category, _lod=0):
        """Register asset in db

        :param str _name: name
        :param str _project: project
        :param int _asset_category: asset_category
        :param int _lod: lod

        :return: asset object created
        :rtype: assetObject
        """

        return Asset(name=_name, project=_project, asset_category=_asset_category, lod = _lod)

    @staticmethod
    def find_all_assets():
        """find all asset, without deleted entities

        :return: list of asset
        :rtype: assetObjects
        """
        return Asset.select(lambda s: s.deletedAt is None)[:]

    @staticmethod
    def find_asset_by_id(_asset_id):
        """find asset by id, without deleted entities

        :param int _asset_id: asset_id

        :return: asset object found and string for potential error
        :rtype: (assetObject, str)
        """

        _asset = Asset.get(lambda s: s.id == _asset_id and s.deletedAt is None)
        if _asset is None:
            return _asset, "Asset Not Found !"

        return _asset, ""

    @staticmethod
    def update_asset_by_id(_asset_id, _asset_updated):
        """Update asset by id

        :param int _asset_id: asset_id
        :param assetObject _asset_updated: new value

        :return: asset object updated and string for potential error
        :rtype: (assetObject, str)
        """

        # get asset
        _targetAsset = Asset.get(lambda s: s.id == _asset_id and s.deletedAt is None)

        # asset exist?
        if _targetAsset is None:
            return _targetAsset, "Asset Not Found !"

        _targetAsset.name = _asset_updated.name
        _targetAsset.lod = _asset_updated.lod
        _targetAsset.project = _asset_updated.project
        _targetAsset.asset_category = _asset_updated.asset_category
        _targetAsset.updatedAt = datetime.datetime.utcnow()

        return _targetAsset, ""

    @staticmethod
    def remove_asset_by_id(_asset_id):
        """Delete a asset

        :param int _asset_id: asset_id
        :return: id of asset deleted and string for potential error
        :rtype: (int, str)
        """

        # get asset
        _targetAsset = Asset.get(lambda s: s.id == _asset_id and s.deletedAt is None)

        # Asset exist?
        if _targetAsset is None:
            return 0, "Asset Not Found !"

        _targetAsset.deletedAt = datetime.datetime.utcnow()

        return _targetAsset.id, ""
