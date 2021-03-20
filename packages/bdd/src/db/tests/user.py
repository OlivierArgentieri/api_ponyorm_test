from pony import orm
from db.server.server import db
from db.models.user import User
import unittest


class TestUser(unittest.TestCase):
    """Test shot class"""

    user = None

    @staticmethod
    def clear_structure(dbo):
        """
        Drop each needed entities tables
        :param dbObject dbo: dbo
        :return:
        """
        dbo.drop_table("user", if_exists=True, with_all_data=True)

    @staticmethod
    def generate_structure(dbo):
        """
        Create each needed entities tables
        :param dbObject dbo: dbo
        :return:
        """
        dbo.create_tables()

    @orm.db_session()
    def fill_datas(self):
        """
        Fill tables with test data
        :return:
        """
        self.user = User.create_user("test", "test@mail.com", 2020, 2021)

    def reset(self, dbo):
        """
        Execute: clear, generate_structure and fill_data
        :param dbObject dbo: dbo
        :return:
        """
        TestUser.clear_structure(dbo)
        TestUser.generate_structure(dbo)
        self.fill_datas()

    def assert_value(self, user_test):
        """
        Asserts with test value
        :param user_test: user object
        :return:
        """
        self.assertTrue(user_test)

        self.assertEqual("test", user_test.name)
        self.assertEqual("test@mail.com", user_test.email)
        self.assertEqual(2020, user_test.year_start)
        self.assertEqual(2021, user_test.year_end)

    # Test CRUD
    def create_user(self, dbo):
        """
        Test create_user, CRUD method
        :param dbObject dbo: dbo
        :return:
        """
        self.reset(dbo)  # create default object in fill_datas function

        # 1. get object in db with ponyorm function (get will be tested lately)
        with orm.db_session:
            temp_shot = User[self.user.id]

            # 2. assert on default value and getted value
            self.assert_value(temp_shot)

    def find_user(self, dbo):
        """
        test find user, CRUD method
        :param dbObject dbo: dbo
        :return:
        """
        self.reset(dbo)

        # 1. find user from db
        with orm.db_session:
            temp_user, _ = User.find_user_by_id(self.user.id)

            # 2. test value
            self.assert_value(temp_user)

            temp_user, err = User.find_user_by_id(-1)

            # 3. assert on error
            self.assertEqual(err, "User Not Found !")
            self.assertEqual(temp_user, None)

            # 4. find_all user from db
            temp_users = User.find_all_users()

            # 5. test value
            self.assertEqual(len(temp_users), 1)
            self.assert_value(temp_users[0])

    def update_user(self, dbo):
        """
        Test update_user, CRUD method
        :param dbObject dbo: dbo
        :return:
        """
        self.reset(dbo)
        with orm.db_session:
            # 1. find update_user from db
            temp_user, _ = User.find_user_by_id(self.user.id)

            temp_user.name = "updated_name"
            temp_user.email = "updated_test@mail.com"
            temp_user.year_start = 2021
            temp_user.year_end = 2022

            temp_user, _ = User.update_user_by_id(temp_user.id, temp_user)

            # 2. assert
            self.assertEqual("updated_name", temp_user.name)
            self.assertEqual("updated_test@mail.com", temp_user.email)
            self.assertEqual(2021, temp_user.year_start)
            self.assertEqual(2022, temp_user.year_end)

    def remove_user(self, dbo):
        """
        Test remove_user, CRUD method
        :param dbObject dbo: dbo
        :return:
        """
        self.reset(dbo)
        with orm.db_session:
            # 1. find user from db
            temp_user, _ = User.find_user_by_id(self.user.id)

            # 2. remove
            User.remove_user_by_id(temp_user.id)

            # 3. re-get
            temp_user, err = User.find_user_by_id(self.user.id)

            # 4. assert
            self.assertEqual(temp_user, None)
            self.assertEqual("User Not Found !", err)

    def main(self):
        self.create_user(db)
        self.find_user(db)
        self.update_user(db)
        self.remove_user(db)
