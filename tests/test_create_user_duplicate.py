from endpoints.create_user_objects import CreateUser


class TestCreateUserDuplicate:

    def test_create_user_duplicate(self):
        create_user_duplicate = CreateUser()
        response = create_user_duplicate.create_user_duplicate()
        assert response.status_code == 403
        create_user_duplicate.check_create_user_duplicate()
