import allure

from endpoints.changing_user_data_objects import ChangingUser


class TestUpdateUserEmail:

    @allure.title('Изменение name пользователя с авторизацией')
    def test_update_user_name_with_auth(self, create_and_delete_user):
        update_user_name = ChangingUser(create_and_delete_user)
        update_user_name.update_user_name_with_auth()
        update_user_name.check_response_is_200()
        update_user_name.check_update_user_name_with_auth_response_body()
