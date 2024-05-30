import random
import string
import allure
import requests

from tests.data import USER, URL, USER_DELETE
from endpoints.base_response_checker import ResponseChecker


class CreateUser(ResponseChecker):
    def __init__(self):
        self.payload = None
        self.access_token = None

    @allure.step('Генерация случайных данных для пользователя')
    def generate_user_data(self):
        email = f"test-data-{random.randint(1, 10000)}@yandex.ru"
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        name = f"TestUser{random.randint(1, 100)}"
        return {'email': email, 'password': password, 'name': name}

    @allure.step('Создание нового пользователя')
    def create_user(self):
        self.payload = self.generate_user_data()
        self.response = requests.post(f'{URL}{USER}', json=self.payload)
        return self.response

    @allure.step('Удаление пользователя')
    def delete_user(self):
        self.access_token = self.response.json()['accessToken'].split(' ')[1]
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        self.response = requests.delete(f'{URL}{USER_DELETE}', headers=headers)

    @allure.step('Проверка тела ответа после создания нового пользователя')
    def check_create_user_response_body(self):
        response_body = self.response.json()
        expected_user_data = {
            'email': self.payload['email'],
            'name': self.payload['name']
        }
        assert response_body['user'] == expected_user_data
