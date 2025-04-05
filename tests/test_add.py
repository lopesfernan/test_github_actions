from main import add_numbers


def test_add_numbers():
    result = add_numbers(5, 7)
    assert result == 12, "Addition function failed"
