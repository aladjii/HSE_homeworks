from main import AVL


def test1():
    avl = AVL()
    for x in [10, 20, 30, 40, 50, 25]:
        avl.insert(x)

    assert avl.root.key == 30
    assert avl.root.left.key == 20
    assert avl.root.right.key == 40


def test2():
    avl = AVL()
    for x in [50, 20, 70, 10, 30, 60, 80]:
        avl.insert(x)

    avl.delete(70)
    assert avl.search(70) is None
    for k in [50, 20, 10, 30, 60, 80]:
        assert avl.search(k) is not None


def test3():
    avl = AVL()
    avl.insert(1)
    avl.insert(2)
    avl.insert(3)
    avl.insert(4)
    avl.insert(5)
    assert avl.root.key in (2, 3)
    for x in [1, 2, 3, 4, 5]:
        assert avl.search(x) is not None


def test4():
    avl = AVL()
    for x in [10, 5, 15, 3, 7, 12, 17]:
        avl.insert(x)
    avl.delete(5)
    assert avl.search(5) is None
    for x in [3, 7, 10, 12, 15, 17]:
        assert avl.search(x) is not None
