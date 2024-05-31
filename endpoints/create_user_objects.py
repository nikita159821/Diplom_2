import random
import string
import allure
import requests

from tests.data import USER, URL, USER_DELETE, MESSAGE_CHECK_CREATE_DUPLICATE, MESSAGE_CHECK_CREATE_USER_EMPTY

from endpoints.base_response_checker import ResponseChecker


class CreateUser(ResponseChecker):
    def __init__(self):
        self.user_data = None
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
        self.user_data = self.payload
        return self.response

    @allure.step('Создание уже зарегистрированного пользователя')
    def duplicate_create_user(self):
        self.response = requests.post(f'{URL}{USER}', json=self.user_data)

    @allure.step('создаем пользователя без данных для регистрации')
    def create_user_empty_payload(self):
        self.response = requests.post(f'{URL}{USER}')

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

    @allure.step('Проверка тела ответа после создания существующего курьера')
    def check_create_duplicate_user_is_body(self):
        response_body = self.response.json()
        assert response_body == MESSAGE_CHECK_CREATE_DUPLICATE

    @allure.step('Проверка тело ответа после создания пользователя без данных для регистрации')
    def check_create_courier_empty_payload(self):
        response_body = self.response.json()
        assert response_body == MESSAGE_CHECK_CREATE_USER_EMPTY

