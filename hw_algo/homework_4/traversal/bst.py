class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class bst:
    def __init__(self, root = None):
        self.root = root
    
    def _insert(self, cur, val):
        if val < cur.val:
            if cur.left is None:
                cur.left = Node(val)
            else:
                self._insert(cur.left, val)
        elif val > cur.val:
            if cur.right is None:
                cur.right = Node(val)
            else:
                self._insert(cur.right, val)

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)
    
    def _search(self, cur, val):
        if cur is None:
            return False

        if cur.val == val:
            return True

        if val < cur.val:
            self._search(cur.left, val)
        else:
            self._search(cur.right, val)
    
    def search(self, val):
        return self._search(self.root, val)