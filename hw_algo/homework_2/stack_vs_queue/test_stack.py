from stack import Stack

def test_stack_push_pop():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert len(s) == 3
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()


def test_stack_peek():
    s = Stack()
    assert s.peek() is None
    s.push(1)
    assert s.peek() == 1
    s.push(2)
    assert s.peek() == 2


def test_stack_pop_empty():
    s = Stack()
    try:
        s.pop()
    except IndexError as e:
        assert str(e) == "pop from empty stack"
