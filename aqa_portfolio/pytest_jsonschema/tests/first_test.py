"""Проверки для запроса FIRST_URL"""
import pytest

from aqa_portfolio.pytest_jsonschema.src.base_classes.response import Response
from aqa_portfolio.pytest_jsonschema.src.schemas.post import POST_SCHEMA


def test_get_200_ok(get_response):
    """Проверяет код ответа 200"""

    Response(get_response).assert_status_code(200).validate(POST_SCHEMA)


@pytest.mark.vshishov
def test_get_300(get_response):
    """Проверяет код ответа 300 и падает, т.к. не получает 200"""

    Response(get_response).assert_status_code(300).validate(POST_SCHEMA)