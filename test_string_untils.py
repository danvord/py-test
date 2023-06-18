import pytest
from string_utils import StringUtils

class TestStringUtils:

    def setup_method(self):
        self.s = StringUtils()

    # Positive test
    @pytest.mark.parametrize("input_string, expected_output", [
        ("skypro", "Skypro"),
        ("SkyPro", "Skypro"),
        ("", "")
    ])
    def test_capitalize_positive(self, input_string, expected_output):
        assert self.s.capitilize(input_string) == expected_output

    @pytest.mark.parametrize("input_string, expected_output", [
        ("   skypro", "skypro"),
        ("skypro   ", "skypro   "),
        (" sky pro ", "sky pro "),
        ("", "")
    ])
    def test_trim_positive(self, input_string, expected_output):
        assert self.s.trim(input_string) == expected_output

    @pytest.mark.parametrize("input_string, delimiter, expected_output", [
        ("a,b,c,d", ",", ["a", "b", "c", "d"]),
        ("1:2:3", ":", ["1", "2", "3"]),
        ("", ",", [])
    ])
    def test_to_list_positive(self, input_string, delimiter, expected_output):
        assert self.s.to_list(input_string, delimiter) == expected_output

    @pytest.mark.parametrize("input_string, symbol, expected_output", [
        ("SkyPro", "S", True),
        ("SkyPro", "U", False),
        ("", "S", False)
    ])
    def test_contains_positive(self, input_string, symbol, expected_output):
        assert self.s.contains(input_string, symbol) == expected_output

    @pytest.mark.parametrize("input_string, symbol, expected_output", [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("", "k", "")
    ])
    def test_delete_symbol_positive(self, input_string, symbol, expected_output):
        assert self.s.delete_symbol(input_string, symbol) == expected_output

    @pytest.mark.parametrize("input_string, symbol, expected_output", [
        ("SkyPro", "S", True),
        ("SkyPro", "P", False),
        ("", "S", False)
    ])
    def test_starts_with_positive(self, input_string, symbol, expected_output):
        assert self.s.starts_with(input_string, symbol) == expected_output

    # Negative test
    def test_capitalize_wrong_input_type(self):
        with pytest.raises(TypeError):
            self.s.capitilize(123)

    def test_trim_wrong_input_type(self):
        with pytest.raises(TypeError):
            self.s.trim(123)

    def test_to_list_wrong_input_type(self):
        with pytest.raises(TypeError):
            self.s.to_list(123, ",")

    def test_contains_wrong_input_type(self):
        with pytest.raises(TypeError):
            self.s.contains("SkyPro", 123)

    def test_delete_symbol_wrong_input_type(self):
        with pytest.raises(TypeError):
            self.s.delete_symbol("SkyPro", 123)

    def test_starts_with_wrong_input_type(self):
        with pytest.raises(TypeError):
            self.s.starts_with("SkyPro", 123)

    def test_to_list_invalid_delimiter(self):
        with pytest.raises(ValueError):
            self.s.to_list("a,b,c,d", "")

    def test_contains_symbol_not_in_string(self):
        assert self.s.contains("SkyPro", "Z") == False

    def test_to_list_empty_string(self):
        assert self.s.to_list("", ",") == []

    def test_delete_symbol_not_in_string(self):
        assert self.s.delete_symbol("SkyPro", "Z") == "SkyPro"

    def test_starts_with_empty_string(self):
        assert self.s.starts_with("", "S") == False

    def test_to_list_wrong_delimiter(self):
        with pytest.raises(ValueError):
            self.s.to_list("a,b,c,d", "")