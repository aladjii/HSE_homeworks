from queue import Queue

def test_queue_enqueue_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert len(q) == 3
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.is_empty()


def test_queue_peek():
    q = Queue()
    assert q.peek() is None
    q.enqueue(1)
    assert q.peek() == 1
    q.enqueue(2)
    assert q.peek() == 1


def test_queue_dequeue_empty():
    q = Queue()
    try:
        q.dequeue()
    except IndexError as e:
        assert str(e) == "dequeue from empty queue"
