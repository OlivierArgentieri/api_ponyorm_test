from db.server.server import db
from pony.orm import Required, Set, Optional
from db.models.task import Task
import datetime


class Variant(db.Entity):
    """Variant Entity class."""

    name = Required(str)
    state = Optional(str)
    task = Required(Task)

    createdAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="created_at")
    updatedAt = Required(datetime.datetime, default=datetime.datetime.utcnow, column="updated_at")
    deletedAt = Optional(datetime.datetime, nullable=True, column="deleted_at")

    @staticmethod
    def create_variant(_name, _task, _state=""):
        """Register variant in db

        :param str _name: name
        :param int _state: asset
        :param int _task: task

        :return: variant object created
        :rtype: variantObject
        """

        return Variant(name=_name, task=_task, state=_state)

    @staticmethod
    def find_all_variants():
        """find all variant, without deleted entities

        :return: list of variant
        :rtype: variantObjects
        """
        return Variant.select(lambda s: s.deletedAt is None)[:]

    @staticmethod
    def find_variant_by_id(_variant_id):
        """find variant by id, without deleted entities

        :param int _variant_id: variant_id

        :return: variant object found and string for potential error
        :rtype: (variantObject, str)
        """

        _variant = Variant.get(lambda s: s.id == _variant_id and s.deletedAt is None)
        if _variant is None:
            return _variant, "Variant Not Found !"

        return _variant, ""

    @staticmethod
    def update_variant_by_id(_variant_id, _variant_updated):
        """Update variant by id

        :param int _variant_id: variant_id
        :param variantObject _variant_updated: new value

        :return: variant object updated and string for potential error
        :rtype: (variantObject, str)
        """

        # get variant
        _targetVariant = Variant.get(lambda s: s.id == _variant_id and s.deletedAt is None)

        # variant exist?
        if _targetVariant is None:
            return _targetVariant, "Variant Not Found !"

        _targetVariant.name = _variant_updated.name
        _targetVariant.state = _variant_updated.short_name
        _targetVariant.task = _variant_updated.year_start
        _targetVariant.updatedAt = datetime.datetime.utcnow()

        return _targetVariant, ""

    @staticmethod
    def remove_variant_by_id(_variant_id):
        """Delete a variant

        :param int _variant_id: variant_id
        :return: id of variant deleted and string for potential error
        :rtype: (int, str)
        """

        # get variant
        _targetVariant = Variant.get(lambda s: s.id == _variant_id and s.deletedAt is None)

        # Variant exist?
        if _targetVariant is None:
            return 0, "Variant Not Found !"

        _targetVariant.deletedAt = datetime.datetime.utcnow()

        return _targetVariant.id, ""
