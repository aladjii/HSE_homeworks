from bst import Node, bst

def pre_order(bst):
    def _preorder(node):
        if not node:
            return []
        return [node.val] + _preorder(node.left) + _preorder(node.right)
    return _preorder(bst.root)

def reverse_preorder(bst):
    def _rpreorder(node):
        if not node:
            return []
        return [node.val] + _rpreorder(node.right) + _rpreorder(node.left)
    return _rpreorder(bst.root)

def inorder(bst):
    def _inorder(node):
        if not node:
            return []
        return _inorder(node.left) + [node.val] + _inorder(node.right)
    return _inorder(bst.root)

def reverse_inorder(bst):
    def _rinorder(node):
        if not node:
            return []
        return _rinorder(node.right) + [node.val] + _rinorder(node.left)
    return _rinorder(bst.root)

def postorder(bst):
    def _post(node):
        if not node:
            return []
        return _post(node.left) + _post(node.right) + [node.val]
    return _post(bst.root)

def reverse_postorder(bst):
    def _rpost(node):
        if not node:
            return []
        return _rpost(node.right) + _rpost(node.left) + [node.val]
    return _rpost(bst.root)
