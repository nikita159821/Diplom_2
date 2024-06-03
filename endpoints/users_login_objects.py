from endpoints.create_user_objects import CreateUser
import allure
import requests

from tests.data import URL, USER_LOGIN, LOGIN_AND_PASSWORD_INVALID, MESSAGE_LOGIN_AND_PASSWORD_INVALID


class UserLogin(CreateUser):
    def __init__(self):
        super().__init__()
        self.user_data = None
        self.response = None
        self.email = None
        self.password = None
        self.access_token = None

    @allure.step('Авторизация под существующим пользователем')
    def users_login(self, create_and_delete_user):
        self.response = create_and_delete_user.response
        self.email = self.response.json()['user']['email']
        self.password = create_and_delete_user.user_data['password']
        self.access_token = self.response.json()['accessToken'].split(' ')
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
    def check_users_login_response_body(self, create_and_delete_user):
        response_body = create_and_delete_user.response.json()
        assert response_body['success'] == True

    @allure.step('Авторизация с неверным логином и паролем')
    def login_with_invalid(self):
        payload = LOGIN_AND_PASSWORD_INVALID
        self.response = requests.post(f'{URL}{USER_LOGIN}', json=payload)

    @allure.step('Проверка тела ответа после авторизации с неверным логином и паролем')
    def check_login_with_invalid_response_body(self):
        response_body = self.response.json()
        assert response_body == MESSAGE_LOGIN_AND_PASSWORD_INVALID
        assert self.response.status_code == 401
