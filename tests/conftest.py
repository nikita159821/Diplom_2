import allure
import pytest
from endpoints.create_user_objects import CreateUser


@pytest.fixture
@allure.step('Создаем и удаляем пользователя')
def create_and_delete_user():
    create_user = CreateUser()
    create_user.create_user()
    yield create_user
    create_user.delete_user()
