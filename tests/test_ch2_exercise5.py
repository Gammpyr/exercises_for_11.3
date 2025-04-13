import pytest

from chapter2_tests.exercise5 import my_slice


@pytest.mark.parametrize(
    "coll, start, end, expected",
    [
        ([], 0, None, []),  # Пустой список
        ([1, 2, 3, 4, 5], 0, None, [1, 2, 3, 4, 5]),  # Все элементы
        ([1, 2, 3, 4, 5], 2, None, [3, 4, 5]),  # Срез с началом
        ([1, 2, 3, 4, 5], 1, 3, [2, 3]),  # Срез с началом и концом
        ([1, 2, 3, 4, 5], -2, None, [4, 5]),  # Срез с отрицательным началом
        ([1, 2, 3, 4, 5], -10, None, [1, 2, 3, 4, 5]),  # Срез с отрицательным началом за пределами длины
        ([1, 2, 3, 4, 5], 0, 3, [1, 2, 3]),  # Срез с концом
        ([1, 2, 3, 4, 5], 1, -1, [2, 3, 4]),  # Срез с отрицательным концом
    ]
)
def test_my_slice(coll, start, end, expected):
    assert my_slice(coll, start, end) == expected
