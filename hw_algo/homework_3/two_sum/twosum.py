def two_sum(arr, k):
    seen = dict()

    for i in arr:
        comp = k - i
        if comp in seen:
            return [seen[comp], i]
        seen[i] = i
