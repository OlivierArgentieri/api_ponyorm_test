from pony import orm
import yaml
from bdd.conf import conf


conf = conf.getConfigFile()
db = orm.Database()
db.bind(provider=conf.get('db_driver', {}), user=conf.get('db_user', {}), password=conf.get('db_password', {}), host=conf.get('db_host', {}), database=conf.get('db_name', {}), port=conf.get('db_port', {}))
orm.set_sql_debug(True)