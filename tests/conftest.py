import pytest
import requests
from tests.data import URL, USER, USER_DELETE
from tests.generate_user_data import generate_user_data


@pytest.fixture(scope="function")
def create_user():
    """
    Фикстура для создания и удаления пользователя в тестах.
    """
    payload = generate_user_data()
    response = requests.post(URL + USER, json=payload)
    yield response, payload
    access_token = response.json()['accessToken']
    requests.delete(URL + USER_DELETE, headers={'Authorization': access_token})


@pytest.fixture(scope="function")
def user_auth_data(create_user):
    """
    Фикстура получения данных для авторизации пользователя.
    """
    response, payload = create_user
    user_data = {
        'email': payload['email'],
        'password': payload['password'],
        'access_token': response.json()['accessToken']
    }
    yield user_data

