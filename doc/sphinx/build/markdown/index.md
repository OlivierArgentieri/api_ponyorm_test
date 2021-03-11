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


### class bdd.models.shot.Shot(\*args, \*\*kwargs)
Shot entity class.


#### static create_shot(_duration, _project, _complexity=0, _value='', _render='', _task='')
Register shot in bdd


* **Parameters**

    
    * **_duration** (*int*) – duration


    * **_project** (*projectObject*) – project


    * **_complexity** (*int**, **(**opt**)*) – complexity


    * **_value** (*str**, **(**opt**)*) – value


    * **_render** (*str**, **(**opt**)*) – render


    * **_task** (*taskObject**, **(**opt**)*) – task



* **Returns**

    shot object created



#### static find_all_shots()
find all shot, without deleted entities
:return: lists of shot


#### static find_shot_by_id(_shotId)
find shot by id, without deleted entities
:return: (shot, string) shot object found and string for potential error


#### static remove_shot_by_id(_shotId)
Delete a shot
:param _shotId: id of shot
:return: (id, string) id of shot deleted and string for potential error


#### static update_shot_by_id(_shotId, _shotUpdated)
Update shot by id
:param _shotId: id of shot target
:param _shotUpdated: new value
:return: (shot, string) shot object updated and string for potential error

# PackageBdd test
