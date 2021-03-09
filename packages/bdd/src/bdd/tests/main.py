from pony import orm
from bdd.conf import conf


conf = conf.getConfigFile()
db = orm.Database()
db.bind(provider=conf.get('db_driver_test', {}), user=conf.get('db_user_test', {}), password=conf.get('db_password_test', {}), host=conf.get('db_host_test', {}), database=conf.get('db_name_test', {}), port=conf.get('db_port_test', {}))

orm.set_sql_debug(True) # to debug request

print("start")

