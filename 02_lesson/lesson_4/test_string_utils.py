from string_utils import StringUtils

# Инициализация объекта класса StringUtils
string_utils = StringUtils()


def test_capitalize():
    # positive
    assert string_utils.capitalize("skypro") == "Skypro"
    assert string_utils.capitalize("тест") == "Тест"
    assert string_utils.capitalize("123abc") == "123abc"

    # negative
    assert string_utils.capitalize("") == ""
    assert string_utils.capitalize(" ") == " "
    assert string_utils.capitalize(None) is None  # Исправлено


def test_trim():
    # positive
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("тест   ") == "тест"
    assert string_utils.trim("   123   ") == "123"

    # negative
    assert string_utils.trim("") == ""
    assert string_utils.trim(" ") == ""
    assert string_utils.trim(None) is None  # Исправлено


def test_contains():
    # positive
    assert string_utils.contains("SkyPro", "S") is True
    assert string_utils.contains("тест", "т") is True
    assert string_utils.contains("123", "1") is True

    # negative
    assert string_utils.contains("SkyPro", "U") is False
    assert string_utils.contains("", "a") is False
    assert string_utils.contains(" ", "a") is False
    assert string_utils.contains(None, "a") is False


def test_delete_symbol():
    # positive
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("тест", "т") == "ес"
    assert string_utils.delete_symbol("123456", "4") == "12356"

    # negative
    assert string_utils.delete_symbol("", "a") == ""
    assert string_utils.delete_symbol(" ", "a") == " "
    assert string_utils.delete_symbol("тест", "x") == "тест"
    assert string_utils.delete_symbol(None, "a") is None
    