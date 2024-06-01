import allure


class TestCreateUser:
    @allure.title("Тест успешного создания нового пользователя")
    def test_create_unique_user(self, create_and_delete_user):
        create_user = next(create_and_delete_user)
        create_user.check_response_is_200()
        create_user.check_create_user_response_body()