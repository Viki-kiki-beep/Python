import pytest
from string_utils import StringUtils


string_utils = StringUtils()

@pytest.mark.parametrize("input_str, expected", [
    ("Вероятность", "Вероятность"),
    ("БЕСКОНЕЧНОСТЬ", "БЕСКОНЕЧНОСТЬ"),
    ("восьмое марта", "Восьмое марта"),
    ("i'll be back", "I'll be back")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("123456", "123456"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("   Перекресток", "Перекресток"),
    ("   Снежная королева", "Снежная королева"),
    ("   Butterfly collection   ", "Butterfly collection   ")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.parametrize("input_str, expected", [
    ("   _123abc", "_123abc"),
    ("   ", ""),
    ("   .", ".")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, input_smb, expected", [
    ("Независимость", "Н", True),
    ("Посторонний", "п", False),
    ("history", "b", False)
])
def test_contains_positive(input_str,input_smb, expected):
    assert string_utils.contains(input_str, input_smb) == expected

@pytest.mark.parametrize("input_str, input_smb, expected", [
    ("123abc45", "1", True),
    ("  #  ", "#", True),
    ("ad-cd.", " ", False)
])
def test_contains_negative(input_str, input_smb, expected):
    assert string_utils.contains(input_str, input_smb) == expected


@pytest.mark.parametrize("input_str, input_smb, expected", [
    ("Birthday", "day", "Birth"),
    ("дед Мороз", " Мороз", "дед"),
    ("123abc45", "123", "abc45")
])
def test_delete_symbol_positive(input_str, input_smb, expected):
    assert string_utils.delete_symbol(input_str, input_smb) == expected


@pytest.mark.parametrize("input_str, input_smb, expected", [
    ("Осторожность", "1", "Осторожность"),
    ("     ", " ", ""),
    ("№№№№№", "№", "")
])
def test_delete_symbol_negative(input_str, input_smb, expected):
    assert string_utils.delete_symbol(input_str, input_smb) == expected