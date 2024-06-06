import allure
import requests
from tests.data import USER, URL, DUPLICATE_USER, USER_WITHOUT_EMAIL, MESSAGE_CHECK_CREATE_DUPLICATE, \
    MESSAGE_CHECK_CREATE_USER_EMPTY


class CreateUser:

    def __init__(self):
        self.response = None

    @allure.step('Создание пользователя, который уже зарегистрирован')
    def create_user_duplicate(self):
        payload = DUPLICATE_USER
        self.response = requests.post(URL + USER, json=payload)
        return self.response

    @allure.step('Создание пользователя без "email"')
    def create_user_without_email(self):
        payload = USER_WITHOUT_EMAIL
        self.response = requests.post(URL + USER, json=payload)
        return self.response

    @allure.step('Проверка тела ответа после создания пользователя, который уже зарегистрирован')
    def check_create_user_duplicate(self):
        response_body = self.response.json()
        assert response_body == MESSAGE_CHECK_CREATE_DUPLICATE

    @allure.step('Проверка тела ответа после создания пользователя без "email"')
    def check_create_user_without_email(self):
        response_body = self.response.json()
        assert response_body == MESSAGE_CHECK_CREATE_USER_EMPTY
