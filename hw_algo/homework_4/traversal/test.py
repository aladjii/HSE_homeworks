import pytest
from bst import bst
from traversal import (
    pre_order, reverse_preorder,
    inorder, reverse_inorder,
    postorder, reverse_postorder
)

@pytest.fixture
def tree():
    t = bst()
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    for v in values:
        t.insert(v)
    return t

def test_preorder(tree):
    assert pre_order(tree) == [8, 3, 1, 6, 4, 7, 10, 14, 13]

def test_reverse_preorder(tree):
    assert reverse_preorder(tree) == [8, 10, 14, 13, 3, 6, 7, 4, 1]

def test_inorder(tree):
    assert inorder(tree) == [1, 3, 4, 6, 7, 8, 10, 13, 14]

def test_reverse_inorder(tree):
    assert reverse_inorder(tree) == [14, 13, 10, 8, 7, 6, 4, 3, 1]

def test_postorder(tree):
    assert postorder(tree) == [1, 4, 7, 6, 3, 13, 14, 10, 8]

