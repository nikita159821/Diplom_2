import allure
import requests
from endpoints.users_login_objects import UserLogin
from tests.data import URL, INGREDIENTS, ORDER, MESSAGE_MISSING_INGREDIENT_IDS, HASH


class CreatingOrder(UserLogin):

    def __init__(self):
        super().__init__()
        self.ingredient_ids = None

    @allure.step('Получение хеша ингредиентов')
    def get_ingredients(self):
        self.response = requests.get(f'{URL}{INGREDIENTS}')
        ingredients_data = self.response.json()['data']
        ingredient_ids = []
        for item in ingredients_data:
            ingredient_ids.append(item['_id'])
        return ingredient_ids

    @allure.step('Создание заказа с авторизацией')
    def create_order_with_auth(self):
        # Авторизуемся под существующим пользователем
        response = self.users_login()
        self.access_token = response.json()['accessToken'].split(' ')[1]
        self.ingredient_ids = self.get_ingredients()

        # Формируем payload с указанным количеством ингредиентов
        # Можно указать любое количество, начиная с 1 и до общего числа ингредиентов
        # В данном примере используются первые 3 ингредиента
        payload = {
            "ingredients": self.ingredient_ids[:3]
        }
        headers = {'Authorization': f'Bearer {self.access_token}'}
        self.response = requests.post(f'{URL}{ORDER}', headers=headers, json=payload)

    @allure.step('Создание заказа без авторизации')
    def create_order_without_auth(self):
        self.ingredient_ids = self.get_ingredients()

        # Формируем payload с указанным количеством ингредиентов
        # Можно указать любое количество, начиная с 1 и до общего числа ингредиентов
        # В данном примере используются первые 2 ингредиента
        payload = {
            "ingredients": self.ingredient_ids[:2]
        }
        self.response = requests.post(f'{URL}{ORDER}', json=payload)

    @allure.step('Создание заказа без ингредиентов')
    def create_order_without_ingredients(self):
        # Авторизуемся под существующим пользователем
        response = self.users_login()
        self.access_token = response.json()['accessToken'].split(' ')[1]
        headers = {'Authorization': f'Bearer {self.access_token}'}
        self.response = requests.post(f'{URL}{ORDER}', headers=headers)

    @allure.step('Создание заказа с неверным хешем ингредиентов')
    def create_order_without_with_hash_ingredients(self):
        self.ingredient_ids = self.get_ingredients()
        payload = HASH
        self.response = requests.post(f'{URL}{ORDER}', json=payload)

    @allure.step('Проверка ответа после создания заказа')
    def check_create_order_response_body(self):
        response_data = self.response.json()
        assert response_data['success'] == True

    @allure.step('Проверка ответа после создания заказа без ингредиентов')
    def check_create_order_with_missing_ingredient_ids(self):
        response_data = self.response.json()
        assert response_data == MESSAGE_MISSING_INGREDIENT_IDS
        assert self.response.status_code == 400

    @allure.step('Проверка ответа после создания заказа с неверным хешем ингредиентов')
    def check_create_order_without_with_hash_ingredients(self):
        assert self.response.status_code == 500
