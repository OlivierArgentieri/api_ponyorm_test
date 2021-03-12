from db.server.server import db
from pony.orm import Required
from db.models.person import Person


class Car(db.Entity):
    make = Required(str)
    model = Required(str)
    owner = Required(Person)