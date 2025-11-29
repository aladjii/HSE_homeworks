import pytest
import random
from heaps import makeheap, makeheap_n_log_n

def is_min_heap(arr):
    n = len(arr)
    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True

@pytest.mark.parametrize("func", [makeheap, makeheap_n_log_n])
def test_empty(func):
    arr = []
    func(arr)
    assert arr == []

@pytest.mark.parametrize("func", [makeheap, makeheap_n_log_n])
def test_sorted(func):
    arr = [1, 2, 3, 4, 5]
    func(arr)
    assert is_min_heap(arr)

@pytest.mark.parametrize("func", [makeheap, makeheap_n_log_n])
def test_reverse(func):
    arr = [5, 4, 3, 2, 1]
    func(arr)
    assert is_min_heap(arr)
    assert arr[0] == 1

@pytest.mark.parametrize("func", [makeheap, makeheap_n_log_n])
def test_random(func):
    arr = [random.randint(-100, 100) for _ in range(100)]
    func(arr)
    assert is_min_heap(arr)
