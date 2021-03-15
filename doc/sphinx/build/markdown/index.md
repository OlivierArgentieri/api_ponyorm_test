<!-- TestPonyORM documentation master file, created by
sphinx-quickstart on Thu Mar 11 15:07:54 2021.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# Welcome to TestPonyORM’s documentation!

# Indices and tables


* Index


* Module Index


* Search Page

# PackageBdd models

## Entity asset


### class db.models.asset.Asset(\*args, \*\*kwargs)
Asset Entity class.


#### static create_asset(name, project, asset_category, lod=0)
Register asset in db


* **Parameters**

    
    * **name** (*str*) – name


    * **project** (*str*) – project


    * **asset_category** (*int*) – asset_category


    * **lod** (*int*) – lod



* **Returns**

    asset object created



* **Return type**

    assetObject



#### static find_all_assets()
find all asset, without deleted entities


* **Returns**

    list of asset



* **Return type**

    assetObjects



#### static find_asset_by_id(asset_id)
find asset by id, without deleted entities


* **Parameters**

    **asset_id** (*int*) – asset_id



* **Returns**

    asset object found and string for potential error



* **Return type**

    (assetObject, str)



#### static remove_asset_by_id(asset_id)
Delete a asset


* **Parameters**

    **asset_id** (*int*) – asset_id



* **Returns**

    id of asset deleted and string for potential error



* **Return type**

    (int, str)



#### static update_asset_by_id(asset_id, asset_updated)
Update asset by id


* **Parameters**

    
    * **asset_id** (*int*) – asset_id


    * **asset_updated** (*assetObject*) – new value



* **Returns**

    asset object updated and string for potential error



* **Return type**

    (assetObject, str)


## Entity assetCategory


### class db.models.asset_category.AssetCategory(\*args, \*\*kwargs)
AssetCategory Entity class.


#### static create_asset_category(name)
Register assetCategory in db


* **Parameters**

    **name** (*str*) – name



* **Returns**

    assetCategory object created



* **Return type**

    assetCategoryObject



#### static find_all_asset_categories()
find all assetCategory, without deleted entities


* **Returns**

    list of assetCategory



* **Return type**

    assetCategoryObjects



#### static find_asset_category_by_id(asset_category_id)
find assetCategory by id, without deleted entities


* **Parameters**

    **asset_category_id** (*int*) – asset_category_id



* **Returns**

    assetCategory object found and string for potential error



* **Return type**

    (assetCategoryObject, str)



#### static remove_asset_category_by_id(asset_category_id)
Delete a assetCategory


* **Parameters**

    **asset_category_id** (*int*) – asset_category_id



* **Returns**

    id of assetCategory deleted and string for potential error



* **Return type**

    (int, str)



#### static update_asset_category_by_id(asset_category_id, asset_category_updated)
Update assetCategory by id


* **Parameters**

    
    * **asset_category_id** (*int*) – asset_category_id


    * **asset_category_updated** (*assetCategoryObject*) – new value



* **Returns**

    assetCategory object updated and string for potential error



* **Return type**

    (assetCategoryObject, str)


## Entity extension


### class db.models.extension.Extension(\*args, \*\*kwargs)
Extension Entity class.


#### static create_extension(name, description)
Register extension in db


* **Parameters**

    
    * **name** (*str*) – name


    * **description** (*str*) – description



* **Returns**

    extension object created



* **Return type**

    extensionObject



#### static find_all_extensions()
find all extension, without deleted entities


* **Returns**

    list of extension



* **Return type**

    extensionObjects



#### static find_extension_by_id(extension_id)
find extension by id, without deleted entities


* **Parameters**

    **extension_id** (*int*) – extension_id



* **Returns**

    extension object found and string for potential error



* **Return type**

    (extensionObject, str)



#### static remove_extension_by_id(extension_id)
Delete a extension


* **Parameters**

    **extension_id** (*int*) – extension_id



* **Returns**

    id of extension deleted and string for potential error



* **Return type**

    (int, str)



#### static update_extension_by_id(extension_id, extension_updated)
Update extension by id


* **Parameters**

    
    * **extension_id** (*int*) – extension_id


    * **extension_updated** (*extensionObject*) – new value



* **Returns**

    extension object updated and string for potential error



* **Return type**

    (extensionObject, str)


## Entity extensionSoftware


### class db.models.extension_software.ExtensionSoftware(\*args, \*\*kwargs)
ExtensionSoftware Entity class.


#### static create_extension_software(extension, software)
Register extensionSoftware in db


* **Parameters**

    
    * **extension** (*str*) – extension


    * **software** (*softwareObject*) – software



* **Returns**

    extensionSoftware object created



* **Return type**

    extensionSoftwareObject



#### static find_all_extension_softwares()
find all extensionSoftware, without deleted entities


* **Returns**

    list of extensionSoftware



* **Return type**

    extensionSoftwareObjects



#### static find_extension_software_by_id(extension_software_id)
find extensionSoftware by id, without deleted entities


* **Parameters**

    **extension_software_id** (*int*) – extension_software_id



* **Returns**

    extensionSoftware object found and string for potential error



* **Return type**

    (extensionSoftwareObject, str)



#### static remove_extension_software_by_id(extension_software_id)
Delete a extensionSoftware


* **Parameters**

    **extension_software_id** (*int*) – extension_software_id



* **Returns**

    id of extension_software deleted and string for potential error



* **Return type**

    (int, str)



#### static update_extension_software_by_id(extension_software_id, extension_software_updated)
Update extensionSoftware by id


* **Parameters**

    
    * **extension_software_id** (*int*) – extension_software_id


    * **extension_software_updated** (*extensionSoftwareObject*) – new value



* **Returns**

    extensionSoftware object updated and string for potential error



* **Return type**

    (extensionSoftwareObject, str)


## Entity file


### class db.models.file.File(\*args, \*\*kwargs)
File Entity class.


#### static create_file(name, ext, iteration, tag, subtask, state='', references=None)
Register file in db


* **Parameters**

    
    * **name** (*str*) – name


    * **ext** (*extensionSoftwareObject*) – file extension


    * **iteration** (*int*) – iteration


    * **tag** (*tagFileObject*) – tag


    * **subtask** (*subtaskObject*) – subtask


    * **state** (*str*) – state (opt)


    * **references** (*fileObject*) – file references (opt)



* **Returns**

    file object created



* **Return type**

    fileObject



#### static find_all_files()
find all file, without deleted entities


* **Returns**

    list of file



* **Return type**

    fileObjects



#### static find_file_by_id(file_id)
find file by id, without deleted entities


* **Parameters**

    **file_id** (*int*) – file_id



* **Returns**

    file object found and string for potential error



* **Return type**

    (fileObject, str)



#### static remove_file_by_id(file_id)
Delete a file


* **Parameters**

    **file_id** (*int*) – file_id



* **Returns**

    id of file deleted and string for potential error



* **Return type**

    (int, str)



#### static update_file_by_id(file_id, file_updated)
Update file by id


* **Parameters**

    
    * **file_id** (*int*) – file_id


    * **file_updated** (*fileObject*) – new value



* **Returns**

    file object updated and string for potential error



* **Return type**

    (fileObject, str)


## Entity project


### class db.models.project.Project(\*args, \*\*kwargs)
Project Entity class.


#### static create_project(_name, _short_name, _year_start, _year_end)
Register project in db


* **Parameters**

    
    * **_name** (*str*) – name


    * **_short_name** (*str*) – short_name


    * **_year_start** (*int*) – year_start


    * **_year_end** (*int*) – year_end



* **Returns**

    project object created



* **Return type**

    projectObject



#### static find_all_projects()
find all project, without deleted entities


* **Returns**

    list of project



* **Return type**

    projectObjects



#### static find_project_by_id(_project_id)
find project by id, without deleted entities


* **Parameters**

    **_project_id** (*int*) – project_id



* **Returns**

    project object found and string for potential error



* **Return type**

    (projectObject, str)



#### static remove_project_by_id(_project_id)
Delete a project


* **Parameters**

    **_project_id** (*int*) – project_id



* **Returns**

    id of project deleted and string for potential error



* **Return type**

    (int, str)



#### static update_project_by_id(_project_id, _project_updated)
Update project by id


* **Parameters**

    
    * **_project_id** (*int*) – project_id


    * **_project_updated** (*projectObject*) – new value



* **Returns**

    project object updated and string for potential error



* **Return type**

    (projectObject, str)


## Entity shot


### class db.models.shot.Shot(\*args, \*\*kwargs)
Shot entity class.


#### static create_shot(duration, project, complexity=0, value='', render='', task='')
Register shot in db


* **Parameters**

    
    * **duration** (*int*) – duration


    * **project** (*projectObject*) – project


    * **complexity** (*int*) – complexity (opt)


    * **value** (*str*) – value (opt)


    * **render** (*str*) – render (opt)


    * **task** (*taskObject*) – task (opt)



* **Returns**

    shot object created



#### static find_all_shots()
find all shot, without deleted entities


* **Returns**

    lists of shot



#### static find_shot_by_id(shot_id)
find shot by id, without deleted entities


* **Parameters**

    **shot_id** (*int*) – shotId



* **Returns**

    (shot, string) shot object found and string for potential error



#### static remove_shot_by_id(shot_id)
Delete a shot


* **Parameters**

    **shot_id** (*int*) – id of shot



* **Returns**

    (id, string) id of shot deleted and string for potential error



#### static update_shot_by_id(shot_id, shot_updated)
Update shot by id


* **Parameters**

    
    * **shot_id** (*int*) – id of shot target


    * **shot_updated** (*shotObject*) – new value



* **Returns**

    (shot, string) shot object updated and string for potential error


## Entity software


### class db.models.software.Software(\*args, \*\*kwargs)
Software Entity class.


#### static create_software(name)
Register software in db


* **Parameters**

    **name** (*str*) – name



* **Returns**

    software object created



* **Return type**

    softwareObject



#### static find_all_softwares()
find all software, without deleted entities


* **Returns**

    list of software



* **Return type**

    softwareObjects



#### static find_software_by_id(software_id)
find software by id, without deleted entities


* **Parameters**

    **software_id** (*int*) – software_id



* **Returns**

    software object found and string for potential error



* **Return type**

    (softwareObject, str)



#### static remove_software_by_id(software_id)
Delete a software


* **Parameters**

    **software_id** (*int*) – software_id



* **Returns**

    id of software deleted and string for potential error



* **Return type**

    (int, str)



#### static update_software_by_id(software_id, software_updated)
Update software by id


* **Parameters**

    
    * **software_id** (*int*) – software_id


    * **software_updated** (*softwareObject*) – new value



* **Returns**

    software object updated and string for potential error



* **Return type**

    (softwareObject, str)


## Entity subtask


### class db.models.subtask.Subtask(\*args, \*\*kwargs)
Entity Subtask class.


#### static create_subtask(name, task)
Register subtask in db


* **Parameters**

    
    * **name** (*str*) – name


    * **task** (*taskObject*) – task



* **Returns**

    variant object created



* **Return type**

    variantObject



#### static find_all_subtasks()
find all subtask, without deleted entities


* **Returns**

    list of subtask



* **Return type**

    subtaskObjects



#### static find_subtask_by_id(subtask_id)
find subtask by id, without deleted entities


* **Parameters**

    **subtask_id** (*int*) – subtask_id



* **Returns**

    subtask object found and string for potential error



* **Return type**

    (subtaskObject, str)



#### static remove_subtask_by_id(subtask_id)
Delete a subtask


* **Parameters**

    **subtask_id** (*int*) – subtask_id



* **Returns**

    id of subtask deleted and string for potential error



* **Return type**

    (int, str)



#### static update_subtask_by_id(subtask_id, subtask_updated)
Update subtask by id


* **Parameters**

    
    * **subtask_id** (*int*) – subtask_id


    * **subtask_updated** (*subtaskObject*) – new value



* **Returns**

    subtask object updated and string for potential error



* **Return type**

    (subtaskObject, str)


## Entity tagFile


### class db.models.tag_file.TagFile(\*args, \*\*kwargs)
TagFile Entity class.


#### static create_tag_file(name, description)
Register tagFile in db


* **Parameters**

    
    * **name** (*str*) – name


    * **description** (*str*) – description



* **Returns**

    tagFile object created



* **Return type**

    tagFileObject



#### static find_all_tag_files()
find all tagFile, without deleted entities


* **Returns**

    list of tagFile



* **Return type**

    tagFileObjects



#### static find_tag_file_by_id(tag_file_id)
find tagFile by id, without deleted entities


* **Parameters**

    **tag_file_id** (*int*) – tag_file_id



* **Returns**

    tagFile object found and string for potential error



* **Return type**

    (tagFileObject, str)



#### static remove_tag_file_by_id(tag_file_id)
Delete a tagFile


* **Parameters**

    **tag_file_id** (*int*) – tag_file_id



* **Returns**

    id of tagFile deleted and string for potential error



* **Return type**

    (int, str)



#### static update_tag_file_by_id(tag_file_id, tag_file_updated)
Update tagFile by id


* **Parameters**

    
    * **tag_file_id** (*int*) – tag_file_id


    * **tag_file_updated** (*tagFile*) – new value



* **Returns**

    tagFile object updated and string for potential error



* **Return type**

    (tagFileObject, str)


## Entity task


### class db.models.task.Task(\*args, \*\*kwargs)
Task Entity class.


#### static create_task(name, progress=0, asset=None, shot=None, need=None)
Register task in db


* **Parameters**

    
    * **name** (*str*) – name


    * **progress** (*str*) – progress (opt)


    * **asset** (*assetObject*) – asset (opt)


    * **shot** (*shotObject*) – shot (opt)


    * **need** (*taskObject*) – need (opt)



* **Returns**

    task  object created



* **Return type**

    taskObject



#### static find_all_tasks()
find all task, without deleted entities


* **Returns**

    list of task



* **Return type**

    taskObjects



#### static find_task_by_id(task_id)
find task by id, without deleted entities


* **Parameters**

    **task_id** (*int*) – task_id



* **Returns**

    task object found and string for potential error



* **Return type**

    (taskObject, str)



#### static remove_task_by_id(task_id)
Delete a task


* **Parameters**

    **task_id** (*int*) – task_id



* **Returns**

    id of task deleted and string for potential error



* **Return type**

    (int, str)



#### static update_task_by_id(task_id, task_updated)
Update task by id


* **Parameters**

    
    * **task_id** (*int*) – task_id


    * **task_updated** (*taskObject*) – new value



* **Returns**

    task object updated and string for potential error



* **Return type**

    (taskObject, str)


## Entity user


### class db.models.user.User(\*args, \*\*kwargs)
User entity class.


#### static create_user(name, email, year_start, year_end)
Register user in db


* **Parameters**

    
    * **name** (*str*) – name


    * **email** (*str*) – name


    * **year_start** (*int*) – year_start


    * **year_end** (*int*) – year_end



* **Returns**

    user object created



* **Return type**

    userObject



#### static find_all_users()
find all user, without deleted entities


* **Returns**

    list of user



* **Return type**

    userObjects



#### static find_user_by_id(user_id)
find user by id, without deleted entities


* **Parameters**

    **user_id** (*int*) – user_id



* **Returns**

    user object found and string for potential error



* **Return type**

    (userObject, str)



#### static remove_user_by_id(user_id)
Delete a user


* **Parameters**

    **user_id** (*int*) – user_id



* **Returns**

    id of user deleted and string for potential error



* **Return type**

    (int, str)



#### static update_user_by_id(user_id, userUpdated)
Update user by id


* **Parameters**

    
    * **user_id** (*int*) – user_id


    * **userUpdated** (*userObject*) – new value



* **Returns**

    user object updated and string for potential error



* **Return type**

    (userObject, str)


## Entity variant


### class db.models.variant.Variant(\*args, \*\*kwargs)
Variant Entity class.


#### static create_variant(name, task, state='')
Register variant in db


* **Parameters**

    
    * **name** (*str*) – name


    * **task** (*taskObject*) – task (opt)


    * **state** (*str*) – state



* **Returns**

    variant object created



* **Return type**

    variantObject



#### static find_all_variants()
find all variant, without deleted entities


* **Returns**

    list of variant



* **Return type**

    variantObjects



#### static find_variant_by_id(variant_id)
find variant by id, without deleted entities


* **Parameters**

    **variant_id** (*int*) – variant_id



* **Returns**

    variant object found and string for potential error



* **Return type**

    (variantObject, str)



#### static remove_variant_by_id(variant_id)
Delete a variant


* **Parameters**

    **variant_id** (*int*) – variant_id



* **Returns**

    id of variant deleted and string for potential error



* **Return type**

    (int, str)



#### static update_variant_by_id(variant_id, variant_updated)
Update variant by id


* **Parameters**

    
    * **variant_id** (*int*) – variant_id


    * **variant_updated** (*variantObject*) – new value



* **Returns**

    variant object updated and string for potential error



* **Return type**

    (variantObject, str)


# PackageBdd test
