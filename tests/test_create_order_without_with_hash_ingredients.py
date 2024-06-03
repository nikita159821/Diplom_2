import allure

from endpoints.сreating_order_objects import CreatingOrder


class TestCreateOrderWithoutWithHashIngredients:

    @allure.title('Создание заказа с неверным хешем')
    def test_create_order_without_with_hash_ingredients(self):
        create_order_without_with_hash_ingredients = CreatingOrder()
        create_order_without_with_hash_ingredients.create_order_without_with_hash_ingredients()
        create_order_without_with_hash_ingredients.check_create_order_without_with_hash_ingredients()
