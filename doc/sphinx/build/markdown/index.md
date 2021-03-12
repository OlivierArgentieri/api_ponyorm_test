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

## Entity shot


### class db.models.shot.Shot(\*args, \*\*kwargs)
Shot entity class.


#### static create_shot(_duration, _project, _complexity=0, _value='', _render='', _task='')
Register shot in db


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


* **Returns**

    lists of shot



#### static find_shot_by_id(_shot_id)
find shot by id, without deleted entities


* **Parameters**

    **_shot_id** (*int*) – shotId



* **Returns**

    (shot, string) shot object found and string for potential error



#### static remove_shot_by_id(_shot_id)
Delete a shot


* **Parameters**

    **_shot_id** (*int*) – id of shot



* **Returns**

    (id, string) id of shot deleted and string for potential error



#### static update_shot_by_id(_shot_id, _shot_updated)
Update shot by id


* **Parameters**

    
    * **_shot_id** (*int*) – id of shot target


    * **_shot_updated** (*shotObject*) – new value



* **Returns**

    (shot, string) shot object updated and string for potential error


## Entity user


### class db.models.user.User(\*args, \*\*kwargs)
User entity class.


#### static create_user(_name, _email, _year_start, _year_end)
Register user in db


* **Parameters**

    
    * **_name** (*str*) – name


    * **_email** (*str*) – name


    * **_year_start** (*int*) – year_start


    * **_year_end** (*int*) – year_end



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



#### static find_user_by_id(_user_id)
find user by id, without deleted entities


* **Parameters**

    **_user_id** (*int*) – user_id



* **Returns**

    user object found and string for potential error



* **Return type**

    (userObject, str)



#### static remove_user_by_id(_user_id)
Delete a user


* **Parameters**

    **_user_id** (*int*) – user_id



* **Returns**

    id of user deleted and string for potential error



* **Return type**

    (int, str)



#### static update_user_by_id(_user_id, _userUpdated)
Update user by id


* **Parameters**

    
    * **_user_id** (*int*) – user_id


    * **_userUpdated** (*userObject*) – new value



* **Returns**

    user object updated and string for potential error



* **Return type**

    (userObject, str)


# PackageBdd test
