import unittest

# ENTITIES #
# END ENTITIES #

from bdd.server.server import db
from bdd.tests.user import TestUser
from bdd.tests.shot import TestShot

class TestMain(unittest.TestCase):

    def generateStructure(self):
        db.generate_mapping(create_tables=True)

    def test_main(self):
        # init ddb
        self.generateStructure()

        test_user = TestUser()
        test_user.testCreateUser()

        test_shot = TestShot()
        test_shot.testCreateShot()