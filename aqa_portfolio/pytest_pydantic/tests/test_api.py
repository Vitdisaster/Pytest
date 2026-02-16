"""Проверки для запроса SECOND_URL"""
import pytest
import requests

#from configuration import SECOND_URL
from aqa_portfolio.pytest_pydantic.src.base_classes.response import Response

from aqa_portfolio.pytest_pydantic.src.schemas.post import UsersListResponse

SECOND_URL = "https://gorest.co.in/public/v1/users"

@pytest.mark.vshishov  #TODO: настроить конфиг запуска
def test_get():
    """Проверяет ответ метода: код ответа и значения id"""
    r = requests.get(url=SECOND_URL)
    response = Response(r)
    response.assert_status_code(300).validate(UsersListResponse)

