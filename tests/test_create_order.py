import allure
from endpoints.receiving_user_orders_objects import ReceivingUserOrders
from endpoints.сreating_order_objects import CreatingOrder


class TestCreateOrder:

    @allure.title('Создание заказа с авторизацией')
    def test_create_order_with_auth(self, user_auth_data):
        creating_order = CreatingOrder()
        response = creating_order.create_order_with_auth(user_auth_data)
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_auth(self):
        create_order_without_auth = CreatingOrder()
        response = create_order_without_auth.create_order_without_auth()
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self, user_auth_data):
        creating_order = CreatingOrder()
        response = creating_order.create_order_without_ingredients(user_auth_data)
        assert response.status_code == 400
        creating_order.check_create_order_with_missing_ingredient_ids()

    @allure.title('Создание заказа с неверным хешем')
    def test_create_order_without_with_hash_ingredients(self):
        create_order_without_with_hash_ingredients = CreatingOrder()
        response = create_order_without_with_hash_ingredients.create_order_without_with_hash_ingredients()
        assert response.status_code == 500

    @allure.title('Получение заказов пользователя с авторизацией.')
    def test_receiving_user_orders_with_auth(self, user_auth_data):
        receiving_user_orders = ReceivingUserOrders()
        response = receiving_user_orders.receiving_user_orders_with_auth(user_auth_data)
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Получение заказов пользователя без авторизации.')
    def test_receiving_user_orders_without_auth(self):
        receiving_user_orders = ReceivingUserOrders()
        response = receiving_user_orders.receiving_user_orders_without_auth()
        assert response.status_code == 401
        assert response.json()['success'] is False
