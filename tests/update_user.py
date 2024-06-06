import random

import allure


@allure.step('Генерируем новые данные для обновления')
def update_data():
    f"new-test-data-{random.randint(1, 10000)}@yandex.ru"
