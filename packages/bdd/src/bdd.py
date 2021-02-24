from pony import orm

db = orm.Database()

db.bind(provider='postgres', user='postgres', password='toor', host='192.168.30.131', database='test')


class Person(db.Entity):
    name = orm.Required(str)
    age = orm.Required(int)
    cars = orm.Set('Car')


class Car(db.Entity):
    make = orm.Required(str)
    model = orm.Required(str)
    owner = orm.Required(Person)


db.generate_mapping(create_tables=True)
orm.set_sql_debug(True)