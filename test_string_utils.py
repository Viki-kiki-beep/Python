# test_string_utils.py
import pytest
from string_utils import StringUtils

# Инициализируем экземпляр класса для тестирования
utils = StringUtils()

class TestStringUtils:
    
    # Тесты для capitilize
    def test_capitilize_positive(self):
        """Позитивные тесты для capitilize"""
        assert utils.capitilize("skypro") == "Skypro"
        assert utils.capitilize("hello world") == "Hello world"
        assert utils.capitilize("123abc") == "123abc"
    
    def test_capitilize_negative(self):
        """Негативные тесты для capitilize"""
        assert utils.capitilize("") == ""
        assert utils.capitilize(" ") == " "
        assert utils.capitilize(None) is None
    
    # Тесты для trim
    def test_trim_positive(self):
        """Позитивные тесты для trim"""
        assert utils.trim("   skypro") == "skypro"
        assert utils.trim("  hello world  ") == "hello world  "
        assert utils.trim("test") == "test"
    
    def test_trim_negative(self):
        """Негативные тесты для trim"""
        assert utils.trim("") == ""
        assert utils.trim(" ") == ""
        assert utils.trim(None) is None
    
    # Тесты для contains
    def test_contains_positive(self):
        """Позитивные тесты для contains"""
        assert utils.contains("SkyPro", "S") is True
        assert utils.contains("SkyPro", "Pro") is True
        assert utils.contains("Hello World", " ") is True
    
    def test_contains_negative(self):
        """Негативные тесты для contains"""
        assert utils.contains("SkyPro", "U") is False
        assert utils.contains("", "a") is False
        assert utils.contains(" ", "a") is False
        assert utils.contains(None, "a") is False
        assert utils.contains("test", None) is False
        assert utils.contains(None, None) is False
    
    # Тесты для delete_symbol
    def test_delete_symbol_positive(self):
        """Позитивные тесты для delete_symbol"""
        assert utils.delete_symbol("SkyPro", "k") == "SyPro"
        assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
        assert utils.delete_symbol("Hello World", " ") == "HelloWorld"
    
    def test_delete_symbol_negative(self):
        """Негативные тесты для delete_symbol"""
        assert utils.delete_symbol("", "a") == ""
        assert utils.delete_symbol("test", "x") == "test"
        assert utils.delete_symbol(None, "a") is None
        assert utils.delete_symbol("test", None) == "test"
    
    # Тесты для starts_with
    def test_starts_with_positive(self):
        """Позитивные тесты для starts_with"""
        assert utils.starts_with("SkyPro", "S") is True
        assert utils.starts_with("123abc", "123") is True
        assert utils.starts_with(" Hello", " ") is True
    
    def test_starts_with_negative(self):
        """Негативные тесты для starts_with"""
        assert utils.starts_with("SkyPro", "P") is False
        assert utils.starts_with("", "a") is False
        assert utils.starts_with(None, "a") is False
        assert utils.starts_with("test", None) is False
    
    # Тесты для end_with
    def test_end_with_positive(self):
        """Позитивные тесты для end_with"""
        assert utils.end_with("SkyPro", "o") is True
        assert utils.end_with("abc123", "123") is True
        assert utils.end_with("Hello ", " ") is True
    
    def test_end_with_negative(self):
        """Негативные тесты для end_with"""
        assert utils.end_with("SkyPro", "y") is False
        assert utils.end_with("", "a") is False
        assert utils.end_with(None, "a") is False
        assert utils.end_with("test", None) is False
    
    # Тесты для is_empty
    def test_is_empty_positive(self):
        """Позитивные тесты для is_empty"""
        assert utils.is_empty("") is True
        assert utils.is_empty(" ") is True
        assert utils.is_empty("  ") is True
    
    def test_is_empty_negative(self):
        """Негативные тесты для is_empty"""
        assert utils.is_empty("SkyPro") is False
        assert utils.is_empty("  test  ") is False
        assert utils.is_empty("123") is False
        assert utils.is_empty(None) is True
    
    # Тесты для list_to_string
    def test_list_to_string_positive(self):
        """Позитивные тесты для list_to_string"""
        assert utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
        assert utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
        assert utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
        assert utils.list_to_string(["a", "b", "c"], "") == "abc"
    
    def test_list_to_string_negative(self):
        """Негативные тесты для list_to_string"""
        assert utils.list_to_string([]) == ""
        assert utils.list_to_string(None) == ""
        assert utils.list_to_string([""]) == ""
        assert utils.list_to_string([" "]) == " "