import unittest

# ENTITIES #
# END ENTITIES #

from bdd.server.server import db
from bdd.tests.user import TestUser
from bdd.tests.shot import TestShot


class TestMain(unittest.TestCase):

    @staticmethod
    def generate_structure():
        db.generate_mapping(create_tables=True)

    def test_main(self):
        # init ddb
        TestMain.generate_structure()

        test_user = TestUser()
        test_user.test_create_user()

        test_shot = TestShot()
        test_shot.test_create_shot()