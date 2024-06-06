import allure

from endpoints.user_login_objects import UserLogin


class TestAuthorizationValidUser:

    @allure.title('Авторизация существующего пользователя')
    def test_authorization_valid_user(self, user_auth_data):
        user_login = UserLogin()
        response = user_login.authorization_valid_user(user_auth_data)
        assert response.status_code == 200
        assert response.json()['success'] is True
