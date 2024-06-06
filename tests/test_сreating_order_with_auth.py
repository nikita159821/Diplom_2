import allure
from endpoints.сreating_order_objects import CreatingOrder


class TestCreateOrderWithAuthorization:

    @allure.title('Создание заказа с авторизацией')
    def test_create_order_with_auth(self, user_auth_data):
        creating_order = CreatingOrder()
        response = creating_order.create_order_with_auth(user_auth_data)
        assert response.status_code == 200
        assert response.json()['success'] is True
