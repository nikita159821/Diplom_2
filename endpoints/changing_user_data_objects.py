import allure
import requests
from endpoints.user_login_objects import UserLogin
from tests.data import URL, NEW_EMAIL, MESSAGE_UNAUTHORIZED, NEW_NAME, UPDATE_USER


class ChangingUser(UserLogin):

    @allure.step('Изменение email пользователя с авторизацией')
    def update_user_email(self, user_auth_data):
        payload = {'email': NEW_EMAIL}
        headers = {
            'Authorization': user_auth_data["access_token"]
        }
        self.response = requests.patch(URL + UPDATE_USER, json=payload, headers=headers)
        return self.response

    @allure.step('Изменение email пользователя без авторизации')
    def update_user_email_without_auth(self):
        payload = {'email': NEW_EMAIL}
        self.response = requests.patch(URL + UPDATE_USER, json=payload)
        return self.response

    @allure.step('Изменение имени пользователя с авторизацией')
    def update_user_name_with_auth(self,user_auth_data):
        payload = {'name': NEW_NAME}
        headers = {
            'Authorization': user_auth_data["access_token"]
        }
        self.response = requests.patch(URL + UPDATE_USER, json=payload, headers=headers)
        return self.response

    @allure.step('Изменение имени пользователя без авторизации')
    def update_user_name_without_auth(self):
        payload = {'name': NEW_NAME}
        self.response = requests.patch(URL + UPDATE_USER, json=payload)
        return self.response

    @allure.step('Проверка тела ответа, после изменения данных пользователя без авторизации')
    def check_update_user_without_auth_response_body(self):
        response_body = self.response.json()
        assert response_body == MESSAGE_UNAUTHORIZED
