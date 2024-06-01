import allure

from endpoints.users_login_objects import UserLogin


class TestLoginExistingUser:
    def test_login_existing_user(self):
        login_existing = UserLogin()
        login_existing.users_login()
        login_existing.check_users_login_response_body()
        login_existing.check_response_is_200()