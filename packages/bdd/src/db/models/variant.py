from db.server.server import db
from db.models.task import Task
from pony.orm import Required, Optional
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
    def create_variant(name, task, state=""):
        """Register variant in db

        :param str name: name
        :param taskObject task: task (opt)
        :param str state: state

        :return: variant object created
        :rtype: variantObject
        """

        return Variant(name=name, task=task, state=state)

    @staticmethod
    def find_all_variants():
        """find all variant, without deleted entities

        :return: list of variant
        :rtype: variantObjects
        """
        return Variant.select(lambda s: s.deletedAt is None)[:]

    @staticmethod
    def find_variant_by_id(variant_id):
        """find variant by id, without deleted entities

        :param int variant_id: variant_id

        :return: variant object found and string for potential error
        :rtype: (variantObject, str)
        """

        variant = Variant.get(lambda s: s.id == variant_id and s.deletedAt is None)
        if variant is None:
            return variant, "Variant Not Found !"

        return variant, ""

    @staticmethod
    def update_variant_by_id(variant_id, variant_updated):
        """Update variant by id

        :param int variant_id: variant_id
        :param variantObject variant_updated: new value

        :return: variant object updated and string for potential error
        :rtype: (variantObject, str)
        """

        # get variant
        target_variant = Variant.get(lambda s: s.id == variant_id and s.deletedAt is None)

        # variant exist?
        if target_variant is None:
            return target_variant, "Variant Not Found !"

        target_variant.name = variant_updated.name
        target_variant.state = variant_updated.short_name
        target_variant.task = variant_updated.year_start
        target_variant.updatedAt = datetime.datetime.utcnow()

        return target_variant, ""

    @staticmethod
    def remove_variant_by_id(variant_id):
        """Delete a variant

        :param int variant_id: variant_id
        :return: id of variant deleted and string for potential error
        :rtype: (int, str)
        """

        # get variant
        target_variant = Variant.get(lambda s: s.id == variant_id and s.deletedAt is None)

        # Variant exist?
        if target_variant is None:
            return 0, "Variant Not Found !"

        target_variant.deletedAt = datetime.datetime.utcnow()

        return target_variant.id, ""
