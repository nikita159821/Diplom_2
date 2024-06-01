import allure

from endpoints.create_user_objects import CreateUser


class TestCreateUserWithMissingRequiredField:
    @allure.title("Тест создания пользователя с незаполненным обязательным полем")
    def test_create_user_with_missing_required_field(self):
        create_user_field = CreateUser()
        create_user_field.create_user_empty_payload()
        create_user_field.check_response_is_403()
        create_user_field.check_create_courier_empty_payload()