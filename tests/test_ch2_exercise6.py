import pytest

from chapter2_tests.exercise6 import merge_dicts


@pytest.mark.parametrize('dict1, dict2, expected',
                         [({1: 1, 2: 2, 3: 3}, {4: 4, 5: 5, 6: 6}, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}),
                          ({1: 1, 2: 2, 3: 3}, {1: 4, 2: 3, 6: 6}, {1: 4, 2: 3, 3: 3, 6: 6}),
                          ({}, {4: 4, 5: 5, 6: 6}, {4: 4, 5: 5, 6: 6}),
                          ({1: 1, 2: 2, 3: 3}, {}, {1: 1, 2: 2, 3: 3}),
                          ({}, {}, {}),
                          ]
                         )
def test_merge_dict(dict1, dict2, expected):
    assert merge_dicts(dict1, dict2) == expected
