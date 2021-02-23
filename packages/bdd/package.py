name = "filesystem"

version = "0.0.0"

description = \
    """
    bdd ORM
    """

requires = [
    "python",
    "SQLAlchemy",
    "psycopg2",
    "psycopg2_binary-2.8.6",
]

vcs = "git"

def commands():
    env.PYTHONPATH.append("{root}/alchemy")

