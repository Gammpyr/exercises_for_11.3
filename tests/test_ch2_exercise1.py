from chapter2_tests.exercise1 import sum_divisible_by_3_or_5


def test_sum_divisible_by_3_or_5():
    test_list = [0, 3, 4, 5, 6, 7, 8, 9]
    assert sum_divisible_by_3_or_5(test_list) == 23

def test_sum_negative_divisible_by_3_or_5():
    test_list = [-3, -4, -5, -6, -7, -8, -9]
    assert sum_divisible_by_3_or_5(test_list) == -23

def test_sum_no_divisible_by_3_or_5():
    test_list = [0, 4, 7, 8]
    assert sum_divisible_by_3_or_5(test_list) == 0

def test_empty_list_sum_divisible_by_3_or_5():
    test_list = []
    assert sum_divisible_by_3_or_5(test_list) == 0

def test_no_list_sum_divisible_by_3_or_5():
    test_list = 10
    assert sum_divisible_by_3_or_5(test_list) == 10
