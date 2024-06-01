class ResponseChecker:
    response = None

    def check_response_is_200(self):
        assert self.response.status_code == 200

    def check_response_is_403(self):
        assert self.response.status_code == 403