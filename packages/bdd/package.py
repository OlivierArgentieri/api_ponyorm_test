name = "filesystem"

version = "0.0.0"

description = \
    """
    bdd ORM
    """

requires = [
    "python-3.7.7",
    "pony",
    "psycopg2",
]

vcs = "git"

def commands():
    env.PYTHONPATH.append("{root}/src")

