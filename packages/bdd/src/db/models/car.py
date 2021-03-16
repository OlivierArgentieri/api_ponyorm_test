from db.server.server import db
from db.models.person import Person
from pony.orm import Required


class Car(db.Entity):
    make = Required(str)
    model = Required(str)
    owner = Required(Person)
