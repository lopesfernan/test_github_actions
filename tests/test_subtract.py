from main import subtract


def test_subtract():
    result = subtract(10, 5)
    assert result == 5, "Subtraction function failed"
