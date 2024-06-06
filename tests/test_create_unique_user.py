import allure


class TestCreateUser:

    @allure.title('Создание нового пользователя через фикстуру')
    def test_create_unique_user(self, create_user):
        response, _ = create_user
        assert response.status_code == 200
        response_body = response.json()
        assert response_body['success'] is True
