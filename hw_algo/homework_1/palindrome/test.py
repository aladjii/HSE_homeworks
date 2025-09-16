from palindrome import is_palindrome

def test_single_digit() -> None:
    assert is_palindrome(0)
    assert is_palindrome(7)

def test_two_digits() -> None:
    assert is_palindrome(11)
    assert not is_palindrome(12)

def test_multiple_digits() -> None:
    assert is_palindrome(121)
    assert is_palindrome(12321)
    assert not is_palindrome(123)

def test_large_number() -> None:
    assert is_palindrome(123456789987654321)
    assert not is_palindrome(123456789123456789)

def test_negative_number() -> None:
    assert not is_palindrome(-121)
    assert not is_palindrome(-111)
    assert not is_palindrome(-123)
