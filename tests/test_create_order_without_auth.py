import allure

from endpoints.сreating_order_objects import CreatingOrder


class TestCreateOrderWithoutAuthorization:

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_auth(self):
        create_order_without_auth = CreatingOrder()
        response = create_order_without_auth.create_order_without_auth()
        assert response.status_code == 200
        assert response.json()['success'] is True
