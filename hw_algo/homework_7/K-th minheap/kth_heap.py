import heapq

# ---своя реализация  ---

def sift_up(arr, idx):
    parent = (idx - 1) // 2
    if idx > 0 and arr[idx] < arr[parent]:
        arr[idx], arr[parent] = arr[parent], arr[idx]
        sift_up(arr, parent)

def sift_down(arr, idx):
    smallest = idx
    left = 2 * idx + 1
    right = 2 * idx + 2

    if left < len(arr) and arr[left] < arr[smallest]:
        smallest = left
    if right < len(arr) and arr[right] < arr[smallest]:
        smallest = right

    if smallest != idx:
        arr[idx], arr[smallest] = arr[smallest], arr[idx]
        sift_down(arr, smallest)

def heappush_custom(heap, val):
    heap.append(val)
    sift_up(heap, len(heap) - 1)

def heappop_custom(heap):
    if not heap:
        return None
    if len(heap) == 1:
        return heap.pop()

    root = heap[0]
    heap[0] = heap.pop()
    sift_down(heap, 0)
    return root

def find_kth_largest_custom(nums, k):
    heap = []
    for n in nums:
        heappush_custom(heap, n)
        if len(heap) > k:
            heappop_custom(heap)
    return heap[0]


# --- реализация с heapq  ---

def find_kth_largest_builtin(nums, k):
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
