from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        fa = {}
        start_node = None

        def dfs(node, from_: Optional[TreeNode]):
            if node is None:
                return
            fa[node] = from_
            if node.val == start:
                nonlocal start_node
                start_node = node
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        def maxDepth(node, form_: Optional[TreeNode]):
            if node is None:
                return -1
            return max(maxDepth(x, node) for x in (node.left, node.right, fa[node]) if x != form_) + 1

        return maxDepth(start_node, start_node)


print(Solution().amountOfTime(TreeNode(1), 1))
