def quickselect(arr, k):
    if len(arr) <= 1:
        return arr

    pivot = len(arr) - 1
    i, j = 0, 0
    for j in range(len(arr)):
        if arr[j] < arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[pivot] = arr[pivot], arr[i]

    if len(arr) - i + 1 == k:
        return arr[i]
    elif len(arr) - i + 1 < k:
        return quickselect(arr[:i], k)
    else:
        return quickselect(arr[i:], k)
