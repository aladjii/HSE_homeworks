def sift_up(arr, idx):
    parent = (idx - 1) // 2
    if idx > 0 and arr[idx] < arr[parent]:
        arr[idx], arr[parent] = arr[parent], arr[idx]
        sift_up(arr, parent)

def makeheap_n_log_n(arr):
    for i in range(len(arr)):
        sift_up(arr, i)

def sift_down(arr, n, idx):
    smallest = idx
    left = 2 * idx + 1
    right = 2 * idx + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != idx:
        arr[idx], arr[smallest] = arr[smallest], arr[idx]
        sift_down(arr, n, smallest)

def makeheap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, n, i)
