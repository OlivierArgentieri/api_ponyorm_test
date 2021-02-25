from pony import orm
from bdd.seed import seeder_basicschema, seeder_pipeline

'''
This is made to fill Bdd with template data
'''


def createStructure(db):
    """
    Same method for all entities -> Map all tables to generates database
    :param db:
    """

    db.generate_mapping(create_tables=True)


def loadSchema(db):
    """
    Call all seeder file, to drop, recreate and fill each entities in database
    :param db:
    """

    seeder_basicschema.clearStructure(db)
    seeder_pipeline.clearStructure(db)

    createStructure(db)

    seeder_basicschema.fillDatas()
    seeder_pipeline.fillDatas()

def load(db):
    """
    Entrypoint of Seeder structure
    :param db:
    """
    loadSchema(db)
