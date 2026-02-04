import pytest
import requests

from configuration import FIRST_URL


@pytest.fixture(scope='function', autouse=False)
def get_response():
    response = requests.get(url=FIRST_URL)
    return response