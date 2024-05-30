import allure
from endpoints.create_user_objects import CreateUser

class TestCreateUser:
    @allure.title("Тест успешного создания нового уникального пользователя")
    def test_create_unique_user(self):
        create_unique_user = CreateUser()
        email, password, access_token = create_unique_user.create_user()
        response = create_unique_user.create_user()
        assert response.status_code == 200
        assert email in response.json()['user']['email']
        assert password in response.json()['user']['name']
        assert access_token

