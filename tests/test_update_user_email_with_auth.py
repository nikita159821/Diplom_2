from endpoints.changing_user_data_objects import ChangingUser


class TestUpdateUserEmail:
    def test_update_user_email_with_auth(self):
        update_user_email = ChangingUser()
        update_user_email.update_user_email_with_auth()
        update_user_email.check_response_is_200()
        update_user_email.check_update_user_email_with_auth_response_body()
