import pytest

#Функция должна выполнять следующую задачу:

#Принимать массив чисел и возвращать новый массив, в котором удалены подряд идущие дубликаты.
#Например: [1, 1, 2, 2, 3] → [1, 2, 3] [0, 0, 1, 1, 0] → [0, 1, 0]
exc = [1, 1, 2, 2, 3, 5, 0, 0, 1, 1, 0, 9, 10]

# text_example:
# []
# [0]
# [0, 0, 0]
# [1, 2, 3, 4, 5]
# [1, 1, 2, 2, 3, 3, 4, 5, 7, 7]

def compress_numbers(numbers):
    """
    Функция получает список и возвращает новый без последовательно идущих дублей

    Пример: [1, 1, 2, 2, 3] → [1, 2, 3]
    """

    if not numbers:
        return []

    if len(numbers) == 1:
        return numbers

    res = []
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1]:
            res.append(numbers[i])
    return res

@pytest.mark.positive
@pytest.mark.parametrize("numbers,expected", [
    ([], []),
    ([0], [0]),
])
def test_pos(numbers, expected):
    assert compress_numbers(numbers) == expected

@pytest.mark.negative
@pytest.mark.parametrize("numbers,expected", [
    ([0, 0, 0], [0]),
    ([1, 1, 2, 2, 3, 3, 4, 5, 7, 7], [1, 2, 3, 4, 5, 7]),
])
def test_neg(numbers, expected):
    assert compress_numbers(numbers) == expected