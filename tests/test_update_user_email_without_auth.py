import allure

from endpoints.changing_user_data_objects import ChangingUser


class TestUpdateUserEmailWithoutAuth:

    @allure.title('Изменение email пользователя без авторизации')
    def test_update_user_email_without_auth(self):
        update_user_email_without_auth = ChangingUser()
        update_user_email_without_auth.update_user_email_without_auth()
        update_user_email_without_auth.check_response_is_401()
        update_user_email_without_auth.check_update_user_without_auth_response_body()