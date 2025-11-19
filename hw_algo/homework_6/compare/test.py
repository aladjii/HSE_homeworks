import random
from main import mergesort, quicksort


def test1():
    arr = [random.randint(0, 10000) for _ in range(100000)]
    _, t1 = mergesort(arr)
    assert _ == sorted(arr)
    _, t2 = quicksort(arr)
    assert _ == sorted(arr)
    print("\nrandom:", t1, t2)
    assert True


def test2():
    arr = sorted([random.randint(0, 10000) for _ in range(100000)])
    _, t1 = mergesort(arr)
    assert _ == sorted(arr)
    _, t2 = quicksort(arr)
    assert _ == sorted(arr)
    print("\nsorted:", t1, t2)
    assert True


def test3():
    arr = list(range(10000, 0, -1))
    _, t1 = mergesort(arr)
    assert _ == sorted(arr)
    _, t2 = quicksort(arr)
    assert _ == sorted(arr)
    print("\nreversed:", t1, t2)
    assert True


if __name__ == "__main__":
    test1()
    test2()
    test3()
