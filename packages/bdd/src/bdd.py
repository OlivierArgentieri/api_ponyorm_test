from pony import orm
from bdd.models.person import Person
from bdd.server import server

from bdd.repositories.tag_file_repository import TagFileRepository

server.run()


# Some Queries
@orm.db_session()
def some_queries():
    req = orm.select(p for p in Person if p.age > 20)[:]

    print(req)


some_queries()

print("Sum of tags : " + str(TagFileRepository.getSumOfTag()))
