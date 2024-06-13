import allure
import requests
from endpoints.сreating_order_objects import CreatingOrder
from tests.data import URL, ORDER


class ReceivingUserOrders(CreatingOrder):

    @allure.step('Получение заказов пользователя с авторизацией.')
    def receiving_user_orders_with_auth(self, user_auth_data):
        self.create_order_with_auth(user_auth_data)
        headers = {
            'Authorization': user_auth_data["access_token"]
        }
        response = requests.get(URL + ORDER, headers=headers)
        return response

    @allure.step('Получение заказов пользователя без авторизации.')
    def receiving_user_orders_without_auth(self):
        response = requests.get(URL + ORDER)
        return response


