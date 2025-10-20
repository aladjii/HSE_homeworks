def is_balanced(root):
    def dfs(node):
        if node is None:
            return 0

        left = dfs(node.left)
        if left == -1:
            return -1

        right = dfs(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1 

        return max(left, right) + 1

    return dfs(root) != -1
