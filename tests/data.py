URL = 'https://stellarburgers.nomoreparties.site/api/'
USER = 'auth/register'
USER_DELETE = 'auth/user'
CREATE_DUPLICATE_USER = {
    "email": "test-data@yandex.ru",
    "password": "password",
    "name": "Username"
}
MESSAGE_CHECK_CREATE_DUPLICATE = {
    "success": False,
    "message": "User already exists"
}

MESSAGE_CHECK_CREATE_USER_EMPTY = {
    "success": False,
    "message": "Email, password and name are required fields"
}
