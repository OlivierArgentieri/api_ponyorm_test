from pony import orm

from bdd.models.person import Person
from bdd.models.car import Car

from bdd.server.server import db



db.drop_table("car", if_exists=True, with_all_data=True)
db.drop_table("person", if_exists=True, with_all_data=True)


db.generate_mapping(create_tables=True)
orm.set_sql_debug(True)

# fill data
# db_session are needed for bd action
# drop table if exist with data
@orm.db_session()
def fill_data():
    p1 = Person(name='John', age=20)
    p2 = Person(name='May', age=22)
    p3 = Person(name='Bob', age=30)

    c1 = Car(make='Toyota', model='Prius', owner=p2)
    c2 = Car(make='Ford', model='Explorer', owner=p3)

    orm.commit()

fill_data()


# Some Queries
@orm.db_session()
def some_queries() :
    req = orm.select(p for p in Person if p.age > 20)[:]

    print(req)

some_queries()
