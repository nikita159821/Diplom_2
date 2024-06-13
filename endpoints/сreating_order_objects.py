import allure
import requests
from tests.data import URL, INGREDIENTS, ORDER, HASH, MESSAGE_MISSING_INGREDIENT_IDS


class CreatingOrder:

    def __init__(self):
        self.response = None

    @allure.step('Получение хеша ингредиентов')
    def get_ingredients(self):
        self.response = requests.get(URL + INGREDIENTS)
        ingredients_data = self.response.json()['data']
        ingredient_ids = [item['_id'] for item in ingredients_data]
        return ingredient_ids

    @allure.step('Создание заказа с авторизацией')
    def create_order_with_auth(self, user_auth_data):
        ingredient_ids = self.get_ingredients()

        # Формируем payload с указанным количеством ингредиентов
        payload = {
            "ingredients": ingredient_ids[:3]
        }
        headers = {
            'Authorization': user_auth_data["access_token"]
        }

        response = requests.post(URL + ORDER, headers=headers, json=payload)
        return response

    @allure.step('Создание заказа без авторизации')
    def create_order_without_auth(self):
        ingredient_ids = self.get_ingredients()

        # Формируем payload с указанным количеством ингредиентов
        # Можно указать любое количество, начиная с 1 и до общего числа ингредиентов
        # В данном примере используются первые 2 ингредиента
        payload = {
            "ingredients": ingredient_ids[:2]
        }
        response = requests.post(URL + ORDER, json=payload)
        return response

    @allure.step('Создание заказа без ингредиентов')
    def create_order_without_ingredients(self, user_auth_data):
        headers = {
            'Authorization': user_auth_data["access_token"]
        }
        self.response = requests.post(URL + ORDER, headers=headers)
        return self.response

    @allure.step('Создание заказа с неверным хешем ингредиентов')
    def create_order_without_with_hash_ingredients(self):
        payload = HASH
        response = requests.post(URL + ORDER, json=payload)
        return response

    @allure.step('Проверка ответа после создания заказа без ингредиентов')
    def check_create_order_with_missing_ingredient_ids(self):
        response_data = self.response.json()
        assert response_data == MESSAGE_MISSING_INGREDIENT_IDS

