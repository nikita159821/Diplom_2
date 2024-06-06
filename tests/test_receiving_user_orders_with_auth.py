import allure

from endpoints.receiving_user_orders_objects import ReceivingUserOrders


class TestReceivingUserOrdersWithAuth:

    @allure.title('Получение заказов пользователя с авторизацией.')
    def test_receiving_user_orders_with_auth(self, user_auth_data):
        receiving_user_orders = ReceivingUserOrders()
        response = receiving_user_orders.receiving_user_orders_with_auth(user_auth_data)
        assert response.status_code == 200
        assert response.json()['success'] is True
