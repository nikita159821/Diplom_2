from endpoints.create_user_objects import CreateUser
import allure
import requests

from tests.data import URL, USER_LOGIN, TEST, LOGIN_AND_PASSWORD_INVALID, MESSAGE_LOGIN_AND_PASSWORD_INVALID


class UserLogin(CreateUser):
    def __init__(self):
        super().__init__()
        self.user_data = None
        self.response = None
        self.email = None
        self.password = None
        self.access_token = None

    @allure.step('Авторизация под существующим пользователем')
    def users_login(self):
        self.user_data = self.generate_user_data()
        self.response = self.create_user().json()
        self.email = self.response['user']['email']
        self.password = self.user_data['password']
        self.access_token = self.response['accessToken'].split(' ')[1]
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.access_token}"
        }

        data = {
            "email": self.email,
            "password": self.password
        }
        self.response = requests.post(f'{URL}{USER_LOGIN}', headers=headers, json=data)
        return self.response

    @allure.step('Проверка тела ответа после авторизации')
    def check_users_login_response_body(self):
        response_body = self.users_login().json()
        assert response_body['success'] == TEST['success']
        assert 'accessToken' in response_body
        assert 'refreshToken' in response_body
        assert response_body['user']['email'] == self.user_data['email']
        assert response_body['user']['name'] == self.user_data['name']

    @allure.step('Авторизация с неверным логином и паролем')
    def login_with_invalid(self):
        payload = LOGIN_AND_PASSWORD_INVALID
        self.response = requests.post(f'{URL}{USER_LOGIN}', json=payload)
        return self.response.status_code

    @allure.step('Проверка тела ответа после авторизации с неверным логином и паролем')
    def check_login_with_invalid_response_body(self):
        response_body = self.response.json()
        assert response_body == MESSAGE_LOGIN_AND_PASSWORD_INVALID
        assert self.response.status_code == 401

