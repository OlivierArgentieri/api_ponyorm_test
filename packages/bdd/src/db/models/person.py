from db.server.server import db
from pony.orm import Required, Set


class Person(db.Entity):
    name = Required(str)
    age = Required(int)
    cars = Set('Car')
