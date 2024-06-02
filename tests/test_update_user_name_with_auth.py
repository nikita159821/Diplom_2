from endpoints.changing_user_data_objects import ChangingUser


class TestUpdateUserEmail:
    def test_update_user_name_with_auth(self):
        update_user_name = ChangingUser()
        update_user_name.update_user_name_with_auth()
        update_user_name.check_response_is_200()
        update_user_name.check_update_user_name_with_auth_response_body()
