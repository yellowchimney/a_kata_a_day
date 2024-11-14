from src.square_digits import square_digits

class TestSquareDigits:
    def test_returns_integer(self):
        result = square_digits(1)
        assert isinstance(result, int)

    def test_returns_single_digit_squared(self):
        result = square_digits(2)
        assert result == 4

        result = square_digits(3)
        assert result == 9

        result = square_digits(4)
        assert result == 16

    def test_returns_multiple_digits_squared(self):
        result = square_digits(22)
        assert result == 44

        result = square_digits(9119)
        assert result == 811181

        result = square_digits(347)
        assert result == 91649