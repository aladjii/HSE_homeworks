import time
import random


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return result, round(end - start, 4)

    return wrapper


@timer
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])[0]
    right = mergesort(arr[mid:])[0]
    return merge(left, right)


def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res


@timer
def quicksort(arr):
    if not isinstance(arr, list):
        arr = list(arr)

    if len(arr) <= 1:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[-1] = arr[-1], arr[pivot_index]

    i = 0
    for j in range(len(arr) - 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[-1] = arr[-1], arr[i]

    left = quicksort(arr[:i])[0]
    right = quicksort(arr[i + 1 :])[0]

    return left + [pivot] + right
