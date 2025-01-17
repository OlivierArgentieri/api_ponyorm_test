from db.models.tag_file import TagFile
from pony import orm


class TagFileRepository:

    @staticmethod
    @orm.db_session()
    def get_sum_of_tag():
        """
        Return Numberof tagFile in database
        :return int: number of tagFile
        """
        return orm.select(c.id for c in TagFile).sum()
