from pony import orm

import unittest
from bdd.tests import main
db = main.db

from bdd.models.person import Person
from bdd.models.car import Car


db.generate_mapping(create_tables=True)


@orm.db_session
def create_entities():
    p1 = Person(name='John', age=20)


create_entities()


#
# class TestShot(unittest.TestCase):
#
#     project = None
#     shot = None
#
#     @staticmethod
#     def clearStructure(db):
#         print("Clear structure")
#
#         #db.drop_table("project", if_exists=True, with_all_data=True)
#         #db.drop_table("shot", if_exists=True, with_all_data=True)
#
#     @staticmethod
#     def generateStructure(db):
#         print("Create structure")
#
#
#
#     @staticmethod
#     @orm.db_session()
#     def fillDatas(db):
#         print("Fill data")
#
#         project = Project(name="tests", short_name="tests", year_start=0, year_end=0)
#         shot, _ = Shot.CreateShot(100, project)
#
#     def testCreateShot(self):
#         TestShot.clearStructure(db)
#         TestShot.generateStructure(db)
#         TestShot.fillDatas(db)
#
#         # tests create
#         temp_shot = Shot(duration=100, complexity=0, value='', render='', task='', project=self.project)
#
#         self.assertEqual(temp_shot.duration, self.shot.duration)
#         self.assertEqual(temp_shot.complexity, self.shot.complexity)
#         self.assertEqual(temp_shot.project, self.shot.project)
#
#
# def run_test(db):
#     unittest.main()
