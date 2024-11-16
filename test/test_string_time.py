from src.string_time import make_readable

def test_returns_a_string():
    result = make_readable(1)
    assert isinstance (result, str)

def test_returns_correct_output():
    assert make_readable(1) == "00:00:01"
    assert make_readable(2) == "00:00:02"
    assert make_readable(60) == "00:01:00"
    assert make_readable(120) == "00:02:00"
    assert make_readable(121) == "00:02:01"
    assert make_readable(3661) == "01:01:01"