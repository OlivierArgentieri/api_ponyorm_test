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

tools = [
    "bdd"
]

vcs = "git"

def commands():
    env.PATH.append("{root}/src")
    env.PYTHONPATH.append("{root}/src")

