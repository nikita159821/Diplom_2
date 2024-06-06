import allure

from endpoints.receiving_user_orders_objects import ReceivingUserOrders


class TestReceivingUserOrdersWithoutAuth:

    @allure.title('Получение заказов пользователя без авторизации.')
    def test_receiving_user_orders_without_auth(self):
        receiving_user_orders = ReceivingUserOrders()
        response = receiving_user_orders.receiving_user_orders_without_auth()
        assert response.status_code == 401
        assert response.json()['success'] is False
