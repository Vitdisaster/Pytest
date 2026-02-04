

class Response:
    """Проверяет состав ответа"""

    def __init__(self, response):

        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        """Валидирует ответ по схеме"""

        print(f"Валидируем с схемой: {schema.__name__}")

        schema.model_validate(self.response_json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, dict):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self

    def __str__(self):
        return \
            f"\nReceived: {self.response_status} \n" \
            f"Url запроса: {self.response.url} \n" \
            f"Тело ответа: {self.response_json}"