import allure

from endpoints.changing_user_data_objects import ChangingUser


class TestUpdateUserEmailWithoutAuth:

    @allure.title('Изменение email пользователя без авторизации')
    def test_update_user_email_without_auth(self):
        update_user_email_without_auth = ChangingUser()
        response = update_user_email_without_auth.update_user_email_without_auth()
        assert response.status_code == 401
        assert response.json()['success'] is False
