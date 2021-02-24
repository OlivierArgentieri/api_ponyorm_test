from pony.orm import Required
from bdd.server.server import db
from bdd.models.person import Person


class Car(db.Entity):
    make = Required(str)
    model = Required(str)
    owner = Required(Person)
