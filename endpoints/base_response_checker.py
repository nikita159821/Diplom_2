class ResponseChecker:
    response = None

    def check_response_is_200(self):
        assert self.response.status_code == 200
