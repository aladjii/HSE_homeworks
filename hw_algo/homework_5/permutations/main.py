from tracer import trace_recursion


@trace_recursion
def permute(x):
    if len(x) <= 1:
        return [x]
    res = []
    for i in range(len(x)):
        rest = x[:i] + x[i + 1 :]
        for p in permute(rest):
            res.append([x[i]] + p)
    return res


if __name__ == "__main__":
    print(permute([1, 2, 3]))
