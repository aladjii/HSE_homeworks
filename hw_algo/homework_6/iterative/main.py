import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return result, round(end - start, 4)

    return wrapper


@timer
def mergesort_iter(arr):
    width = 1
    n = len(arr)
    res = arr[:]
    while width < n:
        for i in range(0, n, 2 * width):
            left = res[i : i + width]
            right = res[i + width : i + 2 * width]
            res[i : i + 2 * width] = merge(left, right)
        width *= 2
    return res


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
def quicksort_iter(arr):
    res = arr[:]
    stack = [(0, len(res) - 1)]
    while stack:
        low, high = stack.pop()
        while low < high:
            pivot_index = (low + high) // 2
            pivot = res[pivot_index]
            i, j = low, high
            while i <= j:
                while res[i] < pivot:
                    i += 1
                while res[j] > pivot:
                    j -= 1
                if i <= j:
                    res[i], res[j] = res[j], res[i]
                    i += 1
                    j -= 1
            if j - low < high - i:
                if low < j:
                    stack.append((i, high))
                    high = j
                else:
                    low = i
            else:
                if i < high:
                    stack.append((low, j))
                    low = i
                else:
                    high = j
    return res
