import pytest
import sys


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-5, 6, 1),
    (0, 0, 0)
])
def test_addition(a, b, expected):
    """ Тест проверяет сложение a и b """
    assert a + b == expected

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, -1),
    (-5, 6, -11),
    (1, 1, 0)
])
def test_substraction(a, b, expected):
    """ Тест проверяет вычитание b из a """
    assert a - b == expected

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (5, 0, 0),
    (-1, -2, 2)
])
def test_multiplication(a, b, expected):
    """ Тест проверяет умножение a на b """
    assert a * b == expected

@pytest.mark.parametrize("a,b,expected", [
    (6, 3, 2),
    (5, 1, 5),
    (11, 11, 1)
])
def test_division(a, b, expected):
    """ Тест проверяет деление a на b """
    assert a / b == expected


@pytest.mark.xfail(reason="Нужно исследовать", run=True)
@pytest.mark.parametrize("a,b,expected", [
    (6, 3, 2),
    (5, 0, 0),
    (11, 11, 1)
])
def test_expon(a, b, expected):
    """ Тест для примера ожидаемого падения и не запуска """
    assert a ** b == expected


@pytest.mark.skipif(sys.version_info < (3, 5), reason="выполняется только на python 3.6 или выше")
def test_expon(a, b):
    """ Тест проверяет что-то для примера скипа по условию """
    assert a == b


@pytest.mark.skip_flaky
def test_expon(a, b, c):
    """ Тест проверяет что-то для примера флаки """
    assert a ** b / c == 21

@pytest.mark.xfail(reason="баг", run=False)
@pytest.mark.bug('TFS-001003')
def test_expon(a, b, c):
    """ Тест проверяет что-то для примера бага """
    assert a % b * c == 8