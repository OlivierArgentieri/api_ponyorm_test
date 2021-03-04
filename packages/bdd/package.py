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
    "PyYAML-5.4.1",
    "os"
]

tools = [
    "bdd"
]

vcs = "git"

build_command = False
timestamp = 0


def commands():
    env.PATH.append("{root}/src")
    env.PYTHONPATH.append("{root}/src")


tests = {
    "unit": {
        "command": "python -c print('test')"
    }
}