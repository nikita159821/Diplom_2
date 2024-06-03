import allure

from endpoints.changing_user_data_objects import ChangingUser


class TestUpdateUserEmail:

    @allure.title('Изменение email пользователя с авторизацией')
    def test_update_user_email_with_auth(self, create_and_delete_user):
        update_user_email = ChangingUser(create_and_delete_user)
        update_user_email.update_user_email()
        update_user_email.check_response_is_200()
        update_user_email.check_update_user_email_with_auth_response_body()
