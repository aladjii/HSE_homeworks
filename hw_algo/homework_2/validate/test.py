from validate import validate

def test_example1():
    pushed = [1, 2, 3, 4, 5]
    popped = [1, 3, 5, 4, 2]
    assert validate(pushed, popped) is True


def test_example2():
    pushed = [1, 2, 3]
    popped = [3, 1, 2]
    assert validate(pushed, popped) is False


def test_single_element():
    assert validate([1], [1]) is True
