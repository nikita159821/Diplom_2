import allure

from endpoints.changing_user_data_objects import ChangingUser


class TestUpdateUserEmailWithoutAuth:

    @allure.title('Изменение name пользователя без авторизации')
    def test_update_user_name_without_auth(self):
        user_name_without_auth = ChangingUser()
        response = user_name_without_auth.update_user_name_without_auth()
        assert response.status_code == 401
        assert response.json()['success'] is False
