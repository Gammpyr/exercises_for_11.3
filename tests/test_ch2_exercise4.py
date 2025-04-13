import pytest
from chapter2_tests.exercise4 import calculate_area


@pytest.mark.parametrize('shape, sides, expected',
                         [('circle', [3], 28.26),
                          ('triangle', [3, 6], 9),
                          ('square', [4], 16),
                          ('rectangle', [4, 5], 20),
                          ('wtf', [10, 5], None),
                          ]
                         )
def test_calculate_area(shape, sides, expected):
    assert calculate_area(shape, sides) == expected
