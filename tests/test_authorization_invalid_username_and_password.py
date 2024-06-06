from endpoints.user_login_objects import UserLogin


class TestAuthorizationInvalidUsernamePassword:

    def test_authorization_invalid_username_and_password(self):
        authorization_invalid_username_and_password = UserLogin()
        response = authorization_invalid_username_and_password.authorization_invalid_username_and_password()
        assert response.status_code == 401
        assert response.json()['success'] is False
