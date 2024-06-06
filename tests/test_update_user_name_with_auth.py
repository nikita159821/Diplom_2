import allure

from endpoints.changing_user_data_objects import ChangingUser


class TestUpdateUserEmail:

    @allure.title('Изменение name пользователя с авторизацией')
    def test_update_user_name_with_auth(self, user_auth_data):
        changing_user = ChangingUser()
        response = changing_user.update_user_email(user_auth_data)
        assert response.status_code == 200
        assert response.json()['success'] is True


