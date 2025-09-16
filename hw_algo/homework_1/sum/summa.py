from typing import List

def max_even_sum(arr: List[int]) -> int:
    total = sum(arr)
    if total % 2 == 0:
        return total

    odd_nums = [x for x in arr if x % 2 == 1]
    if not odd_nums:
        return 0

    return total - min(odd_nums)
