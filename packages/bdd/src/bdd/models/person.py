import os

if os.getenv("IS_UNIT_TEST", 0):
    from bdd.tests.main import db
else:
    from bdd.server.server import db

from pony.orm import Required, Set


class Person(db.Entity):
    name = Required(str)
    age = Required(int)
    cars = Set('Car')