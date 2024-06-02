import random
import allure
import requests
from endpoints.users_login_objects import UserLogin


class ChangingUser(UserLogin):
    def __init__(self):
        super().__init__()
        self.new_name = None
        self.new_email = None

    @allure.step('Изменение email пользователя с авторизацией')
    def update_user_email_with_auth(self):
        # Авторизуемся под существующим пользователем
        response = self.users_login()
        self.access_token = response.json()['accessToken'].split(' ')[1]

        # Генерируем новые данные для обновления
        self.new_email = f"new-test-data-{random.randint(1, 10000)}@yandex.ru"

        # Обновляем email пользователя
        headers = {'Authorization': f'Bearer {self.access_token}'}
        payload = {'email': self.new_email}
        self.response = requests.patch('https://stellarburgers.nomoreparties.site/api/auth/user', headers=headers,
                                       json=payload)
        return self.response

    @allure.step('Проверка тела ответа, после изменения email пользователя. С авторизацией')
    def check_update_user_email_with_auth_response_body(self):
        response_body = self.response.json()
        assert response_body['success'] == True
        assert response_body['user']['email'] == self.new_email
        assert response_body['user']['name'] == self.user_data['name']

    @allure.step('Изменение имени пользователя с авторизацией')
    def update_user_name_with_auth(self):
        # Авторизуемся под существующим пользователем
        response = self.users_login()
        self.access_token = response.json()['accessToken'].split(' ')[1]

        # Генерируем новые данные для обновления
        self.new_name = f"New-Test-User-{random.randint(1, 10000)}"

        # Обновляем имя пользователя
        headers = {'Authorization': f'Bearer {self.access_token}'}
        payload = {'name': self.new_name}
        self.response = requests.patch('https://stellarburgers.nomoreparties.site/api/auth/user', headers=headers,
                                       json=payload)
        return self.response

    @allure.step('Проверка тела ответа, после изменения имени пользователя. С авторизацией')
    def check_update_user_name_with_auth_response_body(self):
        response_body = self.response.json()
        assert response_body['success'] == True
        assert response_body['user']['email'] == self.user_data['email']
        assert response_body['user']['name'] == self.new_name
