import pytest

@pytest.fixture
def number_list_1_6():
    return [1,2,3,4,5,6]

@pytest.fixture
def number_list_with_triple_1():
    return [1,2,1,4,1,6]

@pytest.fixture
def number_list_without_1():
    return [9,2,5,4,0,6]

@pytest.fixture
def empty_list():
    return []

@pytest.fixture
def list_with_one_element():
    return [1]
