from pony import orm

db = orm.Database()
db.bind(provider='postgres', user='postgres', password='toor', host='192.168.30.131', database='test')
