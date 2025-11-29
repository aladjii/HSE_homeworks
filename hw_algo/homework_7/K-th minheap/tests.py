import pytest
from kth_heap import find_kth_largest_custom, find_kth_largest_builtin

@pytest.mark.parametrize("func", [find_kth_largest_custom, find_kth_largest_builtin])
def test_example_1(func):
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    assert func(nums, k) == 5

@pytest.mark.parametrize("func", [find_kth_largest_custom, find_kth_largest_builtin])
def test_example_2(func):
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    assert func(nums, k) == 4

@pytest.mark.parametrize("func", [find_kth_largest_custom, find_kth_largest_builtin])
def test_k_is_1(func):
    # 1-й по величине = максимум
    nums = [10, 5, 20, 15]
    k = 1
    assert func(nums, k) == 20

@pytest.mark.parametrize("func", [find_kth_largest_custom, find_kth_largest_builtin])
def test_k_is_len(func):
    # k равно длине массива = минимум
    nums = [10, 5, 20, 15]
    k = 4
    assert func(nums, k) == 5

@pytest.mark.parametrize("func", [find_kth_largest_custom, find_kth_largest_builtin])
def test_negative_numbers(func):
    nums = [-1, -5, -2, -4, -3]
    k = 2
    assert func(nums, k) == -2

@pytest.mark.parametrize("func", [find_kth_largest_custom, find_kth_largest_builtin])
def test_single_element(func):
    nums = [42]
    k = 1
    assert func(nums, k) == 42
