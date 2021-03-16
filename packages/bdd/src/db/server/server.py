from pony import orm
from db.conf import conf
import os

conf = conf.get_config_file()
db = orm.Database()

if os.getenv("IS_UNIT_TEST", None):
    db.bind(provider=conf.get('db_driver_test', {}), user=conf.get('db_user_test', {}),
            password=conf.get('db_password_test', {}), host=conf.get('db_host_test', {}),
            database=conf.get('db_name_test', {}), port=conf.get('db_port_test', {}))

else:
    db.bind(provider=conf.get('db_driver', {}), user=conf.get('db_user', {}),
            password=conf.get('db_password', {}), host=conf.get('db_host', {}),
            database=conf.get('db_name', {}), port=conf.get('db_port', {}))

orm.set_sql_debug(True)  # to debug request


def run():
    # to avoid circular include in entities->db>seeder->entities->db->seeder ...
    from db.seed import seeder
    seeder.load(db)
