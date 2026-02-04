"""Проверки для запроса SECOND_URL"""

import requests

from configuration import SECOND_URL
from pytest_pydantic.src.base_classes.response import Response

from pytest_pydantic.src.schemas.post import UsersListResponse


def test_get():
    """Проверяет ответ метода"""
    r = requests.get(url=SECOND_URL)
    response = Response(r)
    response.assert_status_code(200).validate(UsersListResponse)

