from pony import orm

db = orm.Database()

db.bind(provider='postgres', user='postgres', password='toor', host='192.168.30.131', database='test')



db.drop_table("person", if_exists=True, with_all_data=True)
class Person(db.Entity):
    name = orm.Required(str)
    age = orm.Required(int)
    cars = orm.Set('Car')

db.drop_table("car", if_exists=True, with_all_data=True)
class Car(db.Entity):
    make = orm.Required(str)
    model = orm.Required(str)
    owner = orm.Required(Person)


db.generate_mapping(create_tables=True)
orm.set_sql_debug(True)

# fill data
# db_session are needed for bd action

@orm.db_session()
def fill_data() :
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
