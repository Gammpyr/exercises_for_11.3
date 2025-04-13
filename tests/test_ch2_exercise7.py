import pytest

from chapter2_tests.exercise7 import multiply_matrix


@pytest.fixture
def matrix1_2x3():
    return [
        [1, 2, 3],
        [4, 5, 6]
    ]


@pytest.fixture
def matrix2_3x2():
    return [
        [7, 8],
        [9, 10],
        [11, 12]
    ]


@pytest.fixture
def matrix3_2x2():
    return [
        [1, 2],
        [3, 4]
    ]


@pytest.fixture
def matrix4_2x2():
    return [
        [5, 6],
        [7, 8]
    ]


@pytest.fixture
def identity_matrix_2x2():
    return [
        [1, 0],
        [0, 1]
    ]


@pytest.fixture
def zero_matrix_2x2():
    return [
        [0, 0],
        [0, 0]
    ]


@pytest.mark.parametrize('matrix1_fixture, matrix2_fixture, expected',
                         [
                             ("matrix1_2x3", "matrix2_3x2", [[58, 64], [139, 154]]),
                             ("matrix3_2x2", "matrix4_2x2", [[19, 22], [43, 50]]),
                             ("matrix3_2x2", "identity_matrix_2x2", [[1, 2], [3, 4]]),
                             ("matrix3_2x2", "zero_matrix_2x2", [[0, 0], [0, 0]]),
                         ]
                         )
def test_multiply_matrix(matrix1_fixture, matrix2_fixture, expected, request):
    matrix1 = request.getfixturevalue(matrix1_fixture)
    matrix2 = request.getfixturevalue(matrix2_fixture)
    assert multiply_matrix(matrix1, matrix2) == expected
