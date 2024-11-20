from src.roman_numbers import convert_to_roman_numeral


def test_returns_correct_numeral_for_single_digit():
    assert convert_to_roman_numeral(1) == "I"
    assert convert_to_roman_numeral(5) == "V"
    assert convert_to_roman_numeral(10) == "X"


def test_returns_correct_numeral_for_digit_combinations():
    assert convert_to_roman_numeral(11) == "XI"
    assert convert_to_roman_numeral(2) == "II"
    assert convert_to_roman_numeral(7) == "VII"


def test_returns_correct_numeral_for_substructive_notations():
    assert convert_to_roman_numeral(4) == "IV"
    assert convert_to_roman_numeral(9) == "IX"


def test_returns_correct_numeral_for_tens_hundreds_thousands():
    assert convert_to_roman_numeral(20) == "XX"
    assert convert_to_roman_numeral(40) == "XL"
    assert convert_to_roman_numeral(53) == "LIII"
    assert convert_to_roman_numeral(225) == "CCXXV"
    assert convert_to_roman_numeral(499) == "CDXCIX"
    assert convert_to_roman_numeral(2038) == "MMXXXVIII"
