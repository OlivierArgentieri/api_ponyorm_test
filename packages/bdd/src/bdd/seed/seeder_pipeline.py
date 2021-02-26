from pony import orm
from bdd.models.file import File
from bdd.models.tag_file import TagFile
from bdd.models.extension import Extension
from bdd.models.software import Software
from bdd.models.extension_software import ExtensionSoftware
from bdd.models.task import Task
from bdd.models.substask import Subtask
from bdd.models.variant import Variant
from bdd.models.asset import Asset
from bdd.models.shot import Shot

from bdd.repositories.task_repository import TaskRepository

def clearStructure(db):
    db.drop_table("tagfile", if_exists=True, with_all_data=True)
    db.drop_table("file", if_exists=True, with_all_data=True)
    db.drop_table("file_references", if_exists=True, with_all_data=True)
    db.drop_table("extension", if_exists=True, with_all_data=True)
    db.drop_table("software", if_exists=True, with_all_data=True)
    db.drop_table("extension_software", if_exists=True, with_all_data=True)
    db.drop_table("subtask", if_exists=True, with_all_data=True)
    db.drop_table("task", if_exists=True, with_all_data=True)
    db.drop_table("task_tasks", if_exists=True, with_all_data=True)
    db.drop_table("shot", if_exists=True, with_all_data=True)
    db.drop_table("asset", if_exists=True, with_all_data=True)


@orm.db_session()
def fillDatas(db):

    # create trigger on task
    TaskRepository.SetTriggerConstraintOnInsert(db)

    tag01 = TagFile(name="test_tag", description="test_tab_desc")

    ma = Extension(name=".ma", description="Maya ascii file")
    mb = Extension(name=".mb", description="Maya binary file")

    maya = Software(name="maya")

    maya_ma = ExtensionSoftware(extension=ma, software=maya)
    maya_mb = ExtensionSoftware(extension=mb, software=maya)

    task01 = Task(name="task01")

    subtask01 = Subtask(name="subtask01", task=task01)

    file01 = File(name="scene001", ext=maya_ma, iteration=1,  tag=tag01, subtask=subtask01)
    file02 = File(name="scene002", ext=maya_ma, iteration=1,  tag=tag01, subtask=subtask01)
    file03 = File(name="scene003", ext=maya_mb, iteration=1,  tag=tag01, subtask=subtask01)
    file04 = File(name="scene004", ext=maya_mb, iteration=1,  tag=tag01, subtask=subtask01, references=[file01, file02])



