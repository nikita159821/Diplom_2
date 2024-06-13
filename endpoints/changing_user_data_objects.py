import allure
import requests
from endpoints.user_login_objects import UserLogin
from tests.data import URL, MESSAGE_UNAUTHORIZED, UPDATE_USER


class ChangingUser(UserLogin):

    @allure.step('Изменение данных пользователя с авторизацией')
    def update_user_data_with_auth(self, user_auth_data, payload):
        headers = {
            'Authorization': user_auth_data["access_token"]
        }
        self.response = requests.patch(URL + UPDATE_USER, json=payload, headers=headers)
        return self.response

    @allure.step('Изменение данных пользователя без авторизации')
    def update_user_data_without_auth(self, payload):
        self.response = requests.patch(URL + UPDATE_USER, json=payload)
        return self.response

    @allure.step('Проверка тела ответа, после изменения данных пользователя без авторизации')
    def check_update_user_without_auth_response_body(self):
        response_body = self.response.json()
        assert response_body == MESSAGE_UNAUTHORIZED
