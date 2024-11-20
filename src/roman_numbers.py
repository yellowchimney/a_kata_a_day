"""This function takes an integer and retuns
a string containing Roman numeral that represents that integer.
The conversion is handled by creating a dictionary and
string concatenation"""


def convert_to_roman_numeral(n):
    roman_numbers = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }
    roman_numeral = ""
    for key, value in roman_numbers.items():
        while n >= value:
            roman_numeral += key
            n -= value
    return roman_numeral
