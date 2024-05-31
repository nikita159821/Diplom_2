import allure

from endpoints.create_user_objects import CreateUser


class TestCreateDuplicateUser:
    @allure.title("Тест создания уже зарегистрированного пользователя")
    def test_duplicate_create_user(self):
        duplicate_create_user = CreateUser()
        duplicate_create_user.create_user()
        duplicate_create_user.duplicate_create_user()
        duplicate_create_user.check_response_is_403()
        duplicate_create_user.check_create_duplicate_user_is_body()
