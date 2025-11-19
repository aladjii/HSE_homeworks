import random


def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    len_right = len(right)
    len_middle = len(middle)

    if k <= len_right:
        return quickselect(right, k)
    elif k <= len_right + len_middle:
        return pivot
    else:
        return quickselect(left, k - len_right - len_middle)
