import pytest
from endpoints.create_user_objects import CreateUser


@pytest.fixture
def create_and_delete_user():
    user = CreateUser()
    user.create_user()
    yield user
    user.delete_user()
