from pony import orm
from bdd.conf import conf


conf = conf.getConfigFile()
db = orm.Database()
db.bind(provider=conf.get('db_driver', {}), user=conf.get('db_user', {}), password=conf.get('db_password', {}), host=conf.get('db_host', {}), database=conf.get('db_name', {}), port=conf.get('db_port', {}))

orm.set_sql_debug(True) # to debug request


def run():
    from bdd.seed import seeder # to avoid circular include in entites->db>seeder->enties->db->seeder ...
    seeder.load(db)

