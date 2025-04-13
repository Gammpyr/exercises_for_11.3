import pytest

from chapter2_tests.exercise8 import is_anagram

@pytest.mark.parametrize(
    "str1, str2, expected",
    [
        ("listen", "silent", True),
        ("anagram", "nagaram", True),
        ("rail safety", "fairy tales", True),
        ("A gentleman", "Elegant man", True),
        ("hello", "world", False),
        ("python", "java", False),
        ("test", "best", False),
        ("anagram", "manga", False),
        ("Listen", "Silent", True),
        ("Dormitory", "Dirty room", True),
        ("The eyes", "They see", True),
        ("School master", "The classroom", True),
    ]
)
def test_is_anagram(str1, str2, expected):
    assert is_anagram(str1, str2) == expected