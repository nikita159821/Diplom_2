from endpoints.сreating_order_objects import CreatingOrder


class TestCreateOrderWithoutIngredients:

    def test_create_order_with_missing_ingredient_ids(self):
        create_order_with_missing_ingredient_ids = CreatingOrder()
        create_order_with_missing_ingredient_ids.create_order_without_ingredients()
        create_order_with_missing_ingredient_ids.check_create_order_with_missing_ingredient_ids()