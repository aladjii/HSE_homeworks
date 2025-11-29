import time
import random
import sys
from heaps import makeheap, makeheap_n_log_n

sys.setrecursionlimit(20000)

def benchmark():
    size = 1_000_000
    arr_base = [random.randint(0, 1000000) for _ in range(size)]

    arr1 = arr_base[:]
    start_time = time.time()
    makeheap_n_log_n(arr1)
    time_n_log_n = time.time() - start_time

    arr2 = arr_base[:]
    start_time = time.time()
    makeheap(arr2)
    time_n = time.time() - start_time

    print(f"Array size: {size}")
    print(f"O(N log N) method: {time_n_log_n:.5f} seconds")
    print(f"O(N) method:       {time_n:.5f} seconds")
    print(f"{time_n_log_n / time_n:.2f}x faster")

if __name__ == "__main__":
    benchmark()
