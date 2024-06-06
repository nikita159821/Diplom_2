import allure
import requests

from tests.data import URL, USER_LOGIN, LOGIN_AND_PASSWORD_INVALID, MESSAGE_LOGIN_AND_PASSWORD_INVALID


class UserLogin:
    def __init__(self):
        self.response = None

    @allure.step('Авторизация существующего пользователя')
    def authorization_valid_user(self, user_auth_data):
        payload = {
            'email': user_auth_data['email'],
            'password': user_auth_data['password']
        }
        headers = {
            'Authorization': user_auth_data["access_token"]
        }
        self.response = requests.post(URL + USER_LOGIN, headers=headers, json=payload)
        return self.response

    @allure.step('Авторизация с неверным логином и паролем')
    def authorization_invalid_username_and_password(self):
        payload = LOGIN_AND_PASSWORD_INVALID
        self.response = requests.post(URL + USER_LOGIN, json=payload)
        return self.response


    @allure.step('Проверка тела ответа после авторизации с неверным логином и паролем')
    def check_response_body_authorization_invalid_username_and_password(self):
        response_body = self.response.json()
        assert response_body == MESSAGE_LOGIN_AND_PASSWORD_INVALID

