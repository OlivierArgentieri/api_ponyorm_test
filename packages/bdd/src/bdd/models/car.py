import os
if os.getenv("IS_UNIT_TEST", 0):
    from bdd.tests.main import db
else:
    from bdd.server.server import db


from pony.orm import Required

from bdd.models.person import Person


class Car(db.Entity):
    make = Required(str)
    model = Required(str)
    owner = Required(Person)
