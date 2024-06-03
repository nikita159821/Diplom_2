import allure

from endpoints.users_login_objects import UserLogin


class TestLoginExistingUser:

    @allure.title("логин с неверным логином и паролем")
    def test_login_with_invalid(self):
        login_with_invalid = UserLogin()
        login_with_invalid.login_with_invalid()
        login_with_invalid.check_login_with_invalid_response_body()
