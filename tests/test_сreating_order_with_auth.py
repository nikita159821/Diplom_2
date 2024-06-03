import allure

from endpoints.сreating_order_objects import CreatingOrder


class TestCreateOrderWithAuthorization:

    @allure.title('Создание заказа с авторизацией')
    def test_create_order_with_auth(self, create_and_delete_user):
        create_order_with_auth = CreatingOrder(create_and_delete_user)
        create_order_with_auth.create_order_with_auth()
        create_order_with_auth.check_response_is_200()
        create_order_with_auth.check_create_order_response_body()