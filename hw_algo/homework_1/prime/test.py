import pytest
from primes_cnt import cnt_of_primes

@pytest.mark.parametrize(
    "n,expected",
    [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 1),   # 2
        (10, 4),  # 2,3,5,7
        (20, 8)   # 2,3,5,7,11,13,17,19
    ]
)
def test_small_cases(n, expected):
    assert cnt_of_primes(n) == expected

def test_large_case():
    result = cnt_of_primes(10**6)
    assert isinstance(result, int)
    assert result > 0
