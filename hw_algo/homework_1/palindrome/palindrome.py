def is_palindrome(n: int) -> bool:
    if n < 0:
        return False
    orig = n
    reversed = 0
    while n > 0:
        reversed = reversed * 10 + n % 10
        n //= 10
    return orig == reversed
