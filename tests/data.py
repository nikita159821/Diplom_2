URL = ' https://stellarburgers.nomoreparties.site/api/'
USER = 'auth/register'
USER_DELETE = 'auth/user'
USER_LOGIN = 'auth/login'

MESSAGE_CHECK_CREATE_DUPLICATE = {
    "success": False,
    "message": "User already exists"
}

MESSAGE_CHECK_CREATE_USER_EMPTY = {
    "success": False,
    "message": "Email, password and name are required fields"
}

TEST = {
    "success": True,
    "accessToken": "",
    "refreshToken": ""
}

LOGIN_AND_PASSWORD_INVALID = {
    "email": "test",
    "password": "test"
}

MESSAGE_LOGIN_AND_PASSWORD_INVALID = {
    "success": False,
    "message": "email or password are incorrect"
}
