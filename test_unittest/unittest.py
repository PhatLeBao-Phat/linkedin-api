# math_utils.py

def add(a, b):
    return a + b


# test_math_utils.py


def test_add_positive_numbers():
    assert add(3, 4) == 7  # Test with positive numbers

def test_add_negative_numbers():
    assert add(-1, -1) == -2  # Test with negative numbers


