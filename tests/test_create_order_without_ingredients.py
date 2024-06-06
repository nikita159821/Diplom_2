import allure
from endpoints.сreating_order_objects import CreatingOrder


class TestCreateOrderWithoutIngredients:

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self, user_auth_data):
        creating_order = CreatingOrder()
        response = creating_order.create_order_without_ingredients(user_auth_data)
        assert response.status_code == 400
        creating_order.check_create_order_with_missing_ingredient_ids()
