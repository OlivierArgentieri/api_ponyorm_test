from pony import orm
from bdd.models.car import Car
from bdd.models.person import Person
from bdd.models.file import File
from bdd.models.tag_file import TagFile


def clearStructureBasicSchema(db):
    db.drop_table("car", if_exists=True, with_all_data=True)
    db.drop_table("person", if_exists=True, with_all_data=True)
    db.drop_table("tag_file", if_exists=True, with_all_data=True)
    db.drop_table("file", if_exists=True, with_all_data=True)


def createStructureBasicSchema(db):
    db.generate_mapping(create_tables=True)


@orm.db_session()
def fillDatas():
    p1 = Person(name='John', age=20)
    p2 = Person(name='May', age=22)
    p3 = Person(name='Bob', age=30)

    c1 = Car(make='Toyota', model='Prius', owner=p2)
    c2 = Car(make='Ford', model='Explorer', owner=p3)

    # fill pipeline

