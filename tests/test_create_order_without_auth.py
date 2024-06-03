import allure

from endpoints.сreating_order_objects import CreatingOrder


class TestCreateOrderWithoutAuthorization:

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_auth(self,create_and_delete_user):
        create_order_without_auth = CreatingOrder(create_and_delete_user)
        create_order_without_auth.create_order_without_auth()
        create_order_without_auth.check_response_is_200()
        create_order_without_auth.check_create_order_response_body()