from endpoints.create_user_objects import CreateUser


class TestCreateUserWithoutEmail:

    def test_create_user_without_email(self):
        create_user_without_email = CreateUser()
        response = create_user_without_email.create_user_without_email()
        assert response.status_code == 403
        create_user_without_email.check_create_user_without_email()
