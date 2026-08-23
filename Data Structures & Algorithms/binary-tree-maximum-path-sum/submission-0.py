# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def dfs(node):
            if not node:
                return 0
            nonlocal max_sum
            max_left = dfs(node.left)
            max_right = dfs(node.right)

            max_left = max(max_left, 0)
            max_right = max(max_right, 0)

            max_sum = max(max_sum, node.val + max_left + max_right)
            return node.val + max(max_left, max_right)

        dfs(root)
        return max_sum