name = "db_package"

version = "0.0.2"


description = \
    """
    db ORM
    """

requires = [
    "python-3.7.7",
    "pony-0.7.14",
    "psycopg2",
    "PyYAML-5.4.1",
    "os",
    "Sphinx",
    "sphinx_rtd_theme",
    "sphinx_markdown_builder",
]


tools = [
    "db"
    "doc_md",
    "doc_html",
]


build_command = False
timestamp = 0


def commands():
    env.PATH.append("{root}/src")
    env.PATH.append("{root}")
    env.PYTHONPATH.append("{root}/src")


vcs = "git"
# ------------------------ TESTS -----------------------


def pre_test_commands():
    if test.name == "unit":
        env.IS_UNIT_TEST = 1
        env.PYTHONPATH.append("{root}/src/tests")


tests = {
    "unit": {
        "command": "python -m unittest discover -s {root}/src/db/tests"
    }
}