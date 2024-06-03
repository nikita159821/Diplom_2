import allure

from endpoints.users_login_objects import UserLogin


class TestLoginExistingUser:

    @allure.title("логин под существующим пользователем")
    def test_login_existing_user(self, create_and_delete_user):
        login_existing = UserLogin()
        login_existing.users_login(create_and_delete_user)
        login_existing.check_response_is_200()
        login_existing.check_users_login_response_body(create_and_delete_user)
