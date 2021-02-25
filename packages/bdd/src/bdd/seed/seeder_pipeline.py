from pony import orm
from bdd.models.file import File
from bdd.models.tag_file import TagFile


def clearStructure(db):
    db.drop_table("tagfile", if_exists=True, with_all_data=True)
    db.drop_table("file", if_exists=True, with_all_data=True)
    db.drop_table("file_references", if_exists=True, with_all_data=True)


@orm.db_session()
def fillDatas():

    tag01 = TagFile(name="test_tag", description="test_tab_desc")

    file01 = File(name="scene001", ext=".ma", iteration=1,  tag=tag01)
    file02 = File(name="scene002", ext=".ma", iteration=1,  tag=tag01)
    file03 = File(name="scene003", ext=".ma", iteration=1,  tag=tag01)
    file04 = File(name="scene004", ext=".ma", iteration=1,  tag=tag01, references=[file01, file02])


