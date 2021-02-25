from bdd.models.tag_file import TagFile
from pony import orm

class TagFileRepository:

    @staticmethod
    @orm.db_session()
    def getSumOfTag():
        return orm.select(c.id for c in TagFile).sum()