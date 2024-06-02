from endpoints.сreating_order_objects import CreatingOrder


class TestCreateOrderWithAuthorization:

    def test_create_order_with_auth(self):
        create_order_with_auth = CreatingOrder()
        create_order_with_auth.create_order_with_auth()
        create_order_with_auth.check_response_is_200()
        create_order_with_auth.check_create_order_response_body()