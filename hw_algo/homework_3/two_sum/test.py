import pytest
from twosum import two_sum


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([1, 2, 3], 4, [1, 3]),
        ([1, 2, 3], 5, [2, 3]),
        ([1, 2, 3], 6, None),
        ([-3, 1, 4, 2, -1], 1, [-3, 4]),
        ([1, 3, 3, 4], 6, [3, 3]),
        ([], 5, None),
        ([5], 5, None),
        ([-5, -2, 7, 10], 5, [-2, 7]),
    ],
)
def test_two_sum(arr, k, expected):
    assert two_sum(arr, k) == expected
