import requests

from configuration import MAIN_URL

from src.base_classes.print_item_response import Response
from src.schemas.post import POST_SCHEMA


def test_getting_info():
    """Проверяет ответ запроса"""
    r = requests.get(url=MAIN_URL)
    response = Response(r)

    response.assert_status_code(200).validate(POST_SCHEMA)