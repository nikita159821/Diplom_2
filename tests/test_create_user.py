import allure
from endpoints.changing_user_data_objects import ChangingUser
from endpoints.create_user_objects import CreateUser
from tests.data import NEW_EMAIL, NEW_NAME


class TestCreateUser:

    @allure.title('Создание нового пользователя через фикстуру')
    def test_create_unique_user(self, create_user):
        response, _ = create_user
        assert response.status_code == 200
        response_body = response.json()
        assert response_body['success'] is True

    @allure.title('Создание пользователя без "email"')
    def test_create_user_without_email(self):
        create_user_without_email = CreateUser()
        response = create_user_without_email.create_user_without_email()
        assert response.status_code == 403
        create_user_without_email.check_create_user_without_email()

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_user_duplicate(self):
        create_user_duplicate = CreateUser()
        response = create_user_duplicate.create_user_duplicate()
        assert response.status_code == 403
        create_user_duplicate.check_create_user_duplicate()

    @allure.title('Изменение email пользователя с авторизацией')
    def test_update_user_email(self, user_auth_data):
        payload = {'email': NEW_EMAIL}
        changing_user = ChangingUser()
        response = changing_user.update_user_data_with_auth(user_auth_data, payload)
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Изменение email пользователя без авторизации')
    def test_update_user_email_without_auth(self):
        payload = {'email': NEW_EMAIL}
        changing_user = ChangingUser()
        response = changing_user.update_user_data_without_auth(payload)
        assert response.status_code == 401
        assert response.json()['success'] is False

    @allure.title('Изменение имени пользователя с авторизацией')
    def test_update_user_name(self, user_auth_data):
        payload = {'name': NEW_NAME}
        changing_user = ChangingUser()
        response = changing_user.update_user_data_with_auth(user_auth_data, payload)
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Изменение имени пользователя без авторизации')
    def test_update_user_name_without_auth(self):
        payload = {'name': NEW_NAME}
        changing_user = ChangingUser()
        response = changing_user.update_user_data_without_auth(payload)
        assert response.status_code == 401
        assert response.json()['success'] is False
