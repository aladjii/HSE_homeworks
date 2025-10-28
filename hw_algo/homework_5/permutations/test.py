from main import permute


def test1():
    assert sorted(permute([1, 2, 3])) == sorted(
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    )


def test2():
    assert sorted(permute([0, 1])) == sorted([[0, 1], [1, 0]])


def test3():
    assert permute([1]) == [[1]]
