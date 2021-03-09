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


build_command = False
timestamp = 0


def commands():
    env.PATH.append("{root}/src")
    env.PYTHONPATH.append("{root}/src")


vcs = "git"
# ------------------------ TESTS -----------------------

def pre_test_commands():
    if test.name == "unit":
        env.IS_UNIT_TEST = 1
        env.PYTHONPATH.append("{root}/src/tests")

tests = {
    "unit": {
        "command": "python -m unittest discover -s {root}/src/bdd/tests"
    },
    "test": {
        "command": "python -m unittest discover -s {root}/src/bdd/tests"
    }
}