from pony import orm
from db.models.file import File
from db.models.tag_file import TagFile
from db.models.extension import Extension
from db.models.software import Software
from db.models.extension_software import ExtensionSoftware
from db.models.task import Task
from db.models.substask import Subtask
from db.models.variant import Variant
from db.models.asset import Asset
from db.models.shot import Shot
from db.models.project import Project
from db.models.user import User
from db.models.asset_category import AssetCategory
from db.repositories.task_repository import TaskRepository


def clear_structure(db):
    db.drop_table("tagfile", if_exists=True, with_all_data=True)
    db.drop_table("file_references", if_exists=True, with_all_data=True)
    db.drop_table("extension_software", if_exists=True, with_all_data=True)
    db.drop_table("extension", if_exists=True, with_all_data=True)
    db.drop_table("software", if_exists=True, with_all_data=True)
    db.drop_table("subtask", if_exists=True, with_all_data=True)
    db.drop_table("file", if_exists=True, with_all_data=True)

    db.drop_table("task_need", if_exists=True, with_all_data=True)
    db.drop_table("variant", if_exists=True, with_all_data=True)
    db.drop_table("project_user", if_exists=True, with_all_data=True)
    db.drop_table("user", if_exists=True, with_all_data=True)
    db.drop_table("project", if_exists=True, with_all_data=True)

    db.drop_table("assetcategory", if_exists=True, with_all_data=True)
    db.drop_table("asset", if_exists=True, with_all_data=True)
    db.drop_table("shot", if_exists=True, with_all_data=True)
    db.drop_table("task_task", if_exists=True, with_all_data=True)
    db.drop_table("task", if_exists=True, with_all_data=True)


@orm.db_session()
def seed_user():
    return User.create_user("test", "test@mail.com", 2020, 2021)


@orm.db_session()
def seed_project():
    _project = Project.create_project("sample_project", "SP", 2020, 2021)

    # get user and link it to project
    _user = User.find_all_users()[0]

    _project.users += _user
    return _project


@orm.db_session()
def seed_asset():
    # get project
    _project = Project.find_all_projects()[0]

    # create category and asset
    _assetCategory = AssetCategory.create_asset_category("sample_asset")
    return Asset.create_asset("sample_project", _project, _assetCategory)


@orm.db_session()
def seed_shot():
    # get project
    _project = Project.find_all_projects()[0]

    # create shot
    return Shot.create_shot(10, _project)


@orm.db_session()
def seed_tasks():
    # get shot and asset (create 2 task)
    _shot = Shot.find_all_shots()[0]
    _asset = Asset.find_all_assets()[0]

    _task_shot = Task.create_task(name="shot_task_test", shot=_shot)

    # create a needed task
    _neededTask = Task.create_task("needed_task", asset=_asset)
    _neededTask2 = Task.create_task("needed_task2", asset=_asset)
    _task_asset = Task.create_task("asset_task_test", need=[_neededTask, _neededTask2], asset=_asset)

    return [_task_shot, _task_asset]


@orm.db_session()
def seed_variant():
    # get task
    _task = Task.find_all_tasks()[0]

    return Variant.create_variant("test_variant", _task)


@orm.db_session()
def seed_subtask():
    # get task
    _task = Task.find_all_tasks()[0]
    return Subtask.create_subtask("test_subtask", _task)


@orm.db_session()
def seed_file():

    # create extensions
    ma = Extension(name=".ma", description="Maya ascii file")
    mb = Extension(name=".mb", description="Maya binary file")

    # create software
    maya = Software(name="maya")

    # link extensions and software
    maya_ma = ExtensionSoftware(ma, maya)
    maya_mb = ExtensionSoftware(mb, maya)

    # create tag
    tag = TagFile.create_tag_file("test_tag", "test_tag_desc")

    # get subtask
    subtask = Subtask.find_all_subtasks()[0]

    # create file
    file1 = File.create_file("my_folder/test_file.ma", subtask, maya_ma, 0)
    file2 = File.create_file("my_folder/test_file.mb", subtask, maya_mb, 0)

    return


@orm.db_session()
def fill_datas(db):
    # create trigger on task
    TaskRepository.set_trigger_contraint_on_insert(db)

    # _user = seed_user()
    # _project = seed_project()
    # _asset = seed_asset()
    # _shot = seed_shot()
    # _tasks = seed_tasks()
    # _variant = seed_variant()
    # _subtask = seed_subtask()



    # tag01 = TagFile(name="test_tag", description="test_tab_desc")
    #
    # ma = Extension(name=".ma", description="Maya ascii file")
    # mb = Extension(name=".mb", description="Maya binary file")
    #
    # maya = Software(name="maya")
    #
    # maya_ma = ExtensionSoftware(extension=ma, software=maya)
    # maya_mb = ExtensionSoftware(extension=mb, software=maya)
    #
    # project01 = Project(name="tests", short_name="tests", year_start=0, year_end=0)
    #
    # shot01 = Shot.create_shot(100, project01)
    #
    # task01 = Task(name="task01", shot=shot01)
    #
    # subtask01 = Subtask(name="subtask01", task=task01)
    #
    # file01 = File(name="scene001", ext=maya_ma, iteration=1,  tag=tag01, subtask=subtask01)
    # file02 = File(name="scene002", ext=maya_ma, iteration=1,  tag=tag01, subtask=subtask01)
    # file03 = File(name="scene003", ext=maya_mb, iteration=1,  tag=tag01, subtask=subtask01)
    # file04 = File(name="scene004", ext=maya_mb, iteration=1,  tag=tag01, subtask=subtask01, references=[file01, file02])

    # todo : remove (test repositories):
    from db.repositories.tag_file_repository import TagFileRepository

    print("Sum of tags : " + str(TagFileRepository.get_sum_of_tag()))
