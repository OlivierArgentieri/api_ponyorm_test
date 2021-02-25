from pony import orm
from bdd.models.file import File
from bdd.models.tag_file import TagFile
from bdd.models.extension import Extension
from bdd.models.software import Software
from bdd.models.extension_software import ExtensionSoftware


def clearStructure(db):
    db.drop_table("tagfile", if_exists=True, with_all_data=True)
    db.drop_table("file", if_exists=True, with_all_data=True)
    db.drop_table("file_references", if_exists=True, with_all_data=True)
    db.drop_table("extension", if_exists=True, with_all_data=True)
    db.drop_table("software", if_exists=True, with_all_data=True)
    db.drop_table("extension_software", if_exists=True, with_all_data=True)


@orm.db_session()
def fillDatas():

    tag01 = TagFile(name="test_tag", description="test_tab_desc")

    ma = Extension(name=".ma", description="Maya ascii file")
    mb = Extension(name=".mb", description="Maya binary file")

    maya = Software(name="maya")

    maya_ma = ExtensionSoftware(extension=ma, software=maya)
    maya_mb = ExtensionSoftware(extension=mb, software=maya)


    file01 = File(name="scene001", ext=maya_ma, iteration=1,  tag=tag01)
    file02 = File(name="scene002", ext=maya_ma, iteration=1,  tag=tag01)
    file03 = File(name="scene003", ext=maya_mb, iteration=1,  tag=tag01)
    file04 = File(name="scene004", ext=maya_mb, iteration=1,  tag=tag01, references=[file01, file02])



