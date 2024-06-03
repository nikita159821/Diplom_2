import allure

from endpoints.сreating_order_objects import CreatingOrder


class TestCreateOrderWithoutIngredients:

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_with_missing_ingredient_ids(self,create_and_delete_user):
        create_order_with_missing_ingredient_ids = CreatingOrder(create_and_delete_user)
        create_order_with_missing_ingredient_ids.create_order_without_ingredients()
        create_order_with_missing_ingredient_ids.check_create_order_with_missing_ingredient_ids()