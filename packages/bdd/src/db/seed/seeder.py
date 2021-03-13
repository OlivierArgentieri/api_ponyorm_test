from pony import orm
from db.seed import seeder_basicschema, seeder_pipeline

'''
This is made to fill Bdd with template data
'''


def create_structure(db):
    """
    Same method for all entities -> Map all tables to generates database
    :param db:
    """

    db.generate_mapping(create_tables=True)


def load_schema(db):
    """
    Call all seeder file, to drop, recreate and fill each entities in database
    :param db:
    """

    seeder_basicschema.clear_structure(db)
    seeder_pipeline.clear_structure(db)

    create_structure(db)

    #seeder_basicschema.fill_datas()
    seeder_pipeline.fill_datas(db)


def load(db):
    """
    Entrypoint of Seeder structure
    :param db:
    """
    load_schema(db)
