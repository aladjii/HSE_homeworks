from bbt import is_balanced 

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1 — пустое дерево
def test1():
    assert is_balanced(None) == True


# 2 — один узел
def test2():
    root = Node(5)
    assert is_balanced(root) == True


# 3
#        4
#      /   \
#     2     6
#    / \   / \
#   1   3 5   7
def test3():
    root = Node(4,
                Node(2, Node(1), Node(3)),
                Node(6, Node(5), Node(7)))
    assert is_balanced(root) == True


# 4
#      3
#     / \
#    2   4
#   /
#  1
def test4():
    root = Node(3,
                Node(2, Node(1), None),
                Node(4))
    assert is_balanced(root) == True


# 5 
#      3
#     /
#    2
#   /
#  1
def test5():
    root = Node(3,
                Node(2,
                     Node(1)))
    assert is_balanced(root) == False


# 6 
#  1
#   \
#    2
#     \
#      3
def test6():
    root = Node(1,
                None,
                Node(2,
                     None,
                     Node(3)))
    assert is_balanced(root) == False


# 7 
#       5
#     /   \
#    3     8
#         /
#        7
#       /
#      6
def test7():
    root = Node(5,
                Node(3),
                Node(8,
                     Node(7,
                          Node(6))))
    assert is_balanced(root) == False


# 8
#        4
#      /   \
#     2     6
#    /     /
#   1     5
#  /
# 0
def test8():
    root = Node(4,
                Node(2, Node(1, Node(0)), None),
                Node(6, Node(5), None))
    assert is_balanced(root) == False


# 9
#        5
#      /   \
#     3     9
#      \   /
#       4 8
def test9():
    root = Node(5,
                Node(3, None, Node(4)),
                Node(9, Node(8), None))
    assert is_balanced(root) == True