from chapter2_tests.exercise3 import count_number_in_list
from tests.conftest import number_list_with_triple_1


def test_count_number_in_list(number_list_with_triple_1):
    assert count_number_in_list(number_list_with_triple_1, 1) == 3

def test_count_number_in_list_with_one_repeat(number_list_1_6):
    assert count_number_in_list(number_list_1_6, 1) == 1

def test_count_number_in_list_without_repeat(number_list_without_1):
    assert count_number_in_list(number_list_without_1, 1) == 0

def test_count_number_in_list_with_one_element(list_with_one_element):
    assert count_number_in_list(list_with_one_element, 1) == 1

def test_count_number_in_list_without_elements(empty_list):
    assert count_number_in_list(empty_list, 1) == 0

