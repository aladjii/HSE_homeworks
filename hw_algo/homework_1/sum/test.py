import pytest
from summa import max_even_sum

@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 2, 3, 4], 10),
        ([1, 3, 5], 8),
        ([2, 4, 6], 12),
        ([1], 0),
        ([2], 2),
        ([1, 1, 1, 1, 1], 4),
        ([10, 15, 7, 2], 34),
    ]
)
def test_max_even_sum(arr, expected):
    assert max_even_sum(arr) == expected
