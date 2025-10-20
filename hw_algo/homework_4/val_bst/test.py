import pytest
from val import is_valid_bst

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1 — пустое дерево
def test1():
    assert is_valid_bst(None) == True


# 2 — один узел
def test2():
    root = Node(5)
    assert is_valid_bst(root) == True


# 3
#     5
#    / \
#   3   7
def test3():
    root = Node(5, Node(3), Node(7))
    assert is_valid_bst(root) == True


# 4
#     5
#    /
#   8   ← 8 слева от 5 → ошибка
def test4():
    root = Node(5, Node(8), None)
    assert is_valid_bst(root) == False


# 5
#     5
#      \
#       2   ← 2 справа от 5 → ошибка
def test5():
    root = Node(5, None, Node(2))
    assert is_valid_bst(root) == False


# 6
#         5
#       /   \
#      1     7
#          /
#         3   ← нарушение: 3 < 5 но справа
def test6():
    root = Node(5)
    root.left = Node(1)
    root.right = Node(7, Node(3), Node(9))
    assert is_valid_bst(root) == False


# 7
#     5
#    / \
#   3   5   ← дубликат
def test7():
    root = Node(5, Node(3), Node(5))
    assert is_valid_bst(root) == False


# 8
#       0
#     /   \
#   -3     9
def test8():
    root = Node(0, Node(-3), Node(9))
    assert is_valid_bst(root) == True


# 9
# 1 -> 2 -> 3 -> 4
def test9():
    root = Node(1, None, Node(2, None, Node(3, None, Node(4))))
    assert is_valid_bst(root) == True


# 10
# 4 <- 3 <- 2 <- 1
def test10():
    root = Node(4, Node(3, Node(2, Node(1))), None)
    assert is_valid_bst(root) == True
