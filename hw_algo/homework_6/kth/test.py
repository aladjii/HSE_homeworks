import pytest
from main import quickselect


def test_example_1():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    assert quickselect(nums, k) == 5


def test_example_2():
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    assert quickselect(nums, k) == 4


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1], 1, 1),
        ([1, 2], 1, 2),
        ([1, 2], 2, 1),
        ([1, 2, 3, 4, 5], 1, 5),
        ([1, 2, 3, 4, 5], 5, 1),
        ([-1, -5, -2, -4, -3], 2, -2),
        ([2, 2, 2, 2], 1, 2),
    ],
)
def test_quickselect_various_cases(nums, k, expected):
    assert quickselect(nums[:], k) == expected


def test1():
    nums = [3, 1, 2, 3, 4, 3]
    assert quickselect(nums[:], 3) == 3


def test2():
    nums = [1, 100, 20, 5]
    assert quickselect(nums, 2) == 20
