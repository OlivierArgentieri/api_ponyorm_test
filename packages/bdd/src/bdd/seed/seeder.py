from pony import orm
from bdd.seed import seeder_basicschema

'''
This is made to fill Bdd with template data
'''

def loadBasicSchema(db):
    seeder_basicschema.clearStructureBasicSchema(db)

    seeder_basicschema.createStructureBasicSchema(db)

    seeder_basicschema.fillDatas()


def load(db):
    loadBasicSchema(db)
