import allure

from endpoints.user_login_objects import UserLogin


class TestAuthorization:

    @allure.title('Авторизация существующего пользователя')
    def test_authorization_valid_user(self, user_auth_data):
        user_login = UserLogin()
        response = user_login.authorization_valid_user(user_auth_data)
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Авторизация с неверным логином и паролем')
    def test_authorization_invalid_username_and_password(self):
        authorization_invalid_username_and_password = UserLogin()
        response = authorization_invalid_username_and_password.authorization_invalid_username_and_password()
        assert response.status_code == 401
        assert response.json()['success'] is False
